# lq_permanent_income

- **Series:** lecture-python.myst
- **File:** `lectures/lq_permanent_income.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×3. |
| Math         | 7.5/10 | `qe-math-003` ×5. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×2; `qe-fig-005` ×3; `qe-fig-001` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 5. *Lines:* 338, 340, 341, 343, 344. *Example:* pmatrix environment.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 478, 565, 650. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 488, 497. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 543, 629, 697. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 166, 167, 266. *Example:* 2 spaces.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 658. *Example:* plot() without lw=.


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 3 in-text).

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (5 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
