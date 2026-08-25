# matplotlib

- **Series:** lecture-python-programming
- **File:** `lectures/matplotlib.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×9; `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-005` ×13; `qe-fig-003` ×3; `qe-fig-007` ×1, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 183, 213, 287, 289, 381, 384, 403, 435. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 13. *Lines:* 59, 82, 103, 114, 123, 132, 157, 181, 201, 236, …. *Example:* {image} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 38, 78, 141, 148, 172, 194, 226, 265, 439. *Example:* H3 Title Case: "Matplotlib's Split Personality" (Split, Personality).

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['cycler'].
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 137, 190, 317. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 308, 488. *Example:* plot() without lw=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 42. *Example:* mid-sentence 'Programming'.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 465. *Example:* static image .png.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 1. *Lines:* 245. *Example:* spine removal.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (9 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (13 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-fig-007` — Keep figure box and spines (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (8 occurrences).
