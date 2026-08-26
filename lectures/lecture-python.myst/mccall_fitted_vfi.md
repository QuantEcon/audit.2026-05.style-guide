# mccall_fitted_vfi

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_fitted_vfi.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-003` ×3; `qe-writing-002` ×3; `qe-writing-001` ×1, +1 more. |
| Math         | 8/10  | `qe-math-004` ×2. |
| Code         | 7/10  | `qe-code-001` ×13. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×4; `qe-fig-001` ×5, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 13. *Lines:* 271, 282, 315, 318, 340, 378, 438, 457, 527, 578, …. *Example:* `vf = lambda x: jnp.interp(...)` assigns a lambda to a name at 315 and 378, which PEP8 asks to be written as a `def` (and ruff reports as E731 under its default rule set); the label at 457 is an f-string with no placeholders, `f'reservation wage $\bar{{w}}$'`, so the doubled braces are only there to survive a format step that never happens - `r'reservation wage $\bar{w}$'` is what is meant; line 271 leaves one blank line between the `Model` class and `create_mccall_model` where PEP8 asks for two; five closing brackets sit at column 4 under an 8-space hanging indent (282, 340, 527, 668, 745); the continuation at 578 is indented 11 spaces against a visual indent of 12; line 725 runs to 89 characters; line 318 carries trailing whitespace; and the inline comment at 438 sits one space from the code rather than two.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 408, 451, 563, 772, 861. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 210, 407, 448, 557, 812, 852. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 571, 581, 597, 782. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 223, 224, 823. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 2. *Lines:* 187, 188. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 842. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 196, 198, 40. *Example:* three sentences in the methodological core do not parse cleanly: 196 is a 33-word not-only/but-also whose halves do not match ('must not only produce a good approximation to each $v$, but also that it combines well'); 198 reads 'One good choice from both respects' where 'in both respects' is meant; and 40 says 'we continue with this set and, in addition, allow the wage offer process to be continuous', where 'this set' appears to be 'this setup'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 35, 190, 714. *Example:* line 34-38 sends the reader to the wrong prerequisite: the `` {doc} `` target is `mccall_model_with_separation`, the IID lecture, but the next sentence describes what that lecture did as combining 'exogenous job separation events and a Markov wage offer process' - which is `mccall_model_with_sep_markov`, the lecture correctly cited at 94, 107, 112 and 369. Step 4 of the fitted-VFI algorithm (190) says 'take this as the new array and go to step 1', but step 1 (187) is 'Begin with an array representing the values of an initial guess' - the loop should return to step 2. And line 714 computes the time-average unemployment rate from `unemployed_indicator`, a variable created at 585 inside the three-panel plotting cell of the previous subsection, with nothing in the prose saying the comparison depends on that cell.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 203. *Example:* `` {cite} `` in narrative flow: '   `` {cite} ``'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 776. *Example:* the 'Visualization' section's only figure is a two-bar histogram of a binary variable (776-784) whose entire content - the cross-sectional unemployment rate - is already printed in its own title at 782 and in the comparison at 717. Meanwhile `sim_agents_vmap` returns `final_wages` at 695 and the plotting routine throws it away at 765, so the cross-sectional wage distribution, the one genuinely new object the vectorized simulation produces, is computed and discarded. Passing both `density=True` and `weights` at 776-778 also normalises twice.


## Strengths

- The interpolation step is demonstrated on a function whose exact form is known (210-231) before it is put inside a fixed-point iteration, so the reader can see how piecewise-linear approximation behaves between grid points at the moment the method is introduced rather than after it is buried in a solver.
- Lines 52-64 explain why the continuous case is not a repeat of the continuous wage distribution already met in mccall_model: there the problem collapsed to one scalar, here it does not, and that difference is exactly what forces the interpolation step - the motivation for the whole lecture is stated, not assumed.
- The Monte Carlo draws are generated once and stored in the `Model` tuple (270, 286) with the reason given at 259, so every Bellman evaluation integrates against the same draws and the fixed point computed at 360 is a genuine fixed point rather than a noisy one.
- The two definitions of the $P$ operator are set one after the other (131 for the sum, 137 for the integral) so the only substantive change from the discrete lecture is visible at a glance, and 144-155 then derives the change-of-variables form $\int v_u(w^\rho \exp(\nu z))\psi(z)dz$ that the code actually implements.
- The value-function figure is drawn twice on purpose and says so ('Let's repeat our plot, but now inserting the reservation wage', 446), and the ergodicity comparison is not left approximate - after the T = 2,000 comparison the lecture reruns the single agent at T = 10,000 to show the gap closing (722-733).

## Recommended actions

1. Repoint the `` {doc} `` link at 35 to `mccall_model_with_sep_markov` (or rewrite 37-38), and change 'go to step 1' at 190 to 'go to step 2' - both are signposts that currently send the reader somewhere the text does not mean.
2. Add `mystnb: figure: caption/name` metadata to the six un-named figure cells (210, 407, 448, 557, 812, 852) and to the figure drawn inside `plot_cross_sectional_unemployment` (called at 793), and drop the five `figsize` overrides (408, 451, 563, 772, 861) unless the aspect ratios are deliberate (qe-fig-005 x6, qe-fig-001 x5).
3. Move the four `set_title` strings into captions (571, 581, 597, 782) and set `lw=2` on the three thin `plot` calls (223, 224, 823) (qe-fig-003 x4, qe-fig-008 x3).
4. Replace the binary histogram at 772-787 with the cross-sectional wage distribution - `final_wages` is already returned at 695 and discarded at 765 - or drop the figure and keep the printed rate.
5. Remove the bold from the vector at 187-188, `\mathbf v` -> $v$ (qe-math-004, 2 occurrences), and move the mid-narrative citation at 203 into the sentence structure qe-ref-001 asks for (1 occurrence).
6. Make the ergodicity comparison self-contained: compute `unemployed_indicator` in the cell at 708 rather than relying on the plotting cell at 585 having been run.
7. Clear the code items: turn the two lambdas at 315 and 378 into `def`s, make the label at 457 a raw string, split the two-sentence paragraph at 842 (qe-writing-001), and fix the spacing at 271, 318, 438, 578 and the 89-character line at 725.
