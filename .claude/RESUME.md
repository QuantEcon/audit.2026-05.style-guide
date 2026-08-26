# Resume brief — 2026-08 audit pass

Session state as of the last commit on `claude/project-review-lecture-updates-6o9a2f`.
Everything below is committed and pushed.

## Where the pass stands

| | |
|---|---|
| Corpus | 348 lectures, 5 series, pinned per series in `lectures/data/snapshot.json` |
| Evidence layer | **complete** — 41 checks over all 348, 19,101 findings in `lectures/data/violations.csv` |
| Scoring layer | **complete** — corpus mean 7.74, 197 HIGH / 1 MEDIUM / 108 LOW / 42 NONE |
| Judgment layer | **complete** — 348 of 348; the coverage caveat has retired itself |
| Gate | `All checks passed` — 16 narrative claims + 31 line-width claims cross-checked |
| Build | succeeds on Python 3.12 (`.venv`), **0 warnings** |
| Trend | both snapshots measured with current code; 26 improved, 5 level, 4 worse |

Recompute coverage rather than trusting a number in this file:

```bash
ls reviews/*/*.json | wc -l
for s in lecture-python-intro lecture-python-programming lecture-python.myst \
         lecture-python-advanced.myst lecture-dp; do
  for f in ../quantecon/$s/lectures/*.md; do b=$(basename $f .md)
    [ -f "reviews/$s/$b.json" ] || echo "$s/$b"; done; done
```

## Where this leaves the pass

**The audit itself is finished.** All three layers cover all 348 lectures, both snapshots are
measured with the same code, the gate passes and the build is clean. The **pull request is the
only open deliverable** — task 6. Base is `main`; check for a PR template in the four usual
locations and mirror its headings.

The last three reviewer doubts were adjudicated after adversarial refutation; the verdicts and
their reasoning are in the "last three doubts" section of `tools/VERIFICATION.md`.
`.claude/pending-patches.json` is kept only as the starting point for the one that was
rejected. Two things carried forward from it:

- **`qe-math-010`'s `e_is_operator` gate is still narrow.** Widening it to accept the
  juxtaposed evidence measures +168 / −0 and moves reach 124 → 136; the 61 extra additions
  were read and are genuine. It takes seven lectures off a clean 0 on that rule, so it changes
  category scores — a **scoring** decision, not a detector one, and it wants its own pass.
  Related: the gate pattern is a hand-copied duplicate of `applied`. Reusing `applied`
  verbatim is +27 findings and reach 124 → 129 on its own, because `applied` also accepts `(`.
- **`qe-ref-001`'s author-year duplication is real, and now unblocked.** Prose that writes
  "Shavell and Weiss (1979)" and then adds a plain `{cite}` for the same work prints the
  reference twice. 34 of 39 candidate sites are genuine; 3 have an in-text year that does not
  match the cited entry, so the prescribed fix would misdate the sentence. That was first
  written up as unverifiable for want of a bibliography — **wrong**: the `.bib` is not absent,
  only unchecked-out, and `git -C <corpus>/lecture-python-advanced.myst sparse-checkout add
  '/lectures/_static/*.bib'` produces it. Both false positives are now confirmed against the
  real entries. **This is the top follow-up.** The work is to write the branch the filed patch
  never contained, gate it on the in-text year equalling the entry's year, and handle the
  possessive (`Ryoo and Rosen's (2004)`, where `{cite:t}` cannot emit "'s") and markup
  (`**Black-Litterman** (1992)`, a model name) classes.

## The one thing to understand about this pass

**Reviewer `scanner_doubts` are the most productive source of defects in the project.**
Around thirty verified detector and lexer fixes have come from them, and none from any other
source. Read every batch's doubts carefully; ask reviewers to name the pattern *and* the exact
input it mishandles, and to measure their proposed fix in both directions.

**Read `tools/VERIFICATION.md` before "fixing" anything.** It records every fix, the 8 lexer
bugs, a *Known limitations, accepted deliberately* section, and — just as important — the
fixes that were **verified and then rejected** because they deleted real findings. Do not
re-propose those.

### Four measurement traps, each of which has cost real time here

- **Judge every fix in both directions.** Removing false positives is worthless if it also
  removes true positives. Keep a canary list of real findings that must survive. Twice a fix
  that measured well in aggregate was deleting genuine ones.
- **A removal is a set difference between the two rules' hits** — not "everything the new rule
  does not flag". A query built the wrong way reported 256 lost `qe-fig-008` findings; every
  one of them carried `lw=` and so had never been a hit under either version.
- **De-duplicating hits into a set will lie to you.** Identical detail strings collapse, and
  an 8-occurrence change reads as 380. Count occurrences, not set members.
- **A one-character placeholder reads as an initial.** Substituting a link or inline maths with
  `"X"` made the following full stop look like it followed an initial, so sentence detection
  stopped. This has now bitten twice, in `_count_sentences` and in `check_fig_004`. Both sites
  carry the lesson in a comment.

