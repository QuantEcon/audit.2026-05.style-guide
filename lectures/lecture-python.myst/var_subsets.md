# var_subsets

- **Series:** lecture-python.myst
- **File:** `lectures/var_subsets.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-004` ×2. |
| Math         | 7/10  | `qe-math-003` ×15. |
| Code         | 7/10  | `qe-code-002` ×38. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×6; `qe-fig-004` ×3; `qe-fig-005` ×1, +2 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 38. *Lines:* 520, 521, 522, 523, 528, 529, 534, 535, 537, 539, …. *Example:* spelled-out `Sigma`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 725, 758, 761, 788, 1020, 1027. *Example:* .set_title.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 15. *Lines:* 109, 117, 125, 131, 375, 435, 636, 637, 638, 645, …. *Example:* pmatrix environment.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 89, 752, 1011, 1101. *Example:* style override.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 741, 769, 1002. *Example:* caption of 7 words.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 1063, 1188. *Example:* mid-sentence 'Example'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1088. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1017. *Example:* plot() without lw=.


## Strengths

- Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (15 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (38 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
5. `qe-fig-004` — Caption formatting conventions (3 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
