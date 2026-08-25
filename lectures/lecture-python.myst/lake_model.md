# lake_model

- **Series:** lecture-python.myst
- **File:** `lectures/lake_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×6. |
| Math         | 6.5/10 | `qe-math-003` ×4; `qe-math-001` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×8; `qe-fig-003` ×3; `qe-fig-008` ×8, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 364, 433, 473, 610, 690, 708, 798, 816. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 350, 430, 460, 573, 689, 707, 793, 815. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 692, 695, 698, 713, 800, 803, 806, 821. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 97, 128, 148, 173, 380. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 369, 442, 620. *Example:* .set_title.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 267. *Example:* unicode `α` inside a math environment.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 4. *Lines:* 148, 192, 195, 499. *Example:* matrix environment.

### Low severity
_None found._


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (4 occurrences).
3. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (2 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (6 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (8 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (8 occurrences).
