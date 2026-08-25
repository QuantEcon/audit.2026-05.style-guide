# intro_supply_demand

- **Series:** lecture-python-intro
- **File:** `lectures/intro_supply_demand.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-004` ×2; `qe-writing-008` ×7. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×2; `qe-fig-008` ×12. |
| References   | N/A   | no citations in this lecture. |
| Links        | 8/10  | `qe-link-002` ×4. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 183, 209, 301, 349, 448, 449, 490, 556, 634, 755, …. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 53, 87, 390, 642, 678, 700, 703. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 197, 285. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 747, 832. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 853, 854, 898, 899. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 414, 899. *Example:* mid-sentence 'Market'.

### Low severity
_None found._


## Strengths

- Math, Code, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (4 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-fig-004` — Caption formatting conventions (2 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (12 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (7 occurrences).
