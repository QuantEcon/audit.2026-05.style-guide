# Style Audit — tax_smoothing_3

- **Series:** lecture-dp
- **File:** `lectures/tax_smoothing_3.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2 sentence case. |
| Math         | 7/10  | `\cal N`; bare `E_0`. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 2×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | 4 Title-Case `'Time'` xlabels; no matplotlib titles. |
| References   | 9/10  | 4 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | `{doc}` used 4×; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-011 (proposed)]** — Multivariate normal written as `{\cal N}(0,I)` (line 97).
- **[qe-math-010 (proposed)]** — Bare `E_0` for expectation in display equation (line 80). Should be `\mathbb{E}_0`.
- **[qe-fig-006]** — Four Title-Case `xlabel('Time')`. *Lines:* 276, 279, 317, 320.

### Low severity
- **[qe-writing-009 (proposed)]** — Smart quotes ” “ used in narrative (lines 107, 145, 160, 170).
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 2 times.

## Strengths
- Lecture title in correct Title Case.
- All H2 headings sentence case ("Overview", "Roll-over risk", "A dead end", "Better representation of roll-over risk").
- Definitions bolded ("**roll-over risk**").
- "IID"/Greek-letter conventions consistent.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series.
- No matplotlib titles, no spine issues.

## Recommended actions
1. Lowercase `'Time'` axis labels.
2. Replace `{\cal N}` with plain `N`.
3. Replace bare `E_0` with `\mathbb{E}_0`.
4. Normalise smart-quotes.
