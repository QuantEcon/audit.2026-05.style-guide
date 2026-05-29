# Style Audit — calvo_abreu

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/calvo_abreu.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs throughout. |
| Math         | 9/10  | Clean — no transpose primes, no `\mathcal{N}`, no `array`. |
| Code         | 7/10  | Mixed unicode/spelled Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | 1 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 12 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 5 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-writing-005]** — `**credible government policy**`, `**sustainable plan**`, `**time inconsistency**`, `**Ramsey planner**` used as keywords — borderline definitional.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- All subheadings sentence case (qe-writing-006).
- Sequences in curly brackets `\{\mu_t\}_{t=0}^\infty`, `\{\theta_t\}_{t=0}^\infty` (qe-math-005) at L35, L37.
- Clean math notation throughout.
- One-sentence paragraph rule consistently followed (qe-writing-001).
- `{doc}` used for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. No major changes required.
2. Add `:name: fig-...` fields to figures (qe-fig-005).
