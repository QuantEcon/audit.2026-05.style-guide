# irfs_in_hall_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/irfs_in_hall_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-004` ×7; `qe-writing-003` ×5; `qe-writing-001` ×2, +3 more. |
| Math         | 8.5/10 | `qe-math-003` ×1; `qe-math-009` ×2. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-008` ×12. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 85, 168, 173, 183, 261. *Example:* the Example 2 cell breaks the spacing conventions the other two cells keep: 173 writes `ts_length = 300` with spaces around a keyword-argument `=` where 123 and 267 write `ts_length=300`, and 183, 185 and 186 omit the space after the comma (`irf(ts_length=40,shock=None)`, `plt.plot(econ2.c_irf,label='Cons.')`) where the identical calls at 143, 145-146, 283, 285-286 all have it. The names then read as other symbols: `γ` at 85 is the technology *matrix* $\Gamma$ assembled from the scalar `γ_1`, and Example 3 pairs `γ_12 = 0.15` (255, a scalar that looks like $\gamma_{12}$) with `γ_2` (256, the matrix built from it), exactly as `ϕ_12 = 0.2` (168) and `ϕ_13 = 1` (252) are Example 2's and Example 3's values of the single parameter $\phi_1$; 97-105 also downcases $A_{22}$, $C_2$, $U_d$ and $U_b$ to `a22`, `c2`, `ud`, `ub` where the rule permits capitals for matrices. And 261 names the third example's initial condition `x01`, one off from the `x0` of 106, so the suffix numbers the variable rather than the example.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 121, 142, 167, 182, 251, 282. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 126, 127, 145, 146, 176, 177, 185, 186, 270, 271, …. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 5. *Lines:* 52, 192, 200, 207, 261. *Example:* 207-208 writes computed numbers into the prose: "The present economy has a nonstochastic steady state value of 5 for consumption and 0 for both capital and investment" - which is a reading of `print(econ2.css, econ2.iss, econ2.kss)` at 197, and states them in an order (consumption, capital, investment) that is not the order printed. Second, `x01 = np.array([[150], [100], [1], [0], [0]])` at 261 is a different initial condition from the $x_0$ displayed at 75-81 and used everywhere else - the first two entries are swapped and changed, 5 and 150 becoming 150 and 100 - and neither the display nor any sentence records the change; 248-249 only claims it "makes consumption begin near around its non-stochastic steady state", which cannot be checked because Example 3's steady state is never computed (only Example 2's, at 196-197). Third, 192 puts `econ2.endo` in a cell with no sentence saying what it is or that the reader should look at it, and Example 1's eigenvalues - the "unity" that 164-165 and 203-205 compare against - are never printed. Fourth, 200's "The first graph" is four cells and two output cells back (167-180). And 52 refers to a companion lecture by quoted title only, 'See the lecture "Growth in Dynamic Linear Economies" for more details', where 27 uses a `{doc}` link for a different lecture in the same suite.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 52, 68, 161, 164, 276, 295. *Example:* mid-sentence 'Dynamic'.

### Medium severity
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 77. *Example:* array used as matrix.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 62, 242. *Example:* 242 hangs the conditioning information set outside every delimiter, $-\frac{1}{2}\mathbb{E}\sum_{t=0}^\infty \beta^t[(\lambda h_{t-1} - b_t)^2 + l_t^2]|J_0$, so the bar reads as applying to the whole expression rather than as conditioning the expectation, where $\mathbb{E}_0$ says it in one symbol - the same construction appears in the two sibling lectures. $l_t$ in that display is also its only appearance in the file: nothing connects it to the $g_t$ of the technology, so the second term of the objective is an undefined symbol. And 61-63 sets a comma-separated list of six parameter assignments as a display equation, with $\phi_1 = 0.00001$ spelled as a decimal string that the code writes `1e-5` (88) and that 162 then spells out again.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 118, 219. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 26, 65, 161, 248. *Example:* 65-68 opens a parenthesis in one paragraph and closes it in the next - "(In this example $\delta_h$ and $\theta_h$ are arbitrary ..." ends at 66, a blank line follows, and "We set them to values that will become useful in Example 3)" closes the bracket at 68 - so on the built page the reader meets an unmatched `(` and, a paragraph later, an unmatched `)`. 161-162 loses the space before an inline formula in the sentence that defines the whole of Example 2: "the cost of adjusting capital,$\phi_1$, from 0.00001 to 0.2", and calls the other changed parameter only "the production function parameter" at 220 rather than naming the $\gamma_1$ of 62 and 84. 248-249 has "begin near around its non-stochastic steady state". And 26-27 opens with the suite's standard 34-word triple-nested sentence ("another member of a suite of lectures that use the quantecon DLE class to instantiate models within the {cite}`HS2013` class of models described in detail in {doc}`...`").
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 121, 125, 192. *Example:* the lecture is a three-way comparison and none of the three comparisons can be read off its figures. All six are built identically - `plt.plot(econ.c[0], label='Cons.')` and `plt.plot(econ.i[0], label='Inv.')` at 126-127, 176-177, 270-271, and the same pair of `_irf` series at 145-146, 185-186, 285-286 - with no title, no axis labels, no caption, no `name`, no `fig, ax`, and on six independently autoscaled pairs of axes in six separate cells. Every claim the lecture makes is then comparative: "Investment is much more responsive to the endowment shock at shorter time horizons" (155-156), "In contrast to Hall's original model of Example 1, it is now investment that is much smoother than consumption" (276-277), "consumption is now much more responsive to an endowment shock (and investment less so) than in Example 1" (291-293), "As in Example 2, the endowment shock has permanent effects on neither variable" (295-296). Two figures - three consumption-investment pairs on one, three IRF pairs on the other - would carry the entire lecture. The `# This is the right panel of Fig 5.7.1 from p.105 of HS2013` comments at 125, 144, 175, 184, 269 and 284 are both the captions the figures lack and evidence that HS2013 itself puts each simulation next to its IRF, which the lecture splits into separate cells. Third, four separate claims turn on where the largest endogenous eigenvalue sits relative to one (151-153, 164-165, 203-205, 210-211) and `econ.endo` is displayed for exactly one of the three economies, as a bare unlabelled cell at 192, so "the decrease in the largest endogenous eigenvalue from unity in the earlier economy" has nothing to be checked against.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 27. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 224. *Example:* the file's single piece of emphasis is on the term it is defining: "We also change the specification of preferences to make the consumption good *durable*" (223-224), where durability is the subject of the whole of Example 3 and is formalised in the three displays that follow at 229, 236 and 242 - the rule assigns that job to bold. Nothing else in the lecture is bolded or italicised, and the companion lecture title at 52 is set in quotation marks rather than as a link.


