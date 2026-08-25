# phillips_misspecified

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_misspecified.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.3 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×2; `qe-fig-008` ×2, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 298, 338, 388, 418. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 286, 317. *Example:* caption of 13 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 384, 414. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 419, 421. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 54, 189. *Example:* {cite} in narrative flow: 'with {cite}`'.

### Low severity
_None found._


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
3. `qe-fig-004` — Caption formatting conventions (2 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
