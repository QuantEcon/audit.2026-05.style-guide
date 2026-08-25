# cass_fiscal

- **Series:** lecture-python.myst
- **File:** `lectures/cass_fiscal.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×12; `qe-writing-001` ×3; `qe-writing-008` ×56. |
| Math         | 9/10  | `qe-math-001` ×1. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×10; `qe-fig-005` ×6; `qe-fig-008` ×11, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 828, 875, 910, 978, 1057, 1386, 1653, 1708, 1734. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 10. *Lines:* 774, 779, 786, 792, 798, 1022, 1028, 1034, 1043, 1048. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 809, 900, 1054, 1383, 1631, 1686. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 772, 777, 784, 790, 796, 1020, 1026, 1027, 1032, 1039, …. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 39, 112, 169, 232, 275, 283, 331, 598, 1208, 1525, …. *Example:* H2 Title Case: 'The Economy' (Economy).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 56. *Lines:* 18, 20, 22, 24, 32, 34, 75, 87, 102, 125, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['mpmath'].
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 1. *Lines:* 1771. *Example:* LaTeX `\mu` outside math delimiters.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 1173, 1585, 1614. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (3 parenthetical, 1 in-text).

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (12 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (10 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (56 occurrences).
6. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (1 occurrence).
7. `qe-code-003` — Package installation at lecture top (1 occurrence).
