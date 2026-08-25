# re_with_feedback

- **Series:** lecture-python.myst
- **File:** `lectures/re_with_feedback.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×12; `qe-writing-001` ×3; `qe-writing-008` ×33. |
| Math         | 9/10  | `qe-math-004` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×4; `qe-fig-008` ×6. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 449, 450, 493, 494, 937, 952. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 79, 95, 182, 221, 354, 467, 501, 537, 688, 760, …. *Example:* H2 Title Case: 'Linear Difference Equations' (Difference, Equations).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 33. *Lines:* 56, 58, 61, 73, 83, 85, 88, 91, 223, 281, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 452, 496, 955. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 447, 485, 933, 948. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 277. *Example:* {\bf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 195, 629, 1023. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (12 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (33 occurrences).
6. `qe-math-004` — Do not use bold face for matrices or vectors (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (6 occurrences).
