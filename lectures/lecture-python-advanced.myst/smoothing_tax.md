# smoothing_tax

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/smoothing_tax.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-002` ×9; `qe-writing-005` ×4; `qe-writing-003` ×4, +4 more. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×5; `qe-math-002` ×1; `qe-math-009` ×6. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×7; `qe-fig-006` ×9; `qe-fig-005` ×2, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 115, 213, 392, 556, 572, 641, 780. *Example:* 213 reshapes the caller's array in place, `y.shape = (n, 1)`, so calling `consumption_incomplete` permanently changes `cp.y` from a length-$n$ vector to an $n\times 1$ matrix - which is why `display` has to write `self.cp.y.flatten()` at 622 and `self.cp.y[i, 0]` at 635, and why the function is not safe to call twice; `y = np.asarray(y).reshape(n, 1)` says the same thing without the side effect. 115 and 117 give mutable objects as default arguments (`y=[2, 1.5]`, `P=[[.8, .2], [.4, .6]]`). 392 puts one blank line before a top-level `def` where 151 and 197 in the same cell use two. 556 puts one space before an inline comment (`self.states = states # state names`) where PEP8 asks for two. 572 uses a backslash continuation for an assignment that parentheses would wrap. 641 is an f-string with no placeholder. And the matrix literals are padded by hand to columns that do not line up - 777-780 reads `[0,  1-ϕ,   ϕ,     0]` against `[0,    0,  1-ψ,    ψ]`, and 780 leaves a space before the closing bracket, `1-θ ]`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 250, 257, 284, 292, 585, 593, 604. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 255, 263, 289, 298, 590, 600, 607, 608, 613. *Example:* axis label `Periods`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 20. *Lines:* 251, 252, 253, 258, 259, 260, 285, 286, 287, 293, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 364. *Example:* `^T` transpose in `R^T`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 6. *Lines:* 684, 729, 763, 797, 837, 910. *Example:* rows inside `bmatrix` are separated with the plain-TeX `\cr` in all five example chains (684-686, 729-731, 763-766, 797-801, 837-843) while the exercise at 524-527 separates them with `\\` - one file, two spellings, and `\\` is both the AMS form and the one the rest of the corpus uses. The conditional expectation is written two ways as well: `\mathbb E_t` in the continuous-state section (877, 884, 892, 898), then at 910 as `\frac{b(x_{t+1})}{\beta E b(x_{t+1})| x_t}` - a bare $E$ with the conditioning bar left outside the operator's argument, so the denominator renders as $\beta E b(x_{t+1})$ followed by a dangling $| x_t$ rather than $\beta \mathbb{E}_t[b(x_{t+1})]$.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 877, 884, 892, 898. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 9. *Lines:* 26, 78, 82, 425, 501, 808. *Example:* the text has not been proofread and in several places the sentence no longer carries its meaning. 26 is missing the package name: "In addition to what's in Anaconda, this lecture uses the  library:". 78 collapses three phrasings into one: "$a_t$ is the government's holdings of one-period risk-free bonds coming maturing at the due at the beginning of time $t$". 82 does the same: "We'll spend most of this lecture studying acquire finite-state Markov specification". 425: "Here's code that itinitializes government assets to be unity". 808: "We ssume that $b_0 = 1$". Agreement errors in 336 ("the government has sold an Arrow securities paying off"), 419 ("The government then experiences 3 time periods of war and come back to peace again") and 501 ("the government always purchase $1$ units"), a stray space before the full stop at 722, and missing terminal periods at 88, 105, 337 and 425.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 60. *Lines:* 26, 40, 42, 44, 46, 49, 68, 72, 75, 76, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 248, 282. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 239, 281. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 80. *Example:* raw link to python-intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 847. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 452, 861, 869, 913. *Example:* Example 5 does not describe the chain it runs. 848 says "government expenditure levels for the seven states", 852 gives seven levels and 853-859 gives a seven-state $P$, but 861 names only six: `states_ex5 = ['peace1', 'peace2', 'war1', 'war2', 'war3', 'permanent peace']`. Every print in `display` is driven by `self.states`, so 622 prints six labels against seven numbers, 624 prints "Govt debt in 6 states", and the loops at 628-636 and 642-645 silently skip the seventh state - the deterministic example, the one whose whole point (828-830) is that complete and incomplete markets must agree, is the one reported incompletely. Second, the message printed at 452-456 tells the reader "Our assumptions imply that the government always purchases 0 units of the Arrow peace security", which the comment five lines below contradicts ("since the spending on Arrow peace security is not 0 anymore after we change b0 to 1", 461) and which the Explanation section then contradicts again ("the government always purchase $1$ units of the Arrow security that pays off in peace time", 501-502) - and unlike a comment, this one is printed into the built page. Third, the heading tree does not match the content: "### Continuous-state Gaussian model" (869) and "#### Related lectures" (913) are filed as subsections of "## More finite Markov chain tax-smoothing examples" (537), so the continuous-state model and the lecture's closing roadmap are nested under a finite-Markov heading; "## Returns on state-contingent debt" (348) is promoted to H2 although it continues "## Tax smoothing with complete markets" (303), which leaves "### An example of tax smoothing" (406) filed under Returns; and "#### Link to history" (85) jumps two levels down from the H3 above it.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 80. *Example:* mid-sentence 'Savings'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 39, 333, 371, 416. *Example:* the two terms the lecture is organised around are marked both ways within four lines of each other: 39-40 introduces them in bold ("the **complete markets** tradition of Lucas and Stokey", "the **incomplete markets** tradition of Barro") and 42-44 then defines them in italic ("*Complete markets* allow a government to buy or sell claims contingent on all possible Markov states", "*Incomplete markets* allow ..."), with bold returning for the same pair at 921 and 930. Bold is also used for plain emphasis, which the rule assigns to italic - "the government **is owed** $b_i$ or **owes** $-b_i$" (333), "a **particular** assumed path" (416) - while italic does that job correctly elsewhere in the file (73, 329, 509-510, 545, 880). And 371 and 907 use bold as a run-in heading ("**Convention:**", "**Returns:**").
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 371, 620, 682. *Example:* the object the whole lecture turns on is a peace-war Markov chain, and it is given six times as a matrix of symbols (524, 682, 727, 761, 795, 835) and never once as a diagram. By Example 3 the matrix is $4\times 4$, by Example 5 it is $7\times 7$ and lower-shift, and the distinctions the prose draws - "one of the states is a war state with no hope of peace next period, while another state is a war state with a positive probability of peace next period" (755-756) - are exactly what a four-node directed graph shows at a glance and a symbolic matrix does not. Second, `display` emits about twenty lines of bare `print` output per example (620-657) and is called five times, so roughly a hundred lines of unformatted text sit between the figures where a small per-example table of $g$, $\bar T$, $b$ and the ex-post returns would be read rather than skipped. Third, the lecture uses no admonition anywhere, although 371 ("**Convention:** In this code, when $P_{ij}=0$, we arbitrarily set $R(j | i)$ to be $0$") is a `{note}` a reader must not miss, and 907 ("**Returns:**") and the "Link to history" aside at 85-88 are the same shape.

