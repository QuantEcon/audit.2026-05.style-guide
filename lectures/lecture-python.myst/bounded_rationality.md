# bounded_rationality

- **Series:** lecture-python.myst
- **File:** `lectures/bounded_rationality.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×3. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-004` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 313, 455, 690, 1036. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 317, 323. *Example:* .set_title.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 34, 59, 101. *Example:* 2 spaces.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 683. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1035. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 5 in-text).

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
3. `qe-fig-004` — Caption formatting conventions (1 occurrence).
4. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
