# lucas_asset_pricing_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lucas_asset_pricing_dles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×1. |
| Math         | 5.5/10 | `qe-math-002` ×2; `qe-math-003` ×6. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×5; `qe-fig-008` ×9. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 209, 219, 238, 267, 284. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 211, 221, 222, 240, 241, 269, 270, 286, 287. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 141. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 89, 99, 104, 113, 121, 129. *Example:* array used as matrix.

### Medium severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 27, 137. *Example:* {cite} in narrative flow: '{cite}`'.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 38. *Example:* 2 spaces.


## Strengths

- Writing, Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (6 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
4. `qe-ref-001` — Use correct citation style (2 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (9 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
