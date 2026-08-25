# mix_model

- **Series:** lecture-python.myst
- **File:** `lectures/mix_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-002` ×9; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-006` ×2; `qe-fig-005` ×4; `qe-fig-004` ×1, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 9. *Lines:* 138, 158, 469, 485, 592, 746, 747. *Example:* spelled-out `gamma`.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 20. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 123, 409, 913, 942. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 933, 962. *Example:* axis label `Posterior mean of $x$`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 443, 450, 917. *Example:* plot() without lw=.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 269. *Example:* Title Case caption (Monte, Carlo).


## Strengths

- Writing, Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-code-002` — Use Unicode symbols for Greek letters in code (9 occurrences).
2. `qe-fig-006` — Lowercase axis labels (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
4. `qe-code-003` — Package installation at lecture top (1 occurrence).
5. `qe-fig-004` — Caption formatting conventions (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
