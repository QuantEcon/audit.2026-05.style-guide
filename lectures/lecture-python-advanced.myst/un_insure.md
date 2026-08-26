# un_insure

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/un_insure.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-002` ×6; `qe-writing-005` ×3; `qe-writing-003` ×4, +3 more. |
| Math         | 9.5/10 | `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×2; `qe-fig-006` ×3; `qe-fig-005` ×1, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 512, 554, 592, 623, 671, 711, 743, 759, 836. *Example:* the module-level helpers take `self` as their first parameter without being methods of anything - `def u(self, c)` at 554, and the same at 558, 592, 609, 671, 682, 711 and 758 - and are then called as `u(self, 0)` (597) and `iterate_C(self, C_old, Vu_grid)` (766), so the name PEP8 reserves for instance methods is used throughout for a plain first argument. The class it shadows is itself misnamed: `class params_instance` at 512 uses lowercase_with_underscores where PEP8 asks for CapWords. 623-624 assign two lambdas to names (`Vu_error_Λ = lambda Vu, r: ...`), which PEP8 explicitly asks to be written as `def`. 759 binds `iter`, shadowing the builtin, inside a loop that then uses it as a counter. The three docstrings at 672-675, 683-685 and 712-714 use `'''` where the rest of the corpus and PEP257 use `"""`. 836 names a variable `fontSize` in camelCase. And 739-741 and 743-744 run past 79 columns.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 837, 838, 839, 840, 841, 842, 844. *Example:* style override.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 846, 848, 850, 857, 858, 859. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 395, 66, 531, 641, 889, 566. *Example:* several sentences are incomplete or mis-typed rather than merely long. 395 is missing its subject: "The  of benefits on the duration of unemployment is  designed to provide the worker an incentive to search". 66 reads "we'll use assume the same $p(a)$ function". 531 has both "an observerd hazard rate" and a dropped noun in "the probability that an unemployed worker finds a job each  --  in US data". 641 reads "Now that we have calibrated our the parameter $r$". 889-890 reads "search effort rise as the duration of unemployment increases". Separately, three equations are restated under new labels rather than referenced: `` {eq}`eq:yad1` `` at 566 repeats `` {eq}`eq:hugo3` `` (121), `` {eq}`eq:yad2` `` at 572 repeats `` {eq}`eq:hugo4` `` (128), and `` {eq}`eq:yad3` `` at 662 repeats `` {eq}`eq:hugo5` `` (192), leaving six labels for three objects. 57-58 ("The probability of finding a job is $p(a)$") likewise restates 49-52.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 107. *Lines:* 17, 20, 22, 30, 58, 62, 66, 105, 115, 148, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 854, 863. *Example:* plt.title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 852, 861, 862. *Example:* axis label `Replacement ratio (c/w)`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 566, 700, 137. *Example:* the job-finding probability is written $p_r(a)$ and $p_r'(a)$ at 566 and 572 and plain $p(a)$, $p'(a)$ everywhere else (58, 62, 121, 128, 192, 278, 401, 432, 437) for the same function - the subscript adds nothing the surrounding text does not already say. 700 sets code identifiers in math mode, $grid_V$ and $Vu_{grid}$, which typeset as products of italic letters and use two different conventions for the same kind of object in one line; backticks would render them as the names they are. And $V_{\rm aut}$ (137, 142, 145, 166, 266, 426, 810, 868, 870) uses the deprecated `\rm` switch rather than `\mathrm{aut}`.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 411, 705, 700, 847. *Example:* step 6 of the Algorithm at 705 states the iteration as $C_{j+1}(V) = \min_{c,a,V^u}\{c - \beta[1-p(a)]C_j(V)\}$ - a minus sign where `` {eq}`eq:hugo23` `` (489) and `` {eq}`eq:yad3` `` (662) both have a plus, and $C_j(V)$ where both have $C(V^u)$, so the one line a reader would copy to implement the algorithm is wrong in two places. Step 1 (700) also posits two grids, $grid_V$ for $V$ and $Vu_{grid}$ for $V^u$, but only `Vu_grid` is ever built (791) and `iterate_C` uses it for both, passing `Vu_grid[V_i]` as the promised value at 732. Second, 411-413 is an entirely empty `{code-cell} ipython3`, which renders as a blank input cell in the middle of the theory, followed by three blank lines. Third, the figure legend at 847 hard-codes `'$V^u_0$ = 16759 (aut)'` while the autarky value it names is computed at 635 from the calibrated $r$ - so a recalibration silently makes the legend false, and the two companion labels at 849 and 851 hard-code 16942 and 17000, the magic numbers from 823, with nothing saying where they came from.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 755. *Example:* mid-sentence 'Algorithm'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 268, 272. *Example:* 268-269 sets **increases** and **decreases** in bold purely for contrast ("It **increases** the unemployed worker's consumption $c$ and **decreases** his search effort $a$") and 272 sets **higher** the same way, where the rule asks for italic - and the same passage uses italic correctly for emphasis three times, at 296 (*lowering*) and 312-313 (*both*, *and*). The bold at 78 (**insurance agency**, **planner**) and 893-899 (**carrot-and-stick**, **carrot**, **stick**) is correct definitional use, so the file already knows the distinction.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 835. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 317. *Example:* `` {cite} `` in narrative flow: 'Following  `` {cite} ``'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 794. *Example:* the cost function $C(V)$ is the object the entire lecture solves for, its strict convexity is invoked at 178-181, 234-235, 341 and 383 to derive both central results ($V^u = V$ under full information, $V^u < V$ under private information), and it is computed on a 50-point grid at 794 - and it is never plotted. Nor are the three policy functions returned alongside it (`V_star`, `cons_star`, `a_star`, 794), which are used only to simulate paths. The single figure in the lecture (835-864) shows those simulated paths, and even there the full-information benchmark that 881-884 describes in words - a constant replacement ratio over the spell - is not drawn on the same axes as the declining private-information schedule, though that one overlay would make the lecture's central contrast visible in a single panel.


