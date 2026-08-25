# prob_matrix

- **Series:** lecture-python.myst
- **File:** `lectures/prob_matrix.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-004` ×7; `qe-writing-009` (proposed) ×4; `qe-writing-008` ×64, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×7; `qe-math-003` ×15; `qe-math-011` (proposed) ×2. |
| Code         | 7.5/10 | `qe-code-002` ×4; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×10; `qe-fig-006` ×2; `qe-fig-008` ×2, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 10. *Lines:* 955, 965, 991, 1000, 1037, 1056, 1071, 1078, 1703, 1811. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 15. *Lines:* 261, 391, 501, 599, 696, 711, 723, 733, 914, 917, …. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 7. *Lines:* 588, 1632, 1634, 1636, 1676, 1694. *Example:* non-blackboard `\mathrm{E}`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 78, 194, 196, 1626, 1738, 1784. *Example:* mid-sentence 'Values'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 64. *Lines:* 233, 234, 255, 258, 269, 274, 284, 286, 311, 319, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 835, 836, 837. *Example:* spelled-out `xi`.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 43. *Example:* non-Anaconda import with no install cell: ['matplotlib_inline'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 1551, 1830. *Example:* figsize=.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 1722, 1837. *Example:* axis label `Probability`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 1041, 1074. *Example:* plot() without lw=.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 2. *Lines:* 1015, 1016. *Example:* decorated distribution `\mathbb{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1252. *Example:* 2 sentences in one paragraph.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 4. *Lines:* 134, 137, 167, 1788. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (7 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (15 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (10 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (7 occurrences).
5. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (2 occurrences).
6. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (4 occurrences).
7. `qe-fig-006` — Lowercase axis labels (2 occurrences).
