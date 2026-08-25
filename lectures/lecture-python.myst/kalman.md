# kalman

- **Series:** lecture-python.myst
- **File:** `lectures/kalman.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×5. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×5; `qe-math-003` ×5. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×8; `qe-fig-008` ×2; `qe-fig-002` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 140, 189, 280, 396, 586, 600, 662, 764. *Example:* {image} without :name:.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 5. *Lines:* 123, 131, 387, 731, 743. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 354, 355, 706, 711. *Example:* non-blackboard `\operatorname{Var}`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 60, 364, 518, 552. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 623, 689. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 512. *Example:* {cite} in author position: '{cite}`AHMS1996` and'.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 586. *Example:* static image .png.


## Strengths

- Writing, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (5 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (5 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
4. `qe-ref-001` — Use correct citation style (2 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (5 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
7. `qe-fig-002` — Prefer code-generated figures (1 occurrence).
