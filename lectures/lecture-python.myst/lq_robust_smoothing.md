# lq_robust_smoothing

- **Series:** lecture-python.myst
- **File:** `lectures/lq_robust_smoothing.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 7.5/10 | `qe-math-003` ×9. |
| Code         | 7/10  | `qe-code-002` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×2; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 10. *Lines:* 551, 552, 553, 554, 692, 739, 940. *Example:* spelled-out `beta`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 9. *Lines:* 105, 107, 108, 110, 111, 133, 136, 222, 469. *Example:* pmatrix environment.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 834, 840. *Example:* .set_title.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 823. *Example:* figsize=.


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 5 in-text).

## Recommended actions

1. `qe-code-002` — Use Unicode symbols for Greek letters in code (10 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (9 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
4. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
