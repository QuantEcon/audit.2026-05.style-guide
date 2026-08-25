# cass_koopmans_1

- **Series:** lecture-python.myst
- **File:** `lectures/cass_koopmans_1.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×11; `qe-writing-008` ×79. |
| Math         | 5.5/10 | `qe-math-002` ×13. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×1; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 569, 657, 829, 895, 1087. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 577, 672, 852, 901, 1093, 1097, 1101, 1102. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 13. *Lines:* 278, 280, 293, 295, 347, 356, 357, 977, 984, 989. *Example:* apostrophe transpose `f'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 11. *Lines:* 82, 102, 154, 216, 250, 477, 691, 785, 913, 967, …. *Example:* H2 Title Case: 'The Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 79. *Lines:* 30, 33, 37, 39, 54, 61, 84, 86, 95, 116, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 578, 673, 903. *Example:* .set(xlabel='t', ylabel=ylabels[i], title=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 31. *Example:* raw link to python-programming.quantecon.org.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 1079. *Example:* Title Case caption (Manifold, Phase, Plane).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 568. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (11 occurrences).
2. `qe-math-002` — Use \top for transpose notation (13 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (79 occurrences).
5. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-004` — Caption formatting conventions (1 occurrence).
