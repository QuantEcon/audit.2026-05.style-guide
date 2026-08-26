# os

- **Series:** lecture-python.myst
- **File:** `lectures/os.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×3; `qe-writing-003` ×2; `qe-writing-004` ×1, +2 more. |
| Math         | 9.5/10 | `qe-math-009` ×3. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×2; `qe-fig-008` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 299, 78, 253. *Example:* the same subexpression $\beta^{1/\gamma}$ is written two ways, and 299 is the one the rule names explicitly: `return (1 - β ** (1/γ)) * x` puts spaces around the exponentiation operator, which the rule asks to be written `a**b`, while 240 writes `(1 - β**(1 / γ))**(-γ)` - tight `**` but spaced `/`. Neither line matches the other and only `β**(1/γ)` matches the rule. flake8 over every code cell (`--select=E1,E2,E5,E7,W2,W3,W6,F,C4 --max-line-length=79`) reports exactly one item, E226 on that same line 299. Second, all three function definitions open with a blank line between the signature and the first statement (78-80, 238-240, 297-299) - a consistent house style, but not one PEP8 or the rest of the corpus uses. Third, 253-254 sets `fontsize=12` on the first figure's axis label and legend and the second figure (306-312) does without it, so the two figures in the same lecture render their text at different sizes for no stated reason.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 245, 305. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 251, 307, 308, 309. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 338, 476, 72. *Example:* the prime is spelled two ways in one file. `u^{\prime}` and `v^{\prime}` appear at 338, 361, 362, 466, 498 and 508, and plain `u'`/`v'` at 446, 483, 495, 643, 649, 655 and 677 - so `` {eq}`euler-cep` `` at 338 is `u^{\prime}(c^*_t) = \beta u^{\prime}(c^*_{t+1})` while the same equation restated in the exercise solution at 643 is `u'(\sigma(x)) = \beta u'(...)`. The simpler form is already the majority. Second, `` {eq}`bellman_equality` `` at 476 writes $v(x) = g(c,x)$, using one letter $c$ for both a free second argument of $g$ and the maximizer that depends on $x$; 479 then has to disclaim it in words ("acknowledging that the maximizing consumption will depend on $x$") and 484 writes $\partial c / \partial x$, which is meaningful only for the second reading. $v(x) = g(c(x), x)$ costs three characters and removes the need for the disclaimer. Third, 72 writes `\gt` inside `` {eq}`crra_utility` ``, `(\gamma \gt 0, \, \gamma \neq 1)`, where the plain `>` is used at 356 and is the simpler of two equivalent spellings.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 402, 456, 652. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 503, 246. *Example:* 503 drops a step in the derivation the section exists for. It says "But now an application of `` {eq}`bellman_FOC` `` gives" $u'(c) = v'(x)$, but `` {eq}`bellman_FOC` `` alone gives $u'(c) = \beta v'(x-c)$; reaching $u'(c) = v'(x)$ needs `` {eq}`bellman_envelope` `` as well, and 513 then says "Combining this fact with `` {eq}`bellman_envelope` `` recovers the Euler equation" - so `` {eq}`bellman_envelope` `` is used twice and its first use is unacknowledged, which is precisely the step a reader retracing the argument cannot reproduce. Second, the parameter values live inside a figure cell: `β, γ = 0.95, 1.2` is the first line of the plotting cell at 245-257, and 302-303 ("Continuing with the values for $\beta$ and $\gamma$ used above") together with 307-309 depend on them sixty lines later. A reader who treats the figure cell as a figure never sees where the numbers came from, and the notebook breaks if that cell is skipped.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 501. *Example:* mid-sentence 'Theorem'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 117, 411, 245. *Example:* the lecture is called "Cake Eating" and the cake is never drawn. Both of its figures plot a function of the state - $v^*$ against $x$ (245-257) and $\sigma^*$ against $x$ (305-315) - and neither shows a path in time, although the algebra for one is already in the file: the exercise solution derives $x_{t+1} = x_t(1-\theta)$ at 544 and $x_t = x_0(1-\theta)^t$ at 547, so $x_t = \bar x \beta^{t/\gamma}$ and $c^*_t = \sigma^*(x_t)$ are two lines of code given `c_star` at 297. The whole "Intuition" section (127-149) is a claim about paths - "the rate of consumption to be decreasing in both parameters" (147) - checked at 288-292 only against the *policy*. Second, the perturbation argument at 411-417 is a two-bar picture told in five lines of prose: "a feasible perturbation that reduces consumption at time $t$ to $c^*_t - h$ and increases it in the next period to $c^*_{t+1} + h$", with 415 having to say in words that nothing else moves. Third, the "Trade-off" section (115-125) turns on the concavity of $u$ and never plots $u$; one panel with $u$ at two values of $\gamma$ would carry 122-125 and 133-136 together.

### Low severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 179. *Example:* 179 italicises the lecture's central object on first use - "the value function will satisfy a version of the *Bellman equation*" - where 323 bolds the other one, "based on the so-called **Euler equation**", and every other defined term in the file is bold: **feasible** (107), **state variable** / **control variable** / **action** / **parameters** (111-113), **consumption smoothing** (123), **optimal policy** (270), **feasible consumption policy** (350), **satisfy the Euler equation** (355), **functional equation** (374). Nine bolded definitions, one italicised, and it is the one the next section is named after (159). The file's only other italic span, *function* at 270, is emphasis and is correct.


## Strengths

- The lecture commits to a prediction before it computes one: 131-136 guesses that consumption falls in both $\beta$ and $\gamma$, 147 states the summary, and 288-292 returns to check it against `` {eq}`crra_opt_pol` `` - with the figure at 305-315 perturbing exactly those two parameters and nothing else (`β + 0.02`, `γ + 0.2`).
- The five `{note}` blocks each hold a genuine aside and none of them is load-bearing for the main line: the IES gloss (138-145), the CRRA-dependence of the closed form (223-233), what a functional equation is (373-375), the Gateaux-derivative pointer (401-406), and the differentiability assumption with a specific citation, "theorem 10.1.13" (455-458).
- Every labelled equation is genuinely cited later, by label: `crra_utility` (70) at 210; `cake_feasible` (98) at 107; `bellman-cep` (184) at 199, 204, 264 and 453; `crra_vstar` (214) at 219, 224, 279, 521, 531; `crra_opt_pol` (283) at 292, 371, 521, 531, 628; `euler-cep` (336) and `euler_pol` (359) at 365 and 628; `bellman_FOC` (464) at 503; `bellman_envelope` (493) at 513.
- Two independent derivations of the same necessary condition, each self-contained - the perturbation argument at 383-449 and the envelope argument at 451-513 - with 377-381 saying in advance which direction each one covers, sufficiency being cited to proposition 2.2 of `` {cite}`ma2020income` `` rather than asserted.
- The exercise solutions finish the job instead of gesturing at it: 540-622 carries the linear-policy guess through the geometric sum, the first-order condition and the substitution $c = \theta x$ to $\theta = 1 - \beta^{1/\gamma}$ and then back to `` {eq}`crra_vstar` ``, and 646-685 verifies the Euler equation side by side. Both check out arithmetically, including the non-obvious cancellation at 679-681 where $(\beta^{1/\gamma})^{-\gamma} = \beta^{-1}$.
- 109-113 fixes the vocabulary - state variable, control variable / action, parameters - at the point the model is written down rather than assuming it, and 350-353 does the same for a feasible consumption policy, with 353 spelling out in one parenthetical why $\sigma(x) \leq x$ is the constraint it is.
- No `figsize` anywhere in the file: both figure cells (245, 305) call `plt.subplots()` bare and let the theme decide, which is what `qe-fig-001` asks for and is not the norm in this series.

## Recommended actions

1. Plot the cake. Add one figure of $x_t = \bar x \beta^{t/\gamma}$ and $c^*_t = \sigma^*(x_t)$ against $t$ for the three parameter pairs already used at 307-309 - `c_star` (297) and the recursion at 544 are all it takes - so that the object in the lecture's title is visible somewhere in it.
2. Rewrite 299 as `return (1 - β**(1/γ)) * x`: as written it puts spaces around `**`, which the rule names as the one PEP8 exception, and it disagrees with the identical subexpression at 240.
3. Bold **Bellman equation** at 179, to match **Euler equation** at 323 and the nine other bolded definitions in the file.
4. Fix the gap at 503: $u'(c) = v'(x)$ follows from `` {eq}`bellman_FOC` `` *together with* `` {eq}`bellman_envelope` ``, not from `` {eq}`bellman_FOC` `` alone.
5. Move `β, γ = 0.95, 1.2` out of the figure cell at 246 into a cell of its own, since 302-309 depend on it sixty lines later.
6. These drafted findings are all true positives - do not talk anyone out of them: the two `qe-fig-005` cells (245, 305) carry neither `caption` nor `name`, so neither figure can be `{numref}`-referenced; all four `qe-fig-008` calls (251, 307, 308, 309) draw real lines and want `lw=2`; and `qe-writing-004` at 501 is not a proper noun - the same file writes "theorem 10.1.13" (457) and "proposition 2.2" (378) in lower case, so "Envelope Theorem" should be "envelope theorem".
7. Settle the notation: one spelling of the prime (`u'`/`v'` at 338, 361, 362, 466, 498, 508 or `^{\prime}` everywhere), $v(x) = g(c(x), x)$ at 476, and `>` for `\gt` at 72.
8. Sweep the copy: split the two-sentence paragraphs at 456 and 652; "Here are some plots" (294) precedes one figure; "trade off strategy" (202) against "trade-off" at 25 and 117; "right hand side" (199, 204, 264, 280, 460) against "right-hand side" (661, 673, 685); the stray `\\` closing the display at 613; and the code-cell tag `ipython` at 42 where the other five cells are `python3`.
