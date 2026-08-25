# scalar_dynam

- **Series:** lecture-python-intro
- **File:** `lectures/scalar_dynam.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-001` ×2; `qe-writing-008` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-007` ×2; `qe-fig-005` ×1; `qe-fig-008` ×3. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 425, 426. *Example:* spelled-out `alpha`.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 2. *Lines:* 341, 344. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 377, 386, 410. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 300, 421. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 330. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 111. *Example:* 2 spaces.


## Strengths

- Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
2. `qe-fig-007` — Keep figure box and spines (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
