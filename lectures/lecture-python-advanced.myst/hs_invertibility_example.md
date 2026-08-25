# hs_invertibility_example

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hs_invertibility_example.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×9. |
| Math         | 7.5/10 | `qe-math-003` ×8. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×6; `qe-fig-005` ×3; `qe-fig-008` ×12, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 269, 277, 328, 333, 370, 375. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 266, 267, 274, 275, 325, 326, 330, 331, 368, 369, …. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 8. *Lines:* 110, 115, 124, 132, 202, 205, 224, 227. *Example:* array used as matrix.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 9. *Lines:* 29, 50, 53, 62, 65, 72, 235, 253. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 265, 324, 367. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 260, 294, 349. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 29, 235, 257. *Example:* {cite} in narrative flow: '{cite}`'.

### Low severity
_None found._


## Strengths

- Writing, Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (8 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
3. `qe-ref-001` — Use correct citation style (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (12 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (9 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
