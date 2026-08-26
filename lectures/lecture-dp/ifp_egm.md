# ifp_egm

- **Series:** lecture-dp
- **File:** `lectures/ifp_egm.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×10; `qe-writing-003` ×2; `qe-writing-002` ×4, +2 more. |
| Math         | 9/10  | `qe-math-009` ×7. |
| Code         | 6.5/10 | `qe-code-002` ×2; `qe-code-001` ×3; `qe-code-004` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×1; `qe-fig-008` ×8. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 6. *Lines:* 669, 671, 674, 677, 680, 683. *Example:* time.time(.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 476, 695, 710, 789, 906. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 479, 480, 697, 698, 731, 733, 797, 798. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 7. *Lines:* 120, 145, 167, 211, 222, 322, 387. *Example:* `\mathsf Z` and `\mathsf S` used decoratively for the exogenous state support and the state space: 120, 145 (both symbols), 167, 211, 222, 322 and 387. Plain $Z$ and $S$ would carry the same meaning; neither sans-serif symbol reaches the code, where the same objects are `z_grid` and the `(a, z)` pair, and the lecture already writes $\mathbb{R}_+$, $\Pi$ and $\sigma$ without any face decoration.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 73, 80, 165, 207, 251, 325, 340, 488, 495, 767. *Example:* H2 Title Case: 'The Household Problem' (Household, Problem).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 576, 731, 780. *Example:* line 576 has trailing whitespace after `compute_c(jnp.arange(1, len(s)))` (W291); line 731 writes `+ y_bar(k) , label=label` with a space before the comma (E203); line 780 writes `β ** (1/γ)` with spaces around the exponentiation operator, while line 784 two lines below writes `β**(1 / γ)` - the rule asks for the tight `a**b` form, and the two adjacent lines should at least agree with each other.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 565, 567. *Example:* spelled-out `mu`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 916. *Example:* .set(xlabel='assets', title=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 156, 178, 528, 695. *Example:* line 156 'consumption at time $t$ cannot be a function of outcomes are yet to be observed' is missing a 'that'; line 178 writes 'the maximization is overall feasible consumption paths' where 'over all' is meant. The other two are duplication rather than length: lines 528-529 repeat 376-377 word for word ('Here is the operator $K$ that transforms current guess $\sigma$ into next period guess $K\sigma$'), and the two operator docstrings at 397-404 and 538-544 are byte-identical - so the JAX section opens by telling the reader nothing new. Worse, the figure at 693-702 is an exact copy of the figure at 474-484, down to the labels, and both plot `a_vec`/`c_vec`, the NumPy solution from line 469 - the JAX section's plot never shows the JAX policy.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 180, 637. *Example:* line 180 sends the reader to `` {eq}`eqvfs` ``, but the label defined in this file at 170 is `eqvfs_egm` - `eqvfs` is the label in `` {doc}`ifp_discrete` ``, so the reference resolves to nothing and the definition of an optimal consumption path points at an empty target. The larger break is at 637-649: the text says 'To verify the correctness of our JAX implementation, let's compare it with the NumPy version' and then 'These numbers confirm that we are computing essentially the same policy'. They are not the same model. `create_ifp` is defined twice - at 358 with `β=0.96` and again at 509 with `β=0.94` - so `ifp_numpy` (463) and `ifp` (628) differ in the discount factor, and the printed 'Maximum difference in consumption policy' at 644 is measuring that difference, not floating-point agreement. The timing comparison at 668-688 inherits the same mismatch.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 49, 823. *Example:* 2 spaces.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 279. *Example:* the Solution Method section (251-322) is 70 lines describing a construction that is entirely geometric - an exogenous savings grid $s_0 < \cdots < s_m$, the consumption values $c_{ij}$ read off the Euler equation, the endogenous asset grid $a_{ij} = c_{ij} + s_i$, the anchor at the origin, and a piecewise-linear interpolant through $\{(a_{0j}, c_{0j}), \ldots\}$ - and it carries no figure. The one picture that would make EGM click, the interpolation points sitting on an unevenly spaced asset grid with the policy drawn through them, appears nowhere; every other section of this lecture gets a panel.


## Strengths

- The `{note}` at 122-137 does not just change the budget constraint from the previous two lectures - it says which constraint was used before, why the discretization-friendly timing was chosen then, what it costs (a bigger state space), and where the consequence will show up (`` {doc}`ifp_egm_transient_shocks` ``). A reader arriving from `` {doc}`ifp_discrete` `` is told exactly what moved.
- The boundary case is handled explicitly in both registers and the reason is given: $c_{0j} := 0$ at 300-302 with 'This anchors the interpolation at the correct value at the origin, since, without borrowing, consumption is zero when assets are zero' at 312-313, mirrored in code by the loop starting at `range(1, n_a)` (412) and the zero row concatenated at 578-580.
- The sanity check at 767-806 is a real test, not a plausibility glance: passing `r=0.0, z_grid=(-jnp.inf, -jnp.inf)` to the existing constructor collapses the IFP to CRRA cake eating, whose closed form is coded at 779-784, and the numerical and analytical policies are overlaid on one axis.
- Every labelled equation is cited: `eqst` (91) at 151, `ee00`/`ee01` (185, 193) at 213 and 233, `eqtv` (216) at 233, `eqeul1` (258) at 271 and 273, `cfequ` (287) at 387 - no orphan labels, and the Euler-equation pair is referenced as a pair each time.
- The nested vmap in the JAX operator (553-576) keeps its innermost step as a named function with a docstring that writes the exact quantity computed, `u'(σ(R s_i + y(z_k), z_k))` - so the two stacked `jax.vmap` calls can be read against the math at 289-294 rather than taken on faith.
- `y_bar`'s docstring at 716-722 states the conditional expectation it computes and the display at 748-750 states the same formula in math, so the vertical axis of the 45-degree diagram has a documented definition rather than being an unexplained 'expected next assets'.

