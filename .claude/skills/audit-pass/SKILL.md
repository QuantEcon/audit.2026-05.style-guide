---
name: audit-pass
description: Run a full QuantEcon lecture style-audit pass in this repo — clone the corpus at a pinned snapshot, measure it, draft every per-lecture report, run the judgment review, derive scores, splice the aggregate pages, gate, build and commit. Use when asked to refresh the audit, run the next pass, re-assess the lectures, update the report to the current corpus, or add a period to the trend. Also use for a partial re-run after changing a rule check.
---

# Run an audit pass

A pass has three layers. Keep them separate — it is the whole design:

| Layer | What it is | Who does it |
|-------|-----------|-------------|
| **Evidence** | 41 of 49 rules measured over a pinned commit per series | `tools/qestyle_scan.py` |
| **Scoring** | overall score + priority bucket, arithmetic from the rubric | `tools/qestyle_draft.py`, `qestyle_score.py` |
| **Review** | the 8 judgment-only rules, plus Strengths and Actions prose | subagents writing `reviews/*.json` |

`lectures/data/*.csv` is the source of every number. The per-lecture reports, the
scoreboard, the triage page and the charts are **generated from it**. Never hand-edit a
number, and never edit inside a `<!-- qe:NAME -->` marker.

Full reference: [`UPDATE.md`](../../../UPDATE.md) · methodology: [`lectures/spec.md`](../../../lectures/spec.md) §8–§10.

---

## Step 0 — Check what already exists

A previous pass may have left the corpus, the venv and some review overlays in place. Check
before re-doing any of it:

```bash
cd /home/user/audit.2026-05.style-guide          # or wherever this repo is
ls -d ../quantecon/*/ 2>/dev/null | wc -l        # 6 = 5 series + action-style-guide
ls -d ../quantecon-*/  2>/dev/null               # past-snapshot worktrees
find reviews -name '*.json' | wc -l              # review overlays already written
python3 -c "import json;print(json.load(open('lectures/data/snapshot.json'))['snapshot'])"
```

If the corpus is present, **verify it is still at the pinned commits** before trusting any
existing numbers:

```bash
python3 - <<'PY'
import json, subprocess
for s, m in json.load(open('lectures/data/snapshot.json'))['snapshot'].items():
    live = subprocess.run(['git','-C',f'../quantecon/{s}','rev-parse','HEAD'],
                          capture_output=True, text=True).stdout.strip()
    print(('OK   ' if live == m['commit'] else 'DRIFT'), s, m['commit'][:10])
PY
```

## Step 1 — Corpus and build environment

Blobless sparse clones: a few MB per series, because only `lectures/*.md` is ever read.

```bash
CORPUS=../quantecon; mkdir -p $CORPUS
for r in lecture-python-intro lecture-python-programming lecture-python.myst \
         lecture-python-advanced.myst lecture-dp action-style-guide; do
  git clone --depth 1 --filter=blob:none --sparse \
      https://github.com/QuantEcon/$r $CORPUS/$r
  git -C $CORPUS/$r sparse-checkout set --no-cone '/lectures/*.md' \
      '/lectures/_config.yml' '/style_checker/rules/*.md'
done
```

The build needs **Python 3.12+** — `quantecon-book-theme==0.15.1` will not resolve on 3.11:

```bash
uv venv --python 3.12 .venv          # .gitignore already covers it
uv pip install --python .venv/bin/python -r requirements.txt
```

To add an **earlier** period to the trend (only needed when back-filling history):

```bash
git -C $CORPUS/$r fetch --unshallow --filter=blob:none
SHA=$(git -C $CORPUS/$r log --until=YYYY-MM-DD -1 --format=%H)
git -C $CORPUS/$r worktree add --no-checkout ../quantecon-YYYY-MM/$r $SHA
git -C ../quantecon-YYYY-MM/$r sparse-checkout set --no-cone '/lectures/*.md'
git -C ../quantecon-YYYY-MM/$r checkout
```

## Step 2 — Measure, then draft

