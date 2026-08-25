# getting_started

- **Series:** lecture-python-programming
- **File:** `lectures/getting_started.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-006` ×17; `qe-writing-008` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×12. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 12. *Lines:* 154, 182, 195, 207, 230, 276, 320, 338, 357, 363, …. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 17. *Lines:* 50, 67, 77, 213, 220, 238, 261, 268, 306, 329, …. *Example:* H2 Title Case: 'Python in the Cloud' (Cloud).

### Medium severity
_None found._

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 144. *Example:* 2 spaces.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (17 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (12 occurrences).
3. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
