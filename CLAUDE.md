# CLAUDE.md

Guidance for Claude Code (and other agents) working in this repo. Keep it short — the
authoritative detail lives in `UPDATE.md`, `lectures/spec.md` and `ROADMAP.md`; this file
is the read-me-first orientation and the guardrails.

## What this is

The **single source of truth** for the QuantEcon lecture style audit. It's a Jupyter Book
published to GitHub Pages (<https://quantecon.github.io/audit.2026-05.style-guide/>),
built from `lectures/` by `.github/workflows/deploy.yml` on every push to `main`.

## Read first

- **`/audit-pass`** — the skill that drives a full pass end to end
  (`.claude/skills/audit-pass/SKILL.md`). Start here for the *how*; it carries the
  step order, the resumable review loop, and the traps that have actually cost time.
- **[`UPDATE.md`](UPDATE.md)** — the runbook: how to run a pass, the consistency gate, how
  to maintain `contributions/`, how to start a new audit period. **Follow it before any
  structural change.**
- **[`lectures/spec.md`](lectures/spec.md)** §8–§10 — the pass methodology (evidence /
  scoring / review layers), the measured deterministic coverage, and the exact commands.
- **[`ROADMAP.md`](ROADMAP.md)** — direction and the open decisions, including the
  unresolved repo-naming question.
- **`QuantEcon/project-style-guide`** (private hub) — program-level direction. Where this
  repo's docs and the hub overlap, **the hub is the home of record**.

## The one thing to understand

**The numbers are not written, they are derived.** `lectures/data/*.csv` is the source:
`tools/qestyle_scan.py` measures the corpus into it, and the per-lecture reports, the
scoreboard, the triage page and the charts are all generated from it.

```
corpus snapshot → qestyle_scan → data/*.csv → qestyle_draft → per-lecture reports
                                            → qestyle_score → scores.csv
                                            → qestyle_report → spliced tables
                                            → qestyle_check  → the gate
```

So: **never hand-edit a number.** If a count looks wrong, fix the check in
`tools/qestyle_rules.py` and re-run — editing the report instead makes it disagree with
the CSVs, and `tools/qestyle_check.py` will fail.

## Non-negotiable conventions

Enforce everywhere. `tools/qestyle_check.py` asserts all of these; run it before pushing.

- **Rule IDs:** canonical `qe-*` only (e.g. `qe-fig-001`). Never legacy `W#`/`M#` or
  `qe-*-A#` placeholders.
- **Proposed rules:** the 7 not-yet-registered rules (`qe-writing-009`,
  `qe-math-010`–`qe-math-015`) always carry a **(proposed)** tag where cited. A section
  that is itself about the proposed rules need not repeat the tag on every row.
- **Titles:** per-lecture report H1 = bare lecture stem (`# lqcontrol`); each series
  `index.md` H1 = `# Summary`. No `# Style Audit —` prefix.
- **No `Spec version` line** in report headers. Every report header *does* carry a
  **Corpus snapshot** line naming the commit it was measured against.
- **JAX is out of scope** — distinct from `N/A` ("not applicable to this lecture").
- **One pass, no process narrative.** A report describes the corpus at one pinned
  snapshot; it never narrates how the pass was run in "v1/v2" or "two-pass" terms.
  Comparing *against a previous period* is different and is wanted — that is what
  `data/rule_reach_history.csv` and the trend chart are for.
- **Spliced regions are generated.** Anything between `<!-- qe:NAME -->` and
  `<!-- /qe:NAME -->` is overwritten by `tools/qestyle_report.py --splice`. Write prose
  outside the markers.

## Operational gotchas

- **The build needs Python 3.12+.** `quantecon-book-theme==0.15.1` requires it; a 3.11
  environment fails to resolve. Build is vanilla `jupyter-book` +
  `quantecon-book-theme` — *not* the QuantEcon build container. `lectures/charts.md`
  executes at build time and reads `lectures/data/`, so `matplotlib`/`numpy` must stay in
  `requirements.txt`.
- **The corpus is not in this repo.** Clone the 5 series plus `action-style-guide` as
  blobless sparse checkouts (`UPDATE.md` § Getting the corpus) — a few MB each, because
  only `lectures/*.md` is needed. Do not clone them whole.
- **Reading the corpus needs auto mode ON** if you fan work out to subagents; otherwise
  every cross-repo read is denied and the run stalls. This stalled the original run once.
- **`lecture-dp` syncs lectures from `lecture-python.myst`** (`cross_product_trick`,
  `ifp_advanced`, `inventory_q`, `rs_inventory_q`, …). Their findings appear twice in the
  corpus totals; fix upstream and both clear.
- **`contributions/` mirrors live `action-style-guide` issues #18–#21.** Edit a body here →
  re-sync with `gh issue edit` (see `UPDATE.md`). That repo is not attached to this
  session's GitHub access, so a re-sync has to be done by someone who has it.
- **Pushing to `main` deploys the site.** Only push when the change is ready; watch the run
  with `gh run watch`.

## Layout

- `tools/` — the pipeline: `qestyle_lex` (MyST lexer) · `qestyle_rules` (one function per
  checkable rule) · `qestyle_scan` (evidence) · `qestyle_draft` (report drafts) ·
  `qestyle_score` (scores) · `qestyle_report` (aggregate tables) · `qestyle_check` (gate) ·
  `qestyle_toc`
- `lectures/` — published book: `intro` (triage) · `details` · `charts` · `spec` ·
  `appendix` · `data/` (the numbers) · `lecture-<series>/` (`index` = Summary +
  per-lecture reports)
- `contributions/` — issue bodies + rule drafts (root, not published)
- `.claude/skills/audit-pass/` — the pass skill; keep it in step with `UPDATE.md`
- `README.md` · `ROADMAP.md` · `UPDATE.md` · `CLAUDE.md` — root docs

## Commits

Follow the global commit conventions (co-author trailer; neutral cross-repo issue
references — no closing keywords before `owner/repo#N`). Commit/push only when asked.
