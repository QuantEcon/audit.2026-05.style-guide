# Resume brief — 2026-08 audit pass

Session state as of commit `5b31e36` on `claude/project-review-lecture-updates-6o9a2f`.
Everything below is committed and pushed; the working tree is clean.

## Where the pass stands

| | |
|---|---|
| Corpus | 348 lectures, 5 series, pinned per series in `lectures/data/snapshot.json` |
| Evidence layer | **complete** — 41 checks over all 348, 19,076 findings in `lectures/data/violations.csv` |
| Scoring layer | **complete** — corpus mean 8.03, 153 HIGH / 1 MEDIUM / 102 LOW / 92 NONE |
| Judgment layer | **189 of 348 reviewed** — 159 to go, queued in `.claude/review-queue.json` |
| Gate | `All checks passed` |
| Build | succeeds on Python 3.12 (`.venv`), 353 pages, 5 charts |
| Trend | 2026-05 and 2026-08 both measured with today's code; 27 rules improved, 5 level, 3 worse |

The only unfinished work is the judgment review. Nothing else is waiting on it: the
front-page caveat, the five per-series coverage lines and the scoreboard all regenerate
themselves from whichever overlays exist, so the book is publishable at any coverage level
and says so honestly.

## What the 2026-08-25 session changed

Five verified detector fixes came out of reviewer `scanner_doubts`, which is now the most
productive source of defects in the project — worth reading every batch's doubts carefully.

- **`qe-math-010`** was undercounting: `[PEV]\b` never fires before a subscript, because
  `_` is a word character, so `\mathbb E_t` — the corpus's usual conditional expectation —
  was invisible. Its Roman branch also missed `\textrm{…}`, `{\rm …}` and `Prob`.
  Reach 105 → 117.
- **`qe-math-011`**'s bare-`\mathcal` alternative did not consume its closing brace, so
  `{\mathcal N}(0,1)` failed the distribution-context gate. Reach 24 → 34.
- **`qe-math-002`** had three false-positive classes, all guards a sibling branch already
  had: no guard at all on `^\prime`, no relation guard on `prime_vec`, and no
  double-prime exclusion. Occurrences 2,129 → 1,865.

Both snapshots were re-measured after each fix, so the trend is still like-for-like.
`tools/VERIFICATION.md` carries the details, plus a *Known limitations, accepted
deliberately* section listing what was left and why — read it before "fixing" something
there.

The gate also grew a `narrative-claims` check that holds hand-written tables to
`rule_reach_history.csv`, and the `intro.md` coverage caveat is now a generated
`<!-- qe:review-coverage -->` block rather than two hand-typed figures.

## Resuming the review — one agent, many sessions

**Run a single review agent at a time.** Not a fan-out. Two concurrent agents burned
through a session limit in under half an hour, and a run that dies mid-batch leaves the
repo in a state someone has to reason about. One agent is slower per hour and strictly
more predictable, which is what matters when the work spans sessions.

And it does span sessions. Measured on this box: **one overlay per ~5 agent-minutes**, so
the 179 remaining are roughly **14 hours of single-agent work** — four to six sessions, not
one. No concurrency setting changes that total; it only changes how much gets wasted when a
session ends mid-flight. So do not try to finish. Aim to end every session with durable,
consistent, pushed state and the next resume already scheduled.

The architecture is built for exactly this, so use it:

- **`reviews/<series>/<stem>.json` is the durable unit.** Commit overlays in batches of
  about ten, with a plain message (`Review 10 more advanced lectures`). An overlay is worth
  keeping the moment it is written — it does not need the reports regenerated to be useful,
  and a later session folds it in.
- **Everything else is derived**, so it costs nothing to redo. Run the refresh below **once
  per session**, at the end, rather than after every batch: it rewrites all 348 reports and
  a diff that size per batch buries the actual work.
- **Before the session budget runs out**, run the refresh, the gate and the build, commit,
  push, and schedule the next resume with `send_later`. Leaving overlays committed but
  unfolded is fine and safe; leaving the tree dirty is not.


