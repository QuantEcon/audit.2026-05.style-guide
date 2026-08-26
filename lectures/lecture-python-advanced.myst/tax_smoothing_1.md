# tax_smoothing_1

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_1.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 6.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×5; `qe-writing-002` ×6; `qe-writing-003` ×4, +2 more. |
| Math         | 4.5/10 | `qe-math-002` ×11; `qe-math-011` (proposed) ×1. |
| Code         | 7/10  | `qe-code-001` ×6; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-006` ×6; `qe-fig-005` ×3; `qe-fig-008` ×3. |
| References   | 7.5/10 | `qe-ref-001` ×9. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 291, 300, 321, 373, 479. *Example:* `T` is bound to the simulation length at 373, 386 and 499, in a lecture whose central variable $T_t$ is tax collections (184, 203, 262, 341) - the one name in the file that should not have been reused, and `ts_length` is already the keyword it is passed to. 291-292 pads an array literal to align columns, `[[1,    0], [Gbar, ρ],]`, and leaves a trailing comma before the closing bracket; 300-302 names the two blocks of the state-transition matrix `A_t` and `A_b`, where `A_t` reads as a time subscript on $A$; 321 writes `R[0, 0] = R[0, 0] + 1e-9` for `+=`; 479 ends `lqm.stationary_values();` with a semicolon to suppress notebook output, which PEP8 rules out; and 372-379 and 385-392 are the same eight-line simulation loop twice, re-running 250 paths of 500 periods to plot a different row of the same `x` that the first loop already computed.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 6. *Lines:* 377, 378, 390, 391, 504, 505. *Example:* axis label `Time`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 11. *Lines:* 262. *Example:* apostrophe transpose `x_t'`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 9. *Lines:* 41, 43, 61, 63, 82, 123, 132, 175. *Example:* `` {cite} `` in narrative flow: 'by  `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 41, 43, 95, 152, 404, 447. *Example:* the same attribution is made three times in fifty lines - "modified versions of his 1979 model suggested by `` {cite}`barro1999determinants` `` and `` {cite}`barro2003religion` ``)" (40-41), "we extend `` {cite}`Barro1979` `` along lines he suggested in `` {cite}`barro1999determinants` `` and `` {cite}`barro2003religion` ``)" (60-61), and "Partly inspired by `` {cite}`barro1999determinants` `` and `` {cite}`barro2003religion` ``" (82) - and two of the three end with a stray closing parenthesis that has no opening. The description of what a Markov jump LQ program is also appears twice, at 95-101 and again at 110-119. Four sentences are broken: 43 "`` {cite}`Barro1979` `` m is about a government that borrows and lends"; 82-83 "our generalizations of `` {cite}`Barro1979` ``,  assume"; 152-154 "A `` {doc}`sequel to this lecture <tax_smoothing_2>` `` describes applies Markov LQ control"; and 447 "each Markov state is persistent, and there is are equal chances of moving from one state to the other". 404 has "quandratic".
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 30, 52, 93, 111. *Example:* the lecture's own subject term is set both ways within twenty lines: **Markov jump linear quadratic dynamic programming** in bold at 30, 95-96 and 111, and *Markov jump linear quadratic dynamic programming* in italic at 52-53. 93 uses bold for plain emphasis - matrices that are "**time-varying** and **stochastic**" - as does 65, "an **exogenous sequence** of expenditures", where the surrounding bullets state the same kind of assumption without emphasis. Meanwhile genuine definitions are italicised: *control* variables at 223, *portfolio management* at 138. The three bolded terms at 98-101 (**linear quadratic dynamic programming**, **finite state Markov chains**) are then bolded again at 111-113, so the same two terms are marked as new definitions twice.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 36. *Lines:* 30, 41, 47, 52, 53, 60, 61, 82, 83, 123, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 158. *Example:* install cell at line 158 of 508 (not near the top).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 372, 385, 498. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 376, 389, 503. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 178. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 220. *Example:* decorated distribution `{\cal N}`.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 321, 329, 366, 499. *Example:* the three figures the lecture builds to are not comparable, and the text treats them as if they were. The constant-interest-rate simulations start from $x_0 = (100, 1, 25)$ and run 500 periods (329, 373, 386); the time-varying-interest-rate simulation starts from $x_0 = (1000, 1, 25)$ and runs 2000 (499-500), a tenfold change in initial debt and a fourfold change in horizon that no line of prose mentions - so the claim at 492-496 that "debt tends to stay low and stable but recurrently surges" is read off a different experiment from the one at 382-383, which promises "a similar, but a smoother pattern". Second, the model actually solved is not the model derived: 320-321 adds `R[0, 0] = R[0, 0] + 1e-9` with the comment "Small penalty on the debt required to implement the no-Ponzi scheme", a modification to the objective `` {eq} `` at 203 that the prose never mentions, though it is what keeps the solution well defined. Third, the martingale property that 357-361 states as the condition $(S-MF)(A-BF) = (S-MF)$ is "checked" at 365-367 by printing two matrices as a bare tuple and leaving the reader to compare them entry by entry, where `np.allclose` would state the result the text claims.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 320, 374, 501. *Example:* all three figures are 250 paths drawn one `plt.plot` call at a time inside a `for` loop (374-379, 387-392, 501-506), so matplotlib assigns each path the next colour in the default property cycle - 250 lines in ten rotating colours, at full opacity, with no alpha. The text asks the reader to see a distribution in them: "the fanning out of the conditional empirical distribution of taxation across time" (369) and "debt tends to stay low and stable but recurrently surges" (492-496). A fan chart of simulated percentiles, or a single colour at low alpha with the median overlaid, would show exactly those two claims; the rainbow of overlaid lines shows neither, and at 2000 periods and 250 paths the third figure is a solid block. The lecture also has no admonition anywhere, which is where the no-Ponzi penalty of 320-321 belongs - it is a substantive modelling choice currently living in a code comment - and the two-state interest-rate process introduced at 428-451 is never drawn, though its whole point is that the mean price 0.9515 exceeds $\beta$.

### Low severity
_None found._


## Strengths

- The mapping from Barro's problem into the LQ framework is done step by step and every matrix is accounted for: the state and control are named (233-235), the transition law gives $(A,B,C)$ (239-241), $G_t$ and $b_{t-1,t}$ are written as selections from the state (247-249), the budget constraint turns taxation into $T_t = Sx_t + M_tu_t$ (251-257), and squaring that expression exhibits $(R,Q,W)$ (259-263) - so the reader can check the code at 299-318 line against line.
- The isomorphism claimed at 178-180 is then tested rather than asserted: 332-361 derives the exact algebraic condition under which taxation is a martingale, $(S-MF)(A-BF) = (S-MF)$, and 365-367 evaluates both sides on the solved model.
- The extension is introduced at the smallest possible step: 423-424 allows the interest rate exactly two values, 428-434 gives both numerically as $\beta \pm$ a small number, 443-445 gives a symmetric persistent transition matrix, and 450-455 states the consequence that makes the exercise interesting - the unconditional mean price 0.9515 exceeds $\beta$, so the constant-rate model at that price would explode.
- The lecture is explicit about where it sits in a sequence: 35-38 names both sequels by `{doc}` reference, 30-31 points back to the Markov jump LQ lecture for the method, and 146-154 says what this lecture covers and what the next one adds (debt of different maturities).
- The public-finance questions are separated by which model answers them (121-140): the two coarse questions that `` {cite}`Barro1979` `` addresses, then the three fine-grained ones - short versus long maturity, roll-over risk, long-short portfolio management - that motivate the extensions, which is what makes the added state dimension feel necessary rather than decorative.
- The Markov jump problem is solved through the library class rather than a reimplementation (477-479), and 406-416 says what the class does, where its source is, that it iterates a coupled system of matrix Riccati difference equations, and which attributes hold $P_s$, $F_s$ and $d_s$ - so the two decision rules printed at 484-490 can be interpreted.

## Recommended actions

1. Make the three simulations comparable or say why they are not: 329 starts from debt 100 over 500 periods and 499-500 from debt 1000 over 2000, while 382 and 492-496 read the figures as variations of one experiment.
2. Move the no-Ponzi penalty out of the comment at 320-321 and into the prose (or a `{note}`) beside the objective at 202-204, since it changes the problem being solved.
3. Redraw the three figures as fan charts, or as one colour at low alpha with a median path: 250 `plt.plot` calls in a loop (374-379, 387-392, 501-506) take 250 colours from the default cycle, which hides exactly the "fanning out" and the "recurrent surges" the text points at.
4. Turn the martingale check at 365-367 into an assertion (`np.allclose(S - M @ F, (S - M @ F) @ (A - B @ F))`) so the claim at 357-363 is stated rather than left for the reader to compare two printed matrices.
5. Cut the triplicated attribution to `` {cite}`barro1999determinants` `` and `` {cite}`barro2003religion` `` (40-41, 60-61, 82-83) to one, delete the two stray closing parentheses at 41 and 61, and repair "m is about" (43), "describes applies" (152-154), "there is are" (447) and "quandratic" (404); also collapse the duplicated definition of a Markov jump LQ program at 95-101 and 110-119.
6. Rename the simulation length `T` (373, 386, 499), which collides with the tax collections $T_t$ that the lecture is about, and settle the emphasis convention on the lecture's own key term - bold at 30, 95 and 111, italic at 52.
7. Sweep the mechanical load: move the install cell from 158 up to the top of the lecture (qe-code-003), the 11 apostrophe transposes at 262 to `\top`, the `{\cal N}` at 220 to plain $N$, the six capitalised axis labels (377, 378, 390, 391, 504, 505), the three `plot()` calls without `lw=2`, `mystnb` caption and `name:` metadata on the three figure cells (372, 385, 498), the two spelled-out `beta=` arguments (327, 478), the 36 double-space runs, the raw link at 178, and the bare "here" link text at 406-407.
