# navy_captain

- **Series:** lecture-python.myst
- **File:** `lectures/navy_captain.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×7; `qe-writing-005` ×5; `qe-writing-003` ×6, +4 more. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×4; `qe-math-009` ×5. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-003` ×20; `qe-fig-005` ×19; `qe-fig-006` ×4, +2 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 294, 366, 488, 579, 893, 916, 1070. *Example:* 294 is `l = lambda z: wf.f0(z) / wf.f1(z)` - the ambiguous single-character name PEP8 singles out in E741 and a lambda binding (E731) in the same line, and `l0_arr`/`l1_arr` at 298-299 inherit the name; 488 binds a second lambda, `h_func = lambda p: np.interp(p, π_grid, h)`. Twenty code lines exceed 79 characters (E501): 366 (93), 893 (101), 911, 942, 943, 949, 950, 1015, 1016, 1017, 1040, 1043, 1078, 1079, 1081, 1082, 1099, 1100, 733, 740. 579 omits the space after a comma, `np.column_stack([h_star, cost_L0, cost_L1]),axis=1` (E231). 1070 and 1071 both put two spaces after the operator, `(1 - π_star) *  A / (...)` (E222). 916 ends `plt.legend();` with a semicolon (E703), the only one in the file. 558-565 wraps `np.searchsorted(` so that the closing bracket and `- 1]` sit alone at 30 and 15 columns of indent, and 1021, 1023, 1038, 1043 and 1097 indent continuations under `plt.plot(` to a flat 8 spaces instead of aligning with the opening bracket (E128). 688, 690 and 734 write `B+0.01`, `A+0.01`, `π_optimal+0.05` where 582-583 write `B + 0.01`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 446, 573, 723, 762, 816, 940. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 20. *Lines:* 193, 326, 400, 437, 450, 456, 692, 738, 740, 766, …. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 19. *Lines:* 186, 284, 309, 394, 434, 445, 539, 681, 720, 750, …. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 31. *Lines:* 316, 319, 398, 435, 448, 452, 453, 575, 576, 577, …. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 5. *Lines:* 220, 244, 410, 639, 823. *Example:* `\left`/`\right` is used where plain delimiters would do throughout - `\left\{ z_{i}\right\} _{i=0}^{t}` (80, 220), `L\left(z^{t}\right)` (218), `\bar{V}_{fre}\left(t,d\right)` (244, 268, 336), `V^{0}\left(\pi\right)` (614, 624), `\left(1-\pi\right)` (633, 639) - and nothing in the file is taller than a one-line fraction. $PFA$ and $PD$ (244, 250, 251, 257, 259, 262, 263, 307, 443) are multi-letter names set in italic math, so they render as the products $P\cdot F\cdot A$ and $P\cdot D$; `\mathrm{PFA}` would read correctly. 410 puts a code identifier into math as $t_{\rm optimal}$. The same two objects carry two names and two bar commands: $\bar{V}_{fre}$/$\bar{V}_{Bayes}$ in the prose (244, 336, 639, 699, 831) against $\overline{V}_{baye}$ in the figures (737, 740, 766, 802, 819). And 823 labels the lecture's punchline series `label='$diff$'`, four italic letters in math mode where the prose two lines later (830-831) names it $\bar{V}_{fre}-\bar{V}_{Bayes}$.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 250, 251, 340, 698. *Example:* non-blackboard `\Pr`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 55, 59, 64, 867, 1000. *Example:* 64 is one 48-word sentence (301 characters) carrying two bolded terms, a spelled-out cross-reference title and both decision rules; 55 is 33 words that reach their point through "proceeded to try to solve"; 59-62 is 45 words that name two lectures as "this lecture `` {doc}`Exchangeability and Bayesian Updating` ``" and "this lecture `` {doc}`Likelihood Ratio Processes` ``" in one breath, and the full title "A Bayesian Formulation of Friedman and Wald's Problem" is spelled out six times over the file (42, 64, 98, 229, 466, 473). 867-868 says it twice and ungrammatically: "the frequency distribution of Bayesian times to decide of Bayesian decision maker". 1000-1003 is 43 words whose "and similarly it equals $1$ minus the optimal probability of a false alarm under $f_0$" attaches "it" to the wrong probability - the sentence starts from the correct decision under $f_1$ and ends by describing the correct decision under $f_0$.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 6. *Lines:* 228, 259, 265, 835, 925, 1092. *Example:* six places where the text does not join up with what surrounds it. 259-260 defines $PD$ as "the probability of a **detection error**, i.e., not rejecting $H_0$ when $H_1$ is true", but 251 sets $PD = \Pr\{L(z^t) < d \mid q = f_1\}$ and `` {eq}`val1` `` at 244 charges $\bar L_0$ on $(1-PD)$ - so $PD$ is the probability of *detection* and the sentence describes $1-PD$; a reader checking the equation against the definition is stopped cold. 228-229 says the loss parameters are "$\bar L_1$ and $\bar L_2$" - there is no $\bar L_2$ in the lecture, the pair defined at 89-92 is $\bar L_0$ and $\bar L_1$. 265-266 defers receiver operating characteristic curves to another lecture ("please see this lecture `` {doc}`Likelihood Ratio Processes` ``") and then 305-328 draws them here, forty lines later. The H2 "More Details" at 835 promises "more insights by focusing on the case in which $\pi^*=0.5=\pi_0$" and contains no insight at all - three code cells that set `π_star = 0.5`, print `t_optimal` and define `t_idx`. 925-926 promises "Later we'll figure out how these distributions ultimately affect objective expected values under the Neyman-Pearson and Bayesian decision rules", but that comparison was already made at 809-833 and nothing after 925 returns to it. And 1092-1094 says "The next graph plots the unconditional distribution of Bayesian times to decide" when the cell at 1096-1107 plots the unconditional distribution of $\log L$ at the frequentist $t$ - the times-to-decide graph it describes is back at 981-992.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 64, 306, 845, 875, 876. *Example:* definitions are bolded correctly - **frequentist decision rule** (51), **type I error** (89), **type II error** (91), **false alarm** (257), **detection error** (259), **receiver operating characteristic curve** (262) - but bold is then reused for plain emphasis in four places the rule assigns to italic: **frequentist** and **Bayesian** at 64 (contrastive emphasis, and 51 has already defined the first of them), **ex ante** at 845, and **earlier**/**later** at 875-876, which carry the lecture's headline result. 306 re-bolds **receiver operating characteristic curves** as though defining it again, 44 lines after the definition at 262. The one correct italic emphasis in the file is *and* at 1007, so the two markers are doing each other's jobs.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 208, 461, 779, 835, 860, 995, 1054. *Example:* H2 Title Case: 'Frequentist Decision Rule' (Decision, Rule).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 32. *Lines:* 46, 51, 64, 70, 80, 86, 91, 94, 95, 102, …. *Example:* 3 spaces.

