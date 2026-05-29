# Style Audit — opt_tax_recur

- **Series:** lecture-dp
- **File:** `lectures/opt_tax_recur.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 sentence case throughout. |
| Math         | 6/10  | `{\cal S}` for state space; `\left(\begin{matrix}\right)` matrices. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 5×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | One `ax.set_title('Gross Interest Rate')` Title-Case; one Title-Case xlabel `'Initial Government Debt'`; figsize 5×. |
| References   | 9/10  | 5 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | `{doc}` used 5×; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-004]** — `{\cal S}` used for state space (lines 78, 812, 818, 829, 840, 850, 926). *Count:* 7+.
- **[qe-math-003]** — Two matrix blocks use `\left(\begin{matrix} … \end{matrix}\right)` (lines 1053, 1064).
- **[qe-fig-003]** — `ax.set_title('Gross Interest Rate')` (line 1175) — Title Case.
- **[qe-fig-006]** — Title-Case `xlabel('Initial Government Debt')` (line 1254).
- **[qe-fig-001]** — `figsize=` set 5 times.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs.
- **[qe-writing-A1]** — Smart quotes ’ used in narrative.

## Strengths
- Lecture title in correct Title Case.
- H2/H3 headings sentence case.
- Definitions bolded ("**government policy**", "**feasible allocation**", "**price system**", "**competitive equilibrium with distorting taxes**", "**Ramsey problem**", "**Ramsey allocation**").
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- `\mathbb{E}` used; `aligned` properly inside `$$`.
- No transpose, no bold vectors, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series.

## Recommended actions
1. Replace `{\cal S}` with plain `S`.
2. Replace `\left(\begin{matrix} … \end{matrix}\right)` with `\begin{bmatrix} … \end{bmatrix}`.
3. Remove the embedded title; lowercase the `'Initial Government Debt'` xlabel.
4. Reduce unnecessary `figsize=` usage.
5. Normalise smart-quotes.
