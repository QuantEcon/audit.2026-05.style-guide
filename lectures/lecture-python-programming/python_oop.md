# python_oop

- **Series:** lecture-python-programming
- **File:** `lectures/python_oop.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×8; `qe-writing-004` ×4; `qe-writing-008` ×16. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×4; `qe-fig-008` ×2; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 64, 75, 126, 146, 199, 353, 460, 695. *Example:* H2 Title Case: 'OOP Review' (Review).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 16. *Lines:* 101, 132, 170, 172, 189, 195, 247, 266, 279, 301, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 439, 549, 646, 660. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 447, 667. *Example:* plot() without lw=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 154, 209, 297, 765. *Example:* mid-sentence 'Classes'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 444. *Example:* figsize=.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (8 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (16 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
