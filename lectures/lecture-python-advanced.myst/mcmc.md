# mcmc

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/mcmc.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-006` ×1. |
| Math         | 6/10  | `qe-math-010` (proposed) ×2; `qe-math-005` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×1; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 158, 322. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1001. *Example:* H3 Title Case: 'A Student-t prior' (Student-t).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1158, 1205. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 3. *Lines:* 107, 313, 591. *Example:* parenthesised sequence.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 1161. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 1032. *Example:* Title Case caption (Student-t).


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
2. `qe-math-005` — Use curly brackets for sequences (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-fig-004` — Caption formatting conventions (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
