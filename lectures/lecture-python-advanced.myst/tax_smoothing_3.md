# tax_smoothing_3

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_3.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×4; `qe-writing-003` ×4; `qe-writing-002` ×4, +2 more. |
| Math         | 8.5/10 | `qe-math-011` (proposed) ×1; `qe-math-009` ×2. |
| Code         | 6.5/10 | `qe-code-001` ×6; `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×4; `qe-fig-006` ×4; `qe-fig-005` ×2, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 198, 222, 243, 264, 297, 314. *Example:* 264 binds `T` to the simulation horizon in a lecture whose objective is built from tax collections $T_t$ (67, 77, 80, 86, 132) - and the value is then passed as `ts_length=T` at 265, so the keyword already carries the meaning. 222-223 write `R1[0, 0] = R[0, 0] + 1e-9` and `R2[0, 0] = R[0, 0] + 1e12` where `+=` says it. 198 leaves a trailing comma and a space inside the closing bracket, `np.array([[1, 0], [Gbar, ρ], ])`. 243 ends `lqm.stationary_values();` with a semicolon to suppress notebook output, which PEP8 rules out. 314 has two spaces after `=` (`fig, (ax1, ax2) =  plt.subplots(...)`). And 296-302 repeats the six list assignments of 234-240 verbatim in the second cell while omitting the `stationary_values()` call that 243 makes for the first, so the two experiments are set up asymmetrically for no stated reason; 269-270 and 310-311 also loop 300 times to compute `tax[i, :] = S @ x[:, i] + M @ u[:, i]`, twice, where the whole path is one matrix product. 265 and 305 additionally bind `w`, shadowing the shock $w_{t+1}$ of 94-97, and never use it.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 29, 32, 33, 35, 39, 41, 44, 100, 101, 103, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 242, 304. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 273, 314. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 275, 278, 316, 319. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 262, 290. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 276, 279, 317, 320. *Example:* axis label `Time`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 274, 277, 315, 318. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 77, 86. *Example:* three conventions index the same pair of dates in the space of ten lines. 77 states the choice variables as $\{b_{t+1}, T_t\}_{t=0}^\infty$ with a single subscript; 86 and 100-103 write the same object as $b_{t,t+1}$ and its inherited counterpart as $b_{t-1,t}$; and the price of that very bond, in the same display at 86, is $p^t_{t+1}$, with the issue date raised to a superscript. One of the two two-index forms would do, and the single-subscript $b_{t+1}$ at 77 should match whichever is chosen, since 100 immediately re-declares the control as $b_{t,t+1}$.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 97. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 32, 35. *Example:* `` {cite} `` in narrative flow: 'of  `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 32, 35, 141, 252. *Example:* 32-33 carries the same stray closing parenthesis as the two earlier lectures in the series - "some ideas of `` {cite}`barro1999determinants` `` and `` {cite}`barro2003religion` ``) that extend" - with nothing opening it. 35 and 39 both drop the noun after the citation, so a bibliography key becomes the subject of the sentence: "`` {cite}`Barro1979` `` is about a government that borrows and lends" and "Technically, `` {cite}`Barro1979` `` looks a lot like a consumption-smoothing model" (the sibling lecture has the identical pair at its lines 35 and 39). 138-143 ends a sentence without punctuation and continues it as a one-item bullet ("because that is cheap" / " * Riccati equations will tell us this"). And 252-257 splits a two-part contrast across a one-item bulleted list and a following paragraph - "positive spikes occur when debt is positive" as a bullet, "Negative spikes occur when the government has positive asset holdings" as a paragraph - so the parallel structure the sentence sets up is broken by the markup.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 143, 222, 246, 263. *Example:* 246-260 sits between the setup cell and the simulation cell and reads results off a figure that does not exist yet - "The spikes in the tax collection series indicate periods when the government is unable to access financial markets" - before 263-265 has set $x_0$ or the horizon, and its opening line sends the reader to `tax_smoothing_2` for "the same process for $G_t$" that the cell immediately above has already fixed at 195-200 (`β, Gbar, ρ, σ = 0.95, 5, 0.8, 1`). The claim at 249-250 that "government debt fluctuates around zero" is also partly a property of `x0 = np.array([[0, 1, 25]])` at 263, whose three entries are never identified (initial debt 0, the constant, and $G_0 = 25$, which is the unconditional mean $5/(1-0.8)$ implied by 195-198) - the sibling lecture starts the same state vector at 100 and at 1000. Second, the dead-end argument at 134-143 rests entirely on a computation it never shows: "the government would have an incentive to set $b_{t,t+1}$ to a large negative number" is supported only by the bullet "Riccati equations will tell us this", and no Riccati equation appears in the lecture. Third, 222 adds `1e-9` to `R1[0, 0]` - a penalty on debt in the *good* states - where the prose at 170-176 describes only the large penalty in states 2 and 4, so the model solved has a perturbation the model derived does not.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 45, 100, 107, 171. *Example:* the lecture's own term gets three different treatments: bold at 45 (**roll-over risk**, correct - it is being defined) and then curly quotes at 107-108, 145 and 327 (“roll-over risk”), with italic *roll-over* risk at 136 in between. Two terms that are being defined are set in italic instead of bold: *controls* at 100, in the list that introduces the choice variables, and *effectively* at 171 - which the same sentence announces as a definition ("this is important because it defines what we mean by *effectively*"), after 160 has promised it. The italics that are genuinely emphasis are correct (*assets* at 140).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 181, 265, 273. *Example:* the Markov state path is computed and thrown away. 265 and 305 both unpack `x, u, w, state = lqm.compute_sequence(...)`, and `state` - which period is a bad state - is never used again, while 252-260 and 327-330 ask the reader to identify exactly those periods by eye ("positive spikes occur when debt is positive and the government must urgently raise tax revenues now", "debt is recurrently reset to zero and tax collections spike up"); shading the bad states on the two panels would turn every one of those claims into something visible. Second, the two figures (262-281 and 290-322) are drawn by identical code with identical titles - 'One-period debt issuance' and 'Taxation' at 275/278 and 316/319 - and nothing in either records which of the two price parameterisations produced it, so the comparison the closing paragraph rests on is between two indistinguishable pictures separated by nine lines of prose. Third, the four-state construction at 152-155 and its transition matrix at 181-185 is the natural candidate for a small transition diagram: the one property that matters has to be argued in words at 188-191 ("the Markov state cannot move, for example, from state 3 to state 1"), which a four-node diagram with the two forbidden arrows absent would show at a glance.

