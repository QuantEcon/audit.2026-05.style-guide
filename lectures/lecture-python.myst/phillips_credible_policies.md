# phillips_credible_policies

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_credible_policies.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-006` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×4; `qe-fig-004` ×2; `qe-fig-005` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 381. *Example:* H2 Title Case: 'The Abreu–Pearce–Stacchetti method' (Pearce, Stacchetti).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 235, 816, 1045. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 248, 821, 825, 828. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 223, 805. *Example:* caption of 11 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 238, 240, 242. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 82. *Example:* raw link to python-advanced.quantecon.org.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1037. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (5 parenthetical, 3 in-text).

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
2. `qe-fig-004` — Caption formatting conventions (2 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
4. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
