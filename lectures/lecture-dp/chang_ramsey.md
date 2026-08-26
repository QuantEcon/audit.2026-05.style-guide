# chang_ramsey

- **Series:** lecture-dp
- **File:** `lectures/chang_ramsey.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-005` ×12; `qe-writing-004` ×2; `qe-writing-001` ×2, +4 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×2; `qe-fig-008` ×5, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 941, 1054, 1071, 1101, 1124. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 1057, 1079, 1104, 1105, 1131. *Example:* plot() without lw=.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 12. *Lines:* 378, 386, 460, 473, 514, 535, 605, 643, 668, 676, …. *Example:* bold is used exclusively as a structural label and never for a definition: '**Definition:**' at 378, 386, 460, 514, 643, 668 and 676, '**Proposition:**' at 473, 535, 605, 752 and 757, and '**Step 1**' / '**Step 2**' / '**Step 3**' at 849, 851 and 894. Every term the lecture actually defines is italicised instead - *value of money* (164), *government strategy* (626), *admissible* (643), *outer hyperplane approximation algorithm* (837). Seven definitions and five propositions written as bold run-in labels also means there is nothing for `qe-admon-004` to check, which is why the whole Admonitions category is N/A for this file.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 26. *Lines:* 36, 44, 46, 109, 125, 137, 214, 232, 249, 270, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 934, 946, 947, 967. *Example:* line 934 declares `def plot_competitive(ChangModel):` - a CapWords parameter shadowing the class of the same name (PEP8 asks for lowercase parameter names). Line 946 writes `ax.fill(ext_C[:,0], ext_C[:,1], ...)` with no space after the slice commas (E231) while lines 947 and 948 immediately below write `ext_C[:, 1]` with the space. Line 947-948 also makes the plotting function mutate its argument - `ChangModel.min_theta = min(...)`, `ChangModel.max_theta = max(...)` - so calling a plot routine silently writes attributes onto the model. Line 967 writes `h_max=1/0.8` unspaced where the earlier call at 929 writes `h_max=2`, and lines 957-958 under-indent the `ax.annotate(...)` continuation (E128).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 1072, 1106, 1125. *Example:* .suptitle.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1053, 1100. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 44, 581. *Example:* `` {cite} `` in narrative flow: '  `` {cite} ``'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 831, 851. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 179, 750, 833, 891. *Example:* line 179-180 drops a conjunction: 'how real balances $q_t M_t$ carried out of period $t$ depend on real balances $q_t M_{t-1}$ carried into period $t$, income, consumption, taxes'; line 750 reads 'It is possible to establish.' with a full stop where the colon introducing the proposition belongs; lines 833-835 pack a parenthetical and two sentences into one paragraph ('...a grid of possible values for $m$ and $h$ (note that $x$ is implied by $m$ and $h$). This discretization simplifies...'); line 891-892 writes the nested sequence as '$S_{t+1} \subset S_t \subset S_{t-1} \cdots \subset S_0$', missing the $\subset$ before the ellipsis.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 594, 1017, 1091. *Example:* line 594-600 defines the central operator as a fragment: the display reads $B(Q) = \theta \in \mathbb{R}$ 'such that there is $(m,x,h,\theta') \in E \times Q$' with no set braces at all, and the three conditions that complete the definition are named in prose two lines later at 599-600 rather than inside the display - so as printed the lecture asserts that a set equals a real number. Line 1017-1029 then claims 'We have solved the Bellman equation for the two sets of parameter values for which we computed the equilibrium value sets above. Hence for these parameter configurations, we know the bounds of $\Omega$', and quotes $\Omega = [0.0088, 0.0499]$ and $[0.0395, 0.2193]$ - but `ch1` and `ch2` are rebuilt at 1030-1033 with different parameters (`h_min=0.99, h_max=1/0.3, N_g=50` against the earlier `h_min=0.9, h_max=2, N_g=10`), so those bounds belong to the discarded parameterisation, and the `solve_bellman` calls at 1037-1038 use 0.0499 from the old bounds but 0.15 rather than the quoted 0.2193. Third, $\bar\theta$ carries the punchline of the numerical section - 'the choice of $\bar\theta$ is clearly important' (1091), 'does not intersect the 45-degree line until $\bar\theta$' (1097) - and is never defined anywhere in the lecture.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 852, 887. *Example:* mid-sentence 'Step'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 837, 1101. *Example:* the outer hyperplane approximation algorithm (837-895) is described as producing 'a sequence of progressively smaller sets $S_{t+1} \subset S_t \subset \cdots \subset S_0$' (890-892) by cutting a polytope back with subgradient linear programs, and no figure shows a single intermediate set - the equilibrium-set figure at 934-960 plots only the converged object, although the machinery for drawing a polytope from its extreme points is right there at 938-946. Second, lines 1093-1098 tell the reader precisely what to look for in the next figure - whether $\theta'(\theta)$ meets the 45-degree line in the interior or only at $\bar\theta$ - and the figure at 1101-1109 draws both curves but marks neither $\bar\theta$ nor the intersection, so the one feature the text singles out is the one thing the panel does not show.

