# theil_1

- **Series:** lecture-python.myst
- **File:** `lectures/theil_1.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-001` ×1. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×3. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-004` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 103, 105, 154. *Example:* non-blackboard `\mathcal{E}`.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 285, 376. *Example:* spelled-out `beta`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 295, 301. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 161. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 290. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 264. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 360. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 16 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-fig-004` — Caption formatting conventions (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
