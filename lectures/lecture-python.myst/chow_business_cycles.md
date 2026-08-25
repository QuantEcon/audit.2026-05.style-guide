# chow_business_cycles

- **Series:** lecture-python.myst
- **File:** `lectures/chow_business_cycles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×16. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×5. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×14; `qe-fig-001` ×11; `qe-fig-008` ×6. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 11. *Lines:* 234, 262, 630, 825, 1084, 1178, 1208, 1300, 1373, 1471, …. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 14. *Lines:* 222, 257, 608, 701, 787, 1065, 1175, 1207, 1241, 1291, …. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 281, 1184, 1186, 1214, 1216, 1475. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 317, 319, 321, 333, 914. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 16. *Lines:* 34, 35, 46, 50, 304, 847, 1199, 1203, 1227, 1230. *Example:* 2 spaces.

### Medium severity
_None found._

### Low severity
_None found._


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (8 parenthetical, 12 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (5 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (14 occurrences).
3. `qe-writing-008` — Remove excessive whitespace between words (16 occurrences).
4. `qe-fig-001` — Do not set figure size unless necessary (11 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (6 occurrences).
