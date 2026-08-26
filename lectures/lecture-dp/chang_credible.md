# chang_credible

- **Series:** lecture-dp
- **File:** `lectures/chang_credible.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-001` ×5; `qe-writing-005` ×9; `qe-writing-002` ×5, +4 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 5. *Lines:* 459, 612, 725, 792, 797. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 76, 423, 429, 566, 582. *Example:* line 76 ends a bullet with the placeholder 'but $\ldots$.'; line 423 has a stray word - 'For a credible government plan, we the two-dimensional state vector $(w_t, \theta_t)$ encodes history dependence'; line 429 ends the definition of a sustainable plan with a full stop where a colon belongs ('are said to constitute a *sustainable plan* (SP) if.'); line 566 reads '**Proposition:**.'; line 582 says 'by iterating on `` {eq}`chang501` ``, which we repeat here for convenience' and then reprints the whole five-equation system at 584-592, thirteen lines after the labelled original at 368-378.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 9. *Lines:* 328, 336, 349, 561, 566, 693, 695, 725, 771. *Example:* every bold in this file is a structural label and every defined term is in italic - the rule inverted twice over. Bold is used for '**Definition:**' (328, 336), '**A credible government policy with a recursive representation**' (349), '**Proposition:**' (561, 566) and '**Step 1**' through '**Step 4**' (693, 695, 725, 771), all of which want headings or `{prf:}` directives. Meanwhile the terms the lecture actually defines are italicised: *credible public policy* / *sustainable plan* (66), *gradual deflation* (103), *value of money* (170), *government policy* / *price system* / *allocation* (330-332), *competitive equilibrium* (339), *credible* (385), *sustainable plan* again (429). So a reader scanning for definitions finds section labels instead.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 21. *Lines:* 38, 41, 43, 60, 69, 91, 93, 103, 134, 215, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 829, 855, 869. *Example:* line 829 declares `def plot_equilibria(ChangModel):` - a parameter in CapWords that shadows the class of the same name being passed into it (PEP8 asks for lowercase parameter names, and `model` or `ch` would also read better at the call sites 860 and 879). Line 855 under-indents the continuation of `ax.annotate(...)`: `R[1]), fontsize=18)` sits below the `xytext=(` opening paren rather than aligned with it (E128). Line 869 indents the continuation of the `ChangModel(...)` call by four spaces instead of aligning it with the opening delimiter, and writes `h_max=1/0.8` unspaced where the same argument at 818 is `h_max=2`.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 399, 625. *Example:* line 399 attaches the wrong function to the continuation value. The five-tuple at 372-376 assigns $w_{t+1} = \chi(h_t, w_t, \theta_t)$ and $\theta_{t+1} = \Psi(h_t, w_t, \theta_t)$, but the sentence explaining the credibility inequality says 'a government attains a weakly higher lifetime utility with continuation value $w_{t+1} = \Psi(h_t, w_t, \theta_t)$' - $\Psi$ where $\chi$ is meant, in the one sentence that says why credibility holds. Line 625 has the matching problem in the other central derivation: the household constraint is $m(h)(u'(f(x(h))) - v'(m(h))) \leq \beta\theta'(h)$ in `` {eq}`eqn_chang16` `` (547) and in both Step 2 and Step 3 restatements (717, 757), but at 625 it is written with a plus - and 625 sits inside the passage arguing that $E(Z)$ is 'equivalent to the $\tilde D(Z)$ operator but simpler to implement', which is exactly where the reader needs to be able to check the two against each other.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 726, 765. *Example:* mid-sentence 'Step'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 466, 693. *Example:* line 466-467 announces a picture and then does not draw one: 'Now recall the within-period timing protocol, which we can depict $(h,x) \rightarrow m = qM \rightarrow y = c$' - an inline arrow chain in math mode standing in for the diagram the sentence promises, and the within-period ordering is what the whole confirm-or-disappoint structure hinges on. Second, the four-step algorithm at 693-780 is a set-shrinking iteration - build a large initial polytope, compute the best deviation value, cut the set back with a subgradient linear program, stop when consecutive sets are close - and the only figure in the 882-line lecture (833-858, called at 860 and 879) shows the converged sets. One panel with $S_0 \supset S_1 \supset S_2 \supset \cdots \supset S$, or the subgradient hyperplanes of Step 3, would make the operator concrete; the plotting machinery for polytope extreme points already exists at 838-844.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 833. *Example:* figsize=.


## Strengths

