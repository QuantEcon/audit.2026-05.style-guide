# market_diffusion

- **Series:** lecture-python.myst
- **File:** `lectures/market_diffusion.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 4.5/10 | `qe-math-002` ×5; `qe-math-010` (proposed) ×2. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×1; `qe-fig-004` ×1; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 5. *Lines:* 304, 309, 324, 950, 952. *Example:* apostrophe transpose `V'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 143, 184. *Example:* non-blackboard `\Pr`.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 154, 156, 159. *Example:* spelled-out `sigma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 92, 509, 608, 968. *Example:* style override.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 592. *Example:* caption of 9 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 963. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 10 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (5 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-fig-004` — Caption formatting conventions (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
