# chang_ramsey

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/chang_ramsey.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 8/10  | Clean — primes are derivatives / next-period, not transpose. |
| Code         | 6/10  | Heavy spelled Greek (17 occurrences); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 2 `ax.set_title` calls; 5 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 10 `{cite}` used; never `{cite:t}`. |
| Links        | 9/10  | 14 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-003]** — `ax.set_title` used in 2 cells.
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, `delta`, etc.) in code parameters (17 occurrences).

### Low severity
- **[qe-writing-005]** — `**competitive equilibria**`, `**Ramsey plan**`, `**dynamic programming squared**` bold-as-keyword use is borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 5 `figsize=` settings.

## Strengths
- Primes in this file are derivatives (`u'`, `v'`, `f'`) and next-period notation (`\theta'`) — not transpose.
- Title in Title Case (qe-writing-006); sentence-case headings (qe-writing-006).
- `\begin{bmatrix}` used where matrices appear (qe-math-003).
- One-sentence paragraph rule respected (qe-writing-001).
- Heavy `{doc}` use for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Remove `ax.set_title` calls (qe-fig-003).
2. Convert spelled Greek to unicode in code (qe-code-002).
3. Add `:name: fig-...` fields to figures (qe-fig-005).
