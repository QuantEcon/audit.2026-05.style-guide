# pricing_information

- **Series:** lecture-python.myst
- **File:** `lectures/pricing_information.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×6; `qe-math-003` ×1. |
| Code         | 7/10  | `qe-code-002` ×64. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-004` ×3; `qe-fig-005` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 64. *Lines:* 181, 183, 184, 185, 186, 200, 202, 203, 204, 238, …. *Example:* spelled-out `theta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 90, 240, 484, 751, 814. *Example:* style override.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 6. *Lines:* 115, 160, 364, 374, 411. *Example:* non-blackboard `\Pr`.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 248, 497, 755. *Example:* .suptitle.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 314, 477, 805. *Example:* caption of 8 words.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 155. *Example:* pmatrix environment.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 941. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 16 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (6 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (64 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-fig-004` — Caption formatting conventions (3 occurrences).
5. `qe-math-003` — Use square brackets for matrix notation (1 occurrence).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
