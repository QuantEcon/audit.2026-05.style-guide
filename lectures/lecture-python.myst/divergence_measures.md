# divergence_measures

- **Series:** lecture-python.myst
- **File:** `lectures/divergence_measures.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-006` ×1; `qe-writing-008` ×26; `qe-writing-009` (proposed) ×1. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×1; `qe-math-006` ×1; `qe-math-005` ×1. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×4; `qe-fig-008` ×2, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 1. *Lines:* 134. *Example:* bare \begin{align} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 219. *Example:* bare expectation `E_{f}\left[`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 148. *Example:* H2 Title Case: 'Two Beta distributions: running example' (Beta).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 26. *Lines:* 32, 34, 36, 38, 40, 42, 68, 70, 71, 77, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 56, 173. *Example:* spelled-out `gamma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 185, 274, 438, 473. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 443, 448, 499. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 166, 268, 433, 467. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 492, 494. *Example:* plot() without lw=.

### Low severity
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 1. *Lines:* 310. *Example:* parenthesised sequence.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 336. *Example:* iid.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
6. `qe-math-006` — Use aligned environment correctly for PDF compatibility (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (26 occurrences).
