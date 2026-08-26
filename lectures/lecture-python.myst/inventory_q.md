# inventory_q

- **Series:** lecture-python.myst
- **File:** `lectures/inventory_q.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×3; `qe-writing-001` ×3; `qe-writing-005` ×4, +4 more. |
| Math         | 6/10  | `qe-math-010` (proposed) ×3; `qe-math-005` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×2; `qe-fig-008` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 379, 684, 685, 691, 692, 730, 740. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 143, 415, 432. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 76, 154, 394. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 682, 721. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 689, 696, 732, 742. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 681, 718. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 3. *Lines:* 92, 94, 96. *Example:* parenthesised sequence.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 488, 557, 561. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 398, 463, 512. *Example:* the "### What the manager needs to know" section (463-477) reproduces the Introduction's list at 42-49 almost item for item - inventory level, order quantity, resulting profit, next inventory level, plus the discount factor from 49 - and 398-402 makes the same point a third time ("suppose the agent does not know the demand distribution $\phi$, the cost parameters ... or the transition function $h$"), so one claim is stated three times in 420 lines; separately, 512-514 is a 36-word sentence carrying a because-clause, a main clause and an em-dash aside ("affects only which $(x, a)$ entries get visited -- and hence updated -- over time").
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 521, 549. *Example:* 521 asserts convergence of the Q-table conditional on "the learning rates satisfy standard conditions (see below)", but those conditions are not given until the "### Learning rate" section at 531-535, so the central convergence claim rests on a forward reference; and 549 introduces $\lambda$ in the decay rule $\varepsilon_{t+1} = \max(\varepsilon_{\min},\; \varepsilon_t \cdot \lambda)$ without ever saying what it is - the reader has to reach the `ε_decay=0.999999` default at 643 to find out.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 51, 396, 465, 708. *Example:* the lecture's bold-for-definition discipline is otherwise excellent, which makes the four exceptions stand out: 51 italicises the term being introduced ("A key idea is the *Q-factor* representation") and then bolds the same concept at 410, so the reader meets it in the wrong typeface first; and 396, 465 and 708 use bold for pure emphasis - "can an agent **learn** the optimal policy", "Notice what is **not** required", "All panels use the **same demand sequence**" - which the rule reserves for italic.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 485, 538. *Example:* "### The Q-table and the role of the max" (480-506) spends 27 lines describing a two-dimensional lookup table, which single entry $q_t(x,a)$ an update touches, and how the scalar $\max_{a'} q_t(X_{t+1}, a')$ differs from the action $\argmax_{a'} q_t(X_{t+1}, a')$ - all of it inherently spatial, and all of it in prose; a heatmap of the final `q` array (which the lecture already has in memory at 659) with the updated cell marked would carry the whole argument. "### Exploration: epsilon-greedy" (538-551) likewise states a decay law $\varepsilon_{t+1} = \max(\varepsilon_{\min}, \varepsilon_t \lambda)$ over 5 million steps without plotting it, so the reader cannot see when exploration effectively stops.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 489. *Example:* 2 spaces.


## Strengths

- Bold marks definitions and italic marks emphasis almost throughout, and the definitions are the ones that matter: **$v$-greedy policy** (171, 273), **Q-function** (410), **Q-table** (485), **behavior policy** (510), **off-policy** (516), **optimistic initialization** (555), against *that one entry* (490), *actually takes* (504), *speed* and *limit* (523, 525).
- The "role of the max" discussion at 493-506 anticipates and corrects the standard misreading of Q-learning - that the $\max_{a'}$ in the update prescribes the next action - and separates the update target from the behavior policy; the code then makes the distinction visible by computing `best_next` and `a_next` in the same loop and using them in different places (616-633).
- The Bellman equation is the file's single labelled equation (`inventory_q_bellman`, 140-148) and it is cited by `{eq}` at 423 at exactly the point where the Q-factor derivation needs it.
- Both solution methods run off the same `Model` NamedTuple with the same unicode-Greek fields (`ϕ_values`, `κ`, `β`, and `σ`, `α`, `ε` in the kernels), which is what makes the VFI-versus-Q-learning overlay at 682-699 a like-for-like comparison rather than two separate exercises.
- The learning-over-time panels at 718-747 hold the demand path fixed across snapshots (`sim_seed = 5678`, stated at 708), so what varies between panels is only the policy - a controlled comparison rather than three unrelated simulations.
- The timing convention is stated explicitly and defended: the arrow diagram at 109 and the parenthetical at 111-112 explain why the order is indexed $A_t$ even though the stock arrives in $t+1$.

## Recommended actions

1. Replace `\mathbf{1}\{a > 0\}` at 231 with the plain `1\{a > 0\}` already used at 119, or with `\mathbb{1}` - this is a qe-math-004 violation that the draft report does not list (see scanner doubts), and it is also the only place the indicator changes typeface mid-lecture.
2. Add `mystnb: figure: caption`/`name` metadata to the two un-named figures (681, 718) and move the four `set_title` calls (689, 696, 732, 742) into those captions or into panel labels; then `lw=2` on the seven line plots (379, 684, 685, 691, 692, 730, 740).
3. Settle the expectation and argmax notation: `\EE` at 86 against `\mathbb E` at 143, 415, 432, and `\argmax` at 174, 495, 669 against `\arg\max` at 277, 441 - then add the braces `\mathbb E` -> `\mathbb{E}` (qe-math-010 (proposed), proposed).
4. Delete either "### What the manager needs to know" (463-477) or the Introduction bullets at 42-49; keeping both means the reader is told the same five observables three times, counting 398-402.
5. Add a picture to the Q-table section: a heatmap of the final `q` array over $(x, a)$ with the infeasible region masked would show both the shape of the solution and why only feasible $a \leq K - x$ entries are ever updated.
6. Curly-bracket the three sequences at 92, 94 and 96 (`(D_t)_{t \geq 0}` -> `\{D_t\}_{t \geq 0}`), lower-case the H2s at 76 and 154, and change "## Q-Learning" at 394 to "## Q-learning" to match how the prose spells it at 40, 447 and 583.
7. Introduce $\lambda$ where it is first used at 549, move the Robbins-Monro conditions (531-535) ahead of the convergence claim at 519-521, split the three two-sentence paragraphs (488, 557, 561), and bring the `n_steps=20_000_000` default at 642 into line with the 5 million steps actually run at 657.
