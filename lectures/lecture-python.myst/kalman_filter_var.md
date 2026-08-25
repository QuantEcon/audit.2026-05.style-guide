# kalman_filter_var

- **Series:** lecture-python.myst
- **File:** `lectures/kalman_filter_var.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 8/10  | `qe-math-003` ×3. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×3; `qe-fig-005` ×2; `qe-fig-001` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 825, 828, 830. *Example:* spelled-out `Omega`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 705, 1010. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 714, 721, 726. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 987, 1074. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 3. *Lines:* 961, 962, 963. *Example:* pmatrix environment.

### Low severity
_None found._


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 1 in-text).

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (3 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
