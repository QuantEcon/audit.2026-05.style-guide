# ols

- **Series:** lecture-python.myst
- **File:** `lectures/ols.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-006` ×2. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×5; `qe-fig-003` ×3; `qe-fig-006` ×4, +2 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 60, 102, 136, 281, 411. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 651, 665. *Example:* apostrophe transpose `}'`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 80, 314, 398, 444, 544. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 78, 304. *Example:* H2 Title Case: 'Simple Linear Regression' (Linear, Regression).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 163, 298, 435. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 161, 162, 433, 434. *Example:* axis label `Average Expropriation Risk 1985-95`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 155, 427. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 638. *Example:* raw link to python-programming.quantecon.org.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 68. *Example:* style override.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-math-002` — Use \top for transpose notation (3 occurrences).
3. `qe-ref-001` — Use correct citation style (5 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
6. `qe-fig-006` — Lowercase axis labels (4 occurrences).
7. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