### Medium severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 323, 324, 1028, 1048. *Example:* axis label `Probability of false alarm`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 73. *Example:* 3 sentences in one paragraph.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 823, 875, 935. *Example:* the figure that answers the question in the section title "Was the Navy Captain's Hunch Correct?" (815-828) is the least labelled in the lecture - neither panel gets a title, the left panel's two series are distinguished only by legend, and the right panel's sole label is `'$diff$'` (823). Second, the continuation region $B \leq \pi \leq A$ is the whole content of the Bayesian rule (600-605), but it is only ever shown as two annotations on the value-function plot (582-586) and two `vlines` at 687-690; the belief paths that actually wander inside it are computed at 935-936 and then immediately collapsed to a mean and a variance (942-956), so the reader never sees one $\pi_t$ path crossing a cutoff even though the data is in hand. Third, the file contains no admonition of any kind, and the two results it exists to deliver - 833 "It is always positive" and 875-876 "the Bayesian rule decides **earlier** ... and **later**" - are bare paragraphs using bold to do the work a `{note}` would do.

### Low severity
_None found._


## Strengths

- The value-function figure at 573-592 makes the cutoff rule readable rather than asserted: it overlays the two terminal payoffs `cost_L0` and `cost_L1` (570-571, 576-577) on the continuation value, draws their pointwise minimum as a wide translucent band (578-580), and then annotates $A$ and $B$ exactly where the band switches branch (582-586) - so the rule stated at 600-605 can be checked against the picture.
- The claim $\pi_0^* = \pi^*$ is established at three increasing strengths instead of once: four worked cases at 720-742, then all 20 values of $\pi^*$ at 750-777 with an explicit 45-degree line drawn for comparison (769-771), then used at 838 to fix the parameterisation of the comparison that follows.
- 959-971 supplies the mechanism, not just the plot: it points out at 962-964 that the two conditional mean-belief paths lie on top of each other, and then attributes the Bayesian's longer wait under $f_1$ to the lower posterior variance visible in the right panel of 940-956.
- Events are written with braces throughout - $\Pr\{L(z^t)<d \mid q=f_0\}$ (250-251), $\pi^*=\Pr\{\text{nature selects }f_0\}$ (340, 698) - which is exactly what proposed qe-math-014 (proposed) asks for and is not common in this corpus.
- The two rules are scored on equal terms: the same $c$, $\bar L_0$, $\bar L_1$ (98-102), the frequentist minimising over $(t,d)$ (330-337) and the Bayesian over $\pi_0$ (701-702), both evaluated on the same simulated likelihood-ratio panels `L0_arr`/`L1_arr` (301-302) - which is what makes the comparison at 815-833 mean anything.
- 97-100 states which parameters were changed from the source lecture and why - "we increase both $\bar L_0$ and $\bar L_1$ from $25$ to $100$ to encourage the Bayesian decision rule to take more draws before deciding" - so the reader can reproduce the difference from `wald_friedman_2`.

