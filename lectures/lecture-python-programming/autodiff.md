# autodiff

- **Series:** lecture-python-programming
- **File:** `lectures/autodiff.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-003` ×3; `qe-writing-006` ×1; `qe-writing-008` ×1. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×11; `qe-fig-008` ×14. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 93, 316, 322, 324, 339, 341. *Example:* `return (f(x + h) - f(x))/h` at 93 has no spaces around the division, unlike every other operator in the same function; and the `grad_descent` body carries trailing whitespace on the `tol=1e-5,` continuation line (316) plus four whitespace-only lines (322, 324, 339, 341) - pycodestyle W291/W293.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 11. *Lines:* 82, 193, 216, 257, 271, 289, 362, 381, 416, 448, …. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 14. *Lines:* 97, 98, 195, 196, 218, 219, 259, 260, 277, 291, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 140, 141. *Example:* apostrophe transpose `)'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 295. *Example:* H2 Title Case: 'Gradient Descent' (Descent).

### Medium severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 263, 293, 450. *Example:* two figures are produced and the narrative moves straight on without saying what the reader should see - the derivative through control flow (257-263) and the derivative of the linear interpolant (289-293) are each followed immediately by a new heading, while the comparable plot at 216-222 does get its comment at 224; and at 450 `α_hat` and `β_hat` are bound for the third time to a third pair of objects (closed-form OLS slope/intercept at 373-374, gradient-descent slope/intercept at 411, quadratic and linear coefficients at 450), with the plot annotations at 455-456 still labelling them α and β.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 468. *Example:* 2 spaces.


## Strengths

- The lecture defines autodiff by elimination - "not finite differences" (64), "not symbolic calculus" (117), then autodiff (150) - and backs each negation with a runnable demonstration rather than an assertion.
- The finite-difference failure is shown before it is claimed: `Df` is plotted against the true `f'` (95-100) and only then does the text say the approximation is inaccurate and unstable (103).
- Gradient descent is validated against the closed-form OLS estimates (370-379) before it is trusted on harder problems, and the check is stated explicitly at 426.
- `grad_descent` is written once with a documented Barzilai-Borwein step rule (312-340) and then reused unchanged for all three loss functions (403, 441, 501).
- Greek and mathematical unicode identifiers (`λ`, `ϵ`, `Δx`, `Δdf`, `α`, `β`, `σ`) keep the code next to the mathematics - exactly the PEP8 exception qe-code-001 allows.

## Recommended actions

1. Add mystnb figure metadata (caption plus name) to the 11 code-cell figures (82, 193, 216, 257, 271, 289, 362, 381, 416, 448 and the solution figure) - not one plot in the lecture can be cross-referenced, and the prose refers to them only by position.
2. Add `lw=2` to the 14 plot calls (97, 98, 195, 196, 218, 219, 259, 260, 277, 291 ...).
3. Fix the comment at 356: `α, β, σ = 0.5, 1.0, 0.1  # Set the true intercept and slope.` names them in the wrong order - the model at 359 is `y = α * x + β`, so α is the slope.
4. Give the three fits distinct names instead of rebinding `α_hat`/`β_hat` at 373, 411 and 450, and add a comment at 263 and 293 saying what the reader should look for in those two plots.
5. Sentence-case "Gradient Descent" (295), and strip the 15 stray `+++` jupytext cell separators (115, 119, 148, 160, 164, 168, 172, 203, 232, 267, 297, 303, 307, 392, 428) from published source.
6. Clean the code cells: the unspaced division at 93 and the trailing/blank-line whitespace at 316, 322, 324, 339, 341.
7. Delete the double space at 468 (qe-writing-008) and the trailing double-space line breaks at 105, 150 and 466.
