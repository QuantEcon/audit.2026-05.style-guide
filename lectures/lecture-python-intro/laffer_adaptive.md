# laffer_adaptive

- **Series:** lecture-python-intro
- **File:** `lectures/laffer_adaptive.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×31; `qe-writing-001` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×3; `qe-fig-004` ×2; `qe-fig-008` ×7, +1 more. |
| References   | 7.5/10 | `qe-ref-001` ×6. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 241, 373, 374, 375, 376, 468, 469. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 6. *Lines:* 23, 49, 51. *Example:* {cite} in author position: '{cite}`Cagan` and'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 31. *Lines:* 14, 18, 20, 22, 23, 31, 33, 37, 44, 46, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 364, 529. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 219, 398. *Example:* caption of 10 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 360, 457, 524. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 33. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (6 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
3. `qe-fig-004` — Caption formatting conventions (2 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (31 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (7 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
