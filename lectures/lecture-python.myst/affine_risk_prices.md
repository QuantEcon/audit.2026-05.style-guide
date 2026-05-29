# Style Audit — affine_risk_prices

- **Series:** lecture-python.myst
- **File:** `lectures/affine_risk_prices.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | "i.i.d." used instead of "IID". |
| Math         | 5/10 | Normal distribution written with `\mathcal{N}` rather than plain `N`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=7, uni=10). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-011 (proposed)]** — Normal distribution written with `\mathcal{N}` rather than plain `N`. *Examples:* lines 110, 222, 231, 234, 331, 454, 1041, 1049, 1073, 1083. *Count:* 11 occurrences.
- **[qe-fig-006]** — Axis labels capitalised in 15 places (should be lowercase). *Examples:* line 610, line 611, line 620.

### Medium severity
- **[qe-math-003]** — Matrices use `\begin{pmatrix}` rather than `\begin{bmatrix}`. *Examples:* line 731, line 1303. *Count:* 2 occurrences.
- **[qe-writing-009 (proposed)]** — "i.i.d." used instead of "IID". *Example:* line 110 `is an i.i.d. $m \times 1$ random vector`.

### Low severity
- **[qe-writing-001]** — A handful of multi-sentence paragraphs (e.g. line 53–54) that could be broken into one-sentence units.
- **[qe-code-002]** — Mixed Greek conventions in code (word=7, uni=10).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.

## Strengths
- Consistent use of `^\top` for transpose throughout (~95 instances).
- Equations use the recommended `\begin{math} :label:` form.
- Probability and expectation use `\mathbb{P}`, `\mathbb{E}` correctly.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-math-011 (proposed)`: Normal distribution written with `\mathcal{N}` rather than plain `N`.
2. Address `qe-fig-006`: Axis labels capitalised in 15 places (should be lowercase).
3. Address `qe-math-003`: Matrices use `\begin{pmatrix}` rather than `\begin{bmatrix}`.
4. Address `qe-writing-009 (proposed)`: "i.i.d." used instead of "IID".
5. Address `qe-writing-001`: A handful of multi-sentence paragraphs (e.g. line 53–54) that could be broken into one-sentence units.
