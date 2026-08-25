# UPDATE.md — how to run a pass and refresh this report

This is the runbook for reproducing the style audit and updating every document in
this repo. Pair it with [`ROADMAP.md`](ROADMAP.md) (direction and open decisions) and
the [scoring spec](lectures/spec.md) (the rubric, the pass methodology, and the
measured deterministic coverage).

---

## Source of truth

**This git repository is the single source of truth for the audit report.** The
published site at <https://quantecon.github.io/audit.2026-05.style-guide/> is built
from `lectures/` by `.github/workflows/deploy.yml` on every push to `main`.

Within the repo, the ordering is: `lectures/data/*.csv` is the source of the numbers,
per-lecture reports are the source of the scores, and the aggregate pages
(`intro.md`, `details.md`, `charts.md`, `README.md`) are **generated from those** —
never edited by hand in their table regions. Section [§ Step 5](#step-5--derive-scores-and-splice-the-aggregates)
explains how.

---

## Update in place, or start a new audit period?

- **Correcting or refreshing *this* audit** → run the pass below and push.
- **A new audit period** → see [§ Starting a new audit period](#starting-a-new-audit-period).
  Note the open naming question in `ROADMAP.md` §1: the recorded decision was one new
  dated repo per period, but the cross-period time series in `lectures/data/` now argues
  for a single durable home. Settle it in the planning hub before standing up a new repo.

---

## Inputs

| Input | Where | Role |
|-------|-------|------|
| The 5 lecture series | cloned under a corpus directory as `<corpus>/<series>/lectures/*.md` | The lectures being audited |
| Canonical rules | `<corpus>/action-style-guide/style_checker/rules/*.md` (8 category files) | Rule definitions — **never redefined here**, only consumed |
| Scoring spec | `lectures/spec.md` | Rubric, severity tiers, pass methodology, report templates |
| The tools | `tools/qestyle_*.py` | The evidence, scoring and reporting layers |

JAX rules are **out of scope** for this corpus (they target `lecture-jax`).

### Getting the corpus

Blobless sparse clones keep this to a few megabytes per series — the audit only ever
reads `lectures/*.md`:

```bash
CORPUS=../quantecon; mkdir -p $CORPUS
for r in lecture-python-intro lecture-python-programming lecture-python.myst \
         lecture-python-advanced.myst lecture-dp action-style-guide; do
  git clone --depth 1 --filter=blob:none --sparse \
      https://github.com/QuantEcon/$r $CORPUS/$r
  git -C $CORPUS/$r sparse-checkout set --no-cone '/lectures/*.md' '/lectures/_config.yml' \
      '/style_checker/rules/*.md'
done
```

To re-measure a **past** snapshot (which is how the trend chart gets its earlier
point), add history and check the date out into a worktree:

```bash
git -C $CORPUS/$r fetch --unshallow --filter=blob:none
SHA=$(git -C $CORPUS/$r log --until=YYYY-MM-DD -1 --format=%H)
git -C $CORPUS/$r worktree add --no-checkout ../quantecon-YYYY-MM/$r $SHA
git -C ../quantecon-YYYY-MM/$r sparse-checkout set --no-cone '/lectures/*.md'
git -C ../quantecon-YYYY-MM/$r checkout
```

---

## The process

The pass has three layers — evidence (code), scoring (arithmetic), review (judgment).
[Spec §8](lectures/spec.md) explains why they are separate; this section is the
mechanics.

### Step 1 — Measure the corpus

```bash
python3 tools/qestyle_scan.py --corpus $CORPUS --out lectures/data \
    --period YYYY-MM --append-history lectures/data/rule_reach_history.csv \
    --evidence /tmp/evidence
```

This pins one commit per series into `lectures/data/snapshot.json`, writes
per-lecture per-rule counts to `violations.csv`, corpus and per-series reach to
`rule_reach.csv` / `series_rule_reach.csv`, rule titles to `rule_titles.csv`, and
appends this pass to `rule_reach_history.csv`. `--evidence` dumps per-lecture JSON
(counts, line numbers, sample matches) for the review layer to read.

> The lecture count changes between passes — 299 lectures in 2026-05, 348 in 2026-08.
> Do not carry a count forward; the scan reports it.

### Step 2 — Draft every per-lecture report

```bash
python3 tools/qestyle_draft.py --corpus $CORPUS --out lectures --date YYYY-MM-DD
```

One report per lecture at `lectures/<series>/<stem>.md`, following the
[spec §6](lectures/spec.md) template: header with the pinned snapshot, score table,
severity-bucketed issue list with line numbers.

### Step 3 — Review pass

Fan out reviewers (one batch of lectures each) to add what the scanner cannot
measure: the 6 judgment-only registry rules and 2 judgment-only proposed rules
(spec §9), plus per-lecture **Strengths** and **Recommended actions**. Reviewer
instructions are [spec §8.3](lectures/spec.md).

> 🔑 **Sandbox gotcha:** subagents can only read outside the working directory when
> **auto mode is ON**. With auto mode off every read of the corpus is denied and the
> run stalls. This bit the original pass.

Reviewers must **not** edit a mechanical count. If one looks wrong it is a scanner
defect: fix `tools/qestyle_rules.py`, re-run Steps 1–2, and note it. Otherwise the
reports stop matching the CSVs and Step 6 will catch it.

### Step 4 — Write the series summaries

One `lectures/<series>/index.md` per series, H1 `# Summary`, following the
[spec §7](lectures/spec.md) template. The ranked-lecture table and the priority
distribution come from `lectures/data/scores.csv` after Step 5, so write the prose
first and fill the tables from the generated numbers.

### Step 5 — Derive scores and splice the aggregates

```bash
python3 tools/qestyle_score.py --root lectures --fix --csv lectures/data/scores.csv
python3 tools/qestyle_report.py --summarise --history YYYY-MM --splice
```

`qestyle_score.py --fix` recomputes each report's overall score and priority bucket
from its own score table, so a header can never contradict its categories.
`qestyle_report.py --splice` regenerates the marked table regions in `README.md`,
`lectures/intro.md` and `lectures/details.md`:

| Marker | What it generates |
|--------|-------------------|
| `<!-- qe:readme-scoreboard -->` | README landing scoreboard |
| `<!-- qe:focus -->` | intro.md "where to focus" table |
| `<!-- qe:wins -->` | intro.md highest-reach fixes |
| `<!-- qe:full-scoreboard -->` | details.md full scoreboard |
| `<!-- qe:systemic -->` | details.md every recurring rule, ranked |
| `<!-- qe:high-list -->` | details.md every HIGH-priority lecture |
| `<!-- qe:snapshot -->` | details.md pinned-snapshot table |

**Prose outside those markers is hand-written** — rewrite it to match the new
numbers. Never edit inside a marker; the next `--splice` overwrites it.

`charts.md` needs no step: it reads `lectures/data/*.csv` at build time.

### Step 6 — Check consistency

```bash
python3 tools/qestyle_check.py --root lectures --data lectures/data --corpus $CORPUS
```

All checks must pass before pushing. See [§ Consistency checks](#consistency-checks).

### Step 7 — Regenerate the TOC (only if lectures were added or removed)

```bash
python3 tools/qestyle_toc.py --root lectures
```

### Step 8 — Build and deploy

```bash
jupyter-book build lectures          # must succeed; see the warning note below
git add -A && git commit -m "Refresh audit — <period>" && git push origin main
gh run watch "$(gh run list --limit 1 --json databaseId -q '.[0].databaseId')" --exit-status
```

The build carries a standing set of warnings (~87) from the audit quoting rule examples
— stray `$`, `\begin{align}`, `` {eq}`…` `` — inside prose. `_config.yml` suppresses the
classes that are expected; the rest are pre-existing and not introduced by a pass. Treat
a *new* warning class as a regression, not the absolute count.

The build uses **vanilla jupyter-book + `quantecon-book-theme`** (pinned in
`requirements.txt`) — not the QuantEcon build container. It needs **Python 3.12+**
(`quantecon-book-theme` 0.15.1 requires it), and `charts.md` executes at build time,
so `matplotlib`/`numpy` must stay in `requirements.txt`.

---

## Consistency checks

`tools/qestyle_check.py` asserts the things that silently broke in the previous pass:

| Check | What it catches |
|-------|-----------------|
| **Coverage** | A lecture in the corpus with no report, or a report with no lecture. The previous pass missed 2 `lecture-dp` lectures and carried a report for `supply_demand_foundations_v2`, which exists in no repository's history. |
| **Score arithmetic** | A header whose overall score is not the mean of its own in-scope categories (95 of 299 reports in the previous pass). |
| **Priority buckets** | A priority that is not what spec §4 gives for that score and category floor (24 of 299). |
| **Report ↔ CSV agreement** | A per-lecture report citing a count that `violations.csv` does not have — i.e. a reviewer edited a mechanical number. |
| **Conventions** | Legacy `W#`/`M#` or `qe-*-A#` rule IDs; a proposed rule cited without its **(proposed)** tag; a `# Style Audit —` title prefix; a `Spec version` line; two-pass or "carry-forward" narrative. |
| **Snapshot** | Reports whose pinned snapshot does not match `snapshot.json`. |

Run it after any agent pass. It exits non-zero on any failure.

---

## Maintaining the contributions & feedback loop

[`contributions/`](contributions/) holds the source behind the four
`action-style-guide` issues
([#18–#21](https://github.com/QuantEcon/action-style-guide/issues/18)) plus 7
ready-to-merge rule drafts. The published [appendix](lectures/appendix.md) is the
reader-facing summary. Keep them consistent.

**Sync rule.** The files in `contributions/issues/` are the issue *bodies*. If you
edit one, re-push it so the record and GitHub agree (mapping: #18←01, #19←02,
#20←03, #21←04):

```bash
gh issue edit <n> --repo QuantEcon/action-style-guide --body-file contributions/issues/<file>.md
```

**When corpus counts change.** The issues and the appendix cite per-rule evidence
counts. Take the new numbers from `lectures/data/rule_reach.csv` — do not re-estimate
them — then update the appendix's proposed-rule table, the affected issue bodies, the
rationale blocks in `contributions/rule-drafts/`, and the lecture count in
`contributions/README.md`. Re-sync the live issues afterwards.

**Lifecycle.** As the team responds:

- *Rule accepted* → per the program direction (coordinated in
  `QuantEcon/project-style-guide`, a private hub), accepted rules are transcribed into
  the consolidated `QuantEcon/style-guide` rule database — the `rule-drafts/` entries
  here are the transcription inputs. Record the outcome in `contributions/README.md`;
  once a rule ships in the registry the checkers consume, drop its **(proposed)** tag
  across the report (`grep -rl '(proposed)' lectures`) and move it out of
  `PROPOSED` in `tools/qestyle_rules.py`.
- *Issue resolved/closed* → record the outcome in `contributions/README.md`.

**New audit period.** `contributions/` is audit-specific — don't copy old issues
forward blind. Open fresh issues only for gaps the new pass surfaces, and reference
any rules adopted since the previous period.

---

## Repository layout

```
audit.2026-05.style-guide/
├── README.md                     repo landing (scoreboard + links)
├── ROADMAP.md                    direction, phases, open decisions
├── UPDATE.md                     this runbook
├── CLAUDE.md                     read-me-first orientation for agents
├── requirements.txt              build deps (pinned; needs Python 3.12+)
├── tools/                        the audit pipeline
│   ├── qestyle_lex.py            MyST lexer (regions: text / code / math / directives)
│   ├── qestyle_rules.py          one function per mechanically-checkable rule
│   ├── qestyle_scan.py           evidence layer → lectures/data/*.csv
│   ├── qestyle_draft.py          drafts every per-lecture report
│   ├── qestyle_score.py          derives overall score + priority; writes scores.csv
│   ├── qestyle_report.py         builds and splices the aggregate tables
│   ├── qestyle_check.py          consistency gate (run before pushing)
│   └── qestyle_toc.py            regenerates lectures/_toc.yml
├── contributions/                source behind the action-style-guide issues (#18–#21)
├── .github/workflows/deploy.yml  build + deploy to GitHub Pages
└── lectures/                     Jupyter Book source (published)
    ├── _config.yml, _toc.yml, _static/
    ├── data/                     the numbers — everything else is derived from these
    │   ├── snapshot.json         pinned corpus commit per series
    │   ├── violations.csv        per lecture, per rule, count
    │   ├── rule_reach.csv        corpus-wide reach per rule
    │   ├── series_rule_reach.csv per-series reach per rule
    │   ├── rule_titles.csv       rule id → title
    │   ├── scores.csv            per-lecture category scores, overall, priority
    │   ├── series_summary.csv    per-series averages + priority counts
    │   ├── history.csv           per-period series scores
    │   └── rule_reach_history.csv per-period rule reach (feeds the trend chart)
    ├── intro.md                  front-page triage      ← spliced in Step 5
    ├── details.md                full findings          ← spliced in Step 5
    ├── charts.md                 visual summary         ← reads data/ at build time
    ├── spec.md                   rubric, methodology, deterministic coverage
    ├── appendix.md               feedback to style guide & action-style-guide
    └── lecture-<series>/
        ├── index.md              series "Summary" rollup   ← Step 4
        └── <stem>.md             one per lecture            ← Steps 2–3
```

---

## Known follow-ups

- `actions/deploy-pages@v4` runs on Node 20 (GitHub deprecation mid-2026) — bump when
  convenient.
- The 6 judgment-only registry rules (spec §9) are the remaining manual cost of a
  pass. `qe-code-001` could plausibly be delegated to `ruff`.
- `qe-math-002` and `qe-writing-004`/`006` are heuristic. The proper-noun and
  common-noun lists in `tools/qestyle_rules.py` are curated from this corpus and will
  need extending as lectures are added.
- `cross_product_trick.md:133` in `lecture-python.myst` still carries a malformed
  `` {eq}`eq:Kalman102} `` reference — worth an issue against that repo.

---

## Starting a new audit period

```bash
NEW=audit.YYYY-MM.style-guide
gh repo create QuantEcon/$NEW --public --clone
# carry forward the machinery and the history, not the findings:
cp -r tools requirements.txt ROADMAP.md UPDATE.md CLAUDE.md .github ../$NEW/
mkdir -p ../$NEW/lectures/data
cp lectures/_config.yml lectures/spec.md lectures/charts.md ../$NEW/lectures/
cp -r lectures/_static ../$NEW/lectures/
cp lectures/data/rule_reach_history.csv lectures/data/history.csv ../$NEW/lectures/data/
# then run Steps 1–8 and enable Pages:
gh api -X POST repos/QuantEcon/$NEW/pages -f build_type=workflow
```

Carrying `rule_reach_history.csv` and `history.csv` forward is what keeps the trend
charts working across periods — they are the only files whose *old* rows matter.
Generate everything else fresh.
