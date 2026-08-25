# ak_aiyagari

- **Series:** lecture-python.myst
- **File:** `lectures/ak_aiyagari.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-008` ×53. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-003` ×1; `qe-code-004` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×18; `qe-fig-005` ×8; `qe-fig-001` ×6, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 603, 988, 1202, 1255, 1338, 1420. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 18. *Lines:* 570, 610, 617, 1039, 1040, 1041, 1153, 1207, 1212, 1224, …. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 563, 599, 1136, 1201, 1252, 1337, 1373, 1417. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 53. *Lines:* 30, 33, 34, 44, 99, 101, 109, 193, 246, 253, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 3. *Lines:* 519, 557, 742. *Example:* %time.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 565, 1149, 1377. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 33, 34, 35. *Example:* {cite} in narrative flow: 'in   {cite}`'.

### Low severity
_None found._


## Strengths

- Math, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (18 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
3. `qe-ref-001` — Use correct citation style (4 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (53 occurrences).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
