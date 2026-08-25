# autodiff

- **Series:** lecture-python-programming
- **File:** `lectures/autodiff.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-006` ×1; `qe-writing-008` ×1. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×11; `qe-fig-008` ×14. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 11. *Lines:* 82, 193, 216, 257, 271, 289, 362, 381, 416, 448, …. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 14. *Lines:* 97, 98, 195, 196, 218, 219, 259, 260, 277, 291, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 140, 141. *Example:* apostrophe transpose `)'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 295. *Example:* H2 Title Case: 'Gradient Descent' (Descent).

### Medium severity
_None found._

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 468. *Example:* 2 spaces.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (11 occurrences).
2. `qe-math-002` — Use \top for transpose notation (3 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
4. `qe-fig-008` — Use lw=2 for line charts (14 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