## Strengths

- Each example is one stated change from the last, with both the old and the new value given: 160-162 raises $\phi_1$ from 0.00001 to 0.2, and 219-221 raises it to 1.0 and the production parameter from 0.1 to 0.15 - and the code changes exactly those, rebuilding only the affected tuple and reusing `info1`, `ϕ_c`, `ϕ_g`, `δ_k`, `θ_k` and `β` untouched (170, 263).
- Every figure names the exact figure, panel and page of HS2013 it reproduces - right panel of Fig 5.7.1 p.105 (125), left panel of the same (144), the two panels of Fig 5.8.1 p.106 (175, 184), and the two panels of Fig 5.11.1 p.111 (269, 284) - so all six are checkable against the book.
- One mechanism is carried through all three examples: 70-71 notes that the Example 1 parameters give $\beta(\gamma_1 + \delta_k) = 1$, 151-153 explains the permanent effects by "the endogenous unit eigenvalue in this economy", 164-165 predicts that a higher adjustment cost pushes it below one, and 203-205 and 210-211 attribute both the downward drift and its slowness to that same eigenvalue.
- 65-68 anticipates the reader's question about two parameters that do nothing in Example 1 and says why they are nonetheless given specific values - because Example 3 will need them - which is what makes 245-246's "we have already set $\theta_h = 1$ and $\delta_h = 0.9$" verifiable against 95-96.
- Example 3 states the modified preferences in full before implementing them - the durable stock $h_t = \delta_h h_{t-1} + c_t$ (229), services from the beginning-of-period stock $s_t = \lambda h_{t-1}$ (236), and the objective (242) - so the mapping onto $\Lambda = 0.1$, $\Pi = 0$ at 245-246 and `l_λ2`, `π_h2` at 258-259 can be checked line by line.
- 135-136 documents the default a reader would otherwise not know, that `irf` with no selector vector responds to the first shock in $w_{t+1}$, before relying on it three times (143, 183, 283).
- 276-280 states the economics as a reversal rather than a description - durability "tends to undo the strong consumption smoothing result that Hall obtained" - which is precisely the contrast the three examples were constructed to produce.

## Recommended actions

1. Draw two figures instead of six: the three consumption-investment simulations on one set of axes and the three impulse responses on another, so the comparisons asserted at 155-156, 276-277, 291-293 and 295-296 become visible - the HS2013 references now hidden in the comments at 125, 144, 175, 184, 269 and 284 are the captions.
2. Print `econ1.endo`, `econ2.endo` and `econ3.endo` together with a sentence saying what they are: four separate claims (151-153, 164-165, 203-205, 210-211) turn on the largest one relative to unity, and only Example 2's is displayed, unlabelled, at 192.
3. Replace the hand-written steady state at 207-208 with the values the cell at 196-197 prints, in the order it prints them, and compute Example 3's steady state so the claim at 248-249 can be checked.
4. Display and explain `x01` at 261: it differs from the $x_0$ displayed at 75-81 in its first two entries and no line of the lecture records the change.
5. Close the parenthesis of 65-68 inside a single paragraph, add the missing space at 161-162 (`capital,$\phi_1$`), fix "near around" at 248, and name $\gamma_1$ at 220 rather than calling it "the production function parameter".
6. Link "Growth in Dynamic Linear Economies" at 52 with `{doc}` as line 27 does for `hs_recursive_models`.
7. Tidy the Example 2 cell to match the other two: `ts_length=300` at 173, and a space after the comma at 183, 185 and 186.
8. Rename the parameter variables so the suffixes do not read as subscripts: `γ` at 85 and `γ_2` at 256 are the matrix $\Gamma$ while `γ_1` and `γ_12` are the scalar $\gamma_1$; `ϕ_12` (168) and `ϕ_13` (252) are Example 2's and Example 3's $\phi_1$; `x01` (261) is Example 3's $x_0$; and `a22`, `c2`, `ud`, `ub` (97-105) can keep their capitals.
9. Bold *durable* at 224, and write $\mathbb{E}_0$ in the objective at 242 rather than hanging `|J_0` outside the bracket.
10. Sweep the measured items: `lw=2` on the twelve plot calls, `mystnb` `caption`/`name` on the six figure cells (121, 142, 167, 182, 251, 282), the `\left[ {\begin{array}...} \right]'` display at 77 recast as `bmatrix` with `\top` (qe-math-003), `{cite:t}` at 27, and the two paragraphs holding two sentences (118, 219).
