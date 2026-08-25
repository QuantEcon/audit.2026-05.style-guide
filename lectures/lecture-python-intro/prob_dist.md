# prob_dist

- **Series:** lecture-python-intro
- **File:** `lectures/prob_dist.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×1. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×3. |
| Code         | 7.5/10 | `qe-code-002` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 8. *Lines:* 911, 912, 934, 935, 983, 984, 1006, 1007. *Example:* spelled-out `beta`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 152, 591, 615. *Example:* missing braces: `\mathbb P`.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 306, 434, 528, 571. *Example:* plot() without lw=.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 473. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 269. *Example:* 2 spaces.


## Strengths

- Writing, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (8 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
4. `qe-fig-008` — Use lw=2 for line charts (4 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
