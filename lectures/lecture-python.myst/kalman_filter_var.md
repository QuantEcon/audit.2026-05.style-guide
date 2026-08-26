# kalman_filter_var

- **Series:** lecture-python.myst
- **File:** `lectures/kalman_filter_var.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×3; `qe-writing-003` ×2; `qe-writing-002` ×4, +1 more. |
| Math         | 7.5/10 | `qe-math-003` ×3; `qe-math-009` ×3. |
| Code         | 5.5/10 | `qe-code-002` ×11; `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×3; `qe-fig-005` ×2; `qe-fig-001` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 656, 709, 828, 996, 1104. *Example:* continuation-line indentation is inconsistent from cell to cell: 656 indents two spaces under the opening bracket, 709-713 indent eight where visual alignment would be thirteen (PEP8 E128), while 717-718 and 724-725 in the same cell do align, and 996-998 and 1084-1085 over-indent past the opening paren (E127); 828 binds `sign, logdet = np.linalg.slogdet(Omega)` and never uses `sign` (F841); 1104 has three spaces after a comma inside `ax.axvline(ρ_true, color='k',   ls='--', ...)` (E241). Separately, the same four matrices are disambiguated three different ways across cells - `H_`, `lss_`, `kf_`, `T_`, `m_` at 812-819, `A_`, `C_`, `G_`, `R_` at 938-941, `A_t`, `C_t`, `G_t`, `R_t` at 1078-1082 - and 1105 and 1108 escape LaTeX inside plain f-strings where the rest of the file uses `r''` and `rf''`.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 11. *Lines:* 682, 687, 717, 761, 812, 815, 817, 825, 828, 830, …. *Example:* spelled-out `Sigma`.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 705, 1010. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 714, 721, 726. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 987, 1074. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 3. *Lines:* 961, 962, 963. *Example:* pmatrix environment.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 463, 638, 853. *Example:* three letters carry two or three meanings each. $L$ is introduced at 173-200 as the population regression coefficient and filtering gain ($L_0 = \Sigma_0 G^\top(G\Sigma_0 G^\top + R)^{-1}$, and $K_0 = AL_0$) and then re-introduced at 463 as the lag operator ("Letting $L$ denote the lag operator, so that $L x_t = x_{t-1}$"), used that way through 572-595. $H$ is the closed linear span $H(y^t)$, $H(a^t)$ at 305-317 and the measurement-noise factor with $R = HH^\top$ at 638-639, 654 and in every code cell after it. And $S_y$ is the spectral density of $\{y_t\}$ at 529-556 and the selector matrix in "$y_t = S_y Y_t$" at 853. Renaming the lag operator, the linear span and the selector costs three characters and removes all three collisions.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 54, 492, 564, 843. *Example:* "### Wold and autoregressive representations" (564-607) re-derives what section 423-469 already derived: the display at 575 is character-for-character the display at 467, the VAR at 594-596 is the VAR at 451, and 598 concedes it ("which is the vector autoregression already stated in `` {eq}`eq:var1` ``"). The lecture also ends twice - "## Where this leads" (843-858) and "## Summary" (861-880) both close the lecture and both hand off to `` {doc}`var_subsets` ``, which the Overview at 70-72 has already announced, so the sequel is introduced three times. On top of that, 54-56 is a 37-word sentence with an appositive definition inside it and 492-494 is 34 words.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 463, 609. *Example:* 463 and 519 use two different operator conventions for the same operation 56 lines apart - the lag operator $L$ with $Lx_t = x_{t-1}$ at 463, then the $z$-transform with $z^{-1}x_t = x_{t-1}$ at 519-523 - and 572 switches back to $L$, so the reader has to translate between them mid-derivation with no note that they are the same thing; and the lecture's first code cell is at 616, after 535 lines of algebra, so the Riccati equation (269-285), the whitening property (287-326) and the spectral factorization (503-556) are each stated, and then illustrated only in a block of numerical work 100 to 350 lines later, if at all.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 58, 411, 512. *Example:* the Overview bullet list at 58-68 bolds a term in six of its seven bullets, two of them in the same bullet ("the **innovations representation** and the **Gram-Schmidt** whitening property"), and every one of those terms is bolded again where it is actually defined (279, 323, 330, 346, 387) - so the bold on first mention is emphasis, not definition, and the density of it dulls the marker for the whole lecture; 411 bolds the adjective in "a **time-invariant** matrix $\Sigma$", which is emphasis; and 512 italicises the term as it is coined ("yields the *spectral factorization identity*") before bolding the same phrase at 549.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 287, 503. *Example:* the theory runs from 74 to 607 with no figure at all, and two sections in it are asking for one. "## The Gram-Schmidt process" (287-326) establishes that $[a_t, \ldots, a_0]$ is an orthogonal basis for the same space as $[y_t, \ldots, y_0]$ - the canonical orthogonalization picture, and the lecture even sets up the geometry with $H(y^t)$, $H(a^t)$ and $a_{t+1} \perp H(y^t)$ at 304-318 without drawing it; the code later computes the whitening numerically (748-753) but plots nothing. "## Spectral factorization identity" (503-607) derives two different formulas for $S_y(z)$ and equates them, which is a numerical check the lecture is fully equipped to run: evaluate `` {eq}`eq:sf_original` `` and `` {eq}`eq:sf_innov` `` on the unit circle from the same $(A, C, G, R)$ and $K = $ `kf.stationary_values()`, and plot them on one axis.

