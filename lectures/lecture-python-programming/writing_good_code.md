# writing_good_code

- **Series:** lecture-python-programming
- **File:** `lectures/writing_good_code.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×9; `qe-writing-001` ×3; `qe-writing-008` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×4; `qe-fig-008` ×4; `qe-fig-001` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 45, 142, 156, 176, 196, 215, 226, 236, 246. *Example:* H2 Title Case: 'An Example of Poor Code' (Example, Poor, Code).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 80, 270. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 73, 250, 353, 388. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 91, 108, 125, 263. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 27, 319, 327. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 148, 207. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (9 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (2 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (4 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
