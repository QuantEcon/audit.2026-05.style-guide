# learning_approximation

- **Series:** lecture-python.myst
- **File:** `lectures/learning_approximation.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 257, 351, 484, 605, 828. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 112, 137. *Example:* apostrophe transpose `u'`.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 492, 499. *Example:* .set_title.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 190. *Example:* spelled-out `mu`.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 598. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 827. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 607. *Example:* plot() without lw=.


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 3 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (3 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
4. `qe-fig-004` — Caption formatting conventions (1 occurrence).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
