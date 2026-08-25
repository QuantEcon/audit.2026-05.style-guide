# atkeson_1991

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/atkeson_1991.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 5/10  | `qe-math-002` ×71. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×2; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 71. *Lines:* 66, 145, 185, 198, 334, 419, 443, 444, 460, 476, …. *Example:* apostrophe transpose `Y'`.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 561. *Example:* install cell at line 561 of 1633 (not near the top).
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 1079, 1156, 1341. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1165, 1176. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1496, 1582. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 1343, 1512. *Example:* plot() without lw=.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 977. *Example:* Title Case caption (Program).


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 6 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (71 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-code-003` — Package installation at lecture top (1 occurrence).
5. `qe-fig-004` — Caption formatting conventions (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
