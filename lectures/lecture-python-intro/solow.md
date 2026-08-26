# solow

- **Series:** lecture-python-intro
- **File:** `lectures/solow.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-001` ×2; `qe-writing-005` ×2; `qe-writing-003` ×3, +4 more. |
| Math         | 8/10  | `qe-math-005` ×2; `qe-math-009` ×1. |
| Code         | 7/10  | `qe-code-001` ×16. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×1; `qe-fig-008` ×7; `qe-fig-001` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 16. *Lines:* 150, 249, 250, 358, 461, 493, 591, 616. *Example:* the exponentiation spacing the rule names explicitly is done both ways in the same lecture: `k**α` at 131 and 602 is right, but 461, 474 and 525 write `A * k_star ** α` / `A * k ** α` with spaces around `**`. Beyond that: 150 has a double space after a comma inside `ax.plot(xgrid, g_values,  lw=2, ...)`; 249 and 616 write `%x_init` with no space around the `%` operator (`label=r'$k_0=%g$' %x_init`); 250 and 358 omit the space after a comma (`np.full(ts_length,k_star)`, `ax.set_xlabel("$k$",fontsize=10)`); 493 leaves a space before a closing bracket, `(s_star_max, )`, immediately beside a correctly written `(c_star_max,)`; 591 uses one space before an inline comment; the three `ax.annotate(...)` calls at 158-164, 348-354 and 495-501 all under-indent their continuation lines relative to the opening delimiter; and 348 and 624 put two blank lines inside a function body while 601 puts only one between two top-level defs.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 248, 250, 339, 340, 502, 503, 615. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 70, 94, 103, 275, 296, 316. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 237, 338, 488, 607. *Example:* figsize=.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 2. *Lines:* 108, 556. *Example:* parenthesised sequence.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 316, 464. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 295, 316, 511. *Example:* 316-318 says the same thing twice inside one sentence: "high marginal returns to savings at low levels of capital combined with low rates of return at high levels of capital combine to yield global stability" - `combined with ... combine to` in 27 words. 511 loses its parallelism and its point: "One can also try to solve this mathematically by differentiating $c^*(s)$ and solve for $\frac{d}{ds}c^*(s)=0$" - `differentiating ... and solve`, plus "try to solve this mathematically" where "solve this symbolically" is what is meant and what the cell does. And 295-296 repeats 102-103 almost verbatim ("Our aim is to learn about the evolution of $k_t$ over time, given an exogenous initial capital stock $k_0$" / "given an initial stock $k_0$") 190 lines later without acknowledging the repetition.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 312, 570, 587. *Example:* the continuous-time section reuses the symbol $g$ for a different function. `` {eq}`solow` `` at 98-99 defines $g(k) := s f(k) + (1 - \delta) k$, cited at 116 and drawn as the 45-degree map; then 312-313 writes "$k'_t = g(k_t)$ with $g(k) = s Ak^\alpha - \delta k$", which is a different mapping with a different fixed-point interpretation, and the reader has no signal that the name has been recycled. The code does not make that mistake - it names the two functions `g` (130) and `g_con` (329) - so the prose is out of step with its own implementation. Second, the stochastic exercise contradicts itself: 565 says "$(A_t)$ is IID and lognormal", then 570 says "Consider $A=2.0, s=0.6, \alpha=0.3,$ and $\delta=0.5$" without saying what a single value of $A$ now means; the solution silently reinterprets it as a mean (585-586, `μ = np.log(2) - σ**2 / 2`) and 587's `A = 2.0` is then dead - `k_next` at 601-602 calls `lgnorm()` and never reads `A`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 536. *Example:* mid-sentence 'Rule'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 544, 595. *Example:* 595 sets a code identifier in italic - "Let's define the function *k_next* to find the next value of $k$" - where italic is reserved for emphasis and inline code is the right markup; the parallel sentence at 465 gets it right with `` `minimize_scalar` ``. And 544 uses bold as a pseudo-heading, `**Stochastic Productivity**`, on its own line at the top of the exercise body; it is neither a definition nor emphasis, and it is the only bold in the lecture that is not a definition (49, 59, 61, 187 and 298 all are).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 333, 408. *Example:* the continuous-time figure (333-364) plots $g(k) = sAk^\alpha - \delta k$ against the zero line and marks $k^*$, but omits the one device that makes a phase line carry the argument: arrows on the $k$-axis showing the direction of motion either side of $k^*$. Lines 312-318 spell that direction out in prose ("values of $k$ with $g(k) > 0$ imply $k'_t > 0$, so capital is increasing ... When $g(k) < 0$, the opposite occurs") - exactly the content a phase diagram exists to show. Second, `` {eq}`ssivs` `` at 408-419 gives the entire capital path in closed form and it is never plotted; overlaying it on the discrete-time simulation at 260-262, for the same parameters, would show the reader in one figure why the continuous-time detour was worth taking (271-272 promises that "the smoothing provided by continuous time can simplify our analysis").

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 484. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 61. *Example:* the CES function at 61 is written $F(K, L) = \left\{ a K^\rho + b L^\rho \right\}^{1/\rho}$ - curly braces used as a plain grouping delimiter, where parentheses are both the conventional choice and the simpler one, and where the same lecture reserves braces for nothing else (curly braces are the series convention for sequences, qe-math-005). The rest of the notation is commendably plain: no calligraphic or blackboard letters anywhere, and the algebra runs on $k$, $f$, $g$, $A$, $s$, $\alpha$, $\delta$.