```bash
R=$CORPUS/action-style-guide/style_checker/rules
python3 tools/qestyle_scan.py --corpus $CORPUS --out lectures/data --rules $R \
    --period YYYY-MM --append-history lectures/data/rule_reach_history.csv \
    --evidence /tmp/evidence

python3 tools/qestyle_draft.py --corpus $CORPUS --out lectures --date YYYY-MM-DD \
    --rules $R --reviews reviews --judgment-csv lectures/data/judgment.csv
```

`--reviews reviews` is load-bearing: it folds existing overlays back in. Omit it and you
silently discard every review already written.

**Retire reports for lectures that no longer exist** — `qestyle_draft` only writes:

```bash
python3 - <<'PY'
import os, glob
for s in os.listdir('lectures'):
    if not s.startswith('lecture-'): continue
    have = {f[:-3] for f in os.listdir(f'../quantecon/{s}/lectures') if f.endswith('.md')}
    for p in glob.glob(f'lectures/{s}/*.md'):
        stem = os.path.basename(p)[:-3]
        if stem != 'index' and stem not in have:
            os.remove(p); print('retired', p)
PY
```

## Step 3 — The judgment review

Send subagents, one batch of ~10 lectures each, over the lectures with **no overlay
yet** — one agent at a time; see *Pace it for the session limit* below. Reviewers judge only these 8 rules — everything else is already measured:

`qe-writing-002` `qe-writing-003` `qe-writing-005` `qe-writing-007` `qe-math-009`
`qe-code-001` `qe-math-014` *(proposed)* `qe-math-015` *(proposed)*

Each writes one `reviews/<series>/<stem>.json`:

```json
{
  "series": "lecture-dp", "lecture": "lqcontrol",
  "judgment": [{"rule": "qe-writing-002", "count": 4, "lines": [138, 156],
                "detail": "sentences of 45+ words carrying two ideas each"}],
  "strengths": ["Equation labels and {eq} cross-references used consistently"],
  "actions": ["Replace every apostrophe transpose with ^\\top"],
  "scanner_doubts": []
}
```

Rules for reviewers, which matter:

- **Do not re-count a mechanical rule.** The drafted counts are authoritative. A count that
  looks wrong goes in `scanner_doubts` — never quietly edited, or the report stops matching
  the CSVs and Step 5 fails.
- **Omit a rule that is satisfied.** Two or three judgment findings per lecture is typical;
  none is a legitimate answer. Invented findings are worse than no findings.
- Strengths must be **specific to that lecture**. Never "well written".

Overlays are deliberately decoupled from the counts, so fixing a check and re-running
Steps 2 and 5 never destroys review work. That also makes the review resumable: recompute
the to-do list and only review what is missing.

```bash
python3 - <<PY
import glob, os, json
CORPUS = "$CORPUS"
todo = {}
for s in sorted(d for d in os.listdir('lectures') if d.startswith('lecture-')):
    have = {os.path.basename(p)[:-5] for p in glob.glob(f'reviews/{s}/*.json')}
    todo[s] = [os.path.basename(p)[:-3]
               for p in sorted(glob.glob(f'{CORPUS}/{s}/lectures/*.md'))
               if os.path.basename(p)[:-3] not in have]
    print(f'{s:32s} {len(have):3d} done, {len(todo[s]):3d} to do')
json.dump(todo, open('/tmp/todo.json','w'), indent=1)
PY
```

### Pace it for the session limit, not for wall-clock

This step is the whole pass's token budget. Measured here: **one overlay per ~5
agent-minutes**, so a 348-lecture review is on the order of **30 agent-hours**. It will not
fit in one session at any concurrency, and concurrency does not reduce the total — it only
raises the burn rate and the amount in flight when a session ends.

- **One agent at a time.** Two concurrent agents exhausted a session limit in under half an
  hour mid-batch. Sequential is slower per hour and far more predictable, which is what
  matters when the work spans sessions.
- **Batch ~10 lectures, and commit each batch.** `reviews/<series>/<stem>.json` is the
  durable unit; an overlay is useful the moment it is written and does not need the reports
  regenerated. A session that dies then loses at most one batch.
