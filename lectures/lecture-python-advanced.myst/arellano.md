# arellano

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/arellano.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×2; `qe-writing-003` ×2; `qe-writing-002` ×2, +2 more. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 6.5/10 | `qe-code-001` ×8; `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×8; `qe-fig-002` ×4; `qe-fig-001` ×4. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 343, 346, 359, 394, 417, 492, 535, 573. *Example:* line 346 writes `B_grid_size= 251` - a space after `=` but not before, in a keyword default that should have neither; 359 leaves a dangling comma in `self.β, self.γ, self.r, = β, γ, r`; 394 writes `c**(1-γ)/(1-γ)` with no spaces around `-` or `/` while 417 three lines later writes `(1 - delta ) / (1 + r)` - which itself has a stray space before the closing paren (E202); 493's continuation is indented 44 columns against an opening paren at 48 (E128); 535 is 88 characters (E501); 573 writes `T+1` unspaced; and the class docstring at 343 is a single-quoted string padded with spaces rather than a `"""` docstring.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 631, 652, 661, 672, 711, 742, 757, 777. *Example:* {figure} without :name:.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 101. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 32, 128, 133, 184, 301, 636. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 416, 417. *Example:* spelled-out `delta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 721, 745, 766, 799. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 4. *Lines:* 631, 652, 661, 672. *Example:* static image .png.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 128, 505. *Example:* line 128 ends mid-thought - "To purchase $B'$  next period costs $q B'$ now, or, what is equivalent." - with a full stop where the equivalent statement should follow, and that statement is then a separate bullet at 129; 505-507 is a 40-word sentence carrying two relative clauses ("take an instance of `ArellanoEconomy`, which is hard for the JIT compiler to handle, and strip it down to more basic objects, which are then passed out to jitted functions"). The rest of the prose is unusually tight - one short sentence per paragraph throughout - so these are the only two places the rule bites.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 323, 624. *Example:* the algorithm at 325-330 is numbered `1. 2. 2. 4.` in the source, so the rendered list reads 1-2-3-4 and step 4's instruction "go to step 2" lands on what the source calls step 2 but the reader sees as step 2 *or* 3 depending on which numbering they trust - and the two sub-steps at 328-329 are the part that actually repeats; and the Results section (612-678) shows four figures as static PNGs while telling the reader at 624 that "Details on how to compute the figures are reported as solutions to the exercises", so the code producing every result in the lecture sits 90 lines later inside a dropdown.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 187, 288. *Example:* the lecture contains no bold at all and exactly one italic, at 288 - "An *equilibrium* is" - which italicises a term at its point of definition, the reverse of the rule; and the definition of the lecture's central action at 187, "Defaulting means declining to repay all of its current obligations", carries no emphasis on the defined term either.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 317. *Example:* {cite} in narrative flow: 'to {cite}`'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 198. *Example:* the default/exclusion/reentry structure - pay or default at 181-196, output falling from $y$ to $h(y)$ on default, loss of market access, then reentry each period with probability $\theta$ at 200-201 - is a three-state timing diagram and is given entirely in prose bullets. Every other mechanism in the lecture gets a picture (bond price schedule, value functions, default-probability heat map, simulated series), which makes this the one unillustrated piece of the model.


## Strengths

- The three Bellman equations at 239-261 map one-to-one onto the code that implements them: `T_d` at 424 is the default value, `T_c` at 441 the repayment value, and `np.maximum(v_c, v_d)` at 434 and 459 is the max that links them, so the reader can check each operator against its equation.
- The class/JIT split is explained rather than just performed - 381-386 says why `params()` and `arrays()` hand back bare tuples, and 502-507 says why `solve` is deliberately *not* jitted.
- Every parameter default carries an inline comment naming what it is (346-356), and 622 goes further and sources one of them: `r=0.017` is the average quarterly rate on a 5-year US Treasury over 1983-2001.
- The lecture states where it departs from the paper and why: 315-321 explains that the bond price is updated at every value-function iteration rather than after convergence, that this is faster, and that the two procedures agree.
- The simulated series shades the default episodes directly on the plot (`fill_between` over `start_end_pairs`, 783-811) and fixes the seed at 779, so the exclusion periods described at 670 are visible and the figure is reproducible.

## Recommended actions

1. Promote the figure code out of the exercise solution: the four Results figures at 631, 652, 661 and 672 are static PNGs whose generating code already exists at 711-816, so the Results section can show live figures with `:name:` labels and captions and be cross-referenced with `{numref}` (qe-fig-002 ×4, qe-fig-005 ×8).
2. Fix the algorithm list at 325-330 - the source numbers it 1, 2, 2, 4, and "go to step 2" needs to name a step the reader can actually count to; the loop is over the two sub-steps at 328-329.
3. Bold the defined terms: "**Defaulting** means..." at 187 and "An **equilibrium** is" at 288 (currently italic, which the rule reserves for emphasis).
4. Brace the expectation operator at 101 - `\mathbb E` should be `\mathbb{E}` (qe-math-010 (proposed), proposed) - and rename `delta` to `δ` at 416-417 so the code matches $\delta(B',y)$ in the algebra (qe-code-002 ×2).
5. Add a small timing diagram for the pay/default/exclusion/reentry structure described at 179-201; it is the only part of the model with no picture.
6. Run the code cells through a PEP8 pass for the eight items above, and drop the four `figsize=(10, ...)` overrides at 721, 745, 766 and 799 (qe-fig-001 ×4).
7. Sweep the typos and the 7 double-space runs: "Because household are averse" (116), "operators that updated" (420), "recieved" (371), "$Y_H$" where 636 writes $y_H$ (628), "Arrelano's" (640), and recast the citation at 317 as `{cite:t}`.
