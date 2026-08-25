# genetic_classifier

- **Series:** lecture-python.myst
- **File:** `lectures/genetic_classifier.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-006` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-004` ×2; `qe-fig-003` ×1; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 178. *Example:* H2 Title Case: 'Associative memory: the Hopfield network' (Hopfield).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 151, 262, 458, 588. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 275. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 252, 563. *Example:* caption of 7 words.

### Low severity
_None found._


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 5 in-text).

## Recommended actions

1. `qe-fig-004` — Caption formatting conventions (2 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
3. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
4. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
