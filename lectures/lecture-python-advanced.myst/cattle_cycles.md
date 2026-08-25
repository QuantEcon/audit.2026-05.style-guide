# cattle_cycles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cattle_cycles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-002` ×2; `qe-writing-005` ×1; `qe-writing-007` ×2, +1 more. |
| Math         | 7/10  | `qe-math-003` ×10. |
| Code         | 9/10  | `qe-code-001` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×5; `qe-fig-005` ×3; `qe-fig-008` ×11, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 337, 358, 364, 391, 395. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 335, 355, 356, 357, 361, 362, 363, 389, 390, 393, …. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 10. *Lines:* 127, 132, 144, 149, 154, 159, 171, 176, 181, 186. *Example:* array used as matrix.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 354, 388. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 331, 347, 384. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 27, 206, 325. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 26, 100. *Example:* line 100-104 is a 44-word remark with an inverted verb phrase - "included for technical reasons to make well posed and well behaved the linear quadratic dynamic programming problem solved by the fictitious planner who in effect chooses equilibrium quantities and shadow prices"; lines 26-27 open the lecture with a 34-word triple-nested sentence ("another member of a suite of lectures that use the quantecon DLE class to instantiate models within the {cite}`HS2013` class of models described in detail in ...").
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 56, 100. *Example:* the "time-to-grow" cohort structure is the whole point of the model - x_t = (1-delta)x_{t-1} + g x_{t-3} - c_t at 73-75 and y_t = x_t + g x_{t-1} + g x_{t-2} at 83-85 describe a calf/yearling/adult pipeline with a three-year lag - and it is only ever written algebraically; a small flow diagram of the three cohorts would carry it. Separately, the important side note at 100 is typeset as bold **Remark** followed by running prose instead of a `{note}` admonition.

### Low severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 1. *Lines:* 229. *Example:* line 229 `[0, 0, 1,0]` omits the space after the third comma, breaking the alignment of the surrounding literal. The column padding in the other matrix literals (234-238, 240-242, 257-265, 291-302) is deliberate matrix-like alignment and falls under the rule's own mathematical-notation exception, so it is not counted.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 100. *Example:* **Remark** at line 100 uses bold as a paragraph label rather than to mark a defined term; nothing in the lecture is bolded at its point of definition (the breeding stock and total stock are introduced in plain text at 68-69).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 38. *Example:* 2 spaces.


## Strengths

- Every code variable is the Unicode Greek letter used in the algebra - `ϕc`, `ϕg`, `ϕi`, `γ`, `δk`, `θk`, `ρ1`-`ρ3`, `β`, `πh` - so the code cells at 224-272 can be read straight off the matrix definitions at 143-189.
- The HS2013 mapping is given in full (Preferences 114-119, Technology 123-163, Information 167-195): every one of Δ_k, Θ_k, Φ_c, Φ_g, Φ_i, Γ, A_22, C_2, U_b, U_d is written out, so the reader can check the code against the paper rather than trusting it.
- The three-persistence experiment is set up once (info1/info2/info3 at 286-304, for ρ_3 = 0.6, 1, 0) and then reused for both replicated figures, and the prose at 369-376 reads the economics of each case off the plot instead of just displaying it.
- The two figures are explicitly labelled as replications of Figures 3 and 4 of Rosen, Murphy and Scheinkman (341, 378), which makes the lecture checkable against its source.
- The namedtuple cell carries a comment saying why namedtuples were chosen (198-199) rather than leaving the reader to guess.

## Recommended actions

1. Convert the ten `\left[ {\begin{array}...} \right]` matrices at 127, 132, 144, 149, 154, 159, 171, 176, 181 and 186 to `bmatrix` - the largest single fix in this lecture (qe-math-003, 10 occurrences).
2. Move the five embedded `set_title` calls (337, 358, 364, 391, 395) into figure captions and add `mystnb: figure: caption/name` metadata to the three plotting cells at 331, 347 and 384, so the figures can be captioned and cross-referenced (qe-fig-003 ×5, qe-fig-005 ×3).
3. Fix the notation slips in the mapping section: line 115 sets $\Pi = \alpha_1^{-1/2}$ but the demand curve at 106 and the code at 213 use $a_1$, and lines 192-193 write $\Psi_1, \Psi_2, \Psi_3$ for the small quadratic-cost parameters that 93 and 100 call $\psi_1, \psi_2, \psi_3$.
4. Set `lw=2` on the eleven `plot` calls (335, 355-357, 361-363, 389, 390, 393, 394) and drop the `figsize=(12, 4)` overrides at 354 and 388 (qe-fig-008 ×11, qe-fig-001 ×2).
5. Rewrite the 44-word remark at 100 as two sentences inside a `{note}` admonition, and fix "Demand for beef is government by" at 106 (should read "governed").
6. Recast the citations that stand as the grammatical subject - 27, 206, 325 and also 341 and 378 - as `{cite:t}` (qe-ref-001).
7. Add a figure showing the calf-yearling-adult pipeline, and close the loop on the lecture's own claim: the closing paragraph at 399-402 refers back to "the first graph of this lecture", which is exactly the cross-reference `{numref}` plus figure names would make clickable.
