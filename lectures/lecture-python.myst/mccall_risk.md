# mccall_risk

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_risk.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×4; `qe-math-001` ×1. |
| Code         | 8/10  | `qe-code-003` ×1; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-006` ×2; `qe-fig-005` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 339. *Example:* non-blackboard `\text{Var}`.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 69. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 287, 651. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 615, 754. *Example:* axis label `Reservation wage`.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 1. *Lines:* 460. *Example:* unicode `β` inside a math environment.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 208. *Example:* spelled-out `beta`.


## Strengths

- Writing, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
2. `qe-fig-006` — Lowercase axis labels (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (1 occurrence).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
