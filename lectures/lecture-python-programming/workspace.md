# workspace

- **Series:** lecture-python-programming
- **File:** `lectures/workspace.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-004` ×4; `qe-writing-006` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×18; `qe-fig-003` ×2; `qe-fig-008` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 18. *Lines:* 56, 79, 141, 149, 164, 169, 185, 199, 221, 227, …. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 211. *Example:* H2 Title Case: 'A walk through Visual Studio Code' (Visual, Studio, Code).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 69, 96. *Example:* plt.title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 66, 93. *Example:* plot() without lw=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 37, 213, 246, 252. *Example:* mid-sentence 'Code'.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (18 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
