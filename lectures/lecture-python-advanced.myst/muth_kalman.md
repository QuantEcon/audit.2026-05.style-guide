# muth_kalman

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/muth_kalman.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-005` ×4; `qe-writing-003` ×3; `qe-writing-001` ×1, +2 more. |
| Math         | 6/10  | `qe-math-010` (proposed) ×2; `qe-math-011` (proposed) ×1; `qe-math-009` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×3; `qe-fig-006` ×3; `qe-fig-005` ×4, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 280, 281, 301, 302, 319, 350, 352. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 144, 145. *Example:* bare expectation `E [`.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 284, 304, 321. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 278, 299, 317, 339. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 283, 305, 322. *Example:* axis label `Time`.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 97. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 267, 288. *Example:* the filtered state is written `\hat`` {x_t}` at 267 and 288, which sets the hat over the whole subscripted symbol, while every other occurrence - 144, 195, 213, 234, 274, 290 - uses the simpler and correct ` ``\hat x_t`. Related, 129 writes `\epsilon_{2t}` where the rest of the lecture (104, 116, 123, 207, 213, 220) writes `\epsilon_{2,t}`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 116. *Example:* decorated distribution `{\mathcal N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 314. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 78, 140, 369. *Example:* the lecture's punchline is never stated. Friedman's smoothing parameter is $K$ in `` {eq}`expectations` `` (65) and the Kalman gain is also called $K$ from 140 onwards, but nothing says the two are deliberately the same object - which is the entire content of "reverse engineering a la Muth". The reader is left to infer it from 362-363 ("the **autoregressive coefficients** decline geometrically with decay rate $(1-K)$") and the bare `print` at 369. Second, the horizon index slips: 68-69 defines $y^*_{t+i,t}$ as a forecast "over horizon $i$", and 78-79 then says the scheme "gives linear least forecasts of $y_{t+j}$ for any horizon $i$" - $j$ is already in use at 65 as the summation index over past $y$. Third, the lecture ends on the code cell at 368-369 with no closing sentence after "These are exactly the target outcomes that Muth (1960) aimed to reverse engineer" (365-366).
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 84, 85, 135, 162. *Example:* bold is used for emphasis and italic for the definition, i.e. both backwards. 84-85 sets **question** and **answer** in bold purely for contrastive emphasis ("for what optimal forecasting **question** is Milton Friedman's adaptive expectation scheme the **answer**"), where the rule asks for italic. Conversely the term the lecture actually defines - the time-invariant *innovations representation*, introduced at 135 and named again at 149 - is italicised rather than bolded, and the same term appears a third time at 162 in plain double quotes ("innovations representation"), so one object carries three different typographic treatments. `*permanent income*` at 291 is the same case: a named concept in italic.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 72, 155. *Example:* 2 spaces.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 349. *Example:* the MA/AR figure (349-355) is the one that carries the result the lecture is building to, and it is the only figure with no title on either panel and no axis label at all - the horizontal axis is the lag $j$ and nothing says so, where the three earlier figures at 278-285, 299-306 and 317-323 each set a title and an x-label. It also stops short of the claim in the prose: 362-363 says the autoregressive coefficients "decline geometrically with decay rate $(1-K)$", which could be shown by overlaying $(1-K)^j$ on the bottom panel instead of asserted and then printed as a number at 369.


## Strengths

- The lecture names the question before answering it: 81-85 states in one sentence what Muth was actually asking ("for what optimal forecasting **question** is Milton Friedman's adaptive expectation scheme the **answer**"), and 87-95 then says exactly which tool is being swapped in for Muth's, with 90-92 pointing at the two classical-methods lectures for the original route.
- The two `{note}` admonitions at 121-126 and 147-153 carry the single property that separates the two representations - that neither $\epsilon_{1,t}$ nor $\epsilon_{2,t}$ lies in the space spanned by square-summable combinations of $y_t, y_{t-1},\ldots$, while $a_t$ does - so the pivot of the whole argument sits in two boxes instead of being buried in a paragraph.
- The stacking trick is derived in prose before it is coded: 204-215 substitutes $a_t = x_t + \sigma_y \epsilon_{2,t} - \hat x_t$ into the innovations recursion, 219-230 writes out the resulting $3\times 3$ system, and the code comment at 241-242 says "Use stacking trick above", so the matrix literal at 243-250 can be read straight off the display.
- Every figure is bracketed by a sentence saying what to look for and one saying what was seen - 274-276 then 288-291, 295-297 then 309-310 - so no plot is left for the reader to interpret unaided.
- The scalar extraction at 181-182 (`S1, K1 = S1.item(), K1.item()`) with its comment, together with `np.set_printoptions(linewidth=120, precision=4, suppress=True)` at 53, keeps the reported gain and conditional variance at 262-263 readable as plain numbers rather than nested arrays.

## Recommended actions

1. State the identification the lecture exists to make: say at 140, where the Kalman gain $K$ first appears, that it is the same $K$ as Friedman's smoothing parameter in `` {eq}`expectations` ``, and close the lecture after 369 with the sentence that this is what Muth reverse-engineered.
2. Fix the three notation slips: the horizon index at 78-79 ($y_{t+j}$ "for any horizon $i$" - $j$ is already the summation index at 65), `\epsilon_{2t}` at 129, and `\hat{x_t}` at 267 and 288.
3. Give the MA/AR figure at 349-355 a title per panel and an x-label naming the lag, and overlay $(1-K)^j$ on the bottom panel so the geometric-decay claim at 362-363 is visible rather than only printed.
4. Correct "consumer's forecast their future disposable income" at 59 to "consumers forecast", and drop the redundant "(1956)" at 58 which repeats what `` {cite}`Friedman1956` `` already renders.
5. Settle the emphasis convention: italicise **question**/**answer** at 84-85, bold the definition of the *innovations representation* at 135, and use that same form at 149 and 162 instead of italic and quotes.
6. Sweep the figures: `lw=2` on the seven `plot` calls (280, 281, 301, 302, 319, 350, 352), lowercase the axis labels at 283, 305 and 322, and move the `set_title` calls at 284, 304 and 321 into `mystnb: figure: caption/name` metadata on the four figure cells (278, 299, 317, 339).
7. Replace the raw URL at 97 with a `{doc}` cross-reference and write the two bare expectations at 144-145 as `\mathbb{E}`.