### Low severity
_None found._


## Strengths

- Every display equation in the file is labelled with the `$$ ... $$ (eq:name)` form and the labels are used: `eq:statespace` is cited at 106, 113, 330, 477, 486, 496 and 508, `eq:riccati` at 279, 410, 414, 892 and 908, `eq:kalf10` at 256, 299, 314, 382 and 677, `eq:innovti` at 426, 438, 447, 492, 509, 534 and 566 - 25 labelled displays and no orphans, which is what lets the second half refer back precisely instead of restating.
- The filter's timing convention is stated in the prose (674-678) and then defended: 692-696 explains what would go wrong if `kf.x_hat` were recorded after `update` rather than before - the series would not be the innovation and would not have variance $G\Sigma G^\top + R$ - and 745-749 then checks exactly that, printing the sample sd against $\sqrt{G\Sigma_\infty G^\top + R}$ and the first-order autocorrelation.
- The derivation is genuinely from first principles and says so at each step: 150 states the method ("regress what we do not know on what we know"), 186-192 writes down the normal equations rather than quoting the answer, and 200 draws the distinction that most treatments skip - $L_0$ updates the estimate of $x_0$ while $K_0 = AL_0$ updates the forecast of $x_1$.
- The `{note}` at 152-162 states precisely what the joint-normality assumption buys and what survives without it ("wide-sense conditional expectations that coincide with true conditional expectations only when those conditional expectations are linear") - a caveat most expositions leave implicit.
- Transposes are `^\top` throughout - 117, 145, 190, 191, 197, 219, 232, 242, 244, 261, 263, 275, 276, 298, 302, 356, 379, 435, 436, 457, 523, 529, 541 and more - with not one apostrophe in a lecture that is almost entirely matrix algebra.
- Exercise `kf_ex1` asks for the closed-form $\Sigma_\infty$ and then has the reader check it against `kf.Sigma_infinity` to eight decimals (946-947), so the algebra and the solver corroborate each other rather than either being taken on trust.

## Recommended actions

1. Collapse "### Wold and autoregressive representations" (564-607) into a cross-reference to 423-469, keeping only what is new there - the invertibility identity at 586-589 and the zeros-inside-the-unit-circle argument at 600-607; and merge "## Where this leads" (843-858) with "## Summary" (861-880) into one closing section.
2. Rename the three overloaded symbols: the lag operator at 463 and 572-595 (it collides with the filtering gain $L_t$ at 173-200), the linear span $H(\cdot)$ at 305-317 (it collides with the noise factor $H$ at 638 onward), and the selector matrix $S_y$ at 853 (it collides with the spectral density $S_y(z)$ at 529).
3. Add the two missing figures: an orthogonalization diagram for section 287-326, and a numerical check of the spectral factorization identity - evaluate `` {eq}`eq:sf_original` `` and `` {eq}`eq:sf_innov` `` around the unit circle and overlay them, which turns 548-556 from an assertion into a verified identity.
4. Convert the three `pmatrix` environments to `bmatrix` (961, 962, 963) and rename the `Omega` variable in `log_likelihood` to `Ω` (825, 828, 830), matching the unicode `ρ`, `σ_w`, `σ_v` already used at 643-645.
5. Move the three `set_title` calls (714, 721, 726) into the caption of `fig-kfvar-scalar`, which the cell already has, and add `mystnb: figure: caption`/`name` metadata to the two exercise-solution figures (987, 1074); the `fig.suptitle` at 1018 belongs in the same caption.
6. Bring one convention for the lag/z-transform operator into the whole of 405-607, and either move some numerical illustration forward into the theory sections or say at 74 that the code all lives in section 609 onward.
7. Trim the bold in the Overview bullets (58-68) to the two or three terms not defined later, switch 411 to plain text and 512 to bold, drop the unused `sign` at 828, and standardise the continuation indentation and the `H_`/`A_`/`A_t` suffix conventions across the four code cells.
