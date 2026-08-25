# lq_robust_bewley

- **Series:** lecture-python.myst
- **File:** `lectures/lq_robust_bewley.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 5.5/10 | `qe-math-003` ×13; `qe-math-002` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×2; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 345. *Example:* apostrophe transpose `}'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 13. *Lines:* 87, 89, 90, 92, 95, 115, 345, 564, 566, 567, …. *Example:* pmatrix environment.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 448, 462. *Example:* .set_title.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 441. *Example:* figsize=.


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 1 in-text).

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (13 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
3. `qe-math-002` — Use \top for transpose notation (1 occurrence).
4. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
