# CLAUDE.md

Guidance for Claude Code (and other agents) working in this repo. Keep it short — the authoritative detail lives in `UPDATE.md` and `ROADMAP.md`; this file is the read-me-first orientation and the guardrails.

## What this is

The **single source of truth** for the QuantEcon **May 2026 style audit**. It's a Jupyter Book published to GitHub Pages (<https://quantecon.github.io/audit.2026-05.style-guide/>), built from `lectures/` by `.github/workflows/deploy.yml` on every push to `main`.

## Read first

- **[`UPDATE.md`](UPDATE.md)** — the runbook: how to re-run the audit, refresh the documents, maintain `contributions/`, and start a new audit period. **Follow it before any structural change.**
- **[`ROADMAP.md`](ROADMAP.md)** — direction and open decisions (durable-vs-disposable, dashboard, cadence).

## Non-negotiable conventions

Enforce everywhere — these were deliberately applied and are easy to regress on a re-run. `UPDATE.md` has the residue-check commands and cleanup one-liners.

- **Rule IDs:** canonical `qe-*` only (e.g. `qe-fig-001`). Never legacy `W#`/`M#` or `qe-*-A#` placeholders.
- **Proposed rules:** the 7 not-yet-registered rules (`qe-writing-009`, `qe-math-010`–`qe-math-015`) always carry a **(proposed)** tag wherever cited.
- **One audit, no process narrative:** the report reads as a single audit. No "v1/v2", "two-pass", or "carry-forward" wording.
- **Titles:** per-lecture report H1 = bare lecture stem (`# lqcontrol`); each series `index.md` H1 = `# Summary`. No `# Style Audit —` prefix.
- **No `Spec version` line** in report headers.
- **JAX is out of scope** — distinct from `N/A` ("not applicable to this lecture").

## Operational gotchas

- **Re-running the audit fans out one subagent per series, and they must read the lecture repos + `action-style-guide` rule files (outside this repo).** Subagents can only do that with **auto mode ON** — otherwise every cross-repo read is denied (this stalled the original run once).
- **Build is vanilla `jupyter-book` + `quantecon-book-theme`** (pinned in `requirements.txt`) — *not* the QuantEcon build container. Charts in `lectures/charts.md` execute at build time, so `matplotlib`/`numpy` must stay in `requirements.txt`.
- **`contributions/` mirrors live `action-style-guide` issues #18–#21.** Edit an issue body here → re-sync with `gh issue edit` (see `UPDATE.md` § Maintaining the contributions & feedback loop).
- **Pushing to `main` deploys the site.** Only push when the change is ready; watch the run with `gh run watch`.

## Layout

- `lectures/` — published book: `intro` (triage) · `details` · `charts` · `spec` · `appendix` · `lecture-<series>/` (`index` = Summary + per-lecture reports)
- `contributions/` — issue bodies + rule drafts (root, not published)
- `README.md` · `ROADMAP.md` · `UPDATE.md` · `CLAUDE.md` — root docs

## Commits

Follow the global commit conventions (co-author trailer; neutral cross-repo issue references — no closing keywords before `owner/repo#N`). Commit/push only when asked.