1. **Get the corpus back** — the container is ephemeral, so it will be gone. Clone it
   **inside this repo**, at `.corpus/` (gitignored), not at `../quantecon`:

```bash
CORPUS=.corpus; mkdir -p $CORPUS
for r in lecture-python-intro lecture-python-programming lecture-python.myst \
         lecture-python-advanced.myst lecture-dp action-style-guide; do
  git clone --depth 1 --filter=blob:none --sparse \
      https://github.com/QuantEcon/$r $CORPUS/$r
  git -C $CORPUS/$r sparse-checkout set --no-cone '/lectures/*.md' \
      '/lectures/_config.yml' '/style_checker/rules/*.md'
done
```

   Then check each series out at the commit `lectures/data/snapshot.json` pins — the
   snapshot is what makes this pass reproducible, and the gate fails if a report's
   snapshot line disagrees with it.

   `UPDATE.md` § *Getting the corpus* uses `../quantecon` and is still the convention for
   an interactive run. In-repo is for **this** resume specifically: it fires unattended, and
   a path under the working directory needs no permission prompt, so the run cannot stall
   on one with nobody there to answer. Every tool takes `--corpus`, so the path is free.
   The `../quantecon-2026-05` worktrees are only needed to re-measure the trend, which this
   resume does not do.
2. **Do not depend on auto mode.** With the corpus in `.corpus/` you do not need it. If you
   do find yourself reading outside the working directory and being denied, that is the
   cause — move the clone rather than waiting for an approval that is not coming.
3. **Fan out** over `.claude/review-queue.json`, which lists the 179 unreviewed lectures
   **worst-scoring first within each series**, series ordered by how much coverage they
   still need. `lecture-python-advanced.myst` (52 left) is the priority: it is the series
   the evidence calls weakest, so its scores are the least trustworthy while coverage is
   thin. Reviewer instructions are in `.claude/skills/audit-pass/SKILL.md` § *Step 3*;
   spec §8.3 is what the reviewer must read first.
   Give one agent a batch of about ten and let it finish before starting the next, so a
   session that ends abruptly loses at most one batch.
4. **Fold in and regenerate** — never hand-edit a number:

```bash
CORPUS=.corpus; R=$CORPUS/action-style-guide/style_checker/rules
python3 tools/qestyle_draft.py --corpus $CORPUS --out lectures --date 2026-08-25 \
    --rules $R --reviews reviews --judgment-csv lectures/data/judgment.csv
python3 tools/qestyle_score.py --root lectures --fix --csv lectures/data/scores.csv
python3 tools/qestyle_report.py --summarise --history 2026-08 --splice
python3 tools/qestyle_check.py --root lectures --data lectures/data --corpus $CORPUS
```

5. **Build**, then commit and push to the same branch.
6. **Re-arm.** If coverage is not finished, `send_later` the next resume before ending the
   turn, pointing at this file again. If it *is* finished — the front-page caveat will say
   so itself, having switched to "every one of the 348 lectures has been through the
   judgment layer" — then open the PR against `main`. The user has asked for it once the
   pass is ready, and not before: it should describe a finished pass.

## What is still open when coverage lands

- **Rename to `audit-lectures-style-guide`** — [#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2).
  `_config.yml` plus 16 Pages URLs change **with** the rename, not before.
- **Review-coverage comparability** — [#5](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/5).
  Finishing the fan-out closes it, and the generated caveat retires itself when it does.
- **`contributions/issues/*.md` need re-syncing** to live `action-style-guide` issues
  #18–#21 by someone whose session has access to that repo; this one does not.
- **`contributions/issues/05-rule-format-for-checkability.md`** has no home issue yet.

## Two things not to re-learn

- **Never hand-edit a number.** `qestyle_check.py` now also verifies the hand-written
  tables — the `intro.md` trend row and any counts table whose header names *Lectures* and
  *Occurrences* — against `rule_reach_history.csv`. It cannot check a number written into a
  sentence, so re-read those by hand after any rule change.
- **A detector fix is not a corpus improvement.** Two 2026-05 history rows had to be
  dropped because they were measured before their checks were fixed, which made them look
  like the corpus had improved to zero. Re-measure both snapshots with the same code.
