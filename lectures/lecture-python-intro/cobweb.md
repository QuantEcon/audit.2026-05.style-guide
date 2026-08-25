# cobweb

- **Series:** lecture-python-intro
- **File:** `lectures/cobweb.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×7; `qe-fig-003` ×1; `qe-fig-008` ×9, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 75, 139, 239, 346, 441, 488, 561. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 81, 144, 145, 271, 286, 296, 362, 504, 576. *Example:* plot() without lw=.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 443, 567. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 453. *Example:* .set_title.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 67, 69. *Example:* {cite} in author position: '{cite}`cobweb_model` and'.

### Low severity
_None found._


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
2. `qe-ref-001` — Use correct citation style (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
4. `qe-fig-008` — Use lw=2 for line charts (9 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
