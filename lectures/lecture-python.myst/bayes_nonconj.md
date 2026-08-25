# bayes_nonconj

- **Series:** lecture-python.myst
- **File:** `lectures/bayes_nonconj.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-001` ×4. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×5; `qe-fig-003` ×2; `qe-fig-008` ×3. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 228, 238, 270, 480, 493. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 287, 485. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 245, 247, 482. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 55. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 178, 325, 425, 436. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
4. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
