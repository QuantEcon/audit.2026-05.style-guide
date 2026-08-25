# ls_learning

- **Series:** lecture-python.myst
- **File:** `lectures/ls_learning.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-006` ×1. |
| Math         | 6.5/10 | `qe-math-002` ×6. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-006` ×2; `qe-fig-005` ×3; `qe-fig-008` ×10, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 779, 871, 1010, 1193, 1340, 1476, 1522, 1609. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 793, 797, 883, 887, 1024, 1028, 1207, 1211, 1367, 1369. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 314, 315, 342, 522, 538, 539. *Example:* apostrophe transpose `D'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 822. *Example:* H2 Title Case: 'Counterexample: Unstable Bray feedback' (Bray).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 1471, 1521, 1608. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 1217, 1658. *Example:* axis label `Accumulated step size $\\tau$`.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 839. *Example:* Title Case caption (Bray).


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 21 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (6 occurrences).
2. `qe-fig-006` — Lowercase axis labels (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
6. `qe-fig-004` — Caption formatting conventions (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (8 occurrences).
