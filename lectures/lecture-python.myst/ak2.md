# ak2

- **Series:** lecture-python.myst
- **File:** `lectures/ak2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-006` ×2; `qe-writing-008` ×197. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×8; `qe-fig-003` ×3; `qe-fig-008` ×25, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 655, 758, 1012, 1098, 1177, 1242. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 734, 757, 801, 816, 843, 1154, 1176, 1241. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 25. *Lines:* 660, 668, 676, 763, 764, 772, 773, 781, 782, 817, …. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 176, 1210. *Example:* H2 Title Case: 'Activities in Factor Markets' (Factor, Markets).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 197. *Lines:* 26, 29, 32, 40, 48, 50, 56, 75, 77, 78, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 819, 1026, 1031. *Example:* plt.title.

### Low severity
_None found._


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (197 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (25 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