### Low severity
_None found._


## Strengths

- The lecture presents the wrong construction first and says precisely why it fails: 113-132 sets $p^t_{t+1} = 0$ in the bad state and shows the budget constraint collapsing to $T_t = G_t + b_{t-1,t}$, then 134-140 explains that the government responds by taking $b_{t,t+1}$ to a large negative number because assets are cheap in that state - so by the time the four-state fix arrives at 149-155 the reader knows what it is for.
- The four Markov states are given as four plain English phrases (152-155) and the one property the transition matrix must have is then checked out loud against them: 188-191 picks the state 3 to state 1 entry and explains why it has to be zero, "Because state 3 is “bad today”, the next period cannot have “good yesterday”".
- 170-176 names the exact element of the exact matrix that carries the mechanism - a large penalty on the $b_{t-1,t}$ element in states 2 and 4, deterring debt issue in states 3 and 4 - and the code puts it there and nowhere else: `R2[0, 0] = R[0, 0] + 1e12` at 223 with `Rs = [R1, R2, R1, R2]` at 238 ordering the penalised copy onto states 2 and 4.
- 160 flags the load-bearing word before leaning on it ("We'll explain what *effectively* means shortly") and 170-172 delivers the explanation in the same paragraph that introduces the penalty, so "effectively can issue debt" at 157-158 is not left hanging.
- The second experiment differs from the first in exactly one number and the prose says which: 287-288 "we simply raise $p^t_{t+1}$ to $\beta + 0.02 = 0.97$", realised as the single changed line `M = np.array([[-β - 0.02]])` at 291 - and 304 leaves `beta=β` at 0.95, which is what makes the bond price exceed the discount factor.
- Both simulation cells explain the step a reader would otherwise stall on, in a comment on the spot: `# Calculate taxation each period from the budget constraint and the Markov state` (267, 307-308), implemented at 270 as $S x_t + M u_t$ - literally the constraint of 86, since taxation is not among the solver's outputs.
- The closing paragraph (324-330) reads the second figure as a mechanism rather than as a picture, in three short steps: a lower interest rate gives an incentive to accumulate debt, roll-over risk recurrently resets it to zero, and the cost of a “sudden stop” is what keeps debt from getting too high.

## Recommended actions

1. Use the `state` array that 265 and 305 already return: shade the bad Markov states on both panels so the spike claims at 252-260 and 327-330 become visible, and give the two figures titles or captions that say which price parameterisation each one shows - as it stands 275/278 and 316/319 are the same two strings.
2. Either show the Riccati argument promised at 143 or state the conclusion of 134-140 without it; the whole case for abandoning the two-state formulation rests on that bullet.
3. Say what the `1e-9` added to `R1[0, 0]` at 222 is for, or remove it - the prose at 170-176 accounts only for the `1e12` of 223.
4. Move 246-260 below the cell at 262-281 that produces the figure it describes, and drop the pointer to `tax_smoothing_2` at 246-247 for a $G_t$ process the cell at 195-200 has already set; while there, identify the three entries of `x0` at 263, in particular that 25 is the unconditional mean of $G_t$ implied by `Gbar = 5`, `ρ = 0.8`.
5. Settle one date-index convention: $b_{t+1}$ at 77, $b_{t,t+1}$ at 86 and 100, and $p^t_{t+1}$ in the same display at 86.
6. Bold the two terms being defined - *controls* (100) and *effectively* (171) - and stop re-quoting “roll-over risk” at 107-108, 145 and 327 when 45 has already bolded it.
7. Tidy the code: `+=` at 222-223, drop the output-suppressing semicolon at 243 and the trailing comma inside `A22` at 198, remove the double space after `=` at 314, rename `T` at 264 away from the $T_t$ of the objective, vectorise the two 300-iteration tax loops (269-270, 310-311), and make the second experiment symmetric with the first by calling `lqm2.stationary_values()` or by factoring the repeated list assignments at 296-302 out of both cells.
8. Sweep the measured items: the 19 double spaces, the four `set_title` calls and four `Time` axis labels moved into lowercase `mystnb` captions with `name`s on the two figure cells (262, 290), `lw=2` on the four plot calls (274, 277, 315, 318), both `figsize=(12, 3)` overrides dropped, and `{\cal N}` at 97 written as a plain $N$ per qe-math-011 (proposed).
