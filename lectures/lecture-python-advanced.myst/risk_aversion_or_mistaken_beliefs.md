# risk_aversion_or_mistaken_beliefs

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/risk_aversion_or_mistaken_beliefs.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-001` ×2; `qe-writing-005` ×3; `qe-writing-003` ×4, +3 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×41; `qe-math-011` (proposed) ×18; `qe-math-009` ×4. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3.5/10 | `qe-fig-006` ×19; `qe-fig-005` ×12; `qe-fig-004` ×4, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 10. *Lines:* 196, 549, 603, 657, 758, 1112, 1527, 1572, 1618, 1704. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 12. *Lines:* 188, 278, 539, 594, 646, 756, 885, 1096, 1193, 1503, …. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 19. *Lines:* 212, 213, 214, 554, 555, 612, 662, 663, 776, 1116, …. *Example:* axis label `Density`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 41. *Lines:* 150, 152, 177, 290, 298, 327, 342, 350, 382, 832, …. *Example:* bare expectation `E\bigl[`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 18. *Lines:* 104, 125, 137, 152, 164, 219, 223, 251, 329, 361, …. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 32, 52, 68, 704. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 278, 885, 1193. *Example:* static image .png.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 885, 1193, 1605. *Example:* caption of 7 words.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 944, 1179, 1241, 1264. *Example:* the lecture carries eighteen distortion symbols and two of them collide. $\bar w$ at 944 and 990 is Hansen's *constant* worst-case vector ("the worst-case mean distortion turns out to be a *constant vector*: $w_t = \bar w$"), while $\bar w_t = \bar W x_t$ at 1152 and 1179 is the *state-dependent* distortion of Szőke's feared parametric model - so the same accented letter names a constant and a function of the state, and the summary table at 1560 lists $\bar w_t$ against "Szőke's feared parametric model" with no mention that $\bar w$ meant something else 600 lines earlier. The code keeps them apart (`w_hansen` at 1524, `W_bar` at 1366); the notation does not. $\tilde\theta$ has the same problem: at 1086-1092 it is the multiplier dual to the *untilted* bound $\eta$, at 1199 the multiplier on the *tilted* constraint, and 1241 concedes the third meaning outright - "and $\tilde\theta$ as $\theta$ in the code". And $\tilde W^{sd}$, introduced at 1264 as "denoted informally by", then carries five figure legends and four prose claims (1534, 1547, 1580, 1687, 1711, 1721, 1801) as if it were defined notation, where a named matrix would do.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 703, 1194. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 951, 849, 1064, 1211. *Example:* 951 points forward and calls it backward: "We compute $\bar w$ using the multiplier formulation developed in `` {ref}`the preceding section <mult_pref_section>` ``" - but the `mult_pref_section` label is at 1047, ninety lines *later*, and 1376 refers to the same target correctly as "the multiplier preferences section". So a reader following the reference at 951 is sent to material they have not read, and the derivation at 953-969 depends on it. Second, the same content is stated twice in three places: the cumulative likelihood ratio and what it does at 849 ("These increments cumulate into a date-$t$ likelihood ratio $M_t = \prod_{s=0}^{t-1} m_{s+1}$ (with $M_0 = 1$) that converts the econometrician's probability measure into the distorted one") and again at 879 ("The cumulative likelihood ratio $M_t = \prod_{s=0}^{t-1} m_{s+1}$ converts the original probability measure into the distorted one"); the state-space pair at 826 and again at 864; the distorted dynamics at 928 and verbatim again at 1212; and the risk-sensitivity operator defined in bold at 1074 and re-defined in bold at 1094. Third, 1064-1078 is one equation split across three separate `$$` blocks with prose between them, so the rendered page shows two centred display lines that begin with `=` and `=:` and the sentence at 1074 refers to "The second line", which is a display and not a line.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 25, 305, 1681. *Example:* the assignment is right almost everywhere - definitions in bold (**likelihood ratio** 57 and 107, **twisted density** 117, **relative entropy** 172, **twisted dynamics** 357, **physical measure** 563, **risk-neutral measure** 569, **twisted beliefs** 684, **discounted entropy ball** 818, **martingale** 883, **multiplier preference** 1052, **risk-sensitivity operator** 1074, **affine-quadratic** 1235, **cross-equation restrictions** 1727) and emphasis in italic throughout - which makes the three exceptions conspicuous. The opening sentence italicises the two concepts the lecture is named for and spends the rest of the lecture defining: "how *risk aversion* and *mistaken beliefs* are confounded in asset pricing data" (25). 305 italicises the named object *volatility puzzles*, which 1669 later refers to as the Shiller "volatility puzzle" in quotation marks - a third formatting for one term. And 1681 puts *YES* in italic inside a table cell whose eleven sibling cells are plain "yes"/"no"/"maybe", using emphasis to carry information the table's own structure should carry.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 4. *Lines:* 278, 669, 885, 1533. *Example:* the two pictures that carry the entire second half of the argument - the discounted entropy ball (885-887) and the tilted entropy balls (1193-1195) - are static PNGs with no `:name:`, so 1143-1145's claim that including parametric alternatives tilts the ball cannot be pointed at with `{numref}`, and neither can be redrawn at a different $\theta$ or $\Xi$; the same is true of the state-dependent-dynamics figure at 278-280. Second, the figure at 646-666 is asked to demonstrate the lecture's central claim - 669 says "The two yield curves are identical" - by plotting a solid steelblue curve and then a dashed firebrick curve on top of it, so the blue one is invisible and the reader has to accept "identical" from a plot in which one series is hidden; a difference panel would show it. Third, the legend text in two figures is broken: 1533 and 1580 write `r"Sz\H{o}ke ..."`, and `\H{o}` is a LaTeX accent macro that matplotlib's text renderer does not interpret outside mathtext, so the legends read `Sz\H{o}ke` while every prose mention (1133, 1197, 1683, 1793) uses the unicode `Szőke`. Fourth, the lecture's two organising tables - four likelihood ratios and their roles at 61-66, three probability twisters at 1557-1561 - describe overlapping objects in different symbols ($m_{t+1}^w$ against $w_t^*$, $m_{t+1} \in \mathcal M$ against $\tilde W x_t$) and neither refers to the other.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 1353. *Example:* spelled-out `xi`.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 246. *Example:* i.i.d..


## Strengths

- The lecture is organised around one object and says so before any model appears: the table at 61-66 gives four roles for a likelihood ratio with the exact symbol used later in each ($1$, $m_{t+1}^\lambda$, $m_{t+1}^w$, $m_{t+1} \in \mathcal M$), and 68-70 gives the single log-normal form $m_{t+1}^b = \exp(-b_t^\top\varepsilon_{t+1} - \tfrac12 b_t^\top b_t)$ that every later case instantiates by choosing $b_t$ - so each new section is a choice of $b_t$ rather than a new construction.
- The twist is shown on the smallest case that carries it before being generalised: 101-127 derives $\hat\phi = m\phi \propto \exp(-\tfrac12(\varepsilon+\lambda)^\top(\varepsilon+\lambda))$ and names the mean shift, 174-180 gives relative entropy as $\tfrac12\lambda^\top\lambda$ and reads it as squared distance, and 188-223 plots all three objects side by side at $\lambda = 1.5$ with prose that says which panel is which and why the ratio up-weights negative $\varepsilon$.
- The identification result is demonstrated rather than asserted: 646-666 constructs a risk-neutral model whose transition matrix is the risk-averse model's $A_Q$ with $\Lambda$ set to zero, prices sixty maturities in both, and gets identical curves - which is exactly right, since `bond_coefficients` (431-440) reads only `self.A_Q` and `self.r_bar`, so the demonstration is a consequence of the code's structure and not a coincidence of calibration.
- The augmented-constant-state convention is stated once with all three of its consequences - $k = n-1$, only the lower block $\check C$ is ever inverted, and "stability" always means stability of $\check A$ (254-268) - and then honoured: `augment_state_space` and `augment_state` build it (471-495), `A_core`/`A_Q_core` slice it (418-419), `W_star` and `W_bar` invert only `C[1:, :]` (742, 1366), and 532 asserts the distorted block is stable before anything is priced.
- The three exercises ask for exactly the derivations the main text skips, and the solutions do them: lr_exercise_2 swaps the order of summation, defines $S = \sum \beta^{s+1}E[x_s]$, solves for it and differentiates to reach $\theta\bar w = \tfrac{\beta}{1-\beta}G^\top + \beta C^\top v$ (1009-1043), and lr_exercise_3 verifies the affine-quadratic guess term by term (1436-1458) before deriving the first-order condition that the code implements verbatim at 1307-1310.
- The `T_operator` (1097-1103) subtracts the running maximum before exponentiating, so the log-sum-exp stays finite across the four decades of $\theta$ that the figure sweeps at 1109 - a detail that matters precisely because the risk-sensitivity operator is defined by an exponential tilt and the figure's whole point is the $\theta \to 0$ end.
- The lecture ends by scoring itself against data: 1603-1661 plots five FRED yield series with NBER recession shading in a properly named and captioned figure, 1663-1672 lists the five regularities any theory has to reproduce (including the Shiller volatility puzzle and what it implies about state-dependent risk prices), and 1676-1681 puts four models against three of those facts in a table.
- The eight entries of "Related lectures" (1828-1837) each say what the linked lecture contributes here - the discrete-state counterpart, the martingale properties of the device, the decision-theoretic foundations, the nonparametric bound - rather than listing titles.

## Recommended actions

1. Replace `Sz\H{o}ke` with the unicode `Szőke` in the two matplotlib label strings at 1533 and 1580: `\H{o}` is a LaTeX accent macro that matplotlib does not interpret in label text, so both figure legends render the macro literally while every prose mention uses the correct character.
2. Fix the cross-reference at 951: it calls `mult_pref_section` "the preceding section" when that label is at 1047, ninety lines later - either move the multiplier-preferences material before its first use at 951, or reword as 1376 already does.
3. Give $\bar w$ (Hansen's constant distortion, 944 and 990) and $\bar w_t = \bar W x_t$ (the feared parametric model's state-dependent distortion, 1152 and 1179) distinct symbols, as the code already does with `w_hansen` and `W_bar`, and say at 1199 whether $\tilde\theta$ there is the same multiplier as at 1086.
4. Lowercase the 19 axis labels (qe-fig-006: 212-214, 554-555, 612, 662-663, 776, 1116-1117, 1540-1541, 1587, 1645, 1655-1656) - the lecture already writes lowercase units inside them, so only the first word changes.
5. Sweep the 18 `\mathcal{N}` to plain `N` (qe-math-011, proposed: 104, 125, 137, 152, 164, 219, 223, 251, 329, 361, 365, 372, 566, 574, 823, 925, 1574, 1593) and the 34 bare expectations to `\mathbb{E}` (qe-math-010, proposed: 150, 152, 290, 832, 856, 870, 876, 909, 912, 917 and on), which will also settle whether $\mathcal M$ at 66 should keep its decoration.
6. Generate the three static PNGs (278, 885, 1193) from code, or at minimum give all three `:name:` labels so 1143-1145 and 1501 can point at them with `{numref}` - the two entropy-ball figures are the visual argument of the second half of the lecture.
7. Delete the duplicated statements: the cumulative likelihood ratio at 879 (already given at 849), the state-space pair at 864 (826), the distorted dynamics at 1212 (928), and the second definition of the risk-sensitivity operator at 1094 (1074).
8. Merge the three-part display at 1064-1078 into one `aligned` block so the page does not show two centred lines beginning with `=` and `=:`, and so 1074 need not refer to "The second line".
9. Add a difference panel to the identification figure at 657-666, where the dashed red curve currently hides the solid blue one that 669 asks the reader to see is identical; and finish the small items - "i.i.d." at 246 (qe-writing-009 (proposed)), the ten `figsize=` calls, the twelve figures without `mystnb` names, and the typos "countercyclical risk price" (37), "perpective" (37) and "Especial LRR parametric worry" (1560).
