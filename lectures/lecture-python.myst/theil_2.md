# theil_2

- **Series:** lecture-python.myst
- **File:** `lectures/theil_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-001` ×3; `qe-writing-008` ×4. |
| Math         | 8/10  | `qe-math-004` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-001` ×5. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 163, 341, 660, 709, 779. *Example:* figsize=.

### Medium severity
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 288, 289, 296. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 50, 291, 758. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 50, 292, 467, 760. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 770. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (3 parenthetical, 11 in-text).

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
4. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (4 occurrences).
