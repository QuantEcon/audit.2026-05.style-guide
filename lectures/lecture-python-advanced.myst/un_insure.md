# un_insure

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/un_insure.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×107; `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×2; `qe-fig-006` ×3; `qe-fig-005` ×1, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 837, 838, 839, 840, 841, 842, 844. *Example:* style override.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 846, 848, 850, 857, 858, 859. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 107. *Lines:* 17, 20, 22, 30, 58, 62, 66, 105, 115, 148, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 854, 863. *Example:* plt.title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 852, 861, 862. *Example:* axis label `Replacement ratio (c/w)`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 755. *Example:* mid-sentence 'Algorithm'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 835. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 317. *Example:* {cite} in narrative flow: 'Following  {cite}`'.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
2. `qe-fig-006` — Lowercase axis labels (3 occurrences).
3. `qe-writing-008` — Remove excessive whitespace between words (107 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (6 occurrences).
