# coase

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/coase.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Clean one-sentence paragraphs throughout; sentence-case subheadings. |
| Math         | 8.5/10 | Mostly minimal math; primes are derivatives (`c'(s)`). |
| Code         | 8/10  | Limited code; no install cell needed (numpy/scipy only). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `{figure}` directives reference static PNGs; no `:name:` fields. |
| References   | 8/10  | 6 `{cite}` used; never `{cite:t}`. |
| Links        | 9/10  | no cross-series URL links; self-contained. |
| Admonitions  | 8/10  | 2 gated exercises and 2 solutions with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-002]** — 2 `{figure}` directives reference static PNGs (`subcontracting.png`, `allocation.png`); could be code-generated.

### Low severity
- **[qe-writing-005]** — Bold for keywords (`**transaction costs**`) is borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (via `{index}` directive) (qe-writing-006).
- Sentence-case subheadings (qe-writing-006).
- One-sentence paragraph rule rigorously followed (qe-writing-001).
- Primes are derivatives (`c'(0)`) — no qe-math-002 violation.
- Italics for emphasis (qe-writing-005), e.g. *firms*.
- Exercises gated (qe-admon-001); solutions use `:class: dropdown` (qe-admon-002).

## Recommended actions
1. No major changes required.
2. Consider code-generating the schematic figures (qe-fig-002).
3. Add `:name: fig-...` fields (qe-fig-005).
