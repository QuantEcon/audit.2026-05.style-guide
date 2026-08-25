# mccall_fitted_vfi

- **Series:** lecture-dp
- **File:** `lectures/mccall_fitted_vfi.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-003` ×3; `qe-writing-001` ×1; `qe-writing-005` ×1. |
| Math         | 8/10  | `qe-math-004` ×2. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×4; `qe-fig-001` ×5, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 315, 378, 457, 543, 725, 776. *Example:* `vf = lambda x: jnp.interp(...)` is assigned rather than defined at 315 and 378 (E731), and those two lines head an eleven-line block - `compute_expectation`, `compute_exp_on_grid`, `Pv`, `d`, `v_e` (314-327 and 377-390) - that is duplicated almost verbatim between `T` and `compute_solution_functions`. Line 457 is an f-string whose only braces are escaped (`f'reservation wage $\\bar{{w}}$'`), so the `f` prefix exists only to have to double the braces. Line 543 is `for t in range(T)` with `t` never used in the body. Line 725 is 89 characters (E501). Lines 776-778 pass `density=True` and a `weights` array that already sums to one, so the histogram is normalised twice over while the comment above it (774) claims a single normalisation.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 408, 451, 563, 772, 861. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 210, 407, 448, 557, 812, 852. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 571, 581, 597, 782. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 223, 224, 823. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 2. *Lines:* 187, 188. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 842. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 35, 190, 367. *Example:* line 34-35 names the wrong predecessor. It says 'This lecture follows on from the job search model with separation presented in the {doc}`previous lecture <mccall_model_with_separation>`' and then describes it as the lecture that 'combined exogenous job separation events and a Markov wage offer process' (37-38) - which is `mccall_model_with_sep_markov` (Job Search III), not `mccall_model_with_separation` (Job Search II, IID offers, no Markov chain). Every other cross-reference in the file points to the right place (94, 107, 112, 369), so the very first link is the odd one out. Second, step 4 of the fitted-VFI algorithm says 'take this as the new array and go to step 1' (190), which would re-initialise the guess; the loop has to return to step 2, and the informal version of the same list ten lines earlier gets it right ('go to step 2', 164). Third, $v_e$ and $h$ are used as named objects from 367 onward - in the plot labels (410, 453), in the sentence about the reservation wage (418) and in the code (327-328, 390-391) - but neither is ever defined in this lecture; {eq}`bell2mcmc` (114-126) displays both expressions and names neither.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 203. *Example:* {cite} in narrative flow: '   {cite}`'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 176. *Example:* '**fitted value function iteration**' is bolded twice - at 66-67, where it is genuinely being defined ('The combination of VFI and this interpolation step is called **fitted value function iteration** (fitted VFI)') and again at 176 ('What we will do instead is use **fitted value function iteration**'), where it is the name of the section heading two lines above (174) and the term is 110 lines old. There is no italic anywhere in the file, so the second bolding reads as emphasis rather than definition.


## Strengths

- The interpolation figure at 210-231 is exactly the use of a visual the style guide asks for: an arbitrary oscillating function, six grid points, the piecewise-linear reconstruction on top of it, and dashed verticals marking the grid - so 'the function approximation scheme must not only produce a good approximation' (196) is something the reader sees rather than takes on trust.
- The change from the discrete model is isolated to one line of mathematics and the lecture says so: {eq}`bell2mcmc` is carried over unchanged and only the definition of $P$ is replaced, from a sum (131) to an integral (137) to the explicit change-of-variable form $\int v_u(w^\rho \exp(\nu z))\psi(z)dz$ (147), with the derivation $W_{t+1} = W_t^\rho \exp(\nu Z_{t+1})$ spelled out at 150-152.
- The problem that motivates fitting is stated before the fix: 'the only way to store its update $v'$ is to record its value $v'(w)$ for every $w \in \mathbb R_+$. Clearly, this is impossible' (170-172) - so the interpolation step arrives as a necessity rather than a technique.
- The second figure repeats the first and adds one thing (448-461): the same $h$ and $v_e$ curves with an `axvline` at the computed `w_bar`, so the sentence 'The reservation wage is at the intersection' (418) is verified on the page rather than asserted.
- The time-average and cross-sectional unemployment rates are computed by deliberately different machinery - a Python loop keeping the whole history (522-552) against a `lax.fori_loop` keeping only the final state, vmapped over 20,000 agents (628-700) - the difference is explained in three bullets before either is used (619-623), and the two numbers are then printed side by side with their gap (715-719) and the gap shown to shrink with a longer simulation (724-733).
- Density and CDF conventions are clean: lowercase $p(w, w')$ for the conditional density (137, 140) and lowercase $\psi$ for the standard normal density (144, 251), with no uppercase used for either (qe-math-015 (proposed)).

## Recommended actions

1. Fix the `{doc}` target at line 35: the predecessor described at 37-38 is `mccall_model_with_sep_markov`, not `mccall_model_with_separation`. A reader who follows that link lands on a lecture with IID offers and no Markov structure and cannot make sense of 'we continue with this set' at 40.
2. Change 'go to step 1' to 'go to step 2' in step 4 of the algorithm at 190, and either reference or delete the `(fvi_alg)=` anchor at 186, which is the file's only anchor and is never used.
3. Define $v_e$ and $h$ before using them at 367. They are the two branches of the max in {eq}`bell2mcmc`; naming them there - $v_e$ for the employment value and $h$ for the continuation value, as `mccall_model_with_separation` does - costs two sentences and removes the only genuinely unexplained notation in the lecture.
4. Figures are the weakest category here (5.5/10) and the fix is mechanical: add mystnb caption/name metadata to the 6 code-cell figures (210, 407, 448, 557, 812, 852), drop the 5 hand-set `figsize` (408, 451, 563, 772, 861), move the 4 `set_title` calls into captions (571, 581, 597, 782) and add `lw=2` to the 3 remaining bare plots (223, 224, 823).
5. Replace `\mathbf v` with a plain $v$ or a distinct un-bolded symbol at 187 and 188 (qe-math-004 x2) - the array and the interpolated function need different names, but bold face is not the way to do it - and make `\mathbb{R}_+` (142) and `\mathbb R_+` (170) agree.
6. Factor the eleven-line block duplicated between `T` (314-327) and `compute_solution_functions` (377-390) into one function; while there, drop the dead model unpacking at 400, 429, 487, 533, 679 and 750, where `c, α, β, ρ, ν, γ, w_grid, z_draws = model` binds up to seven names that the function never reads.
7. Small items: line 714 reads `unemployed_indicator`, which is created at 585 inside a plotting cell 130 lines earlier, so the comparison cell breaks if the figure cell is skipped - compute it where it is used; the two-bar histogram at 776-787 conveys only the unemployment rate already printed at 718 and could be dropped; make line 203 `{cite:t}` (qe-ref-001), split the two-sentence paragraph at 842, fix 'this set' to 'this setting' at 40, and clear the trailing whitespace at 162 and 318.
