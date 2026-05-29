# Style Audit — cons_smooth

- **Series:** lecture-python-intro
- **File:** `lectures/cons_smooth.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 sentence case; some multi-sentence paragraphs. |
| Math         | 8/10  | bmatrix; sequences `\{y_t\}_{t=0}^T` (M6 OK); equation labels. |
| Code         | 8/10  | Unicode Greek used (`β`, `R`, etc.) (qe-code-002 OK); standard Anaconda imports only. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 316, 366, 931; 4 `ax.set_title` calls inside solution blocks (exception applies); one axis label "Welfare" capitalised (line 1023). |
| References   | 7/10  | 9 `{cite}` usages; some are end-of-sentence parenthetical, no clear in-text mis-use detected. |
| Links        | 9/10  | `{doc}` links used (7 occurrences). |
| Admonitions  | 9/10  | Solutions use `:class: dropdown` + exercise labels; gated form throughout. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Several multi-sentence paragraphs in Overview (lines 19–30, 38).
- **W7** — Inconsistent quote style: ``''human capital''`` (line 28), ``"consumption-smoothing model."`` (line 21) mixed.
- **[qe-fig-001]** — `figsize=` overrides on lines 316, 366, 931. *Count:* 3 occurrences.

### Low severity
- **W1** — Some short two-sentence paragraphs throughout.
- **[qe-fig-006]** — Axis label "Welfare" (line 1023) is capitalised; should be lowercase "welfare".
- **[qe-fig-005]** — No figures have a `:name:` field.

## Strengths
- Sequences use `\{y_t\}_{t=0}^T` (M6 OK).
- bmatrix throughout (M4 OK).
- Equation labels via `(label)` form (M14 OK).
- Bold for definitions (**boundary conditions**, **terminal condition**, **smoother**, **welfare criterion**).
- `{doc}` cross-series links used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Break Overview multi-sentence paragraphs.
2. Normalize quote style.
3. Remove `figsize=` overrides.
4. Lowercase "Welfare" axis label.
