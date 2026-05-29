# lqramsey

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lqramsey.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 5/10  | Mixed `E_t` and `\mathbb{E}_t`; primes used as transpose. |
| Code         | 7/10  | Mixed unicode/spelled Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `figsize=`; 3 `{only} latex` directives for PDF compat. |
| References   | 8/10  | 4 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | No raw cross-series URLs. |
| Admonitions  | 7/10  | 1 gated exercise and 1 solution with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Bare `E_t` mixed with `\mathbb{E}_t`. *Example:* `lectures/lqramsey.md:497`, `:505`, `:547`, `:555`, `:562`, `:568`. *Count:* 10 occurrences (vs 14 correct).

### Medium severity
- **[qe-math-002]** — Prime `'` used as transpose. *Example:* `Q = H + \beta A' Q A`, `v = \text{trace}(C' Q C) \beta / (1 - \beta)`. *Count:* ~7 occurrences.

### Low severity
- **[qe-writing-001]** — Some longer paragraphs in the model description sections.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003).
- Equation labels and `{eq}` references (qe-math-007).
- Exercise gated; solution has `:class: dropdown` (qe-admon-001, qe-admon-002).
- Use of `{only} latex` for PDF compatibility (qe-fig-010).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Standardise on `\mathbb{E}_t` throughout (qe-math-010, proposed).
2. Replace prime `'` with `^\top` for transpose (qe-math-002).
3. Add `:name: fig-...` fields to figures (qe-fig-005).
