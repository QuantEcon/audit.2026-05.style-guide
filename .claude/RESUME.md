# Resume brief — 2026-08 audit pass

Session state as of the last commit on `claude/project-review-lecture-updates-6o9a2f`.
Everything below is committed and pushed.

## Where the pass stands

| | |
|---|---|
| Corpus | 348 lectures, 5 series, pinned per series in `lectures/data/snapshot.json` |
| Evidence layer | **complete** — 41 checks over all 348, 18,884 findings in `lectures/data/violations.csv` |
| Scoring layer | **complete** — corpus mean 7.75, 197 HIGH / 1 MEDIUM / 108 LOW / 42 NONE |
| Judgment layer | **complete** — 348 of 348; the coverage caveat has retired itself |
| Gate | `All checks passed` — 16 narrative claims + 31 line-width claims cross-checked |
| Build | succeeds on Python 3.12 (`.venv`), **0 warnings** |
| Trend | both snapshots measured with current code; 27 improved, 5 level, 3 worse |

Recompute coverage rather than trusting a number in this file:

```bash
ls reviews/*/*.json | wc -l
for s in lecture-python-intro lecture-python-programming lecture-python.myst \
         lecture-python-advanced.myst lecture-dp; do
  for f in ../quantecon/$s/lectures/*.md; do b=$(basename $f .md)
    [ -f "reviews/$s/$b.json" ] || echo "$s/$b"; done; done
```

## In flight when this was written — read this first

**The pass itself is finished.** All three layers cover all 348 lectures, the gate passes and
the build is clean. What is *not* done is the pull request, and one batch of verified detector
patches that had not yet been applied.

### Three verified patches waiting in `.claude/pending-patches.json`

The final review batch filed three doubts. All three were implemented against the pinned
snapshot in a scratchpad copy, measured in both directions with a `Counter` over
`(line, detail)`, and **every addition was read individually**. Removals are **0** in all
three and every canary held. The exact `patch_old` / `patch_new` text is in that JSON, keyed
by check name, along with the measurement and the canary results.

| Check | Verdict | Measured | Note |
|---|---|---|---|
| `check_math_010` | adopt | 1489 → 1596, +107 / −0 | juxtaposed operator: `\big`-family delimiters, `E \sum` / `E \prod`, `E_t u_{...}` |
| `check_code_002` | adopt-narrowed | 700 → 815, +115 / −0 | Greek word as an identifier *suffix* (`target_mu`, `c_gamma`) |
| `check_ref_001` | adopt | 291 → 330, +39 / −0 | a hand-written author-year followed by its own `{cite}`, rendering the reference twice |

Adversarial refutation of these three was **still running** when this was written. Before
applying, check whether `tools/VERIFICATION.md` already records them — if it does, they
landed and this section is stale. If it does not, apply them, re-measure with the harness in
that file, then run the full refresh, the gate and the build.

### Three things the verification established that are worth not re-deriving

- **The reviewer's `qe-math-010` numbers were bigger than the pattern change justifies**
  because they had silently also widened the per-file `e_is_operator` evidence gate. Their two
  headline lines (`tax_smoothing_3:80`, `un_insure:34`) are *not* reachable by any pattern
  change — those files have no `E[` anywhere, so the whole bare-letter branch is switched off.
  Widening the gate measures +168 / −0 and moves reach 124 → 136, and the 61 extra additions
  were read and are genuine — but it takes seven lectures off a clean 0 on that rule, which
  changes category scores. **That is a scoring decision, not a detector decision, and wants
  its own pass.** Also latent: the gate pattern is a hand-copied duplicate of `applied` that
  lacks the `THIN` steps, so simply reusing `applied` for the gate is worth +1 on its own.
- **The `qe-code-002` doubt's second guard is wrong in every form.** "Skip identifiers the
  file `def`s" deletes the `market_diffusion.md:159` `def mu(self, a)` canary — 8 removals,
  measured — which is the exemption this project has *already* rejected. Narrowed to mixed
  English/Greek names it still deletes 7 HEAD findings; narrowed to distribution names it
  still deletes 4. Do not re-propose it. The cost of dropping it is 45 surviving additions of
  the form `def compute_res_wage_given_beta(β)`, judged real because the rule already counts
  identical HEAD sites. `tv_beta` is **not** a finding — `merging_of_opinions` imports
  `beta as beta_dist`, so the file-level import exemption already excludes it.
- **The one `qe-code-002` false-positive class worth a follow-on is `mu` for *marginal
  utility*** (`ifp_egm.md:556` `def compute_mu_k(k)`, docstring "compute marginal utility").
  12 of the 115 additions, and 4 more already false at HEAD. A surgical gate — skip a
  non-bare `mu` in a cell that binds `u_prime`/`marginal_utility`, in the style of the
  existing `DIST_CALL` gate — measures 815 → 799, reach 71 → 67, and touches nothing else.

### Then: the pull request

Task 6 is the only open deliverable. `main` is the base. The branch is
`claude/project-review-lecture-updates-6o9a2f`. Check for a PR template first
(`.github/pull_request_template.md` and the other three locations) and mirror its headings.
**Do not open it until the gate passes and the build is clean.**

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
      '/lectures/_config.yml' '/style_checker/rules/*.md'
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
