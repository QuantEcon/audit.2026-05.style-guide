# BCG_incomplete_mkts

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/BCG_incomplete_mkts.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×7; `qe-writing-006` ×1; `qe-writing-008` ×41. |
| Math         | 5/10  | `qe-math-002` ×46. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×9; `qe-fig-005` ×2; `qe-fig-010` ×1, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 9. *Lines:* 1866, 1868, 1870, 1872, 1874, 1889, 1915, 1922, 1926. *Example:* .set_title.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 46. *Lines:* 353, 354, 365, 366, 375, 376, 391, 392, 445, 446, …. *Example:* \prime transpose.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 7. *Lines:* 567, 574, 630, 688, 692, 698, 1331. *Example:* 4 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1278. *Example:* H4 Title Case: 'A Modigliani-Miller theorem?' (Modigliani-Miller).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 41. *Lines:* 39, 45, 49, 60, 62, 64, 67, 144, 292, 299, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 1864, 1909. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1862, 1907. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-010]** — Plotly figures require latex directive. *Count:* 1. *Lines:* 1. *Example:* plotly used with no {only} latex directive.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 79. *Example:* {cite} in author position: '{cite}`BCG_2018` and'.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (46 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (7 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (9 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (41 occurrences).
7. `qe-fig-010` — Plotly figures require latex directive (1 occurrence).
