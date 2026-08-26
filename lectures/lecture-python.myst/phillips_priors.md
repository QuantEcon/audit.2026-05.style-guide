# phillips_priors

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_priors.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×3; `qe-fig-004` ×4; `qe-fig-005` ×1, +2 more. |
| References   | 7/10  | `qe-ref-001` ×10. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 328, 366, 397, 553, 655. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 329, 376, 398, 656, 657. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 10. *Lines:* 40, 57, 444, 446, 448, 587, 599, 668. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 372, 379, 564. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 307, 359, 390, 544. *Example:* caption of 10 words.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 615. *Example:* mid-sentence 'Inflation'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 642. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (10 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
3. `qe-fig-004` — Caption formatting conventions (4 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (5 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