### Low severity
_None found._


## Strengths

- The lecture names its organising idea, says where else the reader has met it, and defines it structurally rather than by slogan: 'dynamic programming squared' (36) is characterised at 38-44 as two interrelated Bellman equations, one for the followers with value $v_a$ and one for the leader in which $v_a$ appears as an argument, with pointers to `` {doc}`dyn_stack` `` and `` {doc}`opt_tax_recur` ``.
- The two propositions about $B$ (605-618) are stated and then used immediately for the thing that matters: self-generation plus factorization characterise $\Omega$ as the largest fixed point, monotonicity licenses computing it as a limit of iterations 'provided that iterations begin from a sufficiently large initial set' - the justification for the algorithm arrives before the algorithm.
- The revolution thought-experiment at 501-511 makes time inconsistency concrete rather than definitional: a fresh planner at $t$ would reset $\theta_t$ to $\theta_0$, and the text says exactly what that planner avoids - 'the costs at time $t$ that the original Ramsey planner must pay to reap the beneficial effects that the original Ramsey plan for $s \geq t$ had achieved via its influence on the household's decisions for $s = 0, \ldots, t-1$'.
- The numerical approximation is explained before it is used: $S$ is approximated by an intersection of half-spaces $\tilde S = \{(w,\theta) : H \cdot (w,\theta) \leq C\}$ (825-829), the action space is discretised so that the operator becomes a sequence of linear programs (831-835), and each step of the algorithm then states its own optimisation problem with the full constraint set (859-883).
- Approximation quality is checked rather than assumed - `max(abs(ch1.resid_grid)), max(abs(ch2.resid_grid))` at 1046-1047, introduced as 'a quick check that our approximations of the value functions are good' - and the relationship between two different figures is stated so the reader can verify it: 'The value functions plotted below trace out the right edges of the sets of equilibrium values plotted above' (1050-1051).
- The comparative experiment moves exactly one parameter and the consequence is spelled out: at $\beta = 0.3$ the planner's $\theta'$ hits the upper limit of $\Omega$, at $\beta = 0.8$ it converges to an interior point (1086-1089), which is precisely what makes the choice of the upper bound matter in one case and not the other.

## Recommended actions

1. Fix the set definitions, which are currently split across display blocks in a way that leaves their delimiters unmatched. $D(Z)$ opens `\Bigl\{` in the `$$` block at 712-714 and closes `\Bigr\}` in a different `$$` block at 746-748, six displays later; the second $D(Z)$ definition at 782 opens a `\{` that is never closed in its own block; $CE$ at 460-462 opens `\bigl\{` in one inline span and closes in another with prose between; and $B(Q)$ at 593-597 has no braces at all and no condition. Each definition needs to be a single display, or delimiters need to be balanced per block.
2. Reconcile the Bellman section with the code it claims to describe (1017-1038). Either re-solve the equilibrium sets with the parameters used at 1030-1033, or quote the $\Omega$ bounds that belong to those parameters; as written the two $\Omega$ intervals at 1026-1027 come from a different `ChangModel` than the one whose Bellman equation is solved, and `θ_max=0.15` at 1038 matches neither.
3. Convert the seven '**Definition:**' and five '**Proposition:**' labels to `{prf:definition}` and `{prf:proposition}` directives (378, 386, 460, 473, 514, 535, 605, 643, 668, 676, 752, 757), then bold the terms they define - currently italic at 164, 626, 643, 837 - and turn '**Step 1**'-'**Step 3**' (849, 851, 894) into subheadings.
4. Define $\bar\theta$ where it is first needed, or say at 1091 that it is the upper endpoint of the $\Omega$ computed above. It currently appears for the first time in the concluding discussion of the policy-function figures and carries the section's main claim.
5. Repair the math markup: the malformed limit at 170 (`$u'(c)_{c \rightarrow 0}$` should be $\lim_{c \to 0} u'(c)$, as the right half of the same line already shows), the plain-TeX `{\rm ...}` at 330, 550, 574, 655, 713 and 717 (use `\text{}` or `\operatorname{}`), the bare `|` used for 'such that' at 514 and 828 (use `\mid`), and the missing `\subset` at 891.
6. Clear the 26 double spaces, lower-case the 2 mid-sentence capitals at 852 and 887, split the 2 two-sentence paragraphs at 831 and 851, and switch the 2 in-flow citations at 44 and 581 to `{cite:t}` (qe-writing-008 x26, qe-writing-004 x2, qe-writing-001 x2, qe-ref-001 x2).
7. Finish the figures and the code slips: mystnb `name`/`caption` metadata on the 2 unnamed figure cells (1053, 1100), the 3 `suptitle`/`title` calls moved into captions (1072, 1106, 1125), the 5 hand-set `figsize=` dropped (941, 1054, 1071, 1101, 1124) and `lw=2` added to the 5 line plots (1057, 1079, 1104, 1105, 1131); rename the `ChangModel` parameter at 934, stop mutating it at 947-948, and even out the spacing at 946, 958 and 967 (qe-fig-005 x2, qe-fig-003 x3, qe-fig-001 x5, qe-fig-008 x5).
