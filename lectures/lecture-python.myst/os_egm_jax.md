# os_egm_jax

- **Series:** lecture-python.myst
- **File:** `lectures/os_egm_jax.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-006` ×2; `qe-fig-005` ×2; `qe-fig-008` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 158, 160. *Example:* spelled-out `mu`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 224, 384. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 395, 396. *Example:* axis label `State x`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 230, 393. *Example:* plot() without lw=.

### Low severity
_None found._


## Strengths

- Writing, Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-006` — Lowercase axis labels (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
