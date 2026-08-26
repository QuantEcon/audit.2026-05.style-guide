# likelihood_var

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_var.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-004` ×1; `qe-writing-008` ×5. |
| Math         | 3.5/10 | `qe-math-002` ×5; `qe-math-011` (proposed) ×2; `qe-math-004` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×6; `qe-fig-005` ×6; `qe-fig-001` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 338, 407, 414, 482, 778, 785. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 323, 399, 421, 448, 710, 767. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 5. *Lines:* 167, 172, 191. *Example:* apostrophe transpose `C'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 48, 53, 419. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 401, 772. *Example:* figsize=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 517, 520, 542. *Example:* \mathbf.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 2. *Lines:* 76, 82. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 39. *Example:* mid-sentence 'Vector'.

### Low severity
_None found._


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (5 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (2 occurrences).
5. `qe-math-004` — Do not use bold face for matrices or vectors (3 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (5 occurrences).
