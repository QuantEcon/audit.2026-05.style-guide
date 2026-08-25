# markov_chains_II

- **Series:** lecture-python-intro
- **File:** `lectures/markov_chains_II.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×5. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-008` ×5; `qe-fig-002` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 9/10  | `qe-admon-001` ×1. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 251, 311, 371, 484, 558. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 267, 331, 391, 494, 576. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 96, 114, 224, 344, 420. *Example:* 2 spaces.

### Medium severity
- **[qe-admon-001]** — Use gated syntax for executable code in exercises. *Count:* 1. *Lines:* 429. *Example:* code cell inside non-gated {exercise}.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 79, 116, 296. *Example:* static image .png.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 158, 404, 597. *Example:* {cite} in narrative flow: 'of {cite}`'.

### Low severity
_None found._


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
2. `qe-ref-001` — Use correct citation style (3 occurrences).
3. `qe-admon-001` — Use gated syntax for executable code in exercises (1 occurrence).
4. `qe-writing-008` — Remove excessive whitespace between words (5 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (5 occurrences).
6. `qe-fig-002` — Prefer code-generated figures (3 occurrences).
