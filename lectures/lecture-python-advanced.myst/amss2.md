# amss2

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/amss2.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-005` ×10; `qe-writing-002` ×5; `qe-writing-003` ×3, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×2; `qe-fig-005` ×2; `qe-fig-008` ×2, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 359, 374, 400, 408, 518, 689, 691, 693, 738. *Example:* five lambdas are bound to names where PEP8 asks for `def` - `eq` (359), `τ` (689), `R_s` (691), `X_s` (693) - and 359 and 691 additionally use a backslash continuation *inside* parentheses that already continue the expression; 408 puts a double space before the `+` in `u.Uc(c0, 1)  + u.Un(...)` and continues with two more backslashes; 374 writes `np.eye((2))` with a redundant inner paren; 400 writes `u.G[s-1]` and 738 `1/den2` unspaced while the surrounding lines space every operator; 518 binds the loop variable `id`, shadowing the builtin.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 27, 44, 66, 70, 111. *Example:* lines 32-33, 41-42 and 44-45 state one claim three times in a row, the third opening "Another way to say this is that" - so the paragraph pays for the same idea three times; 27 is a 40-word sentence with a double `whether ... or whether` construction; 66 is a 30-word bullet that uses "gross" four times, including the compound "gross-of-gross-interest-payments"; 70 is a 33-word bullet that ends "restricted to exchange only risk-free debt  debt"; 111-112 is a 44-word bullet holding a parenthetical aside, a starting condition and a comparison.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 10. *Lines:* 58, 59, 61, 73, 111, 113, 128, 302, 474, 486. *Example:* bold carries plain emphasis rather than definition in ten places: **constant over time** (58), **to** (59), **particular** / **loans** / **never** (61), **assets** (73), **weak** (111), **assets** / **constant** (113), **identical** (128 and 474), **same** (302 and 486). The rule assigns italic to all of these; the lecture does bold its genuine terms correctly (**measurability constraints** at 44, **fiscal risk** at 572), so the two uses are running together.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 79. *Lines:* 26, 27, 30, 32, 33, 38, 41, 42, 45, 49, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 462, 516. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 466, 520. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 432, 507. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 465, 519. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 95, 562. *Example:* `` {cite} `` in narrative flow: 'in `` {cite} ``'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 337, 528, 686. *Example:* line 337 reads "**Step 6:** Put steps 2 through 6 in a function minimizer" - Step 6 cannot contain itself, and the minimiser wraps steps 2 through 5; the "Remarks about long simulation" section at 528-539 ends by announcing "We now describe how to find such an initial level of government debt", but that derivation is 230 lines *behind* the reader at 297-423, so the section points forward to something already done; and 686 drops in `c = [0.940580824225584, 0.8943592757759343]` as a hard-coded literal with no statement of where the two numbers came from, which breaks the chain from the reverse-engineering cells above (the comment on the next line, `n = c + g  # Total population`, also mislabels labor supply as population).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 313, 713. *Example:* the lecture's punchline is delivered as bare scalars: 713 prints `bhat, b_bar`, 719 prints their difference and 727 prints `Jmin`, and the reader is told at 722 that the approximation does "a remarkably good job" - all of which the existing long-simulation debt panel at 516 could show directly by drawing $\hat b$ as a horizontal line against the converging AMSS path. The seven-step reverse-engineering algorithm at 313-340, which nests a two-equation solve inside a scalar minimisation inside a final joint solve, is also carried by prose alone where a small flow diagram would carry it.

### Low severity
_None found._


## Strengths

- The reverse-engineered $b_0$ is verified two independent ways: the six-panel short simulation at 432-471 shows the Lucas-Stokey and AMSS paths coinciding, and 704-728 shows the BEGS approximation $\hat b$ matching $\bar b$ with the fiscal-risk criterion $J({\mathcal B}^*)$ evaluating to machine zero.
- The `## Logical flow of lecture` roadmap at 117-129 tells the reader the six moves of the argument in order before any of them happens, including where the reverse-engineering step will land.
- The change of variables into BEGS notation is given as one display (552-560) mapping all four of their objects $B_t, {\mathcal B}_t, {\mathcal R}_t, {\mathcal X}_t$ onto the lecture's own $b_t, R_t, \tau_t$, which is what makes the calligraphic letters informative rather than decorative.
- The convergence claim is closed numerically as well as visually: the mean-reversion speed at 737-739 and the implied time to get within one percent at 745-746 are computed from the BEGS formula and then compared against the 1400-2000 periods actually seen in the long simulation (501, 749-750).
- Most labelled equations are genuinely cited later - `TS_barg10a` and `TS_barg11b` at 223, `eqn_AMSS2_10` at 182 and 340, `amss2_TS_barg10` at 241 and 315, `eq_fiscal_risk` at 572, 602 and 655, `prelim_formula` at 590, 604 and 653, `key_formula` at 633 and 651, `eqn_Jcriterion` at 732.

## Recommended actions

1. Draw the result instead of printing it: overlay $\hat b$ (and, if useful, $\bar b$) on the government-debt panel of the long simulation at 516, so the claim at 722 that the approximation is "remarkably good" is visible rather than inferred from `bhat - b_bar` at 719.
2. Strip the 79 runs of double spaces (qe-writing-008) and cut the two redundant restatements at 41-42 and 44-45, which repeat 32-33.
3. Fix the internal contradictions: "steps 2 through 6" at 337 should be 2 through 5; `T = 2000  # Set T to 200 periods` at 508; "risk-free debt  debt" at 70; the dropped minus sign at 501 (the limit is about -1.07, per 499); the stray colon in the heading at 425; and the comment at 688 that calls labor supply "total population".
4. Replace the hard-coded `c = [0.940580824225584, 0.8943592757759343]` at 686 with the values the earlier cells compute (`c1, c2` from 368), so the BEGS section is reproducible from the reverse-engineering section rather than pasted from it.
5. Move or rewrite "Remarks about long simulation" (528-539): as written it closes by promising a derivation the reader met 230 lines earlier at 297-423.
6. Write expectations and moments the way the guide asks - $\mathbb{E}$ for `E_t` and `E_{t-1}` (554, 557, 609, 619) and $\mathbb{V}$ / `\operatorname{cov}` for `{\rm var}` and `{\rm cov}` (585, 598, 619, 632-635, 646-647, 660) - and convert the ten bold emphases listed above to italic.
7. Clean the figures and the code: `mystnb: figure: caption/name` on the two plotting cells (432, 507), `set(title=)` at 466 and 520 moved into those captions, `lw=2` at 465 and 519, `figsize` dropped at 462 and 516; turn the five named lambdas into `def`s, replace the three `global` statements at 365, 366 and 376 with return values, and rename `bstar`/`bhat`/`den2`/`speedrever`/`ttime` to readable names.