## Recommended actions

1. Fix the definition of $PD$ at 259-260: 251 and `` {eq}`val1` `` make it the probability of detection, and the loss term is $(1-PD)\bar L_0$, so "the probability of a **detection error**, i.e., not rejecting $H_0$ when $H_1$ is true" describes $1-PD$. In the same pass rename the non-existent $\bar L_2$ at 229 to $\bar L_0$.
2. Correct 1092-1094 to describe the graph that follows it - the unconditional distribution of $\log L$ at the frequentist $t$, not "the unconditional distribution of Bayesian times to decide", which is the graph at 981-992.
3. Label the headline figure at 815-828: give both panels titles and replace `label='$diff$'` (823) with the difference the prose names at 830-831. Then work through the figure backlog - `mystnb: figure: caption`/`name` metadata for the 19 un-named figure cells, the 20 `plt.title`/`set_title` calls moved into those captions, the six `figsize` overrides dropped (446, 573, 723, 762, 816, 940), `lw=2` added to the 31 bare `plot()` calls, and the four capitalised axis labels lowercased (323, 324, 1028, 1048).
4. Settle one spelling per object: $\bar{V}_{Bayes}$ (639, 699, 831) against $\overline{V}_{baye}$ (737, 740, 766, 802, 819), and `\bar` against `\overline`; write $PFA$ and $PD$ as `\mathrm{PFA}` and `\mathrm{PD}` so they stop rendering as products; and replace $t_{\rm optimal}$ at 410 with the code name `t_optimal` in backticks.
5. Add a figure that shows a handful of $\pi_t$ paths from `π0_arr` and `π1_arr` (935-936) against horizontal lines at $A$ and $B$, so the stopping rule of 600-605 is visible; the paths are already computed and currently only their mean and variance are plotted (940-956).
6. Either deliver the content "More Details" (835-858) promises or fold its three cells into the section that follows, and drop the forward reference at 925-926 whose comparison has already been made at 809-833.
7. Rename `l` at 294 (E741) and convert both lambdas (294, 488) to `def`s; wrap the twenty over-length code lines (366, 733, 740, 893, 911, 942, 943, 949, 950, 1015-1017, 1040, 1043, 1078, 1079, 1081, 1082, 1099, 1100); drop the trailing semicolon at 916, the double operator spacing at 1070-1071 and the missing comma space at 579.
8. Sweep the mechanical remainder: the 32 double spaces (46, 51, 64, 70, 80, 86, 91, 94, 95, 102 and 22 more), the seven title-case H2 headings (208, 461, 779, 835, 860, 995, 1054), the three-sentence bullet at 72-78, and the missing full stop at 206.
