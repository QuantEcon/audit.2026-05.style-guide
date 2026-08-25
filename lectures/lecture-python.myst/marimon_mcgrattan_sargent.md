# marimon_mcgrattan_sargent

- **Series:** lecture-python.myst
- **File:** `lectures/marimon_mcgrattan_sargent.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×8; `qe-writing-006` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×4; `qe-fig-001` ×2; `qe-fig-008` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 8. *Lines:* 1311, 1316, 1554, 1819, 1874, 1880, 1944, 2028. *Example:* mid-sentence 'Economy'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 89. *Example:* H2 Title Case: 'The Kiyotaki-Wright environment' (Kiyotaki-Wright).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 964, 992. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 969, 975, 1009, 1015. *Example:* .set_title.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 34, 259. *Example:* {cite} in author position: '{cite}`KiyotakiWright1989` studied'.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 996. *Example:* plot() without lw=.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (8 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
3. `qe-ref-001` — Use correct citation style (2 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