- **Refresh once per session, at the end** — not per batch. Step 5 rewrites all 348 reports,
  and a diff that size per batch buries the review work in the history.
- **End every session deliberately:** refresh, gate, build, commit, push, then schedule the
  next resume. Overlays committed but not yet folded in are safe; a dirty tree is not.
- **Order the queue worst-first**, and put a series with little or no coverage ahead of one
  that is nearly done — an uneven judgment layer makes the cross-series scoreboard partly a
  ranking of coverage, which is the one thing the scoreboard must not be.

One more, unrelated to pace:

- **Auto mode must be ON** if the corpus lives outside the working directory. Subagents
  cannot read outside it otherwise, every corpus read is denied, and the run stalls; this
  has bitten two passes. For an *unattended* run there is nobody to approve a prompt, so
  clone the corpus **inside** the repo instead — `.corpus/` is gitignored — and the question
  does not arise. Every tool takes `--corpus`, so the path is free.

## Step 4 — Series summaries

Each `lectures/<series>/index.md` has generated tables plus two **hand-written** marker
regions: `<!-- qe:series-narrative -->` and `<!-- qe:series-recommendations -->`. Write
those from the data, then verify every figure you quoted:

```bash
python3 - <<'PY'
import csv, collections, re, pathlib
per = collections.defaultdict(dict)
for r in csv.DictReader(open('lectures/data/series_rule_reach.csv')):
    per[r['series']][r['rule']] = int(r['lectures_affected'])
n = {r['series']: int(r['lectures'])
     for r in csv.DictReader(open('lectures/data/series_summary.csv'))}
bad = 0
for s in per:
    t = pathlib.Path(f'lectures/{s}/index.md').read_text()
    for m in re.finditer(r'`(qe-[a-z]+-\d{3})`[^(\n]*\((\d+)\s*/\s*(\d+)', t):
        rule, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        if per[s].get(rule) != a or b != n[s]:
            print(f'  MISMATCH {s} {rule}: prose {a}/{b}'); bad += 1
print('all reach claims check out' if not bad else f'{bad} mismatches')
PY
```

Do this even when you are confident. It caught a reach figure written from memory that a
rule fix had since changed.

## Step 5 — Derive, splice, gate

```bash
python3 tools/qestyle_score.py --root lectures --fix --csv lectures/data/scores.csv
python3 tools/qestyle_report.py --summarise --history YYYY-MM --splice
python3 tools/qestyle_toc.py --root lectures          # only if lectures were added/removed
python3 tools/qestyle_check.py --root lectures --data lectures/data --corpus $CORPUS
```

The gate must print **All checks passed**. It asserts coverage, score arithmetic, priority
buckets, report↔CSV agreement, the conventions, and snapshot pinning. It will also catch
your own prose citing a proposed rule without its **(proposed)** tag, and any
hand-written table that still quotes a reach the data has since moved — a trend row
(`A% → B%`) or a counts table whose header names *Lectures* and *Occurrences*.

Also refresh the hand-written trend table in `lectures/intro.md` from the measured history
rather than editing digits:

```bash
python3 - <<'PY'
import csv
h = list(csv.DictReader(open('lectures/data/rule_reach_history.csv')))
periods = sorted({r['period'] for r in h})
prev, cur = periods[-2], periods[-1]
a = {r['rule']: float(r['share_pct']) for r in h if r['period'] == prev}
b = {r['rule']: float(r['share_pct']) for r in h if r['period'] == cur}
moves = sorted(((b.get(k,0)-a.get(k,0), k) for k in set(a)|set(b)
                if max(a.get(k,0), b.get(k,0)) >= 5), key=lambda x: x[0])
for d, k in moves[:3] + list(reversed(moves))[:2]:
    print(f'{k:16s} {a.get(k,0):5.0f}% -> {b.get(k,0):5.0f}%  ({d:+.0f}pp)')
PY
```

## Step 6 — Build and commit

