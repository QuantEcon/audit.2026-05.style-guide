# calvo

- **Series:** lecture-dp
- **File:** `lectures/calvo.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-005` ×8; `qe-writing-002` ×6; `qe-writing-004` ×4, +4 more. |
| Math         | 5.5/10 | `qe-math-002` ×10. |
| Code         | 7.5/10 | `qe-code-001` ×4; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×2; `qe-fig-001` ×5; `qe-fig-008` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 8/10  | `qe-link-002` ×4. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 1051, 1352, 1390, 1414, 1447. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 10. *Lines:* 272, 485, 489, 501. *Example:* apostrophe transpose `}'`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 28, 75, 318, 725, 749, 753. *Example:* the installation cell appears twice: lines 28-34 ('this lecture will need the following libraries') and lines 77-83 ('this lecture will use the following libraries'), running the identical `!pip install --upgrade quantecon`. Lines 749-750 repeat 708-709 word for word ('Time-variation of $\vec \mu$ chosen by a Ramsey planner is the telltale sign of the Ramsey plan's time inconsistency'). Line 75 has 'the recursive structure structure of the Ramsey problem'; line 753 has '**must** must choose'; lines 318 and 321 both read 'is the value of attained by the government'; line 725 has 'defined inequation `` {eq}`eq:barvdef` ``'. Four more of the same kind: 'plannner' (704), 'for computed in subproblem 1 above' (554), 'and of the continuation value' (1341), and 'respectfully' for 'respectively' (1361).
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 153, 220, 251, 329, 345, 646, 715, 753. *Example:* bold used for stress rather than definition at 251 (**costs** / **benefits**), 329 (**policy**), 345 (**output** / **input**), 646-647 ('**promised inflation** equals **actual inflation**'), 715 (the single word **is**) and 753 (**must**); line 153 uses '**Insight:**' as a bold pseudo-label. Line 220 is the reverse error - the term being defined, 'bliss level', is wrapped in double backticks and so renders as inline code rather than bold, and it is the name the lecture then relies on. The file's genuine definitional bolds (**time inconsistency** 38, **Ramsey plan** 55, **dynamic programming squared** 426, **promised inflation rates** 634) are doing the right job and are diluted by the rest.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 242. *Lines:* 38, 41, 43, 45, 46, 51, 57, 59, 61, 63, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 962, 1259, 1297, 1455. *Example:* line 962 assigns a lambda (E731) and writes a space after the unary minus, `lambda θ_array: - np.array([1, θ_array])`, with a backslash continuation that the surrounding parentheses make unnecessary; line 1259 puts a compound statement on one line, `if not isinstance(clqs, list): clqs, axes = [clqs], [axes]` (E701); line 1297 runs to about 90 characters (E501); line 1455 writes `T-1` unspaced where the same file spaces its other binary operators. Trailing whitespace is also scattered through the class body (923, 937, 947, 967, 998, 1001, 1008, 1010).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1263, 1463. *Example:* .set_title.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 67, 193, 288, 765. *Example:* raw link to python-intro.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 122, 153, 445. *Example:* `` {cite} `` in narrative flow: '.  `` {cite} ``'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 287, 416. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 432, 644. *Example:* the section that names the lecture's method points at the wrong two equations. 'Note on dynamic programming squared' (423-437) says the two Bellman equations are '`` {eq}`eq_old1` ``, which expresses how $\theta_t$ depends on $\mu_t$ and $\theta_{t+1}$' and '`` {eq}`eq_old4` ``, which expresses how value $v_t$ depends on $(\mu_t, \theta_t)$ and $v_{t+1}$'. But `eq_old1` (112) is the Cagan money-demand function $m_t - p_t = -\alpha(p_{t+1}-p_t)$ and `eq_old4` (189) is the state transition $x_{t+1} = Ax_t + B\mu_t$. The equations meant are `eq_old2` (136) and `eq_old8` (302). Both references resolve, so nothing breaks - the reader simply lands on the wrong display twice in the four lines that explain what 'dynamic programming squared' means. Separately, line 644 says '(Here an application of the Big $K$, little $k$ trick is again at work.)' - the trick has not appeared earlier in this lecture, is not explained, and is not linked.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 67, 193, 765, 817. *Example:* mid-sentence 'Control'.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 931. *Example:* spelled-out `beta`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1454. *Example:* plot() without lw=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 371. *Example:* 'Three timing protocols' (369-412) distinguishes three models along three stated dimensions - *what* a policymaker chooses, *when* it chooses, and what it *assumes* about how its choice affects expectations - and then delivers the nine resulting cells as three separate prose passages (373-378, 380-389, 396-412). The reader has to build the grid mentally, and the payoff of the whole lecture depends on holding it. A three-by-three table would do it in one block, and the lecture already renders LaTeX tables from pandas (`generate_table`, 1287-1300), so the machinery is present.


## Strengths

- 'Multiple roles of $\theta_t$' (681-696) is the conceptual payoff of the whole construction and it is stated compactly: the same symbol is the actual inflation rate in `` {eq}`eq_old3` ``, the public's expected rate in `` {eq}`eq_old2` ``, and a promise chosen at time 0 in `` {eq}`eq_old9` `` - and lines 692-696 name what that ambiguity illuminates (whether the government leads or follows the market, forward guidance, inflation targeting).
- Chang's simplifying insight is given as a reason rather than a step: lines 153-157 explain that $\theta_t$ intermediates how every future $\mu_{t+j}$ reaches time-$t$ real balances, so an equivalence class of continuation money-growth sequences delivers the same $\theta_t$ - which is exactly what licenses treating $\theta$ as the state in the sections that follow.
- The comparative statics are predicted before they are shown: 1367-1377 derives from the closed forms that changing $\beta$ must move $\theta_\infty^R$ and $\theta_0^R$ but leave $\theta^*$, $\theta^{CR}$ and $\theta^{MPE}$ alone, 1401-1405 says which of those change when $c$ moves instead, and 1421-1424 explains the $c \to 0$ limit by naming Calvo's wedge. The figures then confirm claims the reader has already been given.
- Every model in the lecture is an attribute of one `ChangLQ` instance built by six methods called in a documented order (908-918), so the Ramsey, constrained-Ramsey and Markov-perfect numbers that appear side by side in the tables are guaranteed to come from the same parameter set rather than from three separate calibrations.
- The five $\theta$ landmarks get their colours and labels from a single helper, `compute_θs` (1029-1043), which every figure and every table calls - so $\theta^*$, $\theta_\infty^R$, $\theta^{CR}$, $\theta_0^R$ and $\theta^{MPE}$ keep the same colour and the same label across the whole lecture, including across the parameter sweeps at 1352, 1390 and 1414.
- The Ramsey problem is split into two explicitly numbered subproblems (462, 573), the split is justified by reference to `` {doc}`dyn_stack` `` and Ljungqvist-Sargent chapter 19 (445), and subproblem 2 is carried through to a closed form for $\theta_0^R$ (600-610) rather than handed to a solver.
- The `{note}` at 415-420 says precisely which sibling lecture handles the fourth timing protocol (`` {doc}`calvo_abreu` ``), what distinguishes it, and which literature it belongs to - so a reader who wonders about credible policy is not left guessing.

## Recommended actions

1. Clear the 242 double spaces (qe-writing-008). This is by far the largest item in the file - at 242 occurrences in 1557 lines they are in most paragraphs, and several sit inside `{eq}` reference sentences where the reader is following closely.
2. Fix the two mis-targeted references at 432-435: `eq_old1` should be `eq_old2` and `eq_old4` should be `eq_old8`. These are the only two equations named in the section that defines the lecture's central technique.
3. Delete one of the two identical install cells (28-34 and 77-83) and the duplicated paragraph at 749-750, which repeats 708-709 verbatim.
4. Replace the 10 apostrophe transposes with `^\top` at 272, 485, 489 and 501 - these are genuine transposes of $\begin{bmatrix} 1 & \theta_t \end{bmatrix}$ and of $x_t$, $A$, $B$, unlike the derivative and next-period primes elsewhere in this series (qe-math-002 x10).
5. Fix `\max` where `\arg\max` is meant at line 739: as written $\mu^{CR} = \max_{\bar\mu} V(\bar\mu)$ says the money growth rate equals the maximised value, and line 745 then feeds $\mu^{CR}$ back into $V(\cdot)$ as an argument. The same slip is worth checking at 578 and 589, where $V^R = \max_{x_0} J(x_0)$ is correct but sits two lines from $\theta_0 = \theta_0^R$.
6. Convert the 4 raw URLs (67, 193, 288, 765). Three point at `lqcontrol`, which is a lecture in this same series, so they want `{doc}`lqcontrol``; the fourth points at `markov_perf`, which lives in lecture-python.myst and wants `{doc}`intermediate:markov_perf``. Note the host used, `python-intro.quantecon.org`, is not in lecture-dp's intersphinx mapping at all (qe-link-002 x4).
7. Finish the smaller items: drop the stale equation numbers from the code comments at 934, 938 and 941 ('(41.16)', '(41.17)', '(41.18)' refer to a numbering this lecture no longer has); move the 2 embedded titles at 1263 and 1463 into captions and drop the 5 hand-set `figsize=` (1051, 1352, 1390, 1414, 1447) and add `lw=2` at 1454 (qe-fig-003 x2, qe-fig-001 x5, qe-fig-008 x1); lower-case the 4 mid-sentence capitals (67, 193, 765, 817) and switch the 3 in-flow citations (122, 153, 445) to `{cite:t}`; and fix the typos listed above plus the code slips at 962, 1259, 1297 and 1455.
