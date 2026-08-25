# inventory_dynamics

- **Series:** lecture-python.myst
- **File:** `lectures/inventory_dynamics.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-001` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9.5/10 | `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-008` ×7; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 161, 181, 209, 252, 293, 383. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 168, 169, 170, 185, 186, 233, 290. *Example:* plot() without lw=.

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 142. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 507. *Example:* %%time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 215. *Example:* figsize=.


## Strengths

- Writing, Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
3. `qe-fig-008` — Use lw=2 for line charts (7 occurrences).
4. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
5. `qe-code-004` — Use quantecon Timer context manager (1 occurrence).