```bash
.venv/bin/jupyter-book build lectures
```

Must succeed. A few dozen warnings are standing — the audit quotes rule examples (stray
`$`, `\begin{align}`, `` {eq}`…` ``) inside prose. Treat a *new* warning class as a
regression, not the absolute count. Confirm the charts rendered:

```bash
ls lectures/_build/jupyter_execute/*.png | wc -l    # expect 5
```

Then commit. **Only push to `main` when the pass is finished** — that deploys the site.

---

## If you changed a rule check

The cheap loop, no review work lost:

```bash
python3 tools/qestyle_scan.py --corpus $CORPUS --out lectures/data --rules $R \
    --period YYYY-MM --append-history lectures/data/rule_reach_history.csv
python3 tools/qestyle_draft.py --corpus $CORPUS --out lectures --date YYYY-MM-DD \
    --rules $R --reviews reviews --judgment-csv lectures/data/judgment.csv
python3 tools/qestyle_score.py --root lectures --fix --csv lectures/data/scores.csv
python3 tools/qestyle_report.py --summarise --history YYYY-MM --splice
python3 tools/qestyle_check.py --root lectures --data lectures/data --corpus $CORPUS
```

**Then re-check any prose that quotes the numbers that moved.** The gate now verifies the
`intro.md` trend table and the `appendix.md` counts table for you; it cannot verify a
number written into a *sentence*, so re-read the narrative claims in `intro.md` /
`details.md` / `README.md` yourself. A rule fix changes reach, and hand-written
sentences do not follow.

### Before trusting a new or changed check

Sample it adversarially — this is where the real defects are, not in the regex:

```bash
cd tools && python3 - <<'PY'
import sys, glob; sys.path.insert(0, '.')
from qestyle_lex import lex
from qestyle_rules import CHECKS
rule = 'qe-fig-003'
for f in glob.glob('../../quantecon/lecture-python.myst/lectures/*.md'):
    for h in CHECKS[rule](lex(f, 'lecture-python.myst')):
        print(f'{f}:{h.line}: {h.detail}')
PY
```

Open at least ten hits in the source and judge them against the rule text. If total reach
is small, read every hit instead of sampling. Then record the outcome in
[`tools/VERIFICATION.md`](../../../tools/VERIFICATION.md) — including a rule that needed
nothing, so the table is not a list of only the broken ones.

19 of 41 checks needed fixing when first sampled. `qe-fig-008` had **149 false positives
in 15 sampled hits**; shipping it would have told authors to add `lw=2` to plots that
already had it.

## Traps that have actually cost time

- **Most wrong counts are structural, not regex errors.** Before blaming a pattern, check
  how `qestyle_lex.py` typed the region. Past bugs: `{math}` directive bodies typed as
  code (1,783 blocks); display math closed at the end of a content line (`… p}$$`);
  blockquoted `> $$`; inline maths spanning a line break; a gated `{exercise-start}`
  treated as a container; HTML comments scanned.
- **`_strip_py` must preserve line structure.** Replacing a docstring with a space joins
  the lines around it and pulls indented code to column zero, which makes an indented
  `plt.show()` look top-level.
- **Masking must not fabricate whitespace.** The lexer masks inline code and maths with
  NUL, not spaces, or `qe-writing-008` fires on prose that is correctly spaced.
- **`lecture-dp` syncs lectures from `lecture-python.myst`** (`cross_product_trick`,
  `ifp_advanced`, `inventory_q`, `rs_inventory_q`, …). Their findings appear twice in the
  corpus totals. Fix upstream; a fix applied in `lecture-dp` is overwritten by the next sync.
- **`qestyle_check` skips `lectures/_build`** — it used to scan its own build output and
  fail. If you add a check that walks markdown, skip that directory.
- **The lecture count changes between passes** (299 → 348). Never carry a count forward in
  prose; the scan reports it.
- **`contributions/issues/*.md` mirror live `action-style-guide` issues.** Editing them here
  does not update GitHub, and that repo is usually outside the session's scope — say so
  rather than implying a re-sync happened.
