# calvo_abreu

- **Series:** lecture-dp
- **File:** `lectures/calvo_abreu.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×7; `qe-writing-002` ×6; `qe-writing-003` ×2, +3 more. |
| Math         | 9/10  | `qe-math-004` ×1. |
| Code         | 7/10  | `qe-code-001` ×3; `qe-code-003` ×1; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-008` ×2; `qe-fig-001` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 40, 45, 86, 262, 521, 602. *Example:* lines 40 and 42 carry the same 30-word clause twice - 'what government authorities who set $\mu_t$ at time $t$ believe how future government authorities who set $\mu_{t+j}$ for $j > 0$ will respond to their decisions' - and both are ungrammatical ('believe how' for 'believe about how'). Line 45 is repeated almost verbatim at 149, and line 47 at 151, both times without a full stop the second time; both also read 'there is sequence of' for 'there is a sequence of'. Line 86 is an ungrammatical parenthetical ('an assumption of **rational expectations** that becomes equivalent to **perfect foresight**') where the parallel passage in `` {doc}`calvo` `` line 122 is correct. Line 262 reads 'That credible plans come in pairs threaten to bring an explosion'. Line 521 says 'We have computed outcomes for this plan' sixty lines before the computation. Line 602 introduces a new term by accident - 'the inequalities required for $\vec \mu^A$ to be **self-confirming**' - where 'self-enforcing' is the term used at 269, 292, 300, 317 and 589.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 7. *Lines:* 117, 151, 238, 292, 300, 589, 684. *Example:* the file re-bolds terms it has already defined, which is the 'overuse of emphasis formatting' arm of the rule. '**self-enforcing**' is bolded on first definition at 269 and then again at 292, 300, 589 and 684; '**sustainable**' / '**credible**' are bolded at 47, then again at 151, 153, 238 and 323; '**Ramsey plan**' at 35 and again at 519. After the fifth bolding of the same word the formatting no longer marks anything. Line 117 also uses '**Insight:**' as a bold pseudo-label where a real heading or plain text would do.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 94. *Lines:* 33, 35, 37, 39, 40, 45, 47, 49, 51, 53, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 453, 549, 622. *Example:* the file spaces its exponentiation operator where the rule asks for the tight `a**b` form, and disagrees with itself about it: `(clq.α / (1 + clq.α)) ** np.arange(T)` at 549, `clq.β ** np.arange(T)` at 556, `(-clq.θ_A) ** 2` and `clq.μ_A ** 2` at 558, `clq.β ** t` at 561 and `** 2` at 566 are all spaced, while line 415 writes `self.α**2` and line 622 writes `)**2` tight. Line 453 assigns a lambda (E731) with a space after the unary minus and a backslash continuation the enclosing parentheses make unnecessary; line 622-623 over-indents a backslash continuation that is likewise inside parentheses.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 275. *Example:* install cell at line 275 of 688 (not near the top).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 573, 579. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 196. *Example:* {\bf.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 39, 357. *Example:* `` {cite} `` in author position: '`` {cite}`Calvo1978` `` showed'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 203. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 213, 679. *Example:* line 213 contains two broken links in one clause: 'described in equation `` {eq}`eq_old6` `` in quantecon lecture `` {cite}`Calvo1978` ``'. `eq_old6` is a label in calvo.md and does not exist in this file (its labels are `eq_old1_new`, `eq_old2_new`, `eq_old3_new`, `eq_old10`, `eq_old100a`, `eq_old11`), so the reference resolves to nothing - and per spec §5 a broken `{eq}` ref is Critical. The same sentence then uses a bibliography citation, `{cite}`Calvo1978``, where the text plainly means the quantecon lecture, i.e. `` {doc}`calvo` ``. The government's one-period return function is the object the entire enforcement argument rests on, and the reader cannot reach its definition. Second, the lecture stops mid-section: lines 679-687 are a summary ('We have also computed **credible plans** for a government or sequence of governments...') sitting under the heading 'Whose plan is it?', with no conclusion heading and nothing after it, so a conceptual discussion ends by summarising a different part of the lecture.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 422. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 571. *Example:* figsize=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 262. *Example:* lines 255-271 describe a branching structure and then its collapse, entirely in prose: credible plans 'come in pairs' (one continuation if the government confirms, one if it disappoints), 'each credible plan itself consists of two credible plans', 'therefore, the number of plans underlying one plan is unbounded' - and then Abreu's insight is that a single self-enforcing plan can stand in for the whole tree. That is a binary tree collapsing to a loop, and it is the conceptual pivot of the lecture. The file's one figure (571-584) plots $\theta^A$, $\mu^A$ and $V^A$ paths; the structure that makes those paths meaningful is never drawn.


## Strengths

- The within-period timing protocol is spelled out as six ordered steps (185-208) that state exactly what the private sector expects entering $t$, what the government is free to do, and which continuation beliefs each of the two branches produces - including that a deviation resets expectations to $\vec \mu^A$ and hence to $\theta_0^A$. This is what makes the model well defined, and it is written out rather than gestured at.
- The whole enforcement problem is traced to one inequality: $s(\theta, 0) \geq s(\theta, \mu)$ at 216-218, with the consequence stated immediately - 'whenever the policy calls for the government to set $\mu \neq 0$, the government could raise its one-period payoff by setting $\mu = 0$' - so the temptation has a single, checkable source.
- Self-enforcement is defined by a displayed pair of inequalities `` {eq}`eq_old10` `` and then verified twice in code, each time as a boolean rather than a figure to squint at: `np.all(clq.V_A[0:20] > clq.V_dev[0:20])` at 606 for the Abreu plan, and `check_ramsey` at 617-627 for the Ramsey plan's credibility given it.
- The carrot-stick construction is given a two-word intuition with the mapping to the model made explicit (366-367: 'Low one-period utilities early are a *stick*', 'High one-period utilities later are a *carrot*'), and the code implements exactly that - `np.append(np.full(T_A, μ_bar), clq.μ_series[:-T_A])` at 546 is the stick concatenated with the Ramsey plan.
- 'Whose plan is it?' (661-675) raises the interpretive question the formalism leaves open - does the government choose $\vec \mu$ or merely confirm forecasts of it - and gives the argument on each side, pointing at the specific inequality `` {eq}`eq_old100a` `` that supports the second reading rather than leaving it as a rhetorical flourish.
- The lecture is precise about which timing protocol it is replacing: 131-138 restates the three dimensions along which `` {doc}`calvo` ``'s three models differ, 143-147 recalls what a Markov perfect policymaker believes, and 149 states the one belief this lecture changes - so the reader knows exactly what moved.

## Recommended actions

1. Fix the two broken links in line 213. `{eq}`eq_old6`` points at a label that exists only in calvo.md, so the definition of $s(\theta, \mu)$ - the function every inequality in this lecture uses - is unreachable; either restate the equation here with its own label or link to the sibling lecture's section. In the same clause, `{cite}`Calvo1978`` should be `{doc}`calvo``, since the sentence says 'quantecon lecture'.
2. Replace the copy-pasted `ChangLQ` class at 395-506 with a `:load:` of a shared file. It is a verbatim duplicate of calvo.md lines 904-1015, stale comments included ('(41.16)', '(41.17)', '(41.18)' at 425, 429, 432 refer to an equation numbering neither lecture has), so a hundred-line class is now maintained in two places. The amss lectures in this series already do this correctly with `_static/lecture_specific/.../*.py`.
3. Clear the 94 double spaces (qe-writing-008) and delete the duplicated passages: 40 against 42, 45 against 149, and 47 against 151 - in each pair the second copy adds nothing and one of the two is missing its full stop.
4. Move the install cell from line 275 to the top of the lecture, before the Overview. It currently sits at line 275 of 688, after eight sections of theory, so a reader who runs cells in order hits `np` and `LQ` usage in the middle of the file (qe-code-003 x1).
5. Settle the value-function notation. The math writes $v_j^A$ and $v_j^{A,D}$ (306-307, 592, 597, 600) while the code and figure labels write `V_A`, `V_dev`, `$V^A_t$` and `$V^{A, D}_t$` (561, 564, 573, 576) - and $V(\cdot)$ already means the constant-$\mu$ value function in `` {doc}`calvo` ``. Also fix the index mismatch at 597, where the left side is subscripted $t$ and the right side $j$, and replace 'self-confirming' at 602 with 'self-enforcing'.
6. Write `\mathbb{R}` in place of `{\bf R}` at line 196 (qe-math-004 x1), switch the two author-position citations at 39 and 357 to `{cite:t}` (qe-ref-001 x2), drop the hand-set `figsize=(8, 12)` at 571 and add `lw=2` at 573 and 579 (qe-fig-001 x1, qe-fig-008 x2).
7. Give the lecture an ending. The summary at 679-687 currently sits inside 'Whose plan is it?' with nothing after it; make it its own concluding section, and make the `**` spacing consistent with the tight form used at 415 and 622.