And two about regexes: an optional-brace pattern like `\{?…\}?` lets the engine backtrack past
your guard, so use an explicit alternation; and a lookahead placed after an *optional* group
can be defeated the same way — check the text after the match instead (`tag_proposed` does).

## The pipeline

```
corpus snapshot → qestyle_scan → data/*.csv → qestyle_draft → per-lecture reports
                                            → qestyle_score → scores.csv
                                            → qestyle_report → spliced tables
                                            → qestyle_check  → the gate
```

`reviews/<series>/<stem>.json` is the durable unit and is deliberately decoupled from the
counts, so fixing a check and re-running never destroys review work. Everything else is
derived, so it costs nothing to redo — run the refresh **once per session, at the end**, not
per batch.

### Refresh, both snapshots, gate, build

```bash
CORPUS=../quantecon; R=$CORPUS/action-style-guide/style_checker/rules
.venv/bin/python tools/qestyle_scan.py --corpus $CORPUS --out lectures/data \
    --period 2026-08 --append-history lectures/data/rule_reach_history.csv
# Re-measure the previous snapshot with the SAME code, or a detector fix reads as a
# corpus improvement. This is not optional after any rule change.
.venv/bin/python tools/qestyle_scan.py --corpus ../quantecon-2026-05 --out /tmp/d05 \
    --period 2026-05 --append-history lectures/data/rule_reach_history.csv
.venv/bin/python tools/qestyle_draft.py --corpus $CORPUS --out lectures --date 2026-08-26 \
    --rules $R --reviews reviews --judgment-csv lectures/data/judgment.csv
.venv/bin/python tools/qestyle_score.py --root lectures --fix --csv lectures/data/scores.csv
.venv/bin/python tools/qestyle_report.py --summarise --history 2026-08 --splice
.venv/bin/python tools/qestyle_check.py --root lectures --data lectures/data --corpus $CORPUS
.venv/bin/jupyter-book build lectures --path-output /tmp/bk   # 0 warnings expected
```

The build is clean. **Any warning means something regressed**, and `escape_roles()` in
`qestyle_draft.py` is the usual cause: it renders MyST roles in reviewer prose literally, and
it took this build from 478 warnings to 0. Its two failure modes are both in
`tools/VERIFICATION.md`: a role name outside its allowlist, and an unbounded target that runs
away across a stray backtick.

## Getting the corpus back

The container is ephemeral, so the corpus will be gone. `UPDATE.md` § *Getting the corpus*
uses `../quantecon`, which is what every command above assumes. If the session will run
**unattended**, clone into `.corpus/` (gitignored) instead — a path under the working
directory needs no permission prompt, so the run cannot stall on one with nobody there to
answer. Every tool takes `--corpus`, so the path is free.

```bash
CORPUS=../quantecon; mkdir -p $CORPUS
for r in lecture-python-intro lecture-python-programming lecture-python.myst \
         lecture-python-advanced.myst lecture-dp action-style-guide; do
  git clone --depth 1 --filter=blob:none --sparse \
      https://github.com/QuantEcon/$r $CORPUS/$r
  git -C $CORPUS/$r sparse-checkout set --no-cone '/lectures/*.md' \
      '/lectures/_config.yml' '/lectures/_static/*.bib' '/style_checker/rules/*.md'
done
```

Then check each series out at the commit `lectures/data/snapshot.json` pins — the snapshot is
what makes this pass reproducible, and the gate fails if a report disagrees with it. The
`../quantecon-2026-05` worktrees are needed for the trend re-measure above.

## Pace, if there is review work left

Measured here: **one overlay per ~5 agent-minutes**. Three concurrent agents on *disjoint
series* worked well once the session had headroom — disjoint is the important part, because
agents writing into the same directory contend, and cross-file family findings need one agent
to see the whole series. Give each a batch of about ten. Commit each batch. An overlay is
useful the moment it is written; tell every agent to **write each file as soon as it finishes
that lecture**, because an API error mid-batch has cost a whole batch before.

Re-arm a `send_later` resume **only if a session limit is what stopped you**. It exists to
carry work across a credit window, not to keep a standing appointment.

## What is still open

- **Rename to `audit-lectures-style-guide`** — [#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2).
  `_config.yml` plus 16 Pages URLs change **with** the rename, not before.
- **Review-coverage comparability** — [#5](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/5).
  The caveat in `intro.md` is generated and retires itself when coverage lands.
- **`contributions/issues/*.md` need re-syncing** to live `action-style-guide` issues #18–#21
  by someone whose session has access to that repo; this one does not.
- **Three contribution drafts have no home issue yet** — `05-rule-format-for-checkability`,
  `06-ref-001-author-name-citations`, `07-fig-008-line-width-tolerance`. The last two are
  rule-*definition* questions: places where the checker deliberately answers a narrower
  question than the rule asks. Both cost each reading, so whoever answers can see the choice.
- **Known limitations** are listed in `tools/VERIFICATION.md`. The live one worth knowing:
  caption maths sits in an `option` region that no math rule reads.
