# Style Audit — chang_credible

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/chang_credible.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 8/10  | Clean — primes are derivatives or next-period, not transpose. |
| Code         | 7/10  | Mixed unicode/spelled Greek (5 spelled vs 2 unicode); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | 1 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 6 `{cite}` used; two narrative refs would benefit from `{cite:t}`. |
| Links        | 9/10  | 11 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.
- **[qe-ref-001]** — Two narrative author references could use `{cite:t}`.

## Strengths
- Primes in this file are derivatives (`u'`, `f'`, `v'`) and next-period state notation (`\theta'`, `w'`), not transpose — no qe-math-002 violation.
- Title in Title Case (qe-writing-006); sentence-case headings (qe-writing-006).
- `\begin{bmatrix}` used where matrices appear; no `array` violations (qe-math-003).
- One-sentence paragraph rule respected (qe-writing-001).
- Heavy `{doc}` use for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Add `:name: fig-...` fields to figures (qe-fig-005).
2. Convert spelled Greek to unicode in code (qe-code-002).
