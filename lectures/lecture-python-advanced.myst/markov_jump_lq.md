# markov_jump_lq

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/markov_jump_lq.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 6.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-003` ×8; `qe-writing-002` ×4; `qe-writing-009` (proposed) ×1, +2 more. |
| Math         | 3/10  | `qe-math-002` ×47; `qe-math-010` (proposed) ×2; `qe-math-011` (proposed) ×1, +1 more. |
| Code         | 7/10  | `qe-code-001` ×40. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×6; `qe-fig-005` ×2; `qe-fig-008` ×12. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 40. *Lines:* 319, 411, 506, 673, 766. *Example:* 40 items in four countable classes. (i) Eight statements end in a semicolon to suppress notebook output - `ex1_a.stationary_values();` at 411, 510, 520, 537, 579, 603, 648, 704 - which PEP8 rules out (E703); assigning the result or calling it in its own cell does the same job. (ii) Fourteen lines write a binary minus with no surrounding spaces inside the transition matrices, `np.array([[1-λ, λ], [λ, 1-λ]])` at 506-507, 516-517, 533-534, 575-576, 599-600, 644-645 and 700-701. (iii) Eight dictionary literals omit the space after the colon, `{"f1_vals":[0.5, 1.]}` at 766, 776, 895, 901, 907, 913, 919, 925. (iv) 319 and 844 write `f1_vals=[1. ,1.]`, with the space before the comma rather than after. Beyond the count: both `construct_arrays` functions take mutable lists as default arguments (319-321, 844-849); 341-342 and 866-867 write `- f1_vals[i] / 2` with a space after the unary minus; 673-675 concatenate label strings with unspaced `+`; 683 writes `min(k_star)+(max(k_star)-min(k_star))/20`; 505 and 515 use a single space before an inline comment; and quote style alternates between `'3d'` (611, 710) and `"b"`/`"r"` (613-615) throughout. 447 also hard-codes `ax.scatter([0.5, 0.5], [0.5, 0.5])` for the fixed point that `k_star` already holds and that line 448 reads from `k_star[0]`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 488, 550, 619, 660, 682, 716. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 443, 444, 448, 451, 485, 545, 546, 655, 656, 672, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 47. *Lines:* 81, 94, 108, 114, 115, 122, 128, 169, 191, 197, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 153, 288. *Example:* non-blackboard `{\rm Prob}`.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 8. *Lines:* 115, 205, 219, 302, 474. *Example:* the review section and the extension it feeds do not agree with each other, and the central Bellman equation is broken in four ways at once. (i) 203-210 opens `\max_u` for the problem that 94 and 163 both state as a `\min`; keeps $u' Q_i u$ and $2u'W_ix$ positive while $x'R_ix$ is negated, so the three terms of the same loss carry two different signs; leaves a stray `x` inside the expectation, `(A_i x + B_i u + C_i w)' P_j (A_i x + B_i u + C_i w) x + \rho_j`; and carries a stray `&` alignment marker in a single-row `aligned`. (ii) The Riccati equation at 113-116 writes `(Q + \beta B P B )^{-1} (\beta B P A + W)` with the transposes on $B$ dropped, where the same equation at 128 has `B' P B` and `B' P A`. (iii) 219 writes $(Q + \beta B_i' P_j B_i)^{-1}$ with no Markov-state subscript on $Q$, though every other matrix in the display carries one and 231 has $Q_i$. (iv) 200-201 and 212-213 index the value functions "for $i = 1, \ldots, n$", but $n$ is the dimension of $x_t$ (57, 72) and the number of Markov states is $N$ (54, 145); 213 also leaves the symbol outside the math, "$\rho_i, i = 1, \ldots$, n". (v) 302 adds the adjustment-cost term, $\ldots x_t + \underbrace{d_{s_t}}u_t{}^2$, where 298 subtracts it and the Example 2 counterpart at 809-816 wraps the whole quadratic in one minus sign. (vi) 262 asks the reader to maximise $r$ where 94 and 163 minimise it. (vii) 474 states the comparison the paragraph exists to make as $|u_{t,2}| > |u_{t,2}|$. (viii) Every figure label uses an overbar state, $\overline{s}_1$ and $\overline{s}_2$ (443-444, 545-546, 655-656, 673-675) and $F(\overline{s}_t)$ (659, 715), that appears nowhere in the text - which writes $s_t \in [1,2,\ldots,N]$ - and the same axis is labelled $F_{s_t}$ at 549 and 618.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 57, 59, 64, 99, 294. *Example:* 3 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 434, 478. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 37. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 281, 298, 785. *Example:* the same six parameters are written two ways throughout. Example 1 introduces them as subscripts, $f_{1,s_t}$, $f_{2,s_t}$, $d_{s_t}$ (268, 298-302, 373-390, 721-737), then 281-282 states their signs as $f_1(s_t) > 0$, $f_2(s_t) > 0$, $d(s_t) > 0$, and Example 2 switches wholesale to the function form with `\left(\right)` armour - $f_{1}\left(s_{t}\right)$, $\alpha_{0}\left(s_{t}\right)$, $\rho\left(s_{t}\right)$, $\sigma\left(s_{t}\right)$ at 785 and 808-840 - while the prose immediately around it (892-925) reverts to $d_{s_t}$, $f_{1,{s_t}}$, $\rho_{s_t}$, $\sigma_{s_t}$. The code has one name for each (`f1_vals`, `α0_vals`, `ρ_vals`), so the second notation buys nothing. 298 and 302 also write the square as `u_{t}{}^{2}`, with an empty group before the superscript, where 795 writes $k_t^2$ plainly; and the Gaussian is `{\cal N}(0,I)` at 180 but plain $N\left(0,1\right)$ at 785, so the lecture already contains the spelling that qe-math-011 (proposed) asks for.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 180. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 39, 41, 43. *Example:* `` {cite} `` in narrative flow: 'in `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 469, 736, 750, 762. *Example:* 469-471 names the same state twice in one sentence: "the optimal decision rule in Markov state $2$, in which the adjustment cost is lower, makes $k_{t+1}$ a flatter function of $k_t$ in Markov state $2$". Three further sentences drop words: 736-737 "So there are different $s_t$-dependent optimal static $k$ level in different states"; 749-750 "each Markov state becomes close to absorbing state"; 761-762 "optimal $k$ levels in the two states Markov jump state". 473-476 then explains the mechanism through the broken inequality at 474, so the paragraph's conclusion rests on a comparison that is not stated.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 608, 895, 925. *Example:* the last section of the lecture is six identical stanzas - 892-925 - each a one-line header ("Only $d_{s_t}$ depends on $s_t$.", "Only $f_{1,{s_t}}$ depends on $s_t$.", and so on) followed by a single `run(...)` call, and each `run` emits five figures (three 2-D panels and two 3-D surfaces, 652-717). That is roughly thirty figures with no caption, no `name:`, titles that read only "coefficient on k" or "coefficient on constant term", and not one sentence of prose after 776 saying what changes between them; the lecture's own model for how to do this is 459-476 and 555-561, where two figures are read carefully. The 3-D panels are also drawn in a way that cannot be read: 613-615 and 711-712 call `plot_surface` twice with `color="b"` and `color="r"` and no `alpha`, so the nearer surface hides the farther one and the reader cannot see the crossing that the surfaces exist to show, and there is no colour bar or legend to say which is the high-adjustment-cost state. Nothing in the lecture is an admonition, including the parenthetical convention at 156-158 about switching between $s_t$ and $i$, which governs every equation that follows.

