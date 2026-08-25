# ifp_advanced

- **Series:** lecture-dp
- **File:** `lectures/ifp_advanced.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×9; `qe-writing-001` ×2; `qe-writing-003` ×2, +3 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×10; `qe-math-002` ×6; `qe-math-004` ×3, +2 more. |
| Code         | 6.5/10 | `qe-code-002` ×2; `qe-code-001` ×3; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×3; `qe-fig-003` ×1; `qe-fig-001` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 179, 182, 213, 234, 235, 294. *Example:* apostrophe transpose `u'`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 14. *Lines:* 117, 166, 170, 172, 200, 219, 223, 228, 241, 243, …. *Example:* `\mathscr C` for the class of candidate consumption policies runs through the whole theory section - 166, 170, 172, 200, 219, 223, 228, 241, 243, 244, 245, 248 - and `\mathsf Z` for the Markov state support appears at 117 and 305. Neither face carries information: plain $C$ and $Z$ would read the same, and neither symbol survives into the code, where the policy class is just a pair of arrays. The lecture writes $\rho$, $\sigma$, $P$ and $K$ undecorated in the same displays, so the script and sans-serif letters are the odd ones out. The 3 `\mathbf S` hits already counted under qe-math-004 (203, 221, 232) are the same object that {doc}`ifp_egm` writes as `\mathsf S` - a third face for the state space across two consecutive lectures.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 10. *Lines:* 85, 121, 141, 150, 152, 157, 181, 212, 292. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 73, 77, 193, 198, 226, 251, 265, 668, 675. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 429, 613, 619. *Example:* line 429 leaves trailing whitespace after the comment `# Fix consumption-asset pair at (0, 0)` (W291); line 613 writes `jnp.arange(1, n+1)` with no spaces around `+` while line 614 immediately below writes `(n + 1) / n` spaced, inside the same four-line function; line 619 writes `p: float=0.01`, which needs spaces around the `=` because the parameter is annotated (E252) - the same file gets this right at 445-446 (`tol: float = 1e-5`).
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 413, 414. *Example:* spelled-out `mu`.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 31. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 652, 752, 829. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 654. *Example:* .set(xlabel='log assets', ylabel='density', title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 638, 719, 796. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 203, 220, 232. *Example:* \mathbf.
- **[qe-math-007]** — Use automatic equation numbering, not manual tags. *Count:* 1. *Lines:* 158. *Example:* \label{ — use $$ … $$ (label) numbering.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 50, 168, 224. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 781, 784. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 508, 513, 670. *Example:* line 508 instructs 'Set `num_households=50_000, T=500`', but every call in the lecture passes `num_households=200_000` (646, 743, 820) - the sentence and the four paragraphs around it (501-514) are copied verbatim from {doc}`ifp_egm` lines 811-824 and were not updated, so the reader is told a number the code contradicts. Line 513-514 is part of that copy and still ends without a full stop, with a double space in 'pair `c_vec`  and `a_vec`'. Line 670 reads 'Lets' look at wealth inequality by computing some standard measures of this phenomenon' - misplaced apostrophe, and the trailing six words say nothing the first six did not.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 253, 490. *Example:* line 253 opens 'In the study of that model we found that it was possible to further accelerate time iteration' - there is no 'that model'. The preceding section (226-249) is about the convergence properties of $K$ in this lecture's own model; the optimal growth model the sentence means is not named until line 258, five lines later. Second, the Implementation section builds up to `a_star, σ_star = solve_model(ifp, a_init, σ_init)` at 490 and the timed re-solve at 496-498, and then simply stops - neither result is printed, plotted or referred to again. The Simulation section at 639-645 re-creates the model and re-solves it from scratch under new names, so the reader who has just followed 190 lines of algorithm never sees what it produced.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 490. *Example:* this is the only lecture in the IFP sequence with no picture of the consumption policy. {doc}`ifp_discrete`, {doc}`ifp_opi` and {doc}`ifp_egm` all plot $\sigma$ against assets by income state, and the whole point of this lecture is what stochastic returns do to that policy - yet `σ_star`, computed at 490, is never drawn. The three figures present are a log-wealth histogram (652) and two Gini-versus-volatility plots inside the exercises (752, 829). The claim at 262-263 that 'optimal consumption can be equal to assets when the level of assets is low', and the $a_0 = c_0 = 0$ anchoring at 278-279, are exactly the features one figure would settle.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 513. *Example:* 2 spaces.


## Strengths

- The stability condition is enforced, not just stated: the requirement $\beta G_R < 1$ at 138-141 is simplified to $\beta \mathbb{E} R_t < 1$ under the IID assumption at 147-152, and `create_ifp` then computes exactly that from the lognormal parameters and asserts it at 355-356 - so a reader who supplies bad parameters is stopped rather than shown a divergent solve.
- The three shocks in the household simulation get independent randomness from a single key by folding in `3*t`, `3*t + 1` and `3*t + 2` (540-547), which keeps the Markov transition, the income innovation and the return innovation independent across periods without threading a key through `fori_loop` state.
- The two exercises are a deliberately matched pair - the same loop, the same 5-point grid, the same simulation size and the same empirical-Gini reference line at 757 and 834 - so the comparison drawn at 843-848 is a like-for-like read of two figures rather than an assertion.
- The model is checked against data on both counts at 687-698, including the one it fails: 'Our model with stochastic returns generates a Gini coefficient close to the empirical value' is immediately followed by 'The top 1% wealth share is, however, too large'.
- The nested expectation in the Coleman--Reffett operator (405-426) names each layer for the quantity it produces (`compute_term`, `inner_expectation`, `compute_expectation`), and the `meshgrid` at 416 with `vmap(vmap(...))` at 417 makes the double Monte Carlo over the two innovation processes explicit rather than hiding it in a reshape.
- Italic is used for emphasis and only for emphasis - '*assume that the interest rate process is IID*' at 147-148 and '*savings*' at 267 - with no bold-for-emphasis anywhere in the file (qe-writing-005 clean).

## Recommended actions

1. Straighten out the argument and return order of `K` and `solve_model`, which is currently inconsistent at four points and only works by accident. `K` is declared `(a_in, c_in, ifp)` at 390-393 and returns `a_out, c_out` (433), but `solve_model`'s body calls `K(c_in, a_in, ifp)` and unpacks `c_out, a_out = ...` (456); `solve_model` is declared `(ifp, c_init, a_init)` at 441-444 yet called as `solve_model(ifp, a_init, σ_init)` at 490 and `solve_model(ifp, a_init, c_init)` at 645, whose result is unpacked as `a_vec, c_vec` even though the function returns `c_out, a_out` (466). Every call happens to be harmless only because `a_init` and `c_init` are set to the same array (484, 644, 735-736, 812-813) - change either initialisation and the lecture breaks silently.
2. Add `jax` to the install cell at line 35. The lecture imports `jax`, `jax.numpy` and `jax.vmap` at 64-66, and the sibling lectures install `quantecon jax`; as written, a fresh environment fails at the import cell (qe-code-003 x1).
3. Sentence-case the 9 headings at 73, 77, 193, 198, 226, 251, 265, 668 and 675 ('The model', 'Set up', 'Solution algorithm', 'A time iteration operator', 'Convergence properties', 'Using an endogenous grid', 'Finding optimal consumption', 'Wealth inequality', 'Measuring inequality') (qe-writing-006 x9).
4. Replace the decorative letters with plain ones: `\mathscr C` -> $C$ at the 12 sites listed above, `\mathsf Z` -> $Z$ at 117 and 305, and `\mathbf S` -> $S$ at 203, 221 and 232 (which also clears qe-math-004 x3). While settling this, pick one face for the state space across {doc}`ifp_egm` and this lecture - they currently disagree.
5. Fix the math markup: brace the 6 bare `\mathbb E` at 85, 141, 150, 152 and 157 (qe-math-010 (proposed), proposed), and delete the raw `\label{a:y0}` at 158, which is LaTeX that MathJax does not honour and which the corpus convention replaces with `$$ ... $$ (label)` numbering (qe-math-007 x1).
6. Plot the consumption policy the lecture spends 190 lines deriving - $\sigma^*(a, z)$ against assets for the two $z$ states, ideally beside the fixed-$R$ policy from {doc}`ifp_egm` - and add mystnb `name`/`caption` metadata to the 3 figure cells at 638, 719 and 796, drop the hand-set `figsize=(10, 6)` at 652, 752 and 829, and move the 3 embedded titles at 654, 756 and 833 into captions (qe-fig-005 x3, qe-fig-001 x3, qe-fig-003 x1).
7. Update the paragraphs copied from {doc}`ifp_egm` at 501-514: the household count at 508 should say 200,000 to match 646, the sentence at 513-514 needs a full stop and loses its double space, and 'Lets'' at 670 should be 'Let's'. Leave the apostrophes at 179, 182, 213, 234, 235 and 294 alone - they are derivatives of $u$, not transposes.
