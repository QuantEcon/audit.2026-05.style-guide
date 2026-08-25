# stats_examples

- **Series:** lecture-python.myst
- **File:** `lectures/stats_examples.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×5; `qe-writing-008` ×29. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×1; `qe-fig-008` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 191, 442, 459, 518, 543. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 45, 143, 238, 275, 338. *Example:* H2 Title Case: 'Some Discrete Probability Distributions' (Discrete, Probability, Distributions).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 29. *Lines:* 48, 53, 58, 74, 114, 145, 275, 277, 280, 284, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 26. *Example:* non-Anaconda import with no install cell: ['matplotlib_inline'].
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 194. *Example:* plt.title.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 193. *Example:* plot() without lw=.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-writing-008` — Remove excessive whitespace between words (29 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
