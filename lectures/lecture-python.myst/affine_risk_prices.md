# affine_risk_prices

- **Series:** lecture-python.myst
- **File:** `lectures/affine_risk_prices.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×2; `qe-writing-009` (proposed) ×1; `qe-writing-008` ×4. |
| Math         | 4/10  | `qe-math-010` (proposed) ×3; `qe-math-011` (proposed) ×9; `qe-math-003` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-006` ×16; `qe-fig-004` ×4; `qe-fig-001` ×5, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 581, 705, 798, 980, 1343. *Example:* figsize=.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 16. *Lines:* 610, 611, 620, 712, 713, 807, 808, 821, 822, 991, …. *Example:* axis label `Maturity (quarters)`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 234, 238, 869. *Example:* non-blackboard `\text{Var}`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 9. *Lines:* 110, 222, 231, 234, 331, 454, 1041, 1049, 1083. *Example:* decorated distribution `\mathcal{N}`.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 567, 782, 958, 1324. *Example:* caption of 7 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 594, 805. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 731, 1303. *Example:* pmatrix environment.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 63. *Example:* {cite} in author position: '{cite}`Bansal_Yaron_2004` and'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 652, 680. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 51, 54, 653, 680. *Example:* 2 spaces.

### Low severity
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 110. *Example:* i.i.d..


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-006` — Lowercase axis labels (16 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
3. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (9 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-math-003` — Use square brackets for matrix notation (2 occurrences).
6. `qe-ref-001` — Use correct citation style (2 occurrences).
7. `qe-fig-004` — Caption formatting conventions (4 occurrences).
