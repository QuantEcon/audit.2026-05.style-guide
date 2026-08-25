# ifp_opi

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_opi.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-006` ×5. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-002` ×2; `qe-code-004` ×14; `qe-code-005` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×2; `qe-fig-008` ×3, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 14. *Lines:* 305, 308, 315, 318, 326, 329, 336, 339, 391, 394, …. *Example:* bare time() reading.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 56, 107, 219, 245, 293. *Example:* H2 Title Case: 'Model and Primitives' (Primitives).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 102. *Example:* spelled-out `rho`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 361, 369, 408. *Example:* .set(xlabel='current assets', ylabel='next period assets', title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 353, 401. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 359, 367, 403. *Example:* plot() without lw=.

### Low severity
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 1. *Lines:* 387. *Example:* hand-rolled benchmark loop — use qe.timeit.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 354. *Example:* figsize=.


## Strengths

- Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
5. `qe-code-004` — Use quantecon Timer context manager (14 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
