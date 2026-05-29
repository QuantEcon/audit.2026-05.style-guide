# Appendix — feedback to the style guide & action-style-guide

This audit doesn't just score lectures — it also feeds back into the tooling and conventions it scores against. This page summarises that feedback. The source material (issue bodies, ready-to-merge rule entries) lives in the repo under [`contributions/`](https://github.com/QuantEcon/audit.2026-05.style-guide/tree/main/contributions).

## How the pieces fit

- The **[QuantEcon manual style guide](https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide)** is the human-readable source of conventions.
- **[`action-style-guide`](https://github.com/QuantEcon/action-style-guide)** is the tool that enforces them — a registry of `qe-*` rules checked at PR time. This audit scores lectures against that registry (see the [scoring spec](spec.md)).
- Where the audit found a convention in the manual that **isn't yet a coded rule**, or a way to make the tool **catch more, faster**, it became feedback. Four issues capture it.

## Four issues opened

| Issue | What it proposes |
|-------|------------------|
| [#18 — 7 new style rules](https://github.com/QuantEcon/action-style-guide/issues/18) | Encode 7 conventions the manual documents but the registry is missing (see table below). |
| [#19 — Phase 4.3 acceleration](https://github.com/QuantEcon/action-style-guide/issues/19) | Extend the planned deterministic-checker scope from ~13 to **22 rules**, prioritised by audit-measured frequency, with this corpus as regression-test data. |
| [#20 — bulk-audit mode](https://github.com/QuantEcon/action-style-guide/issues/20) | A design discussion: should cross-series scoring / synthesis (what produced this report) live inside `action-style-guide`, a sibling tool, or stay ad-hoc? |
| [#21 — corpus offer](https://github.com/QuantEcon/action-style-guide/issues/21) | Offers this 299-lecture labelled corpus as test / evaluation fixtures for the tool. No action required. |

## Proposed new rules (issue #18)

Seven conventions documented in the manual but not yet in the registry. They appear throughout this report tagged **(proposed)**. The five strong-evidence rules are recommended for adoption; the last two are weaker-evidence and may be deferred.

| Proposed ID | Convention | Corpus evidence |
|-------------|-----------|-----------------|
| `qe-writing-009` | Write "IID", not "i.i.d." / "iid" | ~30 lectures |
| `qe-math-010` | `\mathbb{P}` / `\mathbb{E}` / `\mathbb{V}` (with braces) for probability, expectation, variance | ~60 lectures |
| `qe-math-011` | Plain letters for distribution names (`N`, not `\mathcal{N}`) | ~30 lectures |
| `qe-math-012` | `\cdot` or juxtaposition for multiplication — never `*` | ~5 lectures |
| `qe-math-013` | Reference equations via `` {eq}`label` `` | moderate |
| `qe-math-014` *(weaker)* | Braces `\{…\}` for events, parentheses `(…)` for sets under `\mathbb{P}` | limited |
| `qe-math-015` *(weaker)* | Lowercase for densities/PMFs, uppercase for CDFs | limited |

Ready-to-merge rule entries for each are in [`contributions/rule-drafts/`](https://github.com/QuantEcon/audit.2026-05.style-guide/tree/main/contributions/rule-drafts).

## Direct feedback to a lecture repo

Two findings are build-breaking and were flagged for `lecture-python.myst` regardless of the tooling discussion (also on the [front page](intro.md#fix-immediately)):

- [`divergence_measures.md:134`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/divergence_measures.md#L134) — `\begin{align}` inside `$$` (breaks the PDF build).
- [`cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/cross_product_trick.md#L133) — broken `{eq}` reference.

## Status

All four issues are open and awaiting team response. If #18 is accepted, the `rule-drafts/` entries go in as a single PR to `action-style-guide`. See [`contributions/README.md`](https://github.com/QuantEcon/audit.2026-05.style-guide/blob/main/contributions/README.md) for the current status and next steps.