## Strengths

- The lecture builds its result by stacking three models that differ in exactly one assumption each, and says so as it goes: autarky (94-155), full information where the agency controls both $c$ and $a$ (157-254), and private information where it controls only $c$ (315-409) - with 311-313 stating precisely what the full-information contract rests on before that assumption is removed.
- The two central comparative statics are derived rather than asserted, and by the same three-line argument each time: the envelope condition plus the third first-order condition gives $C'(V^u) = C'(V)$ and hence $V^u = V$ under full information (231-235), and $C'(V^u) < C'(V)$ and hence $V^u < V$ under private information (379-383), so the reader sees exactly which term the incentive constraint adds.
- The incentive problem is argued from the worker's own first-order condition rather than by appeal to intuition: 276-291 shows that $[\beta p'(a)]^{-1} > (V^e - V^u)$ holds under the planner's scheme while the worker's condition `` {eq}`eq:hugo4` `` requires equality, and concludes that a free worker would restore it by lowering $a$.
- The calibration is presented as a solved problem with a stated target rather than as chosen numbers: 530-533 says $r$ is picked so that autarky reproduces a 0.1 hazard rate, 601-605 defines the error function that measures the miss, 632-638 solves it by bisection and then prints the achieved hazard as a check.
- The numerical bounds on the state are derived, not guessed: 420-448 shows the lower bound is $V_{\rm aut}$ and derives the upper bound $V^e - [\beta p'(0)]^{-1}$ from the requirement that search effort be positive, and 789-790 builds the grid from exactly those two expressions.
- The economic reading at 873-919 pre-empts the misreading a reader is most likely to make - that declining benefits punish the long-term unemployed - and states the alternative explicitly: the planner "believes that a worker who has been unemployed a long time is unlucky, not that he has done anything wrong" (909-910), and names the carrot-and-stick structure that recurs in the sibling lectures (902).

## Recommended actions

1. Fix step 6 of the Algorithm at 705: the sign should be a plus and the argument $C_j(V^u)$, to match `` {eq}`eq:hugo23` `` at 489 - and reconcile step 1 at 700 with the code, which builds one grid (791) and uses it for both $V$ and $V^u$ (732).
2. Delete the empty code cell at 411-413 and the four `+++` cell markers left in the prose at 535, 643, 647, 657, 780 and 806.
3. Repair the six broken sentences: 395 (missing subject), 66 ("use assume"), 531 ("observerd", and the dropped word in "finds a job each  --"), 641 ("our the parameter"), 889 ("search effort rise"), and 169 ("minimizes an expected present value discounted costs").
4. Plot the computed cost function $C^*(V)$ and the three policy functions from 794, and overlay the constant full-information replacement ratio on the top panel at 845-854 so the contrast described at 881-887 is visible.
5. Drop the duplicated equations - `` {eq}`eq:yad1` `` (566), `` {eq}`eq:yad2` `` (572) and `` {eq}`eq:yad3` `` (662) restate `` {eq}`eq:hugo3` ``, `` {eq}`eq:hugo4` `` and `` {eq}`eq:hugo5` `` - and reference the originals instead.
6. Compute the figure legends from the values they name: 847 hard-codes 16759 for a quantity computed at 635, and 849/851 hard-code the magic numbers set at 823 with no explanation of where 16942 and 17000 come from.
7. Clean the PEP8 items: rename `params_instance` to CapWords (512), drop the `self` first argument from the eight module-level helpers or make them methods, replace the two assigned lambdas at 623-624 with `def`, rename `iter` at 759 and `fontSize` at 836, and switch the three `'''` docstrings (672, 683, 712) to `"""`.
8. Resolve the forward references: `r_error` (609) calls `Vu_error_Λ` defined at 623, and `iterate_C` (711) reads `Vu_min` and `Vu_max` defined at 789-790, so both functions depend on globals that do not exist when their cells run.
9. Sweep the measured items: the 107 double spaces, `lw=2` on the six `plot` calls (846-859), lowercase axis labels at 852, 861 and 862, the two `plt.title` calls at 854 and 863 moved into `mystnb` figure metadata on the cell at 835, the seven `plt.rc` overrides at 837-842 and the `figsize` at 844 removed, `{cite:t}` after "Following" at 317, and `a` put into math mode at 575.
10. Signpost the two comparisons at 265-274 so they do not read as a contradiction: 268-269 says the agency *decreases* search effort relative to autarky, 271-274 says the prescribed effort is *higher* than the worker would choose at that consumption level, and nothing in between says the baseline has changed.
