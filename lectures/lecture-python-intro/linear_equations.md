# linear_equations

- **Series:** lecture-python-intro
- **File:** `lectures/linear_equations.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-001` ×1. |
| Math         | 6.5/10 | `qe-math-002` ×2; `qe-math-003` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-007` ×6; `qe-fig-005` ×5; `qe-fig-008` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 7.5/10 | `qe-link-002` ×5. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 155, 242, 315, 912, 1365. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 6. *Lines:* 161, 163, 248, 250, 321, 323. *Example:* spine removal.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 5. *Lines:* 352, 660, 666, 955, 1388. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 1273. *Example:* `^T` transpose in `A^T`.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 915, 916, 1372, 1373. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 817. *Example:* matrix environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1157. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Writing, Code, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (5 occurrences).
3. `qe-fig-007` — Keep figure box and spines (6 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-math-003` — Use square brackets for matrix notation (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (4 occurrences).