- The lecture states its exact delta from its companion in one line - 'The only change -- and it is a substantial one -- is the timing protocol for making government decisions' (41) - and then itemises precisely what $\tilde D(Z)$ adds to the $D(Z)$ of `` {doc}`chang_ramsey` ``: all of the old restrictions plus the sustainability requirement, glossed as 'the government wants to implement it at all times after all histories' (75-79).
- The two propositions at 561-569 supply exactly what is needed to justify the computation that follows - self-generation, factorization, monotonicity and preservation of compactness - and lines 571-576 draw the conclusion explicitly: $S$ is compact, so highest- and lowest-value sustainable plans exist, and $S$ can be computed by iterating $\tilde D$ from a sufficiently large $Z_0$.
- Chang's simplification is motivated before it is deployed (604-641): only the best deviation and the harshest punishment can bind, so the continuum of incentive constraints collapses to the scalar $BR(Z)$, 'the value of the government's most tempting deviation' - and $E(Z)$ is then introduced as an operator equivalent to $\tilde D(Z)$ but implementable.
- Each of the four algorithm steps (693-780) writes out the exact optimisation problem it solves together with its full constraint set, so the `:load:`ed `changecon.py` at 802-807 can be read line by line against the mathematics rather than taken on trust.
- The economics is settled by an experiment that moves exactly one parameter: at $\beta = 0.3$ the Ramsey point lies outside the sustainable set (863: 'the Ramsey plan, denoted by the $R$, is not sustainable'), at $\beta = 0.8$ it lies inside (882) - the same plotting function, the same axes, the same everything else.
- The figure earns its keep: the competitive-equilibrium and sustainable sets are filled in contrasting colours with the key given in prose before the cell (825-826), and the Ramsey plan is located for the reader as a labelled black point (846-855) rather than left to be found.
- Concrete functional forms for $u$, $v$ and $f$ are supplied (776-787) so every set in the lecture is actually computable, and the speed-accuracy trade is stated openly at 797-798 ('We have set the number of subgradients to 10 in order to speed up the code for now').

## Recommended actions

1. Fix the split-delimiter definitions, which currently leave the lecture's three central objects without their braces. The definition of $S$ opens `\Bigl\{` in the `$$` block at 447-450 and closes `\Bigr\}` in a *different* `$$` block at 454-457, with prose in between; $\tilde D(Z)$ opens `\Bigl\{` at 508 inside a `{math}` directive and closes at 551 inside a separate `$$` block five directives later; $E(Z)$ (647-660 onward) is built the same way. LaTeX delimiters cannot span display environments, so none of these braces render and each fragment is an unbalanced expression. Line 625 also carries a stray closing `\}` with nothing opening it. Each definition needs to be one display block, or the delimiters need to be per-block.
2. Convert the two '**Proposition:**' blocks (561, 566) to `{prf:proposition}` directives and the two '**Definition:**' blocks (328, 336) to `{prf:definition}`, then bold the terms those blocks define (currently italic at 330-332, 339, 385, 429) and turn '**Step 1**'-'**Step 4**' (693, 695, 725, 771) into real subheadings. As a side effect this is why the whole Admonitions category is N/A for this file.
3. Fix the two notation errors that break the arguments they appear in: $\Psi$ should be $\chi$ at line 399 (per 375-376), and the sign in the household constraint at 625 should be a minus to match `` {eq}`eqn_chang16` ``, 717 and 757.
4. Repair the malformed limit at line 176: `$u'(c)_{c \rightarrow 0} = \lim_{m \rightarrow 0} v'(m) = +\infty$` should read $\lim_{c \to 0} u'(c)$ on the left, matching the form already used on the right of the same line.
5. Clear the 21 double spaces, lower-case the 2 mid-sentence capitals at 726 and 765, and split the 5 two-sentence paragraphs at 459, 612, 725, 792 and 797 (qe-writing-008 x21, qe-writing-004 x2, qe-writing-001 x5).
6. Set multi-letter operator names upright: `BR(Z)` at 638, 641 and 644, `SP` at 429 and 469, and `CE_\pi^0` throughout currently render as products of italic letters; `\operatorname{BR}`, `\mathrm{SP}`, `\mathrm{CE}` fix that. While in the math, replace the plain-TeX `\over` at 195 with `\frac`, and tidy the 7 labelled equations that are never referenced (`eqn_chang2a` 210, `eqn_chang3a` 225, `eqn_chang4`, `eqn_chang12` 517, `eqn_chang13` 523, `eqn_chang_15` 537, `eqn_chang16` 545 - the last two are cited in prose by name but not by `{eq}`).
7. Add the two missing pictures - a small diagram for the within-period timing protocol the text at 466 says it will depict, and one panel showing the nested sets $S_0 \supset S_1 \supset \cdots \supset S$ produced by the iteration - drop the hand-set `figsize=(7, 5)` at 833 (qe-fig-001 x1), and fix the code slips at 829, 855 and 869.
