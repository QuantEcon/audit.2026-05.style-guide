# python_by_example

- **Series:** lecture-python-programming
- **File:** `lectures/python_by_example.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×10; `qe-writing-001` ×1; `qe-writing-008` ×3. |
| Math         | 9/10  | `qe-math-012` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×11; `qe-fig-008` ×10. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 7.5/10 | `qe-admon-003` ×2. |

## Issues

### Critical
- **[qe-admon-003]** — Use tick count management for nested directives. *Count:* 2. *Lines:* 499, 549. *Example:* {exercise-start} fence (3 ticks) is never closed — the directive swallows the rest of the block.

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 11. *Lines:* 46, 61, 179, 209, 374, 417, 481, 524, 576, 632, …. *Example:* {figure} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 67, 182, 217, 382, 426, 491, 534, 586, 646, 663. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 39, 99, 147, 174, 195, 204, 294, 338, 364, 399. *Example:* H2 Title Case: 'The Task: Plotting a White Noise Process' (Task, White, Noise, Process).

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 445. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 124, 397, 445. *Example:* 2 spaces.

### Low severity
- **[qe-math-012 (proposed)]** — Multiplication via \cdot or juxtaposition, never *. *Count:* 1. *Lines:* 693. *Example:* * as multiplication.


## Strengths

- Math, Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (10 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (11 occurrences).
3. `qe-admon-003` — Use tick count management for nested directives (2 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
6. `qe-math-012` (proposed) — Multiplication via \cdot or juxtaposition, never * (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
