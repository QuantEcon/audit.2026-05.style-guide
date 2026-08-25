# names

- **Series:** lecture-python-programming
- **File:** `lectures/names.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×8; `qe-writing-008` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×9; `qe-fig-002` ×9. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 9. *Lines:* 453, 459, 469, 477, 524, 529, 536, 560, 564. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 9. *Lines:* 453, 459, 469, 477, 524, 529, 536, 560, 564. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 35, 180, 212, 266, 295, 327, 367, 482. *Example:* H2 Title Case: 'Variable Names in Python' (Names).

### Medium severity
_None found._

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 383. *Example:* 2 spaces.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (8 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (9 occurrences).
3. `qe-fig-002` — Prefer code-generated figures (9 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