## Strengths

- The one-sentence-per-paragraph discipline holds across 632 lines with a single measured lapse (316): the whole model is built at 34-103 as a chain of one-sentence paragraphs that each add exactly one assumption - savings (34-35), the capital identity (39-40), the simplification (42), the production function (44-46), homogeneity (48-55), the saving rate (69-70), depreciation (72-73).
- The reduction from $K_{t+1} = s F(K_t, L_t) + (1-\delta) K_t$ (78) to $k_{t+1} = g(k_t)$ (98) is shown as three explicit equalities (86-91) rather than asserted, which is the right amount of work to show for an introductory audience.
- The 45-degree diagram is shown twice from one function - `plot45()` at 178 with no fixed point, then `plot45(kstar)` at 208 with $k^*$ annotated by an arrow (158-164) - so the steady state appears on a figure the reader has already read, after the prose at 181-192 has said what to look for.
- Every labelled equation is cited: `solow` (97) at 116, `kstarss` (197) at 306, `solowc` (289) at 298, `xsolow` (388) at 403 - and 306 uses the citation to make a substantive point, that the continuous-time steady state coincides with the discrete-time one.
- 189 and 214 hand the general definitions off to `scalar_dynam` by `{ref}` instead of re-deriving steady state and global stability, which keeps this lecture about the Solow model.
- 403-404 asks the reader to verify `` {eq}`xsolow` `` by differentiating rather than leaving the closed form unearned, and 421-424 then reads global stability straight off the signs of $\delta$ and $\alpha$ - a two-line argument replacing the numerical one at 372-373.
- The Golden Rule exercise solves the same problem twice, numerically with `minimize_scalar` (478-481) and symbolically with `sympy` (530-533), and the symbolic pass uses `Rational` (519-521) so the answer is exact rather than a float that happens to agree.

## Recommended actions

1. Fix the stochastic-productivity exercise: 565 makes $(A_t)$ IID lognormal, 570 then gives $A=2.0$ with no interpretation, and the solution encodes 2.0 as the mean at 585-586 while leaving `A = 2.0` at 587 as dead code `k_next` never reads - say in the exercise that 2.0 is $\mathbb{E} A_t$ and delete line 587.
2. Rename the continuous-time drift in the prose at 312-313: `` {eq}`solow` `` already owns $g$, and the code already distinguishes `g` (130) from `g_con` (329), so follow the code.
3. Change `*k_next*` at 595 to `` `k_next` `` (465 already does this correctly for `minimize_scalar`) and fold the bold pseudo-heading `**Stochastic Productivity**` at 544 into the exercise text.
4. Add direction-of-motion arrows on the $k$-axis of `plot_gcon` (333-364) - 312-318 currently describes in words what that one addition would show.
5. Do NOT add `lw=2` to three of the ten drafted qe-fig-008 sites: 156 (`ax.plot(fps, fps, 'go', ms=10, ...)`), 345 (`ax.plot(fps, 0, 'go', ...)`) and 493 (`ax.plot((s_star_max, ), (c_star_max,), 'go', ms=8, ...)`) are marker-only calls that draw no line, so line width has no effect - see scanner_doubts. The other seven (248, 250, 339, 340, 502, 503, 615) are real.
6. Do NOT rewrite "Golden Rule savings rate" at 536: the drafted qe-writing-004 hit is inside the link label `[Golden Rule savings rate](https://en.wikipedia.org/wiki/Golden_Rule_savings_rate)` and is both a proper name and the target page's title - this is the known link-label false-positive class.
7. Sweep PEP8: spaces around `**` at 461, 474 and 525 (131 and 602 show the intended form), `%x_init` at 249 and 616, missing comma spaces at 250 and 358, the double space at 150, `(s_star_max, )` at 493, the inline comment at 591, and the three under-indented `ax.annotate` continuation blocks at 158-164, 348-354, 495-501.
8. Add a second sentence's worth of blank line after the math block at 199 - line 200 starts a new paragraph flush against the closing fence - then clear the six double-space runs (70, 94, 103, 275, 296, 316), split the two-sentence paragraph at 316, brace the two parenthesised sequences at 108 and 556 (qe-math-005), and make the exponent order consistent: 550-551 writes $A k^\alpha_t$ where 303 and 384 write $k_t^\alpha$.
9. Plot `` {eq}`ssivs` `` against the discrete-time simulation at 260-262, and add `mystnb` figure metadata to the un-named figure cell at 484 (qe-fig-005) while dropping the four `figsize=[11, 5]` overrides at 237, 338, 488 and 607.
