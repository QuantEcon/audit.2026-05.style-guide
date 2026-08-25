# likelihood_ratio_process

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_ratio_process.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×7; `qe-writing-001` ×4; `qe-writing-006` ×1, +1 more. |
| Math         | 3.5/10 | `qe-math-010` (proposed) ×52; `qe-math-004` ×3. |
| Code         | 7.5/10 | `qe-code-002` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3.5/10 | `qe-fig-003` ×9; `qe-fig-005` ×7; `qe-fig-006` ×4, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 7. *Lines:* 59, 62, 144, 541, 548. *Example:* spelled-out `gamma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 12. *Lines:* 192, 488, 555, 589, 776, 1018, 1119, 1198, 1224, 1311, …. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 9. *Lines:* 198, 510, 560, 603, 656, 808, 822, 1464, 1670. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 225, 344, 354, 642, 754, 1116, 1306. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 227, 346, 355, 498, 499, 556, 557, 593, 596, 651, …. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 52. *Lines:* 237, 242, 252, 262, 263, 264, 265, 272, 277, 297, …. *Example:* bare expectation `E\left[`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 422, 448, 473, 1847. *Example:* mid-sentence 'Type'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 70. *Example:* H2 Title Case: 'Likelihood Ratio Process' (Ratio, Process).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 31. *Lines:* 847, 848, 850, 859, 869, 872, 873, 874, 876, 878, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 559, 600, 601, 655. *Example:* axis label `Probability`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 1520. *Example:* \boldsymbol.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 876, 924, 1841, 1853. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (52 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (7 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (9 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (7 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
7. `qe-math-004` — Do not use bold face for matrices or vectors (3 occurrences).
