# aiyagari

- **Series:** lecture-python.myst
- **File:** `lectures/aiyagari.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-004` ×2; `qe-writing-006` ×1; `qe-writing-008` ×3. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-008` ×5; `qe-fig-001` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 376, 434, 499, 564, 666. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 380, 508, 591, 597, 677. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 109. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 98. *Example:* H2 Title Case: 'The Economy' (Economy).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 379, 506, 588. *Example:* figsize=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 78, 692. *Example:* mid-sentence 'Dynamics'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 104, 106, 215. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
4. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (5 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
