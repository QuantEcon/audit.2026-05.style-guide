# phillips_escaping_nash

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_escaping_nash.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×7; `qe-fig-004` ×5; `qe-fig-008` ×9, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 172, 219, 324, 420, 508. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 181, 224, 331, 339, 427, 513, 518. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 5. *Lines:* 164, 203, 317, 402, 498. *Example:* caption of 7 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 175, 220, 326, 327, 334, 422, 423, 509, 515. *Example:* plot() without lw=.

### Medium severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 40, 95, 476, 526. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 265. *Example:* mid-sentence 'Theorem'.

### Low severity
_None found._


## Strengths

- Writing, Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (7 occurrences).
2. `qe-fig-004` — Caption formatting conventions (5 occurrences).
3. `qe-ref-001` — Use correct citation style (4 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (9 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
