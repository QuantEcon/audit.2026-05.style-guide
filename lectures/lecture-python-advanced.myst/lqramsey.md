# lqramsey

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lqramsey.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×7. |
| Math         | 3/10  | `qe-math-010` (proposed) ×11; `qe-math-002` ×8. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-006` ×3; `qe-fig-008` ×12; `qe-fig-005` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 787, 788, 789, 794, 795, 796, 801, 806, 807, 808, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 8. *Lines:* 401, 404, 408, 410, 411, 430. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 11. *Lines:* 117, 128, 206, 262, 275, 331, 336, 359, 365, 401, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 53, 59, 382, 541, 572, 860. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 775, 824. *Example:* figsize=.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 780, 835, 842. *Example:* axis label `Time`.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 587. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (11 occurrences).
2. `qe-math-002` — Use \top for transpose notation (8 occurrences).
3. `qe-fig-006` — Lowercase axis labels (3 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (12 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (7 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
