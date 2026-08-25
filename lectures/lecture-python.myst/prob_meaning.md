# prob_meaning

- **Series:** lecture-python.myst
- **File:** `lectures/prob_meaning.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×3; `qe-writing-001` ×6; `qe-writing-004` ×4, +1 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×6; `qe-fig-005` ×8; `qe-fig-008` ×10, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 184, 215, 247, 449, 504, 537, 603, 634. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 188, 219, 251, 606, 613, 641. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 183, 214, 246, 437, 496, 536, 599, 626. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 186, 187, 217, 218, 249, 250, 452, 457, 505, 541. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 578, 592. *Example:* non-blackboard `\operatorname{Var}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 228, 381, 399, 561, 661, 663. *Example:* 2 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 58, 286, 665. *Example:* H2 Title Case: 'Frequentist Interpretation' (Interpretation).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 36. *Lines:* 20, 36, 38, 56, 62, 75, 83, 90, 94, 102, …. *Example:* 2 spaces.

### Medium severity
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 267, 583. *Example:* mid-sentence 'Law'.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (6 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (36 occurrences).
