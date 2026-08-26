# Resume brief — 2026-08 audit pass

Session state as of commit `8d64964` on `claude/project-review-lecture-updates-6o9a2f`.
Everything below is committed and pushed; the working tree is clean.

## Where the pass stands

| | |
|---|---|
| Corpus | 348 lectures, 5 series, pinned per series in `lectures/data/snapshot.json` |
| Evidence layer | **complete** — 41 checks over all 348, 18,783 findings in `lectures/data/violations.csv` |
| Scoring layer | **complete** — corpus mean 7.99, 158 HIGH / 1 MEDIUM / 99 LOW / 90 NONE |
| Judgment layer | **229 of 348 reviewed** — 119 to go, queued in `.claude/review-queue.json` |
| Gate | `All checks passed` — 17 hand-written claims cross-checked |
| Build | succeeds on Python 3.12 (`.venv`), 353 pages, 5 charts, **4 warnings** |
| Trend | both snapshots measured with current code; 27 improved, 4 level, 4 worse |

The only unfinished work is the judgment review. Nothing else is waiting on it: the
front-page caveat, the five per-series coverage lines and the scoreboard all regenerate
themselves from whichever overlays exist, so the book is publishable at any coverage level
and says so honestly.

## What the 2026-08-25/26 session changed

**Fourteen verified detector and lexer fixes, every one traced to a reviewer's
`scanner_doubts`.** That is now far and away the most productive source of defects in the
project — read every batch's doubts carefully, and ask reviewers to name the pattern and the
exact input it mishandles.

The `qe-math-002` work is the substantial part. A bare apostrophe is genuinely ambiguous in
this corpus — a transpose in the LQ lectures, a next-period state in the dynamic-programming
ones — so the check now decides **per file** whether the file uses it as a transpose at all,
and an author's **stated convention overrides that heuristic** (`var_dmd` line 75 says the
prime "is part of the name of the matrix"; `arellano` line 147 says it "denotes a next period
value"). Occurrences went 2,129 → 1,612. Also fixed: derivative primes, summation indices,
second derivatives, `)'` before a parenthesised factor, superscripted `C^{'}`, and the
`^\prime` spelling of the next-period case.

Others: `qe-math-010` was blind to `\mathbb E_t` because `\b` cannot fire before a
subscript; `qe-math-011` missed `{\mathcal N}`; `qe-code-002` counted imported names like
`scipy.stats.beta`; `qe-ref-001`'s `see`/`include` exemption was dead code; `_is_proper`
rejected `Student-t`; and a single stray backtick in `five_preferences` was masking 381 of
its 798 narrative lines because `` [^`] `` matches newlines and made the paragraph-break
guard unreachable.

**Read `tools/VERIFICATION.md` before "fixing" anything here.** It records all of it, plus a
*Known limitations, accepted deliberately* section and — just as important — three fixes that
were **verified and then rejected** because they deleted real findings. Two `qe-writing-004`
exemptions and one `qe-ref-001` line-break repair. Do not re-propose them.

**Two things about measurement**, both of which caught me out:

- Judge every fix in **both directions**. Removing false positives is worthless if it also
  removes true positives, and twice a fix that measured well in aggregate was deleting
  genuine findings. Keep a canary list of real findings that must survive.
- **De-duplicating hits into a set will lie to you.** Every `\prime transpose` match on a
  line carries an identical detail string, so a set collapses them and a −8 change reads as
  −380. Count occurrences with `qestyle_scan`, not with a Python set.

The gate grew two checks that exist because prose went stale after a rule fix: it now holds
hand-written tables *and* the trend sentence's own tallies to `rule_reach_history.csv`. It
has caught me three times since. Separately, `escape_roles()` renders MyST roles in reviewer
prose literally, which took the build from 478 warnings to 4 — if that count climbs with
coverage again, that function is what regressed.

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
