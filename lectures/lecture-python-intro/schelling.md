# schelling

- **Series:** lecture-python-intro
- **File:** `lectures/schelling.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-003` ×1; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 250. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 246, 248, 427. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 154. *Example:* raw link to python-programming.quantecon.org.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 91. *Example:* 2 spaces.


## Strengths

- Writing, Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
2. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
3. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
