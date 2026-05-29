# Style Audit — un_insure

- **Series:** lecture-dp
- **File:** `lectures/un_insure.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 sentence case. |
| Math         | 7/10  | Bare `E` for expectation; stray `%\EQN` LaTeX comment. |
| Code         | 8/10  | Unicode Greek; no pip install needed; PEP8; figsize 1×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Two `plt.title(...)` calls; no Title-Case labels. |
| References   | 9/10  | 9 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | No raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — Bare `E` used for expectation in display equation (line 34: `E \sum_{t=0}^\infty \beta^t [u(c_t) - a_t]`). Should be `\mathbb{E}`.
- **[qe-math-007]** — Stray `%\EQN hugo1` LaTeX comment leaked into MyST source on line 36.
- **[qe-fig-003]** — Two `plt.title(...)` calls. *Lines:* 846 (`plt.title("Optimal replacement ratio")`), 855 (`plt.title("Optimal search effort")`).

### Low severity
- **[qe-writing-A1]** — A few smart quotes ’ in narrative.
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. 83-91, 175-181).
- **[qe-fig-001]** — `figsize=` set 1 time.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Definitions bolded ("**insurance agency**", "**planner**").
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- Unicode Greek in code.

## Recommended actions
1. Replace bare `E` with `\mathbb{E}` on line 34.
2. Remove the stray `%\EQN hugo1` LaTeX comment on line 36.
3. Remove the 2 `plt.title(...)` calls.
4. Optional: normalise smart-quotes.