## Recommended actions

1. Give the two model constructors distinct names - `create_ifp_numpy` at 358 and `create_ifp` at 509 - and make their defaults agree. As written they are the same name with different `β` (0.96 vs 0.94), so the NumPy/JAX comparison at 641-645 and the timing comparison at 668-688 are run on two different models while the prose at 648-649 claims they agree. This is the highest-value fix in the file: it is the lecture's own correctness check that is broken.
2. Make the JAX section's figure show the JAX result. Lines 695-702 are an exact copy of 476-484 and plot `a_vec`/`c_vec` from the NumPy solve at 469; they should plot `a_vec_jax`/`c_vec_jax` from 634 - or the cell should be deleted, since an identical figure was shown 200 lines earlier.
3. Sentence-case the 9 headings at 73, 165, 207, 251, 325, 340, 488, 495 and 767 ('The household problem', 'Value function and Euler equation', 'Optimality results', 'Solution method', 'NumPy implementation', 'Set up', 'JAX implementation', 'A sanity check') (qe-writing-006 x9).
4. Work through the figure debt: mystnb `name`/`caption` metadata on the 5 figure cells (476, 695, 710, 789, 906), `lw=2` on the 8 default-width line plots (479, 480, 697, 698, 731, 733, 797, 798), and move the embedded title at 916 into a caption (qe-fig-005 x5, qe-fig-008 x8, qe-fig-003 x1).
5. Fix the broken cross-reference at line 180 - `` {eq}`eqvfs` `` should be `` {eq}`eqvfs_egm` ``; as written it targets a label that exists only in ifp_discrete.md - and replace `\mathsf Z` / `\mathsf S` with $Z$ and $S$ at 120, 145, 167, 211, 222, 322 and 387.
6. Replace the 6 `time.time()` readings at 669-683 with the `qe.Timer` context manager and move the `import time` at 656 up to the import cell at 62-70 (qe-code-004 x6).
7. Clean the prose and code slips: 'outcomes are yet to be observed' at 156 needs a 'that'; 'overall feasible' at 178 should be 'over all feasible'; rewrite the verbatim repeat at 528-529 and the duplicated docstring at 538-544 to say what the JAX version does differently; and fix trailing whitespace at 576, the space before the comma at 731, and the `**` spacing at 780. Leave the apostrophes at 260, 261 and 267 alone - they are derivatives of $u$, not transposes.
