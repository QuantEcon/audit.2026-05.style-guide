# kalman

- **Series:** lecture-python.myst
- **File:** `lectures/kalman.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-002` ×5; `qe-writing-005` ×2; `qe-writing-003` ×2, +2 more. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×5; `qe-math-003` ×5. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×8; `qe-fig-008` ×2; `qe-fig-002` ×1. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 140, 189, 280, 396, 586, 600, 662, 764. *Example:* {image} without :name:.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 5. *Lines:* 123, 131, 387, 731, 743. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 354, 355, 706, 711. *Example:* non-blackboard `\operatorname{Var}`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 335, 530, 551, 701, 713. *Example:* 335 is a 41-word sentence that introduces a new random vector, an independence assumption and a distribution in one breath; 701 is 45 words with a trailing parenthetical that duplicates its own main clause; 713-715 restates the comparison already set up at 703-711. Two passages say the same thing twice: the `{note}` at 467-471 explains that $\mu_t$ is written $\hat x_t$ in the literature, and the parenthetical at 530 explains it again; and the phrase "The class `Kalman` from the [QuantEcon.py](https://quantecon.org/quantecon-py/) package" appears in full, with the same link, at both 527 and 551.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 60, 364, 518, 552. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 163, 626, 680, 774. *Example:* 163 binds `X, Y = np.meshgrid(x_grid, y_grid)` - the lecture's own $X_t$ (hidden state) and $Y_t$ (signal) reused as plotting grids, and both then sit in the same cells as `μ`, `Σ` and the scalar `y` observation at 157, so `X`, `Y`, `y` and `Z` mean four unrelated things in 40 lines; 774 puts spaces around `=` in the keyword argument `mu_0 = np.zeros(2)` (PEP8 E251), the only such call in the file; 680 binds a lambda to a name (E731) whose parameter `x` shadows the simulated state path `x` returned at 673; and 626 escapes LaTeX inside an f-string (`f'... $\\theta = {θ:.1f}$'`) where an `rf''` string would carry the backslash directly.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 623, 689. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 148, 381. *Example:* the first code cell defines `G` and `R` at 148-151 under the comment "Define the matrices G and R from the measurement equation Y = G X + v", and `A` and `Q` at 152-155 - but the measurement equation is not introduced until `` {eq}`kl_measurement_model` `` at 211, and the law of motion not until `` {eq}`kl_xdynam` `` at 328, so the reader meets four matrices and a signal value `y` roughly 60 to 180 lines before any of them is defined, and the sentence that finally explains the choices ($G = I$, $R = 0.5\Sigma$) arrives at 302, after the figure that used them; separately, 381-382 breaks off mid-thought - "the following figure, where the update has used parameters" - and hands the reader a bare display of $A$ and $Q$.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 274, 704. *Example:* the bold-for-definition pattern is right everywhere else (**prior** 102, **filtering distribution** 314, **Kalman gain** 362, **predictive distribution** 379), which isolates two reversals: 274 italicises a term as it is coined ("the *signal surprise* $Y_t - G\mu$") where the rule asks for bold, and 704 bolds a word used purely for emphasis ("a competitor who **is** allowed to observe $X_{t-1}$") where it asks for italic.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 586. *Example:* static image .png.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 512. *Example:* `` {cite} `` in narrative flow: 'in `` {cite} ``'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 473. *Example:* "## Convergence" (473-520) is the only substantial section of this lecture with no figure, in a lecture that spends four cumulative contour plots on the two preceding steps. It argues that $\Sigma_t$ follows a Riccati difference equation `` {eq}`kalman_sdy` ``, that a fixed point solves `` {eq}`kalman_dare` ``, and that $\{\Sigma_t\}$ converges from any nonnegative definite $\Sigma_0$ when $A$ is stable - all of it a picture the lecture is already equipped to draw, since `Kalman.stationary_values()` (used at 790) gives the limit and `kn.update` gives the path. One plot of the diagonal entries of $\Sigma_t$ against $t$, approaching the dashed stationary values from two different $\Sigma_0$, would make the whole section concrete, and exercise `kalman_ex4` at 822-830 asks the reader to observe exactly that behaviour with nothing to observe it against.


