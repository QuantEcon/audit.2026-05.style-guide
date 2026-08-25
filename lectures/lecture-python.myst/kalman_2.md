# kalman_2

- **Series:** lecture-python.myst
- **File:** `lectures/kalman_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×16. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×5; `qe-fig-004` ×7; `qe-fig-001` ×7, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 64, 65, 339, 563, 587, 620, 653. *Example:* style override.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 293, 301, 354, 459, 467. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 7. *Lines:* 281, 324, 426, 554, 580, 613, 645. *Example:* caption of 9 words.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 246, 249, 252. *Example:* apostrophe transpose `G'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 16. *Lines:* 33, 35, 36, 99, 103, 111, 123, 200, 222, 223, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 536, 545. *Example:* plot() without lw=.

### Low severity
_None found._


## Strengths

- Writing, Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (3 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
3. `qe-fig-004` — Caption formatting conventions (7 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (16 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (7 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
