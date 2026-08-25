# os_numerical

- **Series:** lecture-dp
- **File:** `lectures/os_numerical.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×5; `qe-writing-008` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×3; `qe-fig-008` ×7. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 287, 359, 376, 464, 572, 614. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 362, 379, 380, 469, 470, 635, 636. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 55, 86, 106, 125, 411. *Example:* H2 Title Case: 'Reviewing the Model' (Model).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 309, 365, 384. *Example:* .set_title.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 142. *Example:* 2 spaces.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (7 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
