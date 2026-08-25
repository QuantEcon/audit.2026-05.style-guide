# Resume brief — 2026-08 audit pass

Session state as of commit `c0fb7fc` on `claude/project-review-lecture-updates-6o9a2f`.
Everything below is committed and pushed; the working tree is clean.

## Where the pass stands

| | |
|---|---|
| Corpus | 348 lectures, 5 series, pinned per series in `lectures/data/snapshot.json` |
| Evidence layer | **complete** — 41 checks over all 348, all 19,057 findings in `lectures/data/violations.csv` |
| Scoring layer | **complete** — corpus mean 8.06, 148 HIGH / 3 MEDIUM / 108 LOW / 89 NONE |
| Judgment layer | **169 of 348 reviewed** — 179 to go, queued in `.claude/review-queue.json` |
| Gate | `All checks passed` |
| Trend | 2026-05 and 2026-08 both measured with today's code; 27 rules improved, 5 level, 3 worse |

The only unfinished work is the judgment review. Nothing else is waiting on it: the
front-page caveat, the five per-series coverage lines and the scoreboard all regenerate
themselves from whichever overlays exist, so the book is publishable at any coverage level
and says so honestly.

## Resuming the fan-out

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
   Concurrency is capped at `min(16, nproc - 2)` **per workflow** — 2 on a 4-CPU box, so
   split into several workflows if you want more agents.
4. **Fold in and regenerate** — never hand-edit a number:

```bash
CORPUS=../quantecon; R=$CORPUS/action-style-guide/style_checker/rules
python3 tools/qestyle_draft.py --corpus $CORPUS --out lectures --date 2026-08-25 \
    --rules $R --reviews reviews --judgment-csv lectures/data/judgment.csv
python3 tools/qestyle_score.py --root lectures --fix --csv lectures/data/scores.csv
python3 tools/qestyle_report.py --summarise --history 2026-08 --splice
python3 tools/qestyle_check.py --root lectures --data lectures/data --corpus $CORPUS
```

5. **Build**, then commit and push to the same branch. The PR against `main` is the last
   step and has deliberately **not** been opened yet — it should describe a finished pass.

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
