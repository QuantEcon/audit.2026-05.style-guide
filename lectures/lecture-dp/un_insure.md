# un_insure

- **Series:** lecture-dp
- **File:** `lectures/un_insure.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-002` ×8; `qe-writing-005` ×3; `qe-writing-003` ×3, +3 more. |
| Math         | 9.5/10 | `qe-math-009` ×4. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×2; `qe-fig-006` ×3; `qe-fig-005` ×1, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 512, 554, 744, 759, 836. *Example:* the Python here is a class that was taken apart and not put back together. (1) `class params_instance:` (512) is snake_case where PEP8 asks for CapWords, and it holds only `__init__`. (2) Eight module-level functions take `self` as their first parameter without being methods of anything - `u(self, c)` (554), `u_inv` (558), `Vu_error` (592), `r_error` (609), `calc_c` (671), `calc_a` (682), `iterate_C` (711), `solve_incomplete_info_model` (758) - and are then called as `u(self, 0)` (597) and `solve_incomplete_info_model(params, ...)` (794), so `self` is sometimes an instance and sometimes a parameter named `self` inside another such function. (3) `iterate_C` reads `Vu_min` and `Vu_max` (744) from module scope, and both are defined 45 lines *later* at 789-790, so the function is only callable after a cell further down the page has run; every other quantity it needs comes in through `self`. (4) `iter = 0` (759) shadows the builtin, and `C_init = np.ones(self.n_grid) * 0` (762) is an array of zeros written as ones times zero, with `C_new2` and `V_star2` allocated at 722-723 and never used. (5) `fontSize` (836) is camelCase, and the three docstrings at 672, 683 and 712 use `'''` where the rest of the corpus uses `"""`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 837, 838, 839, 840, 841, 842, 844. *Example:* style override.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 846, 848, 850, 857, 858, 859. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 8. *Lines:* 36, 57, 66, 411, 531, 535, 641, 890. *Example:* three kinds of debris, all visible to a reader. (a) Conversion leftovers: `%\EQN hugo1` at 36 is a LaTeX macro line from the source manuscript, the `{code-cell} ipython3` at 411-413 is empty and will render as an empty input cell in the middle of the theory, and six stray `+++` cell separators sit at 535, 643, 647, 657, 780 and 806 while the other forty cell boundaries in the file have none. (b) One sentence that repeats its predecessor: 'An unemployed worker searches with effort $a$ and with probability $p(a)$ receives a permanent job' (49-52) is followed six lines later by 'The probability of finding a job  is $p(a)$' (57-58). (c) Five sentences that do not parse: 'we'll use assume the same $p(a)$ function' (66), 'an observerd hazard rate --  the probability that an unemployed worker finds a job each  --  in US data' (531, missing the period unit), 'Now that we have calibrated our the parameter $r$' (641), 'search effort rise as the duration' (890), and the missing word at 395 counted above.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 107. *Lines:* 17, 20, 22, 30, 58, 62, 66, 105, 115, 148, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 854, 863. *Example:* plt.title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 852, 861, 862. *Example:* axis label `Replacement ratio (c/w)`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 111, 224, 471, 702. *Example:* four notations with a simpler spelling, three of them TeX primitives the rest of the corpus does not use. (1) Division is written `{u(w) \over (1-\beta)}` (111), `{1 \over u'(c)}` (224), `{1 \over \beta p'(a)}` (225, 364), `{p''(a) \over p'(a)}` (365-366), `{1 \over \beta (V^e - V^u)}` (471), `{\log[\ldots] \over r}` (479) - `\over` throughout, where `\frac` is what the rest of the series uses. (2) The two `aligned` blocks separate their rows with `\cr` (224-227, 363-367) rather than `\\`. (3) The autarky value is `V_{\rm aut}` in eleven places (137, 142, 145, 166, 266, 426, 810, 868, 870, 875) - `\rm` is a font switch, not a text-mode command, so `V_{\mathrm{aut}}` or `V_{\text{aut}}` is the correct spelling of the same thing. (4) The inverse of the derivative is written `p'^{-1}` (471) - a prime carrying its own superscript - where the sibling lecture os_egm writes `(u')^{-1}`; and the two grids at 700-703 are named `$grid_V$` and `$Vu_{grid}$`, one with the word as the base and one with the word as the subscript, in the same sentence.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 395, 700, 705. *Example:* (1) Line 395 is missing its subject: 'The  of benefits on the duration of unemployment is  designed to provide the worker an incentive to search' - the sentence that states the lecture's central conclusion has a word deleted (the *dependence*, or the *decline*), and the double space marks where. (2) The algorithm at 700 says 'Fix a set of grid points $grid_V$ for $V$ and $Vu_{grid}$ for $V^u$', two grids, and the code builds one: `Vu_grid` (791) is passed as both, with `calc_c(self, Vu_grid[Vu_i], Vu_grid[V_i], a_i)` at 732 indexing the same array for the promised value and the continuation value. Either the algorithm should say one grid serves both, or the code should build the second. (3) Step 6 of the same algorithm (705) writes the iteration as $C_{j+1}(V) = \min \{c - \beta [1 - p(a)] C_j(V)\}$ - a minus where `` {eq}`eq:hugo23` `` (489) and the code (734, `c_i + β * (1 - p(a_i, r)) * C_old[Vu_i]`) both have a plus, and $C_j(V)$ where both have $C_j(V^u)$.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 755. *Example:* mid-sentence 'Algorithm'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 268, 269, 272. *Example:* bold is used for emphasis in the one passage where the contrast matters most: 'It **increases** the unemployed worker's consumption $c$ and **decreases** his search effort $a$' (268-269) and 'The prescribed search effort is **higher** than what the worker would choose' (272). The rule reserves bold for definitions, and this file already does that correctly for **insurance agency** / **planner** (78) and **carrot-and-stick** (893, then **carrot** at 896 and **stick** at 899). It also already uses italics for exactly this job elsewhere - *lowering* (296), *both* and *and* (312-313) - so the three bolds are out of step with the file's own two conventions.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 835. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 317. *Example:* `` {cite} `` in narrative flow: 'Following  `` {cite} ``'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 794. *Example:* the lecture's central theoretical result is one plot away from the data it already has and is never drawn. The whole private-information section turns on $V^u < V$ (383) against $V^u = V$ under full information (235), and `solve_incomplete_info_model` returns `V_star` - the continuation-value policy on `Vu_grid` - at 794. Plotting `V_star` against `Vu_grid` with the 45-degree line would show the strict inequality directly, and overlaying the full-information case would show the contrast the theory spends 150 lines establishing. `C_star`, the cost function whose convexity every step of the argument depends on (178-181, 234-235, 341, 383), is also computed and never shown. The file's single figure (835-864) plots the two derived policies, so 780 lines of theory rest on nothing visual.


## Strengths

- The argument is staged as three benchmarks, each ending with the result that forces the next: autarky (94-155) gives $V_{\rm aut}$ as the reservation value, full information (157-254) shows consumption and effort are fully smoothed within the spell, and '### Incentive problem' (256-313) then shows why the agency cannot simply hand over that consumption and let the worker choose effort - 'Here is why' (263) followed by the actual argument.
- That argument is carried out in inequalities rather than asserted: the full-information solution implies $[\beta p'(a)]^{-1} > (V^e - V^u)$ (276-278), the worker's own first-order condition `` {eq}`eq:hugo4` `` requires equality when $a>0$ (283-284), and the lecture then says which way the worker would move $a$ to restore it and what happens if equality cannot be reached before $a$ hits zero (289-305).
- Individual equations inside multi-row `aligned` displays are referred to by position, so a three-equation block stays navigable: 'The first equation of `` {eq}`eq:hugo7` `` determines $c$, and the second equation of `` {eq}`eq:hugo7` `` determines $a$' (242-244), and 'the second equality in the second equation in `` {eq}`eq:hugo8` ``' (371).
- The calibration is a real one, with a target, a method and a check: $r$ is chosen so that the autarky hazard rate is 0.1 to match US data (530-533), solved by `brentq` (632), and then verified by printing `p(a_aut, r_calibrated)` (638) rather than being assumed to have worked.
- The reduction that makes the numerical problem tractable is derived step by step - invert the promise-keeping constraint for $c$ (455-466), invert the incentive constraint for $a$ (468-480), specialise to Hopenhayn and Nicolini's $p(a)$ (475-480) - leaving a minimization over the single variable $V^u$ (450-453), which is exactly what the code does.
- The grid bounds are model-derived rather than chosen: the lower bound is $V_{\rm aut}$ and the upper bound comes from ruling out zero search effort (420-448), and the code uses precisely those two expressions (789-790).
- The interpretation section states the mechanism and then explicitly rules out the wrong reading of it: the declining benefit schedule exists 'in order to provide an unemployed worker with proper incentives, not to punish an unlucky worker who has been unemployed for a long time' (904-907), and 909-919 spells out that the planner believes the long-unemployed worker is unlucky rather than delinquent.

## Recommended actions

1. Put the eight `self`-taking functions back inside `params_instance` as methods (554-775), or rename the parameter to `params`; either way pass `Vu_min`/`Vu_max` into `iterate_C` instead of reading them from globals defined 45 lines later (744 versus 789-790), rename the class to `ParamsInstance`, rename `iter` (759), drop the unused `C_new2`/`V_star2` (722-723), write `np.zeros(self.n_grid)` at 762, and rename `fontSize` (836).
2. Repair the sentence at 395 (the *dependence* of benefits on duration), and make the algorithm at 698-705 agree with the code: one grid or two (700 versus 791), and `+ \beta [1-p(a)] C_j(V^u)` in step 6 rather than `- \beta [1-p(a)] C_j(V)`.
3. Add the figure the theory needs: `V_star` against `Vu_grid` with a 45-degree line, showing $V^u < V$ (383), and the computed cost function `C_star` whose convexity the argument repeatedly invokes.
4. Clear the conversion debris: delete `%\EQN hugo1` (36), the empty code cell (411-413) and the six orphan `+++` separators (535, 643, 647, 657, 780, 806); delete the duplicate sentence at 57-58; and fix the four broken sentences at 66, 531, 641 and 890.
5. One notation per operation in the mathematics: `\frac` rather than `\over` (111, 224, 225, 364, 365, 366, 471, 479), `\\` rather than `\cr` in both `aligned` blocks (224-227, 363-367), `V_{\mathrm{aut}}` rather than `V_{\rm aut}` in all eleven places, `(p')^{-1}` rather than `p'^{-1}` (471), and one convention for the grid names at 700-703.
6. Italicise rather than bold the three emphasised words at 268-272, keeping bold for the defined terms at 78 and 893.
7. Mechanical items from the draft: the 107 double spaces (qe-writing-008), lowercase 'Algorithm' at 755 (qe-writing-004), `{cite:t}` at 317 (qe-ref-001), and in the figure cell - drop the six `plt.rc` style overrides and `figsize` (837-844), move the two `plt.title` calls into mystnb captions (854, 863), lowercase the three axis labels (852, 861, 862), add `lw=2` to the six `plt.plot` calls (846, 848, 850, 857, 858, 859) and `name:` metadata to the figure cell (835).
8. Two things the figure's own labels get wrong while they are being fixed: the legend at 847 hard-codes '$V^u_0$ = 16759 (aut)' for the computed `Vu_aut`, and 823 hard-codes the two comparison values 16942 and 17000 with no explanation of where they come from - f-strings and a sentence would keep the figure honest if the calibration ever changes.
9. This file is byte-identical to `lecture-python-advanced.myst/lectures/un_insure.md`, so all of the above belongs upstream; until it is re-synced every finding here is counted twice in the corpus totals.
