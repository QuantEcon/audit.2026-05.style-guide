# samuelson

- **Series:** lecture-python.myst
- **File:** `lectures/samuelson.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×7; `qe-fig-003` ×3; `qe-fig-007` ×1, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 8/10  | `qe-link-002` ×1; `qe-link-001` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 6. *Lines:* 741, 742, 979. *Example:* spelled-out `alpha`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 413, 653, 1068, 1196, 1310, 1333. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 405, 1143, 1155, 1169, 1358, 1363, 1368. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 430, 431, 432, 654, 1069, 1200, 1316, 1337. *Example:* plot() without lw=.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 1201, 1317, 1341. *Example:* .set(title=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 41. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 315, 352. *Example:* 2 spaces.

### Low severity
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 1. *Lines:* 436. *Example:* spine removal.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 387. *Example:* full URL to own series (python.quantecon.org).
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 403. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- Writing, Math, References score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (6 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-link-001` — Use markdown style links for lectures in same lecture series (1 occurrence).
7. `qe-fig-007` — Keep figure box and spines (1 occurrence).
