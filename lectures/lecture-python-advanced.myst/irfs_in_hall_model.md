# irfs_in_hall_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/irfs_in_hall_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×7; `qe-writing-001` ×2. |
| Math         | 9/10  | `qe-math-003` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-008` ×12. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 121, 142, 167, 182, 251, 282. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 126, 127, 145, 146, 176, 177, 185, 186, 270, 271, …. *Example:* plot() without lw=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 52, 68, 161, 164, 276, 295. *Example:* mid-sentence 'Dynamic'.

### Medium severity
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 77. *Example:* array used as matrix.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 118, 219. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 27. *Example:* {cite} in narrative flow: '{cite}`'.


## Strengths

- Math, Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (7 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-math-003` — Use square brackets for matrix notation (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (12 occurrences).
6. `qe-ref-001` — Use correct citation style (1 occurrence).
