# survival_recursive_preferences

- **Series:** lecture-python.myst
- **File:** `lectures/survival_recursive_preferences.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-001` ×1. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×6; `qe-fig-004` ×5; `qe-fig-005` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 687, 817, 848, 914, 990, 1076, 1115, 1201. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 762, 869, 1127, 1137, 1207, 1219. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 5. *Lines:* 667, 1065, 1108, 1160. *Example:* caption of 7 words.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 270, 311, 322. *Example:* apostrophe transpose `}'`.

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 158. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 903. *Example:* spelled-out `gamma`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 794. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 731. *Example:* plot() without lw=.


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 16 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (3 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
3. `qe-fig-004` — Caption formatting conventions (5 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (8 occurrences).
