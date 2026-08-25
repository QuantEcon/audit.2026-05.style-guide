# phillips_self_confirming

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_self_confirming.md`
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
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×2; `qe-fig-004` ×4; `qe-fig-008` ×6, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 242, 419, 463, 496, 545, 583. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 250, 252, 420, 546, 584, 586. *Example:* plot() without lw=.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 235, 405, 449, 476. *Example:* caption of 11 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 540, 577. *Example:* code-cell figure without mystnb figure metadata.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 312. *Example:* spelled-out `beta`.


## Strengths

- Writing, Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
2. `qe-fig-004` — Caption formatting conventions (4 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
4. `qe-fig-008` — Use lw=2 for line charts (6 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
