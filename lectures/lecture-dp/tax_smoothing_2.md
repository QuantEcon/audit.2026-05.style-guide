# Style Audit — tax_smoothing_2

- **Series:** lecture-dp
- **File:** `lectures/tax_smoothing_2.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2 sentence case. |
| Math         | 6/10  | `\cal N`; bare `E_0`; `\cr` separators in `aligned`. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 3×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | One `ax.set_title('One-period debt issuance share')`; 9 Title-Case `'Time'` xlabels. |
| References   | 9/10  | 6 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | `{doc}` used 4×; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-006]** — Nine Title-Case `xlabel('Time')` axis labels. *Lines:* 477, 480, 524, 527, 822, 825, 828, 831, 842.

### Medium severity
- **[qe-math-A3]** — Multivariate normal written as `{\cal N}(0,I)` (line 142).
- **[qe-math-A1]** — Bare `E_0` for expectation in display equation (line 122). Should be `\mathbb{E}_0`.
- **[qe-math-001]** — `\cr` row separator used throughout `aligned` blocks. *Lines:* 129-138, 181-185, and many more.
- **[qe-fig-003]** — `ax.set_title('One-period debt issuance share')` (line 841).
- **[qe-fig-001]** — `figsize=` set 3 times.

### Low severity
- **[qe-writing-A1]** — Smart quotes ” “ used in narrative (lines 155, 178).
- **[qe-writing-001]** — Some long paragraphs (e.g. 32-37, 53-62).

## Strengths
- Lecture title in correct Title Case.
- H2 headings sentence case ("Overview", "Two example specifications", "One- and two-period bonds but no restructuring", "Mapping into an LQ Markov jump problem", "Penalty on different issues across maturities", "A model with restructuring", "Restructuring as a Markov jump linear quadratic control problem", "Example with restructuring").
- Matrices use `bmatrix` (28 matrix blocks).
- Equation labels used cleanly.
- "IID"/Greek-letter conventions consistent.
- No `\tag`, no bold vectors, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek; `{doc}` used.

## Recommended actions
1. Lowercase `'Time'` axis labels (9 occurrences) — biggest single fix for figures.
2. Replace `{\cal N}` with plain `N`.
3. Replace bare `E_0` with `\mathbb{E}_0`.
4. Replace `\cr` with `\\` inside `aligned`.
5. Remove the `ax.set_title('One-period debt issuance share')` call.
6. Normalise smart-quotes.
