# wealth_dynamics

- **Series:** lecture-python.myst
- **File:** `lectures/wealth_dynamics.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×7; `qe-writing-001` ×2; `qe-writing-008` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9.5/10 | `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×9; `qe-fig-008` ×14; `qe-fig-006` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 9. *Lines:* 108, 136, 173, 429, 469, 499, 514, 564, 645. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 14. *Lines:* 112, 113, 144, 145, 184, 185, 431, 479, 482, 501, …. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 62, 85, 90, 154, 194, 419, 439. *Example:* H3 Title Case: 'A Note on Assumptions' (Note, Assumptions).

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 470, 515. *Example:* %%time.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 249, 612. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 237, 612. *Example:* 2 spaces.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 187. *Example:* axis label `Weibull parameter $a$`.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (7 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (9 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (14 occurrences).
5. `qe-fig-006` — Lowercase axis labels (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (2 occurrences).
7. `qe-code-004` — Use quantecon Timer context manager (2 occurrences).
