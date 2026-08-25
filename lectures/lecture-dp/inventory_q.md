# inventory_q

- **Series:** lecture-dp
- **File:** `lectures/inventory_q.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×2; `qe-writing-001` ×3; `qe-writing-005` ×4, +3 more. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×3; `qe-math-005` ×3; `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×2; `qe-fig-008` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 212, 218, 365, 376, 627, 660. *Example:* `X[t+1]` (365) and `n_steps=n+1` (660) omit the spaces around `+` that the same file uses in `K - x + 1` (246, 291, 576, 620), and `n[x, a] ** 0.51` (627) adds spaces around `**` where line 215 writes `(1 - p)**d` - PEP8 and this rule both prefer the tight form. The closing bracket of `create_sdd_inventory_model` sits at indent 4 against a hanging indent of 8 (212, E124), there is trailing whitespace at 218, and `plot_ts` (376-388) reads `σ_star` and `p` out of the module namespace rather than taking them as arguments, which is why the function cannot be reused for the snapshot policies and the panel loop at 736-742 duplicates it.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 380, 685, 686, 692, 693, 730, 739. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 143, 416, 433. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 76, 154. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 683, 722. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 690, 697, 732, 741. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 682, 719. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 3. *Lines:* 92, 94, 96. *Example:* parenthesised sequence.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 174, 277, 442. *Example:* the argmax is written two ways and with two different relations. `\argmax` - the series MathJax macro, which renders as `arg\,max` - appears at 174, 496 and 670, while `\arg\max` appears at 277 and 442, and the two produce visibly different operator spacing in adjacent displays. More substantively, line 174 is careful to write `\sigma(x) \in \argmax_{a \in \Gamma(x)}` because the argmax is a set and the greedy policy is a selection from it, and then 277 and 442 write `\sigma(x) = \arg\max ...` and drop exactly that distinction.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 489, 558, 562. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 494, 513. *Example:* the point that $\max_{a'}$ in the update target is a value and not an instruction about the next action is made five times in fourteen lines: 'It is tempting to read the $\max_{a'}$ ... as prescribing the manager's next action' (494-496), 'But the $\max$ plays a different role' (498), 'This scalar enters the update as part of the target value' (503), 'Which action the manager *actually takes* at time $t+1$ is a separate decision' (505), 'In short, the $\max$ is doing the work of finding the optimum; it does not dictate the action that the manager actually takes' (507) - and then a sixth time at 513-515 in the next subsection. The distinction is worth making; it is not worth six paragraphs, and the code at 616-635 already labels it in place with `best_next` against `a_next`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 273, 397, 466, 709. *Example:* bold is used for emphasis three times, which is the pattern the rule gives as incorrect: 'can an agent **learn** the optimal policy without knowing the model?' (397), 'Notice what is **not** required' (466), 'All panels use the **same demand sequence**' (709) - all three want italic. And `**$v$-greedy policy**` is bolded twice, at its definition (171) and again 100 lines later at 273 ('Recall that, given a value function $v$, the **$v$-greedy policy** is computed via'), where 'Recall' already tells the reader it is not new. The genuine definitions in the file - **Q-function** (411), **Q-table** (486), **behavior policy** (511), **off-policy** (517), **optimistic initialization** (556), **S-s pattern** (371) - are all correctly bolded once, so the convention is understood and these four are slips.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 350. *Example:* value function iteration produces `v_star` and `σ_star` at 347 and neither is plotted. The only figure in the exact-solution half of the lecture is a simulated inventory path (390), so the S-s policy described in prose at 371-373 is never shown as a policy, and the claim at 562 that '$v^*$ ranges from about 13 to 18' - the number that justifies initialising the Q-table at 20 - cannot be checked by the reader, because $v^*$ does not appear in a figure until line 685, 120 lines later. A two-panel plot of $v^*(x)$ and $\sigma^*(x)$ immediately after 347 would fix all three.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 490. *Example:* 2 spaces.


## Strengths

- The three-item plan at 58-62 is delivered in order and in full: VFI (154-392), the Q-factor Bellman equation (406-443), Q-learning with a convergence demonstration (446-747) - and the third promise, 'show the learned policy converges to the optimal one', is discharged by two comparisons rather than an assertion, the value/policy overlay at 683-701 and the four inventory paths at 719-747.
- The panel comparison at 719-747 holds the demand sequence fixed across all four policies with one seed (`sim_seed = 5678`, 726, passed to every `sim_inventories` call), and line 709 tells the reader that is what makes the panels comparable - the differences really do reflect only the policy.
- The learning rate is justified rather than chosen: $\alpha_t = 1/n_t(x,a)^{0.51}$ (534), the exponent is tied to the Robbins-Monro conditions with a link (536), and the code implements exactly that, incrementing the visit count before using it (626-627).
- Optimistic initialization is explained mechanically - every untried action looks good, so trying it disappoints the agent and pushes it elsewhere (556-560) - and the constant is tied to the model rather than left magic: `q_init=20.0` (646) against a $v^*$ range of 13 to 18 (562).
- The exact and learned solutions are computed by structurally parallel code that a reader can diff: `T_kernel` (241-257) and `get_greedy_kernel` (285-303) differ only in recording the argmax, and line 281-282 says so explicitly.

## Recommended actions

1. Do not act on the 3 qe-math-002 findings (435, 457, 500): each is `a' \in \Gamma(x')` or `q_t(X_{t+1}, a')`, a next-period action inside a max, and no transpose is involved. They matter because Math scores 4/10, which is what puts this lecture in the HIGH priority bucket - see scanner_doubts.
2. Settle the blackboard-operator spelling: `\mathbb E` at 143, 416 and 433 needs braces (qe-math-010 (proposed), proposed), and line 86 writes the same operator a third way as `\EE`, the series MathJax macro defined in `_config.yml:114`. Pick `\mathbb{E}` for all four.
3. Settle the argmax: use one of `\argmax` (174, 496, 670) or `\arg\max` (277, 442) throughout, and restore `\in` in place of `=` at 277 and 442 - line 174 gets this right and the two later displays contradict it.
4. Plot $v^*$ and $\sigma^*$ directly after they are computed at 347. The S-s policy is described in words at 371-373 and the $v^*$ range asserted at 562, but neither is visible until the comparison figure at 685.
5. Sentence-case the two Title Case H2s - 'The Model' (76) and 'Solving via Value Function Iteration' (154) - and switch the three parenthesised sequences to curly brackets: $(D_t)_{t \geq 0}$ at 92 and 94, $(X_t)_{t \geq 0}$ at 96 (qe-writing-006 x2, qe-math-005 x3).
6. Figures: add mystnb caption/name metadata (682, 719), drop the 2 hand-set `figsize` (683, 722), move the 4 `set_title` calls into captions (690, 697, 732, 741) and add `lw=2` to the 7 line plots (380, 685, 686, 692, 693, 730, 739).
7. Cut '### The Q-table and the role of the max' (481-507) to about a third of its length, change the three bold emphases to italic (397, 466, 709) and drop the second bolding of $v$-greedy policy (273); then split the three two-sentence paragraphs (489, 558, 562), clear the double space at 490, and strip the trailing whitespace at 42, 44-46, 218, 498, 501 and 511 - the two-space endings at 498, 501 and 511 are hard line breaks in MyST and are almost certainly unintended.
