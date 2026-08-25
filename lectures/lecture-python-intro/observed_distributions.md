# observed_distributions

- **Series:** lecture-python-intro
- **File:** `lectures/observed_distributions.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-001` ×1; `qe-writing-008` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-004` ×4; `qe-fig-005` ×1; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 457, 557, 715, 741. *Example:* Title Case caption (Amazon).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 536, 823, 854. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 229. *Example:* 4 sentences in one paragraph.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 688. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 231. *Example:* 2 spaces.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-004` — Caption formatting conventions (4 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
4. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
