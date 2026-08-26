# rs_inventory_q

- **Series:** lecture-python.myst
- **File:** `lectures/rs_inventory_q.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×4; `qe-writing-005` ×8; `qe-writing-001` ×2, +5 more. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×5. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×7; `qe-fig-005` ×4; `qe-fig-008` ×9, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 151, 153, 212, 625, 653, 678. *Example:* 153 names the geometric mass function `demand_pdf` and returns `(1 - p)**d * p`, contradicting the lecture's own line 111 ("$\phi(d)$ denotes the demand probability mass function") - `demand_pmf` is the name the prose implies. 151 closes the multi-line signature at an indent of 4, `    ) -> RSModel:`, which matches neither the opening line nor the 8-space argument block (E124). 212 and 254 unpack all eight NamedTuple fields to use six, leaving `x_values` and `p` bound and unused (F841) where `model.d_values` would read better. Exponentiation spacing is inconsistent: 154 writes `(1 - p)**d` as the rule asks, while 625 and 627 write `best_next ** β` and `n[x, a] ** 0.51`. 653 runs to 84 characters (E501). 678 writes `-(1/γ_base) * np.log(...)` with no spaces around the division where 202, 243 and 627 all write `1.0 / γ`. And 644 carries a default `n_steps=20_000_000` that 663 always overrides and that contradicts the "5 million" of 658 - dead, and misleading to anyone calling the function directly.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 318, 323, 360, 692, 699, 728, 738. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 312, 313, 358, 687, 688, 694, 695, 726, 736. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 66, 84, 418, 461, 479. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 381, 387, 395, 434, 439, 517, 522, 533. *Example:* the file contains no bold definition at all and fourteen bold emphases. Eight are plain emphasis that the rule assigns to italic: **deterministic** (381), **revenue** (387), **caps the randomness of revenue** (395-396), **decreasing** (439), **minimum** (440), **positive** (517), **minimize** (518), **power** (522). Six more are whole-phrase bold used as pseudo-headings inside the prose and inside a numbered list: **Step 1.** (434), **Step 2.** (455), **Initialize** (533), **At each step:** (535), **Extract the greedy policy** (547), **Compare** (549). Meanwhile the terms actually being defined go unmarked - "certainty equivalent" (115, 120, 165), "Q-factor" (412), "optimistic initialization" (551), "risk-sensitivity parameter" (113) - and the one place the italic marker is used, 557 (*minimizes*, *below*), is correct emphasis, so the file has the two markers exactly the wrong way round.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 59, 124, 368, 405. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 308, 347, 685, 717. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 307, 345, 684, 714. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 557, 559. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 36, 555, 557, 758. *Example:* 36-40 spends two sentences and 40 words on one idea, the first padded ("Injection of risk-sensitivity acknowledges the fact that, in incomplete markets with financial and informational frictions, firms typically take risk into account in their decision making") and the second a restatement ("In other words, the actions of firms are not, in general, risk neutral"). 555 is 33 words around a mid-sentence em-dash parenthetical, and 557 packs 55 words and two sentences into one block. The Conclusion (758-774) is the third statement of the same three points: that risk-sensitive firms order less aggressively (already at 295 and 370-371), that the update replaces addition with multiplication and max with min (already at 517-523 and restated at 584-586), and that the agent needs only states, actions and profits (already at 525-526).
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 45, 542, 559, 712. *Example:* the roadmap at 45-47 lists only value function iteration and the risk-sensitivity comparative static - "We show how the model can be solved using value function iteration. We then investigate how risk sensitivity affects the optimal policy" - and never mentions Q-learning, which is the second half of the lecture (405-756, 350 of 774 lines) and is in the H1 title at 23. Second, $n$ names two things inside the Q-learning section: visit counts at 534 and 542 ($n_t(x,a)$, and `n = np.zeros((K+1, K+1))` in the kernel at 593), then the number of training steps at 658 ("We run $n$ = 5 million steps ... and $n$") and `n = 5_000_000` at 661. Third, 559-560 asserts that "the true Q-values are on the order of $\exp(-\gamma v^*) \approx 10^{-8}$ to $10^{-6}$" and initialises at $10^{-9}$, but nothing in the lecture computes that range and it holds only at $\gamma = 1$ - at the $\gamma = 0.01$ case solved at 298-304 the Q-values are of order 1, so a reader who reuses `q_init=1e-9` after changing $\gamma$ gets a table initialised far *above* the truth, reversing the optimism the section is about. Fourth, 707-712 says "The top panel shows the optimal policy from VFI" and "how the agent's policy evolves", but every panel of the figure at 714-744 is a simulated *inventory path*, not a policy; the policies themselves are plotted only for the final Q-table (694-699).
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 471. *Example:* mid-sentence 'Step'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 368, 559, 714. *Example:* the section that carries the lecture's whole intuition, "Interpreting the Outcomes" (368-402), has no figure. Its claim is about a distribution: revenue is $\min(x, D)$, which "inherits the full variance of demand" when $x$ is high (389-390) and is "nearly deterministic, capped at the inventory level" when $x$ is low (392-393). One panel of $\mathrm{sd}[\min(x, D)]$ against $x$ on the demand grid already in `model.d_values`, or two histograms of $\min(x, D)$ at a low and a high $x$, would settle in a picture what 373-402 argues in eleven paragraphs against a reader's first instinct. Second, the convergence claims at 746-751 ("barely explored", "still differs noticeably", "nearly indistinguishable") are asked of three noisy 200-period paths at 714-744; $\max_x |\sigma_{\rm snap}(x) - \sigma^*(x)|$ against training step is one line and is the quantity the sentences actually assert. Third, the two passages that most need setting apart - the log-sum-exp shift at 165-178 and the reversed sense of "optimistic" at 551-560, where the $10^{-9}$ constant is easy to copy wrongly - are plain prose; the lecture uses no admonition anywhere.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 557. *Example:* 2 spaces.


## Strengths

- The certainty equivalent is never left abstract: 92-94 gives $\psi(t) = \exp(-\gamma t)$ and $\psi^{-1}(y) = -\frac{1}{\gamma}\ln y$, 96-109 substitutes both to get an explicit sum over the demand grid, and 189-202 is that sum term for term - so `T_rs_kernel` is checkable against the displayed equation without guessing.
- 167-178 states the log-sum-exp reformulation the implementation depends on, names the shift $m = \max_i(-\gamma z_i)$, and links the definition; 198-202 then computes exactly that, so the numerically stable form is derived in the lecture rather than appearing as an unexplained `np.max` in the inner loop.
- The Q-factor derivation at 430-487 turns on one observation and isolates it: because $\psi^{-1}$ is decreasing, the max over $a$ of $\psi^{-1}(q(x,a))$ is attained at the *min* over $a$ of $q(x,a)$ (439-441). That sign flip is what makes every later `argmin` correct, and it is stated as its own step with the consequence $\exp(-\gamma v^*(x)) = \min_a q(x,a)$ (452) written out before being substituted.
- 515-526 lists the four ways the risk-sensitive update differs from the risk-neutral one - Q-values positive rather than signed, argmin rather than argmax, reward entering as $\exp(-\gamma R_{t+1})$ rather than additively, continuation value entering as a power $(\min_{a'} q_t)^\beta$ rather than $\beta \max_{a'} q_t$ - which is precisely the diff a reader arriving from `` {doc}`inventory_q` `` needs.
- 551-560 explains why "optimistic" reverses direction here: since the policy minimises $q$, the table must start *below* the truth, and the mechanism is given - trying an action pushes its entry up, making it look worse and sending the agent elsewhere.
- 373-402 meets the counter-intuitive result head on ("At first glance this may seem surprising: wouldn't holding more inventory reduce variance by ensuring the firm can always meet demand?") and answers it by splitting profit into a deterministic ordering cost chosen before the shock and a random revenue $\min(x, D)$, then adds the second, continuation-value channel at 400-402 rather than stopping at the first explanation.
- The three-$\gamma$ comparison is a controlled experiment: 298-304 solves the same model at $\gamma \in \{0.01, 1.0, 2.0\}$, the value functions and policies go on shared axes (310-323), and the simulated paths at 354-361 all draw from `np.random.default_rng(sim_seed)` with `sim_seed = 5678` (351) so the three panels differ only in the policy. 721 and 724-735 reuse the same seed for the VFI path and every Q-learning snapshot, and 710 says so.
- 677-681 restricts the argmin to feasible actions, `q_table[x, :K - x + 1]`, with a comment saying why - the Q-table is square $(K+1)\times(K+1)$ while $\Gamma(x) = \{0,\dots,K-x\}$, so the unrestricted `argmin` would return infeasible orders read off never-visited cells still sitting at `q_init`.

## Recommended actions

1. Add Q-learning to the roadmap at 45-47 - it is half the lecture and it is in the title, but the introduction promises only value function iteration and the risk-sensitivity comparative static.
2. Swap the two emphasis markers: italicise the eight bold emphases (381, 387, 395, 439, 440, 517, 518, 522), bold the terms actually being defined ("certainty equivalent" 115, "Q-factor" 412, "optimistic initialization" 551), and turn the six bold pseudo-headings (434, 455, 533, 535, 547, 549) into real structure.
3. Move the seven `set_title` strings (318, 323, 360, 692, 699, 728, 738) into `mystnb: figure: caption`/`name` metadata on the four figure cells (307, 345, 684, 714) so the figures can be cross-referenced, and set `lw=2` on the nine `plot` calls.
4. Add the missing picture to "Interpreting the Outcomes": $\mathrm{sd}[\min(x, D)]$ against $x$ over `model.d_values`, which is the claim of 387-393 in one panel.
5. Say what the $10^{-9}$ initialisation at 560 depends on. The stated range $10^{-8}$ to $10^{-6}$ is not derived and holds only at $\gamma = 1$; either compute $\exp(-\gamma v^*)$ from the VFI solution already in hand at 288 and set `q_init` from it, or state the restriction.
6. Fix the two `\mathbb E` occurrences that are missing their braces in each of 66, 84, 418, 461 and 479, and lower-case the three Title Case H2 headings at 59 ("The Model"), 124 ("Solving via Value Function Iteration") and 368 ("Interpreting the Outcomes").
7. Rename `demand_pdf` at 153 to `demand_pmf` to agree with line 111, and pick one name for $n$ - visit counts (534, 542, 593) or training steps (658, 661).
8. Sweep the code: the E124 closing paren at 151, the unused unpacked `x_values`/`p` at 212 and 254, the `**` spacing at 625 and 627 against 154, the 84-character line at 653, `1/γ_base` at 678 against `1.0 / γ` elsewhere, and the dead `n_steps=20_000_000` default at 644. Then correct 707-712, which describes simulated inventory paths as policies.
