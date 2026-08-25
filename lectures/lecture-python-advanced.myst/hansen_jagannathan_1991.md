# hansen_jagannathan_1991

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hansen_jagannathan_1991.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 5/10  | `qe-math-010` (proposed) ×39. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-001` ×6. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 541, 668, 717, 866, 1053, 1157. *Example:* figsize=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 39. *Lines:* 56, 99, 107, 121, 139, 169, 260, 278, 282, 285, …. *Example:* bare expectation `E(`.

### Medium severity
_None found._

### Low severity
_None found._


## Strengths

- Writing, Code, Figures, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 1 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (39 occurrences).
2. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
