# need_for_speed

- **Series:** lecture-python-programming
- **File:** `lectures/need_for_speed.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×10; `qe-writing-001` ×2. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-009` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 70, 103, 130, 136, 217, 223, 236, 441, 450, 481. *Example:* H2 Title Case: 'Major Scientific Libraries' (Scientific, Libraries).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 313, 458, 492. *Example:* {figure} without :name:.
- **[qe-fig-009]** — Figure sizing. *Count:* 2. *Lines:* 458, 492. *Example:* :scale: 40 (outside 80–100%).
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 424, 466. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (10 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
4. `qe-fig-009` — Figure sizing (2 occurrences).
