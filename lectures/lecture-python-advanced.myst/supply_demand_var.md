# supply_demand_var

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/supply_demand_var.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×3; `qe-fig-008` ×10, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 529, 530, 697, 699, 701, 703, 1039, 1040, 1046, 1047. *Example:* plot() without lw=.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 632, 775, 812. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 527, 695, 1038. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 532, 706, 1041, 1048. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 526, 694, 1026. *Example:* code-cell figure without mystnb figure metadata.

### Low severity
_None found._


## Strengths

- Writing, Math, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
