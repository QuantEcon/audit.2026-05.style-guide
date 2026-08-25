# newton_method

- **Series:** lecture-python.myst
- **File:** `lectures/newton_method.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-001` ×2. |
| Math         | 8.5/10 | `qe-math-002` ×1. |
| Code         | 9/10  | `qe-code-004` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×7; `qe-fig-003` ×1; `qe-fig-008` ×8, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 9. *Lines:* 690, 739, 804, 847, 859, 971, 1002, 1010, 1087. *Example:* %%time.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 210, 217, 247, 335, 647, 655, 667. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 189, 254, 255, 348, 351, 354, 357, 360. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 400. *Example:* \prime transpose.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 212, 219, 344, 668. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 641. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 513, 701. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-math-002` — Use \top for transpose notation (1 occurrence).
4. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (8 occurrences).
6. `qe-code-004` — Use quantecon Timer context manager (9 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