## Strengths

- The four contour figures (140, 189, 280, 396) are one picture built in four exposures: prior, prior with the signal $Y_t$ marked, prior with the filtered density laid over it, then all three with the predictive density - each keeps the earlier densities as black contour lines, so every step is visibly a transformation of the previous one rather than a new plot.
- The missile story at 78-98 earns its keep by posing a question a point prediction cannot answer ("what is the probability that the missile is within 500km of Manhattan?") and then introducing the prior density as the object that can, so $p$ arrives as the answer to a stated need.
- Ten display equations are labelled and every one of them is cited where it is used - `kl_measurement_model` at 240 and 450, `kl_filter_exp`/`kl_filter_exp2` at 339, `kl_xdynam` at 335, 451, 483 and 574, `kalman_lom` at 490, `kalman_sdy` at 500 and 508, `kalman_dare` at 510, 520, 556 and 827 - which is what lets the later sections refer back precisely instead of re-deriving.
- Transposes are written `^\top` without exception (255, 263, 346, 355, 356, 357, 375, 461, 495, 505, 548) - there is not one apostrophe transpose in a lecture that is almost entirely matrix algebra.
- The lecture reconciles its own notation with two others: the `{note}` at 467-471 maps $\mu_t$ to the literature's $\hat x_t$, and 545-549 maps its $Q$ and $R$ to `LinearStateSpace`'s $C$ and $H$ via $Q := CC^\top$, $R := HH^\top$ - so a reader moving between the lecture, the textbooks and QuantEcon.py is never stranded.
- Exercise `kalman_ex3` (697-756) sets the filter against a competitor who observes the latent state and predicts optimally, which is a test the filter could fail, and 817 reports the outcome honestly rather than claiming a win.
- Code notation tracks the mathematics: `Σ`, `μ`, `μ_F`, `Σ_F`, `θ`, `ϵ` are unicode and read the same as the display equations they implement.

## Recommended actions

1. Convert the five `array` environments to `bmatrix` (123, 131, 387, 731, 743) - the largest single mechanical fix here, and it removes the `\left( ... \right)` scaffolding around each of them.
2. Add a convergence figure to section 473-520: the diagonal entries of $\Sigma_t$ against $t$ from two different $\Sigma_0$, with the `stationary_values()` solution as dashed horizontals - it is the missing panel in an otherwise well-illustrated lecture and it gives exercise `kalman_ex4` something to look at.
3. Add `:name:` to the static image at 586 and `mystnb: figure: caption`/`name` metadata to the seven code-cell figures (140, 189, 280, 396, 600, 662, 764); the four cumulative contour plots in particular are referred to only as "the next figure" (187), "the following figure" (381) and "shown below" (138), which `{numref}` would fix.
4. Move the matrix definitions in the first code cell (148-155) down to the sections that introduce them, or state the measurement equation and law of motion before that cell; as it stands the reader meets `G`, `R`, `A`, `Q` and `y` up to 180 lines before they are defined.
5. Write `\mathbb{V}` for the two `\operatorname{Var}` (354, 355) and add braces to `\mathbb E` at 706 and 711 (qe-math-010 (proposed), proposed); switch the citation at 512 to `{cite:t}`; and close the five double spaces (60, 364, 518, 552).
6. Cut the duplication: keep one of the two `\hat x_t` explanations (467-471 or 530), collapse 527 and 551 into a single description of the `Kalman` class, and trim 713-715, which restates 703-711.
7. Replace the static PNG at 586 with a code-generated figure (qe-fig-002), add `lw=2` at 623 and 689, gate `kalman_ex4` (822) with `exercise-start`/`exercise-end` to match the other three, put the definition at 274 in bold and the emphasis at 704 in italic, and give the sentences at 42, 187, 279, 314 and 379 their missing full stops.