### Low severity
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 179. *Example:* i.i.d..


## Strengths

- The lecture front-loads exactly what the reader needs to check the extension against: 67-129 restates the ordinary LQ problem - the two triples $(R,Q,W)$ and $(A,B,C)$, the objective, the decision rule, the Riccati equation, the constant $\rho$ and the gain $F$ - and then 133-233 rebuilds each of those five objects with Markov-state subscripts, in the same order, so the extension can be read line against line.
- The convention that makes the algebra legible is stated explicitly before it is used: 149-158 says that $i$ is today and $j$ is tomorrow and warns that the lecture will switch between $s_t$ and $i$, which is why the stacked Riccati system at 216-233 can be read at all.
- Example 1 is chosen so that its answer is known independently: $k^*_{s_t} = f_{1,s_t}/(2f_{2,s_t})$ is the static optimum (737), the code computes it (349-351), and the decision-rule figure at 434-456 plots the closed-loop map against the 45-degree line so the reader can see both rules share the fixed point $k = 0.5$ that the formula predicts (465-467).
- The comparative-statics sequence is genuinely a sequence: the strictly periodic $\Pi_1$ (366-371), the symmetric one-parameter family $\Pi_2$ (497-502) plotted against $\lambda$, and the asymmetric two-parameter family $\Pi_3$ (566-571) plotted as a surface over $(\lambda, \delta)$ - each transition matrix changing one thing about the previous one.
- The distinction that carries the economics is named and then measured: 741-759 separates $k^*_{s_t}$, the static optimum in each state, from $k^{target}_{s_t}$, the fixed point of the optimal policy, explains why they coincide as $\lambda \to 0$ and diverge as $\lambda \to 1$, predicts the switch at $\lambda = 0.5$, and the figure at 664-685 plots both pairs with a vertical line drawn and annotated at exactly that value.
- The eight comparative-statics cases are driven through one wrapper (627-718) rather than eight copies of the same forty lines, and its `if state_vec == ["k", "constant term"]` guard at 666 keeps the Example 1-only figure out of the Example 2 runs.
- Example 2 adds exactly one state variable and says what it is for: $w_t$ is "a rental rate or tax rate that the decision maker pays each period for $k_t$" (788-789), which is why it enters the payoff as the product $w_tk_t$ (795) and shows up as the two $\frac{1}{2}$ entries of $R(s_t)$ at 811-813.
- The lecture closes by naming where the machinery is actually used - the three tax-smoothing lectures at 930-935 - and 43 has already noted that the periodic seasonality models of Hansen-Sargent chapter 14 are a special case, so the reader knows what the method buys.

