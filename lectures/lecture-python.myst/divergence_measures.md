# divergence_measures

- **Series:** lecture-python.myst
- **File:** `lectures/divergence_measures.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-003` ×2; `qe-writing-002` ×4; `qe-writing-006` ×1, +4 more. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×1; `qe-math-006` ×1; `qe-math-005` ×1, +1 more. |
| Code         | 7/10  | `qe-code-002` ×4; `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×3; `qe-fig-005` ×3; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 1. *Lines:* 134. *Example:* bare \begin{align} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 219. *Example:* bare expectation `E_{f}\left[`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 148. *Example:* H2 Title Case: 'Two Beta distributions: running example' (Beta).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 26. *Lines:* 32, 34, 36, 38, 40, 42, 68, 70, 71, 77, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 174, 493, 495, 498. *Example:* line 174 spaces the same exponentiation two ways inside one expression - `x** (a-1)` with a space on only one side of `**`, then `(1 - x) ** (b-1)` - and lines 493, 495 and 498 under-indent continuation lines to 24 spaces against a visual-indent target of 28 (E128).
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 56, 173. *Example:* spelled-out `gamma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 185, 274, 438, 473. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 443, 448, 499. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 166, 268, 433. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 217, 250, 290, 319. *Example:* results already established are restated: the KL-cross-entropy identity is displayed as {eq}`eq:KLcross` (127-129) and proved (134-140), then given again as a bullet at 217; $H(f)$ is defined and named the entropy at 81-84 and then defined a third time at 319. Line 250 ends the asymmetry discussion with 'and vice versa', which undoes the point the sentence exists to make - $D_{KL}(f\|g)$ penalises exactly one of the two directions. The bullet at 290 is one 49-word sentence carrying the mutual-information characterisation, the Bernoulli source variable and both of its branches.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 510, 527. *Example:* '## KL divergence and maximum-likelihood estimation' (510) opens after 'Comparing divergence measures' (366-508) has synthesised all three measures and reads as the close of the lecture; it then introduces empirical distributions and the Dirac delta with no transition, and it is the only section with no code. Inside it, the bullet block at 526-528 introduces $\langle X \rangle_{p_e}$ and $\bar{\mu}$, neither of which appears anywhere else in the lecture, and neither is needed for the derivation at 531-554.

### Low severity
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 1. *Lines:* 310. *Example:* parenthesised sequence.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 207. *Example:* one object carries three notations: `\parallel` at 122 and 533, `\|` at 207, 214, 215 and 250, and the alias `KL(f, g)` introduced by the double equality at 207 and then never used in the mathematics again (only in the Python names). Picking one of the three would cost nothing.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 38. *Example:* 'A statistical divergence is a **function** that maps two probability distributions into a nonnegative real number' bolds 'function' - an ordinary word given emphasis - while the term actually being defined, 'statistical divergence', is left unmarked. Elsewhere the file uses bold correctly for the terms it defines (**surprise**, **entropy**, **Cross-Entropy**, **Chernoff coefficient**).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 343. *Example:* the Chernoff entropy section defines $C(f,g)$ as a minimisation of $\int f^\phi g^{1-\phi}$ over $\phi \in (0,1)$ and then reports only two printed numbers (362-363). The Chernoff coefficient plotted against $\phi$ with the minimiser marked is the picture that makes the definition legible, and the lecture draws a figure for every other concept it introduces (185, 274, 438, 473).
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 336. *Example:* iid.


## Strengths

- Density case discipline is exact: lowercase $f$, $g$, $m$, $p_e$, $p_\theta$ for every density and mass function (67, 204, 261, 515, 531), with uppercase reserved for the functionals $H$, $D_{KL}$ and $C$ - the proposed qe-math-015 (proposed) convention holds without exception.
- The primer at 63-145 builds surprisal, entropy, cross-entropy and KL divergence in dependency order and then proves the identity {eq}`eq:KLcross` that the rest of the lecture reuses, citing Shannon and Kullback-Leibler at the point each concept is introduced.
- One pair of Beta densities is fixed at 166-197 and reused for all three measures (228, 298, 343), so KL, JS and Chernoff entropy are compared on the same picture rather than on three separate examples.
- The comparison table at 370-427 is computed by the same functions the text defines, sorted by JS divergence, so the co-movement claim at 429 can be read straight off it instead of being asserted.
- Every forward reference is a {doc} link to the lecture that actually uses the tool - likelihood_ratio_process and wald_friedman at 223-224, likelihood_ratio_process at 338, and the three at 560-562.

## Recommended actions

1. Fix the entropy claim in the note at 88-93: the maximum-entropy uniform distribution has $H(f) = \log n$, not $-\log(n)$ - the minus sign contradicts the definition two lines above at 81.
2. Convert the raw LaTeX environments to MyST display math: `\begin{equation}` at 114 and 121 to `$$ ... $$`, and the bare `\begin{align}` at 134 to `$$ ... \begin{aligned} ... $$` - the align block is the one build-risk item in the file (qe-math-006).
3. Rename the parameter of `plot_dist_diff` at 470: it declares `para_grid` but the loop at 475 iterates the module-level `param_grid`, so the function silently ignores its argument and the call at 507 only works by coincidence.
4. Figure hygiene, the largest mechanical block here: add mystnb name/caption metadata to the three figure cells at 166, 268 and 433 (qe-fig-005), move the embedded `set_title` calls at 443, 448 and 499 into captions (qe-fig-003), and drop the four `figsize=` overrides at 185, 274, 438 and 473 (qe-fig-001).
5. Add the Chernoff-coefficient-versus-$\phi$ figure described above, and cut the restatements at 217 and 319 so each result is established once.
6. Write `\mathbb{E}_f` for the conditional expectation in the chain-rule bullet at 219 (qe-math-010 (proposed), proposed), brace the weight sequence at 310 as $\{\alpha_i\}_{i=1}^n$ (qe-math-005), and write 'IID' at 336 (qe-writing-009 (proposed), proposed).
7. Sweep the 26 double-space runs in the prose (32, 34, 36, 38, 40, 42, 68, 70, 71, 77, ...) and the trailing whitespace inside the code cells at 415, 458, 460, 461, 492, 494, 497 and 500.
