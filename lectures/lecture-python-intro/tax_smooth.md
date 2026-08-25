# tax_smooth

- **Series:** lecture-python-intro
- **File:** `lectures/tax_smooth.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×2; `qe-writing-006` ×1; `qe-writing-008` ×21. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×7; `qe-fig-006` ×1; `qe-fig-008` ×9, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 315, 361, 567, 627, 645, 739, 844. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 590, 594, 630, 637, 648, 655, 752, 753, 857. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 482. *Example:* H3 Title Case: 'Feasible Tax Variations' (Tax, Variations).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 21. *Lines:* 19, 22, 27, 33, 50, 54, 58, 62, 69, 77, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 319, 373, 746. *Example:* figsize=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 605, 673. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 859. *Example:* axis label `Optimal flat tax $T_0$`.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
4. `qe-writing-008` — Remove excessive whitespace between words (21 occurrences).
5. `qe-fig-006` — Lowercase axis labels (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (9 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