## Recommended actions

1. Rewrite the Bellman equation at 203-210: it is stated as a maximum of a loss, three terms of the same loss carry inconsistent signs, a stray `x` sits inside the expectation after the quadratic form, and a stray `&` remains in a one-row `aligned`.
2. Restore the transposes dropped from $\beta B P B$ and $\beta B P A$ at 115 (cf. 128), add the Markov-state subscript to $Q$ at 219 (cf. 231), fix the sign of the adjustment-cost term at 302 (cf. 298 and 809-816), and settle whether $r$ is minimised (94, 163) or maximised (262).
3. Replace $n$ with $N$ as the number of Markov states at 200-201 and 213, where $n$ already denotes the dimension of $x_t$, and pull the ", n" at 213 back inside the math.
4. Fix the inequality at 474, which reads $|u_{t,2}| > |u_{t,2}|$ and is the only support for the paragraph's conclusion.
5. Give the thirty figures produced by the six `run` calls at 895-925 something to be read by: either a paragraph per case saying what changes, or one combined figure per parameter; and make the 3-D surfaces legible by adding `alpha` and a legend to the `plot_surface` calls at 613-615 and 711-712, where two opaque surfaces currently occlude each other.
6. Define the overbar state notation used in every figure label ($\overline{s}_1$, $\overline{s}_2$, $F(\overline{s}_t)$, $k^{target}(\overline{s}_i)$ at 443-444, 545-546, 655-675, 715) or drop it in favour of the $s_t$ of the text, and make the axis label consistent with 549 and 618.
7. Settle on subscript notation for the Markov-state-dependent parameters ($f_{1,s_t}$ rather than $f_1\left(s_t\right)$, which alternate at 268, 281, 785, 808 and 892-925), and run the PEP8 sweep: the 8 trailing semicolons, the 14 unspaced `1-λ` expressions, the 8 dict literals missing a space after the colon, the two `[1. ,1.]` defaults, and the mutable list defaults at 319-321 and 844-849; then the mechanical load - 45 apostrophe transposes to `\top`, the 8 spelled-out Greek `beta=` arguments, the 6 embedded `set_title` calls moved to `mystnb` captions with `name:` fields, the 12 `plot()` calls without `lw=2`, the raw link at 37, and the three citations in author position (39, 41, 43).
