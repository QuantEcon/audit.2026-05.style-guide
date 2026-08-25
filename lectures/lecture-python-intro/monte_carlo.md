# monte_carlo

- **Series:** lecture-python-intro
- **File:** `lectures/monte_carlo.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-006` ×1; `qe-writing-008` ×2. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×10. |
| Code         | 9/10  | `qe-code-004` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 8. *Lines:* 172, 229, 241, 610, 656, 667, 741, 777. *Example:* %%time.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 10. *Lines:* 94, 101, 168, 273, 290, 341, 371, 382, 575. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 52. *Example:* H2 Title Case: 'An introduction to Monte Carlo' (Monte, Carlo).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 556. *Example:* .set_title.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 124, 368. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 547. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 555. *Example:* plot() without lw=.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (10 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
3. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-code-004` — Use quantecon Timer context manager (8 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (2 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
