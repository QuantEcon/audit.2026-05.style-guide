# calvo_abreu

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/calvo_abreu.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×5; `qe-writing-002` ×6; `qe-writing-003` ×3, +3 more. |
| Math         | 8.5/10 | `qe-math-004` ×1; `qe-math-009` ×2. |
| Code         | 5.5/10 | `qe-code-001` ×17; `qe-code-003` ×1; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-008` ×2; `qe-fig-001` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 17. *Lines:* 414, 426, 428, 438, 444, 446, 453, 455, 456, 458, …. *Example:* fourteen lines inside the code cells carry trailing whitespace (414, 426, 428, 438, 444, 446, 456, 458, 489, 492, 499, 501, 557, 565) - PEP8 W291/W293, and 489 leaves eight trailing spaces after a `def` colon; 453 and 455 bind lambdas to names (`self.J_θ = lambda ...`, `self.V_θ = lambda ...`) where PEP8 asks for `def`; 453-454 and 621-623 use backslash line continuation with a hanging indent inside an expression that parentheses would wrap cleanly.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 35, 39, 42, 149, 151, 242. *Example:* line 35 is a single 65-word sentence carrying four separate ideas (linear-quadratic version, time inconsistency, Stackelberg/Ramsey planner, the once-and-for-all choice of the money-growth sequence); 39-40 is 45 words and garbled ("believe how future government authorities ... will respond" is missing "about"); 42 then restates 39-40 almost verbatim; 149 repeats the whole of 45 verbatim except for the opening clause, and 151 repeats 47 verbatim; 242-247 is a 45-word sentence with a parenthetical em-dash aside embedded in the middle of its subject.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 117, 151, 366, 519, 589. *Example:* bold is used as a paragraph label at 117 ("**Insight:**") rather than to mark a defined term; the terms defined and bolded once are then re-bolded on later mentions where the rule wants italic - **credible government policy** / **sustainable plan** at 151 after 47, **Ramsey plan** at 519, **self-enforcing** at 589 after 269 and 300; and the reverse error occurs at 366-367, where *stick* and *carrot* are italicised at exactly the point they are being defined ("Low one-period utilities early are a *stick*").
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 94. *Lines:* 33, 35, 37, 39, 40, 45, 47, 49, 51, 53, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 275. *Example:* install cell at line 275 of 688 (not near the top).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 573, 579. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 196. *Example:* {\bf.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 590, 641. *Example:* lines 641-643 name the three recursive policy functions $\nu_\mu, \nu_\theta, \nu_v$ - a nu indexed by mu, theta and v, so $\nu_v(v_t, \mu_t)$ sets nu against v and mu against mu in the same expression, which no reader can hold apart on screen; and the deviation value carries two symbols for one object, $v_j^{A,D}$ at 307 and 597-600 but $V_t^{A,D}$ at 590-592 and in the plot label at 573.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 39, 357. *Example:* `` {cite} `` in author position: '`` {cite}`Calvo1978` `` showed'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 203. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 145, 213, 679. *Example:* line 145 asserts that "a time $t$ policymaker cares only about $v_t$" but $v_t$ is never defined anywhere in this lecture; line 213 introduces the government's one-period return function $s(\theta,\mu)$ - used continuously from 217 to 613 - by pointing at "equation `` {eq}`eq_old6` `` in quantecon lecture `` {cite}`Calvo1978` ``", where `eq_old6` is not a label in this file and the citation names Calvo's 1978 paper rather than the quantecon lecture `` {doc}`calvo` ``; and $J(\theta^R_0)$ arrives unexplained at 385. Lines 679-686 then graft a lecture-wide summary ("We have also computed **credible plans**...") onto the end of the "Whose plan is it?" section, which was asking a different question.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 117, 185. *Example:* the within-period/between-period timing protocol at 185-208 is a branching structure - forecasts brought into $t$, then the confirm branch continuing with $\{\tilde\mu_{t+j+1}\}$ versus the disappoint branch restarting at $\vec\mu^A$ - and it is only ever set out as prose bullets, where a two-branch tree diagram would carry the whole mechanism; the lecture also has no admonitions at all, so the emphasised aside at 117 ("**Insight:**") and the reminders at 86 and 311 are typeset as bold labels and bare parentheticals instead of `{note}` blocks.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 422. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 571. *Example:* figsize=.


## Strengths

- Every labelled equation is genuinely load-bearing: `eq_old1_new` is cited at 82 and 89, `eq_old2_new` at 109, `eq_old3_new` at 117, `eq_old10` at 590, `eq_old100a` at 675, and `eq_old11` three times at 650, 653 and 656 - no label is dead weight.
- Self-enforcement is verified rather than asserted: the three-panel plot at 571-584 shows $v_t^A$ against $v_t^{A,D}$, then 606 checks it numerically with `np.all(clq.V_A[0:20] > clq.V_dev[0:20])`, and 617-627 runs the same check for the Ramsey plan.
- The Abreu construction is given its intuition in two lines immediately after the algebra (366-367, low utilities early are a *stick*, high utilities later a *carrot*), so the reader knows what the plan is for before seeing it computed.
- The closing section (661-676) states both readings of a credible plan - the government chooses, versus the government merely confirms private forecasts - and gives the argument for each rather than settling it by assertion.
- Greek letters in code are Unicode throughout the `ChangLQ` class (`α`, `β`, `θ`, `μ`, `θ_n`, `θ_space`, `μ_MPE`), so the class body reads directly against the algebra.

## Recommended actions

1. Strip the 94 runs of double spaces (qe-writing-008) - they are spread over most narrative paragraphs and are the single biggest mechanical item here.
2. Delete the duplicated overview material: 149 repeats 45 verbatim apart from its opening clause, 151 repeats 47 verbatim, and 42 restates 39-40; then break the 65-word sentence at 35 into three.
3. Fix the pointer at 213: define $s(\theta,\mu)$ in this lecture or link it with `` {doc}`calvo` ``, because `{eq}`eq_old6`` is not a label in this file and `{cite}`Calvo1978`` is being used where a lecture reference is meant; define $v_t$ before using it at 145, and $J(\cdot)$ before 385.
4. Rename the recursive policy functions at 641-643 so nu does not sit beside v (for instance $\mu_t = h_\mu(v_t)$, $\theta_t = h_\theta(v_t)$, $v_{t+1} = h_v(v_t,\mu_t)$), and settle on one case for the deviation value - $v^{A,D}$ or $V^{A,D}$, not both.
5. Move the `!pip install` cell from 275 to the top of the lecture (qe-code-003) and replace `{\bf R}` at 196 with `\mathbb{R}` (qe-math-004).
6. Clean up the `ChangLQ` cell: remove the trailing whitespace on the fourteen lines listed above, turn the two named lambdas at 453 and 455 into `def`s, and replace the backslash continuations at 453-454 and 621-623 with parentheses.
7. Set `lw=2` on the two plot calls at 573 and 579, drop the `figsize=(8, 12)` at 571, and add a two-branch timing diagram for the confirm/disappoint protocol described at 185-208.
