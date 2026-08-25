# cons_smooth

- **Series:** lecture-python-intro
- **File:** `lectures/cons_smooth.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×2; `qe-writing-008` ×86. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×8; `qe-fig-008` ×10; `qe-fig-006` ×1, +1 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 312, 354, 575, 634, 652, 859, 923, 991. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 596, 600, 637, 644, 655, 662, 885, 936, 943, 1020. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 19, 35, 127, 183, 670. *Example:* {cite} in author position: '{cite}`Friedman1956` and'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 86. *Lines:* 19, 21, 23, 25, 27, 30, 33, 34, 51, 55, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 316, 366, 931. *Example:* figsize=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 746, 822. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 1023. *Example:* axis label `Welfare`.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (5 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (86 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
6. `qe-fig-006` — Lowercase axis labels (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
