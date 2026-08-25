# phillips_credibility

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_credibility.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-004` ×3; `qe-fig-005` ×1; `qe-fig-008` ×4, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 220, 285, 396, 504. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 213, 278, 387. *Example:* caption of 15 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 236, 238, 288, 297. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 34, 75, 367. *Example:* {cite} in narrative flow: 'by {cite}`'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 36. *Example:* mid-sentence 'Critique'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 503. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (3 occurrences).
2. `qe-fig-004` — Caption formatting conventions (3 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (4 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
