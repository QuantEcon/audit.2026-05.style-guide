# money_inflation_nonlinear

- **Series:** lecture-python-intro
- **File:** `lectures/money_inflation_nonlinear.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×6; `qe-writing-008` ×37; `qe-writing-001` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×4; `qe-fig-004` ×2; `qe-fig-008` ×9, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 188, 362, 365, 368, 371, 509, 585, 586, 668. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 48, 78, 162, 206, 278, 339. *Example:* H2 Title Case: 'The Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 37. *Lines:* 20, 27, 29, 33, 38, 40, 46, 82, 106, 108, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 166, 394. *Example:* caption of 15 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 504, 568, 659, 713. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 73. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 348. *Example:* figsize=.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (6 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
3. `qe-fig-004` — Caption formatting conventions (2 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (37 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (9 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
