# lucas_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lucas_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×3; `qe-fig-001` ×2; `qe-fig-008` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 499, 544. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 495, 519, 543. *Example:* {figure} without :name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 30, 36, 40. *Example:* raw link to python-intro.quantecon.org.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 519. *Example:* static image .png.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 500. *Example:* plot() without lw=.


## Strengths

- Writing, Math, Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-link-002` — Use doc links for cross-series references (3 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
3. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
5. `qe-fig-002` — Prefer code-generated figures (1 occurrence).
