# rational_learning_re

- **Series:** lecture-python.myst
- **File:** `lectures/rational_learning_re.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×3; `qe-fig-004` ×1; `qe-fig-001` ×6. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 9/10  | `qe-admon-001` ×1. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 490, 515, 556, 913, 959, 1003. *Example:* figsize=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 1032. *Example:* non-blackboard `\operatorname{Var}`.

### Medium severity
- **[qe-admon-001]** — Use gated syntax for executable code in exercises. *Count:* 1. *Lines:* 890. *Example:* code cell inside non-gated {exercise}.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 485, 488, 513. *Example:* spelled-out `theta`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 906, 958, 1002. *Example:* code-cell figure without mystnb figure metadata.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 481. *Example:* caption of 7 words.


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 21 in-text).

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
4. `qe-admon-001` — Use gated syntax for executable code in exercises (1 occurrence).
5. `qe-fig-004` — Caption formatting conventions (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
