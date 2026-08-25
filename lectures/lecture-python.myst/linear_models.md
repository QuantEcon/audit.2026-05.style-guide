# linear_models

- **Series:** lecture-python.myst
- **File:** `lectures/linear_models.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×25; `qe-writing-001` ×2; `qe-writing-008` ×30. |
| Math         | 3/10  | `qe-math-002` ×40; `qe-math-010` (proposed) ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×2; `qe-fig-008` ×2; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 40. *Lines:* 239, 404, 431, 444, 488, 535, 543, 575, 609, 635, …. *Example:* apostrophe transpose `A'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 575, 1218. *Example:* non-blackboard `\textrm{Var}`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 25. *Lines:* 77, 119, 147, 224, 293, 374, 446, 508, 516, 560, …. *Example:* H2 Title Case: 'The Linear State Space Model' (Linear, State, Space, Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 30. *Lines:* 87, 88, 465, 469, 488, 551, 552, 589, 613, 614, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 728, 782. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 689, 946. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 1343. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 444, 1409. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 668. *Example:* figsize=.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (25 occurrences).
2. `qe-math-002` — Use \top for transpose notation (40 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (30 occurrences).
7. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
