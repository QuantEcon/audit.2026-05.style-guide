# hoist_failure

- **Series:** lecture-python.myst
- **File:** `lectures/hoist_failure.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-006` ×1; `qe-writing-008` ×25. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-004` ×2; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 168, 174. *Example:* non-blackboard `\Pr`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 356. *Example:* H3 Title Case: 'The Fast Fourier Transform' (Fast, Transform).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 25. *Lines:* 41, 381, 489, 544, 545, 549, 552, 554, 560, 567, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 325, 430, 449, 684. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 235, 250. *Example:* caption of 7 words.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 11 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
2. `qe-fig-004` — Caption formatting conventions (2 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
4. `qe-writing-008` — Remove excessive whitespace between words (25 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
