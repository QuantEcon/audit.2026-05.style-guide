# geom_series

- **Series:** lecture-python-intro
- **File:** `lectures/geom_series.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×3; `qe-writing-001` ×2; `qe-writing-005` ×4, +4 more. |
| Math         | 8.5/10 | `qe-math-002` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-006` ×9; `qe-fig-005` ×4; `qe-fig-004` ×4, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 51, 700, 761, 790, 909, 949. *Example:* `#set default figure size` at 51 has no space after the hash; the `funcs = [` list at 699-702 indents its continuation lines to 8 columns instead of the bracket, and strands the explanatory comment after the closing bracket at 702; `T=np.arange(0, T_max+1)` at 761 omits the spaces around `=` that line 693 has; `plt.figure(figsize = [16, 5])` at 790 adds spaces around a keyword `=`, as does `ax.legend(loc ="lower right")` at 949; `fig,ax = plt.subplots()` at 909 drops the space after the comma.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 51, 790, 932, 994, 1113. *Example:* style override.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 709, 736, 758, 807, 1055, 1056, 1126, 1190, 1191. *Example:* axis label `Present Value, $p_0$`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 733, 734, 766, 887, 915, 940, 943, 997, 1052, 1115, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 616. *Example:* `^T` transpose in `G^{T}`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 118, 268, 438. *Example:* H2 Title Case: 'Example: The Money Multiplier in Fractional Reserve Banking' (Money, Multiplier, Fractional, Reserve).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 948. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 681, 720, 782, 900. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 983, 1041, 1103, 1160. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 110, 459. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 166, 432, 848, 852. *Example:* lines 166-170 run to 53 words, appending a semicolon clause and a parenthesis about pre-1914 bank notes to an already complete sentence; lines 432-436 spend 43 words restating what a multiplier is right after naming the **government expenditures multiplier**; and the two SymPy conclusions at 848-850 and 852-853 are circular as written - "we can see that for $\partial p_0/\partial r<0$ as long as $r>g$, $r>0$ and $g>0$ and $x_0$ is positive, so $\partial p_0/\partial r$ will always be negative" assumes its own conclusion and is ungrammatical at the opening "for".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 857, 869. *Example:* the dynamic Keynesian model is derived at 342-436 but not plotted until 861, with the whole interest-rate, asset-pricing and SymPy material (438-853) in between - the lecture has to signpost the gap with a "Back to the Keynesian multiplier" heading; worse, `calculate_y` at 869-874 and the equilibrium line at 889 include a government-spending term `g` with `g_0 = 0.3`, which the derivation at 379-409 does not contain and which the introducing sentence at 857-859 does not mention: the code silently implements the generalisation of Remark 2 (422-436) while the prose describes the simple model.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 127, 132, 140, 310. *Example:* definitions italicised and claims bolded, in both directions: "a *deposit* is a balance in a checking or savings account..." at 127 and "a *deposit receipt* was a *bank note* that the bank promised to convert into gold or silver" at 132 are definitions in italics - and *deposit receipt* is the same term the lecture bolds at 121; "- *exogenous* means *determined outside this model*" at 310 is a definition in italics; while "**banks create money**" at 140 and "**balance sheets balance**" at 154 are bolded assertions, not defined terms.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 118. *Example:* the money multiplier section (118-266) is the lecture's most fully derived example - eight labelled equations ending in $\sum_{i=0}^\infty (1-r)^i D_0 = D_0/r$ - and it has no figure, in a lecture with eight figures elsewhere; the partial sums of exactly that series are finally plotted in exercise `geom_ex2` at 1041-1059, which shows what the section itself is missing.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 88. *Example:* 2 spaces.


## Strengths

- Every one of the nine labelled equations is cited later with `{eq}` - `infinite` (83) at 88 and 145, `balance` and `reserves` (157, 175) at 213, `deposits` and `fraction` (190, 216) at 224, `geomseries` (233) at 238, `sumdeposits` (249) at 260, `geom1` (482) at 495 and 503, `geom2` (490) at 498 and 528 - so no label is dead weight and no equation is referred to by number in prose.
- All seven figures in the lecture body carry `mystnb: figure:` metadata with a caption and a `name` (681, 720, 748, 782, 861, 900, 925).
- Discounting is developed through units rather than assertion: the units of $R$ are fixed at 459-462 and then propagated to $R^{-1}$, $R^{-2}$ and $R^{-j}$ at 535-538, which is what makes the claim at 540-541 obvious instead of memorised.
- The lecture's thesis - that every "multiplier" in elementary economics is the sum of a geometric series - is stated at 39 and then discharged three times: $1/r$ at 260, $1/(1-b)$ at 320 and 335, and the government-expenditures multiplier at 432.
- The four exercises each check a formula from the lecture numerically rather than restating it: partial sums against $1/(1-c)$ with a log-scale error panel (983-1013), cumulative deposits against $D_0/r$ (1041-1065), the Gordon approximation against the exact lease value with the closed-form error $100r/(1+r)$ (1103-1131), and multiplier size against convergence speed (1160-1198).

## Recommended actions

1. Lower-case the three Title Case section headings at 118, 268 and 438, and the nine capitalised axis labels at 709, 736, 758, 807, 1055, 1056, 1126, 1190, 1191 - "Present Value, $p_0$", "$T$ Periods Ahead", "Number of banks $N$" and the rest (qe-writing-006 x3, qe-fig-006 x9).
2. Reconcile the Keynesian code with the Keynesian text: either add government spending to the derivation before line 857, or drop `g` from `calculate_y` (869) and from the equilibrium line at 889. While there, stop reusing the name `g` for the lease growth rate (694), a SymPy symbol (827) and government spending (869) in one file.
3. Set an explicit `lw` on the 13 default-width line plots (733, 734, 766, 887, 915, 940, 943, 997, 1052, 1115, 1116, 1122, 1189) and remove the 5 figure-size overrides, starting with the global `plt.rcParams["figure.figsize"] = (11, 5)` at 51 (qe-fig-008 x13, qe-fig-001 x5).
4. Add `mystnb: figure: caption/name` metadata to the four solution-cell figures at 983, 1041, 1103 and 1160 - the seven body figures already have it (qe-fig-005 x4).
5. Fix the emphasis: bold **deposit** (127), **bank note** (132) and **exogenous** (310) where they are defined, and drop the bold from the assertions at 140 and 154.
6. Rewrite the two SymPy conclusions at 848-853 so they state the sign of each derivative and the condition that delivers it, instead of asserting the conclusion as its own premise; and split the 53-word sentence at 166-170.
7. Give the money multiplier section a figure - the cumulative-deposits plot from `geom_ex2` (1041-1059) belongs in the body at around line 260 - and shorten the four-step Taylor expansion at 616-646, whose two single-line displays at 616 and 640 run past 200 and 300 characters.
