# phillips_learning

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_learning.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-004` ×1. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-004` ×5; `qe-fig-003` ×1; `qe-fig-005` ×1, +1 more. |
| References   | 7/10  | `qe-ref-001` ×17. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 606, 633, 669, 701, 736, 813. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 5. *Lines:* 597, 624, 662, 694, 729. *Example:* caption of 11 words.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 318. *Example:* non-blackboard `\operatorname{Prob}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 17. *Lines:* 186, 189, 194, 220, 267, 313, 330, 375, 377, 394, …. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 682. *Example:* .suptitle.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 770. *Example:* mid-sentence 'Critique'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 812. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (17 occurrences).
2. `qe-fig-004` — Caption formatting conventions (5 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
