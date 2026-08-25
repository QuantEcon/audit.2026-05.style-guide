# about_py

- **Series:** lecture-python-programming
- **File:** `lectures/about_py.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×10; `qe-writing-001` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 140, 411, 417, 423, 464. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 50, 69, 101, 127, 159, 252, 269, 347, 438, 493. *Example:* H3 Title Case: "Can't I Just Use LLMs?" (Just, Use).

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 84, 440. *Example:* raw link to jax.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 27. *Example:* 3 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (10 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
