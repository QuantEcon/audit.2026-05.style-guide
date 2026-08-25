# phillips_adaptive

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_adaptive.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-004` ×2; `qe-fig-003` ×1; `qe-fig-005` ×1, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 133, 302, 445. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 308. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 114, 295. *Example:* caption of 11 words.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 84, 399. *Example:* {cite} in narrative flow: '{cite}`'.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 219. *Example:* spelled-out `beta`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 438. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (3 occurrences).
2. `qe-fig-004` — Caption formatting conventions (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
