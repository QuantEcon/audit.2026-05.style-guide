# robust_permanent_income

- **Series:** lecture-python.myst
- **File:** `lectures/robust_permanent_income.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-001` ×5. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×5; `qe-fig-005` ×1; `qe-fig-001` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 6. *Lines:* 363, 675, 676, 770. *Example:* spelled-out `sigma`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 179, 193, 516, 832, 838. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 5. *Lines:* 126, 332, 339, 598, 693. *Example:* 2 sentences in one paragraph.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 173, 509, 821. *Example:* figsize=.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 962. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Math, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 33 in-text).

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (5 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (6 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
