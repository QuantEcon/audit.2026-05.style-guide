# cass_fiscal_2

- **Series:** lecture-python.myst
- **File:** `lectures/cass_fiscal_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×2; `qe-writing-001` ×1; `qe-writing-008` ×8. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×6; `qe-fig-005` ×3; `qe-fig-008` ×5, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 351, 358, 364, 374, 380, 387. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 368, 370, 372, 577, 578. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 44, 79. *Example:* H2 Title Case: 'A Two-Country Cass-Koopmans Model' (Two-Country, Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 8. *Lines:* 18, 22, 65, 394, 588. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['mpmath'].
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 441, 503, 569. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 83. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 329. *Example:* figsize=.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 2 in-text).

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (8 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (5 occurrences).
