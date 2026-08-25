# cattle_cycles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cattle_cycles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×1. |
| Math         | 7/10  | `qe-math-003` ×10. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×5; `qe-fig-005` ×3; `qe-fig-008` ×11, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 337, 358, 364, 391, 395. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 335, 355, 356, 357, 361, 362, 363, 389, 390, 393, …. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 10. *Lines:* 127, 132, 144, 149, 154, 159, 171, 176, 181, 186. *Example:* array used as matrix.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 354, 388. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 331, 347, 384. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 27, 206, 325. *Example:* {cite} in narrative flow: '{cite}`'.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 38. *Example:* 2 spaces.


## Strengths

- Writing, Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (10 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
3. `qe-ref-001` — Use correct citation style (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (11 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
