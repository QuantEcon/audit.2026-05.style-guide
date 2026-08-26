# lln_clt

- **Series:** lecture-python.myst
- **File:** `lectures/lln_clt.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-006` ×3; `qe-writing-008` ×1. |
| Math         | 3/10  | `qe-math-010` (proposed) ×42; `qe-math-004` ×121; `qe-math-002` ×5, +1 more. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-001` ×6; `qe-fig-008` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 239, 332, 405, 480, 696, 915. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 226, 331, 390, 444, 675, 883. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 5. *Lines:* 572, 750, 765, 870, 871. *Example:* apostrophe transpose `)'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 121. *Lines:* 529, 531, 533, 536, 537, 538, 541, 545, 548, 564, …. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 42. *Lines:* 95, 104, 109, 134, 140, 154, 155, 162, 163, 167, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 82, 283, 517. *Example:* H3 Title Case: 'The Classical LLN' (Classical).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 462, 463. *Example:* spelled-out `sigma`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 4. *Lines:* 550, 558, 580, 809. *Example:* array used as matrix.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 263. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 825. *Example:* 2 spaces.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (42 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (121 occurrences).
3. `qe-math-002` — Use \top for transpose notation (5 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
6. `qe-math-003` — Use square brackets for matrix notation (4 occurrences).
7. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
