# amss

- **Series:** lecture-dp
- **File:** `lectures/amss.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 sentence case throughout. |
| Math         | 7/10  | `pmatrix` and `\left(\begin{matrix}\right)`; `\mathbb E` braces inconsistent. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize used 3×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 8/10  | No matplotlib titles; lowercase labels; figsize 3×. |
| References   | 9/10  | 6 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 8/10  | `{doc}` used 11 times; no raw cross-series URLs. |
| Admonitions  | 8/10  | Two `{exercise}` directives with labels. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-003]** — Matrices use `pmatrix` (line 794) and `\left(\begin{matrix}…\end{matrix}\right)` (line 807) instead of `bmatrix`. *Count:* 2 matrix blocks.
- **[qe-math-010 (proposed)]** — `\mathbb E_0` written without braces in display equations (line 297). Style is `\mathbb{E}_0`.

### Low severity
- **[qe-writing-009 (proposed)]** — Smart quotes ’ used in narrative (lines 165, 200, 247).
- **[qe-writing-001]** — A few multi-sentence paragraphs (e.g. 121-127).
- **[qe-fig-001]** — `figsize=` set 3 times.

## Strengths
- Lecture title in correct Title Case.
- H2/H3/H4 headings sentence case.
- Definitions bolded ("**natural debt limit**", "**measurability constraints**").
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- No transpose, no bold vectors, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series; no raw URLs.
- No matplotlib titles, no spine, no Title-Case labels.

## Recommended actions
1. Replace `pmatrix` and `\left(\begin{matrix}…\end{matrix}\right)` with `\begin{bmatrix}…\end{bmatrix}`.
2. Standardise `\mathbb E_0` → `\mathbb{E}_0`.
3. Normalise smart-quotes back to straight `'`.
