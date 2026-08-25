# supply_demand_multiple_goods

- **Series:** lecture-python-intro
- **File:** `lectures/supply_demand_multiple_goods.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-006` ×1; `qe-writing-004` ×1; `qe-writing-001` ×1, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-006` ×4; `qe-fig-005` ×2; `qe-fig-008` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 750, 751, 1042, 1043, 1044. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 273. *Example:* H2 Title Case: 'Digression: Marshallian and Hicksian demand curves' (Hicksian).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 10. *Lines:* 52, 54, 144, 219, 355, 448, 934, 1117. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 368, 371, 373. *Example:* spelled-out `beta`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 720, 1007. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 763, 764, 1060, 1061. *Example:* axis label `Quantity`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 482. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 642. *Example:* mid-sentence 'Economy'.

### Low severity
_None found._


## Strengths

- Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-006` — Lowercase axis labels (4 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (10 occurrences).
