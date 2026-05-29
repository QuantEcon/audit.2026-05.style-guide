# Contributions to action-style-guide

Feedback this audit fed back to [QuantEcon/action-style-guide](https://github.com/QuantEcon/action-style-guide) and the [QuantEcon style guide](https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide). This folder is the source material behind the four issues opened from the May 2026 audit; the reader-facing summary is the [Feedback appendix](../lectures/appendix.md) in the report.

## Issues posted

All four are open on `action-style-guide`. The files here are the bodies as posted (kept in sync).

| Issue | Title | Body | Type |
|-------|-------|------|------|
| [#18](https://github.com/QuantEcon/action-style-guide/issues/18) | Proposal: 7 new style rules surfaced by lecture audit | [`issues/01-new-style-rules.md`](issues/01-new-style-rules.md) | Concrete proposal |
| [#19](https://github.com/QuantEcon/action-style-guide/issues/19) | Phase 4.3 acceleration: 22 deterministic-check candidates + corpus test data | [`issues/02-phase-4-3-deterministic-checks.md`](issues/02-phase-4-3-deterministic-checks.md) | Extension of existing plan |
| [#20](https://github.com/QuantEcon/action-style-guide/issues/20) | Discussion: bulk audit / cross-series synthesis mode — where should it live? | [`issues/03-bulk-audit-mode.md`](issues/03-bulk-audit-mode.md) | Design question |
| [#21](https://github.com/QuantEcon/action-style-guide/issues/21) | Offer: 299-lecture corpus with labelled violations as test fixtures | [`issues/04-corpus-offer.md`](issues/04-corpus-offer.md) | Resource offer |

## Rule entry drafts

Each file under [`rule-drafts/`](rule-drafts/) holds one proposed rule in action-style-guide's rules-file format (Type / Title / Description / Check for / Examples), ready to append to `style_checker/rules/<category>-rules.md` once the team accepts it. **Not yet submitted as a PR** — pending discussion on issue [#18](https://github.com/QuantEcon/action-style-guide/issues/18).

| Proposed ID | Category | File | Evidence |
|-------------|----------|------|----------|
| `qe-writing-009` | writing | [`rule-drafts/qe-writing-009-IID.md`](rule-drafts/qe-writing-009-IID.md) | Strong (~30 lectures) |
| `qe-math-010` | math | [`rule-drafts/qe-math-010-blackboard-PEV.md`](rule-drafts/qe-math-010-blackboard-PEV.md) | Very strong (~60 lectures) |
| `qe-math-011` | math | [`rule-drafts/qe-math-011-distribution-naming.md`](rule-drafts/qe-math-011-distribution-naming.md) | Strong (~30 lectures) |
| `qe-math-012` | math | [`rule-drafts/qe-math-012-multiplication.md`](rule-drafts/qe-math-012-multiplication.md) | Moderate, clear rule |
| `qe-math-013` | math | [`rule-drafts/qe-math-013-equation-refs.md`](rule-drafts/qe-math-013-equation-refs.md) | Moderate |
| `qe-math-014` | math | [`rule-drafts/qe-math-014-events-vs-sets.md`](rule-drafts/qe-math-014-events-vs-sets.md) | Weaker — lower priority |
| `qe-math-015` | math | [`rule-drafts/qe-math-015-density-CDF-case.md`](rule-drafts/qe-math-015-density-CDF-case.md) | Weaker — lower priority |

Each rule-draft has two sections: the **rule entry** (ready to paste into the rules file) and the **rationale** (for the issue / PR discussion, not the rules file).

## Status & next steps

- **#18 (new rules)** — awaiting team response. If accepted, submit the `rule-drafts/` entries as a single PR against `style_checker/rules/writing-rules.md` and `math-rules.md`. The two weakest-evidence rules (`qe-math-014`, `qe-math-015`) may be deferred.
- **#19 (Phase 4.3)** — proposes extending the deterministic-checker scope from ~13 to 22 rules, with the audit corpus as regression-test data.
- **#20 (bulk-audit mode)** — open design question on where cross-series synthesis should live.
- **#21 (corpus offer)** — no action required from the team; the published audit is offered as test/eval data.

If these bodies are edited here, re-sync the live issues with `gh issue edit <n> --repo QuantEcon/action-style-guide --body-file issues/<file>` so the record and the live issues stay in agreement.

## Provenance

Generated as part of the May 2026 style audit ([repo](https://github.com/QuantEcon/audit.2026-05.style-guide) · [report](https://quantecon.github.io/audit.2026-05.style-guide/)). See [`../UPDATE.md`](../UPDATE.md) for how the audit is reproduced.
