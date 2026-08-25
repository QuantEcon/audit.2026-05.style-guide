# multivariate_normal

- **Series:** lecture-python.myst
- **File:** `lectures/multivariate_normal.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×2; `qe-writing-009` (proposed) ×3; `qe-writing-004` ×1, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×31; `qe-math-002` ×27; `qe-math-003` ×38, +2 more. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×8; `qe-fig-007` ×2; `qe-fig-008` ×14, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 778, 1684, 2232, 2377, 2526, 2594, 2677, 2769. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 14. *Lines:* 395, 396, 783, 784, 785, 1685, 1686, 1687, 1688, 2539, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 27. *Lines:* 1733, 1734, 1743, 1745, 1758, 1786, 1789, 1795, 1801, 1813, …. *Example:* apostrophe transpose `G'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 38. *Lines:* 121, 130, 133, 274, 277, 539, 607, 620, 626, 632, …. *Example:* array used as matrix.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 5. *Lines:* 606, 650, 1504, 1505. *Example:* \boldsymbol.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 31. *Lines:* 84, 896, 1308, 1351, 1485, 1661, 1758, 1786, 2121, 2266, …. *Example:* bare expectation `E\left[`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 10. *Lines:* 1709, 1729, 1740, 1750, 1768, 1829, 1831, 1833, 1843. *Example:* decorated distribution `{\mathcal N}`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 599, 701, 940, 1758, 1860, 1885, 1886. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 384, 2810. *Example:* figsize=.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 2. *Lines:* 389, 390. *Example:* spine removal.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 2822, 2830. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 2145. *Example:* mid-sentence 'Components'.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 3. *Lines:* 602, 1830, 1832. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (31 occurrences).
2. `qe-math-002` — Use \top for transpose notation (27 occurrences).
3. `qe-math-003` — Use square brackets for matrix notation (38 occurrences).
4. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (10 occurrences).
5. `qe-math-004` — Do not use bold face for matrices or vectors (5 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
7. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
