# pandas_panel

- **Series:** lecture-python-programming
- **File:** `lectures/pandas_panel.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-006` ×4; `qe-writing-001` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-006` ×5; `qe-fig-005` ×8; `qe-fig-003` ×4, +2 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 38, 246, 372, 393, 412, 422, 476, 612. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 5. *Lines:* 379, 397, 416, 427, 617. *Example:* axis label `Country`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 72, 187, 352, 488. *Example:* H2 Title Case: 'Slicing and Reshaping Data' (Reshaping, Data).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 395, 414, 425, 482. *Example:* plt.title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 512. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 41. *Example:* style override.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 246. *Example:* static image .png.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (4 occurrences).
2. `qe-fig-006` — Lowercase axis labels (5 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-fig-002` — Prefer code-generated figures (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
