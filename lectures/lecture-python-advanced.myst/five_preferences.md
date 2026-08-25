# five_preferences

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/five_preferences.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×7; `qe-writing-008` ×24. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-005` ×13; `qe-fig-003` ×5; `qe-fig-008` ×61, +1 more. |
| References   | 7/10  | `qe-ref-001` ×18. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 19. *Lines:* 74, 75, 76, 77, 78, 79, 229, 273, 557, 613, …. *Example:* style override.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 291, 312, 628, 644, 1569. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 13. *Lines:* 221, 265, 554, 610, 761, 802, 1102, 1231, 1342, 1407, …. *Example:* non-descriptive name `figure1`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 61. *Lines:* 230, 285, 306, 558, 559, 615, 616, 617, 622, 623, …. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 18. *Lines:* 380, 477, 899, 1369, 1820, 1826, 1829, 1844, 1916. *Example:* {cite} in author position: '{cite}`HansenSargent2001` and'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 7. *Lines:* 166, 904, 1172, 1254, 1279, 1289, 1833. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 24. *Lines:* 18, 21, 24, 26, 36, 39, 47, 150, 151, 152, …. *Example:* 2 spaces.

### Medium severity
_None found._

### Low severity
_None found._


## Strengths

- Math, Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (18 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (13 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (7 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
5. `qe-fig-008` — Use lw=2 for line charts (61 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (24 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (19 occurrences).
