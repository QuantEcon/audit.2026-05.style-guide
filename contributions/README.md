# Contributions to action-style-guide

Feedback this audit fed back to [QuantEcon/action-style-guide](https://github.com/QuantEcon/action-style-guide) and the [QuantEcon style guide](https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide). This folder is the source material behind the four issues opened from the May 2026 audit; the reader-facing summary is the [Feedback appendix](../lectures/appendix.md) in the report.

## Issues posted

All four are open on `action-style-guide`. The files here are the bodies as posted (kept in sync).

| Issue | Title | Body | Type |
|-------|-------|------|------|
| [#18](https://github.com/QuantEcon/action-style-guide/issues/18) | Proposal: 7 new style rules surfaced by lecture audit | [`issues/01-new-style-rules.md`](issues/01-new-style-rules.md) | Concrete proposal |
| [#19](https://github.com/QuantEcon/action-style-guide/issues/19) | Phase 4.3 acceleration: 41 of 49 rules are mechanically checkable + corpus test data | [`issues/02-phase-4-3-deterministic-checks.md`](issues/02-phase-4-3-deterministic-checks.md) | Extension of existing plan |
| [#20](https://github.com/QuantEcon/action-style-guide/issues/20) | Discussion: bulk audit / cross-series synthesis mode — where should it live? | [`issues/03-bulk-audit-mode.md`](issues/03-bulk-audit-mode.md) | Design question |
| [#21](https://github.com/QuantEcon/action-style-guide/issues/21) | Offer: labelled lecture corpus with per-rule violation counts as test fixtures | [`issues/04-corpus-offer.md`](issues/04-corpus-offer.md) | Resource offer |
| *(not yet posted)* | Proposal: rule-definition format changes so the registry determines its own counts | [`issues/05-rule-format-for-checkability.md`](issues/05-rule-format-for-checkability.md) | Concrete proposal |
| *(not yet posted)* | Question: what `qe-ref-001` means by a narrative citation — 299 author-name sites are undetermined under the current text | [`issues/06-ref-001-author-name-citations.md`](issues/06-ref-001-author-name-citations.md) | Rule-definition question |

### Not yet posted

`issues/05-rule-format-for-checkability.md` and `issues/06-ref-001-author-name-citations.md`
both came out of the 2026-08 pass and have **no issue number yet** — it needs filing against whichever repo ends up owning the rule registry
(`action-style-guide` today, the consolidated `QuantEcon/style-guide` under the current
program direction). It is the one contribution here that is about the *format* of the rule
definitions rather than their content: 144 under-specification gaps across 42 of the
in-scope rules, measured by auditing the rule files against a working implementation of 41
of them. The single strongest datum is that `qe-fig-003` — the only rule in the registry
carrying an explicit exemption clause — is also the only figure rule with zero false
positives.

## Rule entry drafts

Each file under [`rule-drafts/`](rule-drafts/) holds one proposed rule in action-style-guide's rules-file format (Type / Title / Description / Check for / Examples), ready to append to `style_checker/rules/<category>-rules.md` once the team accepts it. **Not yet submitted as a PR** — pending discussion on issue [#18](https://github.com/QuantEcon/action-style-guide/issues/18).

| Proposed ID | Category | File | Evidence |
|-------------|----------|------|----------|
| `qe-writing-009` | writing | [`rule-drafts/qe-writing-009-IID.md`](rule-drafts/qe-writing-009-IID.md) | Measured: 30 / 348 lectures, 61 occurrences |
| `qe-math-010` | math | [`rule-drafts/qe-math-010-blackboard-PEV.md`](rule-drafts/qe-math-010-blackboard-PEV.md) | Measured: **105 / 348**, 1,167 occurrences — strongest of the seven |
| `qe-math-011` | math | [`rule-drafts/qe-math-011-distribution-naming.md`](rule-drafts/qe-math-011-distribution-naming.md) | Measured: 24 / 348, 86 occurrences |
| `qe-math-012` | math | [`rule-drafts/qe-math-012-multiplication.md`](rule-drafts/qe-math-012-multiplication.md) | Measured: 4 / 348, 6 occurrences — narrower than first estimated |
| `qe-math-013` | math | [`rule-drafts/qe-math-013-equation-refs.md`](rule-drafts/qe-math-013-equation-refs.md) | Measured: 6 / 348, 6 occurrences — narrower than first estimated |
| `qe-math-014` | math | [`rule-drafts/qe-math-014-events-vs-sets.md`](rule-drafts/qe-math-014-events-vs-sets.md) | Judgment-only — no mechanical check possible |
| `qe-math-015` | math | [`rule-drafts/qe-math-015-density-CDF-case.md`](rule-drafts/qe-math-015-density-CDF-case.md) | Judgment-only — no mechanical check possible |

Each rule-draft has two sections: the **rule entry** (ready to paste into the rules file) and the **rationale** (for the issue / PR discussion, not the rules file).

## Status & next steps

- **#18 (new rules)** — open. The program direction has since evolved: rules are being consolidated into the `QuantEcon/style-guide` rule database (coordinated in the private hub `QuantEcon/project-style-guide`), and `action-style-guide` is slated to be split & retired. The `rule-drafts/` here are **transcription inputs for that consolidation**, not a PR against `action-style-guide`. The two weakest-evidence rules (`qe-math-014`, `qe-math-015`) may be deferred.
- **#19 (Phase 4.3)** — the body has been rewritten. The original asked whether scope should go from ~13 to 22 rules; building the checks answered it: **41 of 49 are mechanically checkable**, and the issue now also offers `tools/qestyle_rules.py` and `qestyle_lex.py` for adoption rather than parallel maintenance. **The live issue still carries the old "22 rules" text and needs re-syncing.**
- **#20 (bulk-audit mode)** — open design question on where cross-series synthesis should live.
- **#21 (corpus offer)** — no action required from the team; the published audit is offered as test/eval data.

**These bodies are ahead of the live issues.** The 2026-08 pass rewrote #19 and refreshed
the evidence counts cited in the others, but `action-style-guide` is not in the audit
session's GitHub scope, so nothing was pushed. Someone with access needs to run:

```bash
for n in 18:01-new-style-rules 19:02-phase-4-3-deterministic-checks \
         20:03-bulk-audit-mode 21:04-corpus-offer; do
  gh issue edit "${n%%:*}" --repo QuantEcon/action-style-guide \
     --body-file "contributions/issues/${n#*:}.md"
done
```

Note that the bodies contain GitHub Pages links, which do **not** survive the repo rename
tracked in [#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2) — best to
re-sync after that rename rather than twice.

## Provenance

Generated as part of the May 2026 style audit ([repo](https://github.com/QuantEcon/audit.2026-05.style-guide) · [report](https://quantecon.github.io/audit.2026-05.style-guide/)). See [`../UPDATE.md`](../UPDATE.md) for how the audit is reproduced.
