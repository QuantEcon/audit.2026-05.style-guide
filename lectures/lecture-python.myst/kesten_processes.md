# kesten_processes

- **Series:** lecture-python.myst
- **File:** `lectures/kesten_processes.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-004` ×4; `qe-writing-008` ×1. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×21. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×4; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 21. *Lines:* 132, 190, 227, 253, 255, 264, 285, 289, 291, 293, …. *Example:* missing braces: `\mathbb P`.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 104, 331, 448, 726. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 112, 349, 469. *Example:* plot() without lw=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 281, 309, 359, 414. *Example:* mid-sentence 'Theorem'.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 494. *Example:* 2 spaces.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (21 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
