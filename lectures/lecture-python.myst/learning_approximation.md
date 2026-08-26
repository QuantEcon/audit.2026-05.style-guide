# learning_approximation

- **Series:** lecture-python.myst
- **File:** `lectures/learning_approximation.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×4; `qe-writing-003` ×2; `qe-writing-002` ×3, +1 more. |
| Math         | 8/10  | `qe-math-010` (proposed) ×1; `qe-math-009` ×3. |
| Code         | 6.5/10 | `qe-code-001` ×20; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 20. *Lines:* 192, 220, 222, 235, 239, 312, 314, 319, 327, 353, …. *Example:* eighteen lines inside code cells run past 79 characters (PEP8 E501): 192, 220, 235, 239, 314, 319, 327, 353, 386, 460, 473, 582, 594, 701, 752, 753, 754 and 830, with 460 at 93 and 220 at 90 - and in several cases the overrun is a trailing comment (460 pushes `# date t-1 Euler realizes now` out to column 57) or a nested generator expression that would read better split (220, 239). 222 binds a lambda to a name inside `solve_benchmark` (E731) where a two-line `def` would do. Blank-line separation between top-level defs is inconsistent within the same cells: one line at 302-312, two at 316-318, one at 173 after the assignment.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 257, 351, 484, 605, 828. *Example:* figsize=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 112. *Example:* non-blackboard `\operatorname{Prob}`.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 492, 499. *Example:* .set_title.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 203, 425, 549. *Example:* $R$ is the gross return on currency at 120, 128, 131 and 140 - the object the whole functional equation turns on - and then at 425-431 becomes the second-moment matrix of the regressors in the recursive least squares display, with 430 explaining "$R_t$ tracks the second moment of the regressors" three hundred lines after $R_t$ was defined as a return; the code carries the same clash (`R = ridge * np.eye(...)` at 450 in a lecture whose `s_from_psi` implements $f = w_1\psi/(1+\psi)$ derived from returns). $F$ is the transition kernel $F(G', G)$ at 112 and a kernel distribution estimate $\hat F_t(x)$ at 549. And $T$ is "the $T$ map" at 203, cited from another lecture and never defined here, while `T` is the simulation length in every function signature in the file (318, 440, 568, 695).
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 73, 555, 563. *Example:* the epigraph at 73 ("Learning algorithms and equilibrium computation algorithms look like each other") is the opening sentence of the longer Sargent quotation at 520-526, so the same sentence is quoted twice, and the claim is additionally restated in the author's own words at 81-82, 91, 411-417, 528-531 and 650-654 - seven statements of one thesis. 555-558 is a 46-word sentence carrying a definition, a construction and an iteration scheme. And 560-565 states the batch-versus-recursive correspondence a third time in six lines, after 546-553 and 555 have each stated it.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 46, 546. *Example:* "non-parametric" names two different things in the same lecture: at 46 and 92 it is the one-number-per-state rule of the previous lecture, the approach the Overview rejects as hopeless in a continuous state, and at 540-544 it is the kernel smoother offered as the alternative to the parametric route - so the term labels both the method being dismissed and the method being recommended, with no note that the two senses differ. Separately, 546-553 displays a recursion for $\hat F_t(x)$, a kernel estimate of a distribution, in a section whose subject and whose implementation are the conditional expectation $\psi(G)$; 563-565 then claims that display "stands to this smoother exactly as `` {eq}`recursive_pea` `` stands to the batch algorithm", but a Nadaraya-Watson conditional mean is not the batch counterpart of a recursive density estimator, so the correspondence the sentence asserts is not the one the display shows.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 91, 111, 362, 840. *Example:* the lecture uses bold and italic interchangeably for emphasis, sometimes on the same word. Italic is used correctly and often - *separate* (45), *continuous* (53), *computing* (77), *realized* (288), *slow* (509), *happens* (619), *whole* (787) - but bold does the same job at 91 ("**is** a learning economy", a bolded copula), 111 ("a **continuous** Markov process", the same word italicised at 53), 362, 368 and 370 ("the **constant** family", "**linear**", "**quadratic**"), 415 ("**recursively**"), 643 ("**generalize**"), 660 ("**discover**"), and 840, 843, 845, 848 ("**small**", "**variance**", "**large**", "**bias**"). Bold is meanwhile doing genuine definition work elsewhere (**approximate equilibrium** 69, **functional equation** 87, **Nadaraya-Watson** 556), so the marker is carrying two jobs at once.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 700, 822. *Example:* two of the lecture's central claims are about the shape of a curve that is only ever tabulated. 700-712 asks the reader to see that the sup-norm error "falls at first but then rises again" across degrees 0 to 5 while the ergodic RMS "falls monotonically and then flattens" - two error paths, six points each, presented as a rounded DataFrame - and 822-838 does the same across five bandwidths and then asserts "There is an interior optimum". Plotting the two error measures against degree, and against $\log h$, would make both claims visible at a glance and would show the U-shape the bias-variance discussion at 840-852 describes. The lecture is otherwise willing to plot: exercise lae_ex3 even draws the fitted rules at 827-835 without drawing the error curve that is the point of the exercise.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 190. *Example:* spelled-out `mu`.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 598. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 827. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 607. *Example:* plot() without lw=.


