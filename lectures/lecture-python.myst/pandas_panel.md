# pandas_panel

- **Series:** lecture-python.myst
- **File:** `lectures/pandas_panel.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
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
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 234, 364, 370, 391, 408, 418, 472, 608. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 5. *Lines:* 377, 395, 412, 423, 613. *Example:* axis label `Country`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 60, 175, 344, 484. *Example:* H2 Title Case: 'Slicing and Reshaping Data' (Reshaping, Data).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 393, 410, 421, 478. *Example:* plt.title.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 34. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 508. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 367. *Example:* style override.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 234. *Example:* static image .png.


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
6. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
7. `qe-fig-002` — Prefer code-generated figures (1 occurrence).
