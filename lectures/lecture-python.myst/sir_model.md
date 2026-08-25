# sir_model

- **Series:** lecture-python.myst
- **File:** `lectures/sir_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-006` ×5. |
| Math         | 8/10  | `qe-math-001` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 68, 82, 236, 284, 347. *Example:* H2 Title Case: 'The SIR Model' (Model).

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 261, 317. *Example:* plot() without lw=.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 3. *Lines:* 103, 105. *Example:* unicode `σ` inside a math environment.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 313. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
2. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
4. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