## Strengths

- The five-item plan at 84-93 maps one-to-one onto the five H2 sections (105, 198, 273, 409, 533) and every item is actually delivered - including the hardest one, showing that the recursive form of Marcet's algorithm *is* a learning economy, which 415-437 and the code at 439-475 carry out rather than assert.
- The lecture builds ground truth before measuring anything against it (198-262) and then judges every scheme by two numbers, one of which is the theoretically right one: `foc_residual` (234-242) evaluates the first-order condition under the *true* kernel, so it is exactly zero at a rational expectations equilibrium and positive at an approximate one - and 391-393 says precisely that.
- The batch-versus-online comparison is reported honestly: 505-514 states that the online scheme is slower, attributes the residual gap to incomplete convergence rather than to the method, and quantifies the difference (hundreds of thousands of periods against a handful of passes) instead of presenting the two as equivalent.
- Four of the five figures carry `mystnb: figure: caption` and `name` metadata, and every one of them overlays `s_benchmark` as the same black `lw=2.2` line (258, 352, 495, 606, 831), so the four separate comparisons are visually calibrated against each other and against the benchmark figure.
- The `{note}` at 395-407 pre-empts the inference a reader would naturally draw from the degree-0/1/2 figure - that richer is always better - explains the mechanism by which it fails with finite data, ties it back to the rare-state problem of the previous lecture, and points to the exercise that verifies it.
- Exercise lae_ex2 asks a question with a real answer: whether the degree-0 approximate equilibrium coincides with the economy in which the deficit is fixed at its mean. The solution's Jensen argument at 779-788 yields a conceptual result - "an approximate equilibrium is not a naive certainty-equivalent object" - rather than a number, and lae_ex3 then closes the loop by identifying the bandwidth with the polynomial degree (850-852).
- Transposes are written `^\top` wherever the lecture actually transposes something (279, 425, 426); the three qe-math-002 hits reported against this file are derivative primes and next-period primes.

## Recommended actions

1. Rename the second-moment matrix in `` {eq}`recursive_pea` `` (425-431) and in `online_pea` (450, 463, 464) - $R$ is the gross return on currency throughout the first half of the lecture, and the RLS display is the one place where confusing the two would break a reader's understanding of the equation.
2. Plot the error curves the two exercises tabulate: sup and ergodic-RMS error against degree (700-701) and against bandwidth (822-824). The non-monotone sup norm at 708 and the interior optimum at 838 are both claims about a shape, and the tables of five and six rounded numbers make the reader reconstruct it.
3. Fix section 546-565 so the recursive display and the batch implementation are the same object: either show the recursive form of the Nadaraya-Watson conditional mean, or say plainly that the $\hat F_t$ recursion is cited as an example of the shared $1/t$-gain shape and is not the recursive counterpart of the smoother being implemented.
4. Cut the thesis restatements: keep the full Sargent quotation at 520-526 and drop the epigraph at 73 that duplicates its first sentence, then trim one or two of the five paraphrases at 81-82, 91, 411-417, 531 and 650-654.
5. Wrap the eighteen over-long code lines listed above, replace the `foc` lambda at 222 with a `def`, and avoid recomputing `kernel_smoother` inside the plotting loop at 830 - each call simulates 400,000 periods and the same three bandwidths were already computed at 817.
6. Settle the emphasis convention on italic and convert the bold-for-emphasis instances (91, 111, 362, 368, 370, 415, 643, 660, 840, 843, 845, 848), keeping bold for the definitions at 69, 87 and 556.
7. Add `mystnb: figure: caption`/`name` metadata to the figure at 827, move the two `set_title` calls at 492 and 499 into the caption `fig-la-online` already has, add `lw=2` at 607, shorten the caption at 598 (qe-fig-004), and distinguish the two senses of "non-parametric" at 46 and 540.
