# ifp_advanced

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_advanced.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×9; `qe-writing-001` ×2; `qe-writing-003` ×2, +3 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×10; `qe-math-004` ×3; `qe-math-007` ×1, +1 more. |
| Code         | 7/10  | `qe-code-002` ×2; `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×3; `qe-fig-003` ×1; `qe-fig-001` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 10. *Lines:* 85, 121, 141, 150, 152, 157, 181, 212, 292. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 73, 77, 193, 198, 226, 251, 265, 668, 675. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 349, 425, 534, 619. *Example:* line 349 closes a hanging-indent signature with `    ):` at 4 spaces, leaving the arguments at the same indent as the body (E121/E125); the pattern recurs at 394, 447, 519, 569 and 620. Line 425 pads after a comma to align `in_axes` with the line above (E241). Line 534 binds a lambda to a name where PEP8 asks for `def` (E731). Line 619 writes an annotated default without spaces, `p: float=0.01`, where PEP8 requires `p: float = 0.01` (E252).
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 413, 414. *Example:* spelled-out `mu`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 652, 752, 829. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 654. *Example:* .set(xlabel='log assets', ylabel='density', title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 638, 719, 796. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 203, 220, 232. *Example:* \mathbf.
- **[qe-math-007]** — Use automatic equation numbering, not manual tags. *Count:* 1. *Lines:* 158. *Example:* \label{ — use $$ … $$ (label) numbering.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 117, 166, 203. *Example:* three sets get three different exotic fonts in one lecture: $\mathsf Z$ for the Markov chain's state space (117, 305), $\mathscr C$ for the class of candidate policies (166, 170, 172, 200, 219, 223, 228, 241-245) and $\mathbf S$ for the state space (203, 220, 232). Plain $Z$, $C$ and $S$ would carry the same meaning; as it stands the reader has to keep three typefaces apart, and the bold one additionally violates qe-math-004.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 50, 168. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 781, 784. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 305, 670, 672. *Example:* line 305 says 'we held $z \in \mathsf Z$ in the discussion above' with the word 'fixed' missing, so the sentence does not state the assumption it is making. Line 670 opens the inequality section with 'Lets' look at wealth inequality by computing some standard measures of this phenomenon' - misplaced apostrophe, and 'of this phenomenon' adds nothing. Line 672 promises to 'examine how inequality varies with the interest rate', but both exercises vary the *volatility* of returns and of labour income (`a_r`, `a_y`), never the level of the return.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 100, 253. *Example:* the lecture names two different predecessors: line 40 says it continues 'the income fluctuation problem described in `` {doc}`ifp_egm` ``', while line 100 says 'the only difference from `` {doc}`ifp_egm_transient_shocks` `` is that $\{R_t\}$ ... is allowed to be stochastic'. Line 253 then opens '### Using an Endogenous Grid' with 'In the study of that model we found that it was possible to further accelerate time iteration' - 'that model' has no antecedent in this lecture, and the model meant (the optimal growth model of `` {doc}`os_egm` ``) is not named until 258.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 490, 661. *Example:* the optimal consumption policy is the object the entire first half of the lecture constructs - the Coleman-Reffett operator, the endogenous grid, the interpolation scheme - and it is solved at 490 and never plotted. The three figures in the lecture are the wealth histogram (652) and the two Gini sweeps (752, 829); $\sigma^*(a, z)$ for the two values of $z$ never appears, although every companion lecture in the series shows it. Second, the claim at 661-662 that the log histogram 'suggests a long right tail' is exactly what a rank-size or log-log tail plot would settle, and the lecture then builds a whole section on tail inequality without one.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 513. *Example:* 2 spaces.


## Strengths

- The theory's stability requirement is enforced in code rather than left as prose: `assert β * ER < 1, "Stability condition failed."` at 356 implements $\beta G_R < 1$ from `` {eq}`fpbc2` `` under the IID simplification stated at 147-152.
- The endogenous-grid derivation explains the one thing that makes this problem different from the optimal growth version - that the max in `` {eq}`ifpa_euler` `` drops out only for $s > 0$, and that the origin has to be pinned at $a_0 = c_0 = 0$ (271-284) - and the code does exactly that at 428-431.
- The JAX implementation is genuinely vectorised at three levels: `vmap` over the two shock grids (416-417), then over the savings grid and the exogenous state (424-426), with the fixed point run inside `jax.lax.while_loop` (463) so the whole solve stays under one `jit`.
- Both exercises are quantitative comparisons against an empirical target, with the US Gini drawn as a reference line (757, 834) and the two volatility experiments contrasted in numbers at 845-846 rather than described qualitatively.
- Every assumption is attributed where it is used - `` {cite}`ma2020income` `` at 133 for the stability condition, at 168 for the Euler-equation characterisation and at 224 for the fixed-point result - and the model primitives are a `NamedTuple` whose fields are documented one per line (319-333).

## Recommended actions

1. Plot the optimal consumption policy $\sigma^*(a, z)$ after the solve at 490 - it is the lecture's central object and currently never appears.
2. Sentence-case the nine Title Case headings at 73, 77, 193, 198, 226, 251, 265, 668 and 675 (qe-writing-006).
3. Fix the math markup: brace the six blackboard operators (85, 141, 150, 152, 157) (qe-math-010 (proposed), proposed), replace the raw `\label{a:y0}` at 158 with MyST's `$$ ... $$ (a:y0)` numbering (qe-math-007), drop the bold $\mathbf S$ (203, 220, 232) (qe-math-004), and make the three narrative citations at 50, 168 and 224 `{cite:t}` (qe-ref-001).
4. Replace $\mathscr C$, $\mathbf S$ and $\mathsf Z$ with plain letters, so the lecture uses one typeface for its three sets.
5. Figure hygiene: add mystnb name/caption metadata to the three figure cells at 638, 719 and 796 (qe-fig-005), move the embedded titles at 654, 756 and 833 into captions (qe-fig-003), and drop `figsize=` at 652, 752 and 829 (qe-fig-001).
6. Code tidy: fix the closing-paren indent at 349, 394, 447, 519, 569 and 620; `p: float = 0.01` at 619; `def` instead of the lambda at 534; `μ` instead of `mu` at 413-414 (qe-code-002); either use or drop the unused `z` argument of `R` at 378, which the model at 107 says returns depend on; change the `python3` kernel name at 495 to `ipython3` like every other cell; and delete `gini_plot` at 649, which is computed and never used.
7. Prose repairs: 'held $z$ fixed' at 305, 'Let's' at 670, the interest-rate-versus-volatility claim at 672, one named predecessor lecture at 40 and 100, an antecedent for 'that model' at 253, the two-sentence paragraphs at 781 and 784, and a shared helper for the two 40-line exercise solutions at 719-762 and 796-839, which differ only in the parameter being swept.
