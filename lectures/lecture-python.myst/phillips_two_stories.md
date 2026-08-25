# phillips_two_stories

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_two_stories.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×2; `qe-writing-004` ×9. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×8; `qe-fig-004` ×6; `qe-fig-001` ×7. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 162, 203, 232, 260, 498, 536, 575. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 8. *Lines:* 167, 210, 239, 266, 272, 511, 542, 581. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 6. *Lines:* 155, 196, 225, 251, 491. *Example:* caption of 7 words.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 9. *Lines:* 42, 60, 333, 335, 355, 366, 378, 406, 432. *Example:* mid-sentence 'Inflation'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 331, 337. *Example:* H2 Title Case: 'Ignoring the Lucas Critique' (Critique).

### Medium severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 301, 402, 430, 463. *Example:* {cite} in author position: '{cite}`SamuelsonSolow1960` found'.

### Low severity
_None found._


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (9 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (8 occurrences).
4. `qe-fig-004` — Caption formatting conventions (6 occurrences).
5. `qe-ref-001` — Use correct citation style (4 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (7 occurrences).
