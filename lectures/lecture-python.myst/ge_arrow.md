# ge_arrow

- **Series:** lecture-python.myst
- **File:** `lectures/ge_arrow.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×15; `qe-writing-004` ×2; `qe-writing-001` ×4, +1 more. |
| Math         | 3/10  | `qe-math-003` ×11; `qe-math-010` (proposed) ×3; `qe-math-002` ×2, +1 more. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 187, 473. *Example:* apostrophe transpose `s'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 11. *Lines:* 540, 550, 566, 597, 607, 623, 627, 721, 731, 754, …. *Example:* array used as matrix.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 5. *Lines:* 67, 187, 704, 711, 765. *Example:* {\bf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 299, 393, 446. *Example:* non-blackboard `\Pr`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 15. *Lines:* 148, 242, 287, 318, 355, 373, 435, 486, 588, 643, …. *Example:* H2 Title Case: 'Recursive Formulation' (Formulation).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 142. *Lines:* 19, 27, 33, 35, 37, 39, 50, 52, 58, 62, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 1249. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 583, 636, 767, 772. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 584. *Example:* mid-sentence 'Horizon'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 1243. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1242. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1247. *Example:* plot() without lw=.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (15 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (11 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
4. `qe-math-002` — Use \top for transpose notation (2 occurrences).
5. `qe-math-004` — Do not use bold face for matrices or vectors (5 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
7. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