### Low severity
_None found._


## Strengths

- The isomorphism is carried out rather than asserted: 68-74 lists the four relabelings, 75-78 writes the substitution $c_t = T_t$, $y_t = G_t$, $-b_t = a_t$, and the code then reuses the consumption-smoothing functions unchanged, renaming outputs at the call site with the reason attached - "# change notation y to g in the tax-smoothing example" (431) and "# change notation c_bar to T_bar in the tax-smoothing example" (440).
- The same pair of figures is drawn twice from the same arrays, once with consumption labels (239-266) and once with tax labels (281-301), so the claim that the two models are one model is shown on the page instead of argued.
- Each of the five examples is given a purpose before its parameters appear: stylised Civil War and World War I paths (676-697), a war followed by a permanent peace (722), a war state with no hope of peace next period beside one with a positive probability of peace (755-756), and a deterministic peace-war-peace path where complete and incomplete markets must coincide (828-830) - which makes that last example a check on the code rather than another illustration.
- `TaxSmoothingExample` (549-658) wraps solving, relabelling assets as debt and displaying, so the five experiments differ only in $(g, P, b_0, \text{states})$ (700-705, 740-745, 776-782, 811-818, 852-861) and the reader compares economies instead of re-reading code.
- The return on the state-contingent portfolio is treated end to end: defined at 357, compounded over a history at 364-366, given an explicit convention for the zero-probability entries at 371, computed at 374-403, and then read off the assumed peace-war-war-war-peace history at 511-513 ("so long as peace continues, the ex post return on insurance against war is low").
- The closing section (913-931) says exactly what this lecture holds exogenous - one-period interest rates and Arrow prices - and names the four lectures that make them endogenous, so a reader knows where the model's boundary is and where to go next.

## Recommended actions

1. Add the missing seventh state name at 861 - the chain, the expenditure vector and the prose at 848 all have seven states, `states_ex5` has six, and every printed line in `display` is indexed by that list, so Example 5 currently reports six of its seven states and prints "Govt debt in 6 states".
2. Delete or rewrite the message printed at 452-456: it asserts the government buys 0 units of the peace security, which the comment at 461 and the Explanation at 501-502 both contradict, and it is printed into the published output.
3. Proofread the prose: name the library at 26, and repair 78, 82, 336, 419, 425, 501, 722 and 808, each of which is missing a word or an agreement.
4. Fix the conditional expectation at 910 - the bar belongs inside the operator's argument, $\beta \mathbb{E}_t[b(x_{t+1})]$ - and add the braces to the four `\mathbb E_t` at 877, 884, 892 and 898 while in that section.
5. Replace the six matrix presentations of the Markov chains with transition diagrams (or add one beside each matrix at 682, 727, 761, 795, 835), and turn the per-example `print` block at 620-657 into a small table.
6. Restructure the headings so the continuous-state model (869) and Related lectures (913) are not subsections of "More finite Markov chain tax-smoothing examples" (537), demote "Returns on state-contingent debt" (348) under "Tax smoothing with complete markets" (303), and promote "Link to history" (85) to the level above.
7. Fix the in-place reshape at 213 so `consumption_incomplete` does not mutate `cp.y` (which would let 622 and 635 drop their `flatten()` and `[i, 0]`), and clear the smaller code items at 115, 392, 556, 572, 641 and 777-780.
8. Sweep the figures and the rest: move the 7 `set_title` calls (250, 257, 284, 292, 585, 593, 604) into captions, lowercase the 9 axis labels (255, 263, 289, 298, 590, 600, 607, 608, 613), add `lw=2` to the 20 line plots, drop the 2 `figsize=` overrides (248, 282), give the two figure cells `mystnb` names (239, 281), convert the raw `python-intro.quantecon.org` link at 80 to a `{doc}` reference and lowercase "Savings" in its title text, and clear the 60 double spaces.
