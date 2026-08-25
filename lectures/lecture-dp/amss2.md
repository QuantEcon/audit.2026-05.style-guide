# amss2

- **Series:** lecture-dp
- **File:** `lectures/amss2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-005` ×11; `qe-writing-002` ×6; `qe-writing-003` ×2, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×2; `qe-fig-005` ×2; `qe-fig-008` ×2, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 53, 66, 70, 337, 501, 639. *Example:* three bullets trail off into a literal ellipsis rather than finishing - 'bind for many periods, but $\ldots$.' (53), 'eventually, they stop binding evermore, so that $\ldots$' (54), 'is constant across time and states, but $\ldots$.' (64) - which reads as an unfinished draft in published prose. Line 66 is ungrammatical and carries an unparseable compound: 'fluctuations in the interest rate make gross earnings on government debt fully insure the gross-of-gross-interest-payments government budget'. Line 70 ends 'restricted to exchange only risk-free debt debt'. Line 337 says 'Put steps 2 through 6 in a function minimizer' inside Step 6 itself - it means steps 2 through 5. Line 501 says the par value 'converges to about $1.07$' where lines 499-500 have just established $\bar b \approx -1.07$ and $\bar b < 0$, so the sign is dropped at the one place a reader would quote. Line 639 reads 'let $x(s), s = 1,2$ be an arbitrary random variables'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 11. *Lines:* 36, 58, 59, 61, 73, 111, 113, 128, 302, 474, …. *Example:* bold used for stress rather than definition: **measurable** (36), **constant over time** (58), the single word **to** (59), **particular** / **loans** / **never** all in one bullet (61), **assets** (73), **weak** (111), **assets** / **constant** (113), **identical** (128 and again 474), **same** (302 and again 486). Italic is what these want. The file's genuine definitional bolds - **implementability constraints** (41), **measurability constraints** (44), **par value** / **market value** (63, 65), **fiscal risk** (572) - are outnumbered roughly two to one by the emphasis ones.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 79. *Lines:* 26, 27, 30, 32, 33, 38, 41, 42, 45, 49, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 408, 518, 691, 738. *Example:* line 408 writes `(u.Uc(c0, 1)  + u.Un(1, c0 + g0))` with two spaces before the `+` (E221 family); line 518 uses `id` as a loop variable - `for ax, title, id in zip(...)` - shadowing the builtin; line 691 continues an expression with a backslash although it is already inside parentheses (`u.β * (u.Uc(...) * u.π[0, 0] \`), where PEP8 asks for implicit continuation, and 359-360 and 408-410 do the same; line 738 writes `1/den2` unspaced immediately after line 737 writes the same kind of arithmetic spaced.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 462, 516. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 466, 520. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 432, 507. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 465, 519. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 95, 562. *Example:* {cite} in narrative flow: 'in {cite}`'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 123, 539. *Example:* the lecture does not run in the order its own plan sets out, and one section points forward at work already done. The plan at 117-129 lists: describe the economy, run a long simulation from positive debt, observe convergence to $\bar b$, then reverse-engineer the special $b_0$. The file does reverse engineering first (297-423), then the short simulation (425-481), and only then the long simulation (482-526) - so 'Remarks about long simulation' ends at line 539 with 'We now describe how to find such an initial level of government debt', two hundred lines after that description was given. Second, plan item 123-124 promises that the par value converges to the same $\bar b$ 'for alternative realizations of the Markov government expenditure process and for alternative settings of initial government debt $b_0$'. Exactly one long simulation is run, from one realization and $b_0 = 0.5$; line 501 gestures at 'other simulations we have run' without showing any.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 598, 749. *Example:* the lecture's two quantitative claims about the BEGS approximation are both delivered as printed scalars where a figure would settle them. First, ${\mathcal B}^*$ is characterised at 595-602 as the minimiser of a one-dimensional variance criterion, and the code at 726-729 evaluates that criterion at the minimiser and reports 'machine zero' - but $J({\mathcal B})$ as a function of ${\mathcal B}$ is never drawn, so the reader never sees the parabola, its minimum, or where $\bar b$ and $\hat b$ sit on it. Second, line 749-750 asserts that the convergence rate at 736-739 and the implied time-to-convergence at 744-746 'do a good job of approximating our long simulation above' - the long simulation is a figure 250 lines earlier (507-526) and the approximating exponential path is never overlaid on it, so the comparison the sentence claims to make is left entirely to the reader.

### Low severity
_None found._


## Strengths

- The reverse-engineering argument is given as seven numbered steps (313-340), each pinned to a labelled equation - Step 2 to {eq}`amss2_TS_barg10`, Step 3 to {eq}`LSA_xsola`, Step 4 to {eq}`amss2_LSA_bsol`, Step 7 to {eq}`amss2_TS_barg11` and {eq}`eqn_AMSS2_10` - and the code at 346-421 implements them in that order, so a reader can put step and line side by side.
- The BEGS notation is imported with an explicit translation table (552-560) mapping each of their objects to this lecture's, and line 547-548 says why it is being imported: 'so that readers can quickly relate notation that appears in their key formulas to the notation that we have used'. Because $B_t$ and ${\mathcal B}_t$ are two different objects both in play, the calligraphic faces here are carrying information rather than decorating.
- The reverse-engineered $b_0$ is put to a test the reader can see: the short simulation at 432-471 overlays the complete-markets and risk-free-debt economies on the same six panels, and 474-480 states in advance exactly what should be visible - identical allocations, a constant tax rate and par debt for $t \geq 1$, and output and labour supply still varying with the Markov state.
- The BEGS approximation is checked three separate ways rather than once: $\hat b$ printed beside $\bar b$ and then differenced (712-720), the fiscal-risk criterion evaluated at the minimiser and shown to be machine zero (726-731), and the mean-reversion coefficient converted into an interpretable time-to-convergence (736-746).
- The formula ${\mathcal B}^* = -{\rm cov}({\mathcal R}, {\mathcal X})/{\rm var}({\mathcal R})$ is not just quoted: 590-602 reads it as a regression coefficient and then as the solution of an explicit variance-minimisation problem, and identifies the minimand with the fiscal risk defined at 572-576 - so a formula taken from another paper arrives with an economic meaning attached.
- The mechanism the whole lecture is about is stated in one sentence at 73-74 - 'at a particular level of risk-free government assets, fluctuations in the one-period risk-free interest rate provide the government with complete insurance against stochastically varying government expenditures' - and the same idea is picked up again at 66 and formalised at 572-576.

## Recommended actions

1. Fix the ordering problem between the plan and the body. Either move the reverse-engineering sections (297-423) after the long simulation as the plan at 117-129 promises, or rewrite the plan and delete the forward pointer at line 539, which currently tells the reader that a derivation given two hundred lines earlier is still to come.
2. Clear the 79 double spaces (qe-writing-008) - the single largest mechanical item, and in this file they fall inside long sentences that already need careful reading.
3. Fix the numbers and words that a reader will quote: the missing minus sign at 501 ($\bar b \approx -1.07$, per 499-500), 'steps 2 through 6' at 337 (should be 2 through 5), the comment `# Set T to 200 periods` on `T = 2000` at 508, 'risk-free debt debt' at 70, 'an arbitrary random variables' at 639, and the doubled summation `\left(\sum_s \sum_s x(s)^2 \pi(s)\right)` at 646, which sums over the same index twice.
4. Add `import numpy as np` to the import cell at 88-91. The lecture uses `np.` thirteen times (363, 368, 372, 374, 412, 418, 434, 444 and others) and never imports numpy - it works only because one of the `:load:`ed files at 278, 285 or 292 happens to import it into the notebook namespace, which makes the cells non-portable and hides a dependency from the reader.
5. Replace the `global c1` / `global c2` / `global b` channels in `min_Φ` (365-377) with return values. As written, `b_bar = b[0]` at 388 reads whatever the last internal call of `fmin` happened to leave behind, so the printed $\bar b$ depends on the optimiser's final function evaluation rather than on its argmin - a fragile way to get the lecture's headline number.
6. Finish the three trailing bullets at 53, 54 and 64 - each currently ends in a literal '$\ldots$' - and switch the 11 emphasis bolds to italic.
7. Give the BEGS section its figure: plot $J({\mathcal B})$ against ${\mathcal B}$ with ${\mathcal B}^*$ marked (the code at 727 already computes it), and overlay the approximating convergence path from 737-746 on the long-simulation debt panel at 507-526, so the claim at 749-750 is shown rather than asserted. While in those cells, add mystnb `name`/`caption` metadata (432, 507), move the `ax.set(title=title)` calls into captions (466, 520), drop the hand-set `figsize=(14, 10)` (462, 516) and add `lw=2` (465, 519); also switch the in-flow citation at 562 to `{cite:t}`, and replace the deprecated `\rm` in `{\rm cov}`, `{\rm var}`, `{\rm argmin}` (585, 598, 619, 632, 646, 660) with `\operatorname` or `\mathrm`.
