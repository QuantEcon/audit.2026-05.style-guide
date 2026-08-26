# rs_inventory_q

- **Series:** lecture-dp
- **File:** `lectures/rs_inventory_q.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×4; `qe-writing-005` ×9; `qe-writing-001` ×2, +4 more. |
| Math         | 6/10  | `qe-math-010` (proposed) ×5; `qe-math-009` ×1. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×7; `qe-fig-005` ×4; `qe-fig-008` ×9, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 318, 323, 360, 692, 699, 727, 736. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 312, 313, 358, 687, 688, 694, 695, 725, 734. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 66, 84, 418, 461, 479. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 9. *Lines:* 381, 387, 395, 439, 440, 517, 518, 522, 434. *Example:* the rule is inverted systematically: bold is used for emphasis nine times and never once for a definition. Emphasis in bold: 'is **deterministic**' (381), 'The variance comes from **revenue**' (387), 'because it **caps the randomness of revenue**' (395-396), 'is a **decreasing** function' (439), 'corresponds to the **minimum**' (440), 'The Q-values are **positive**' (517), 'we **minimize** rather than maximize' (518), 'enters as a **power**' (522). Bold is also used as a list label at 434, 455, 533, 535, 547 and 549 (`**Step 1.**`, `**Step 2.**`, `**Initialize**`, `**At each step:**`, `**Extract the greedy policy**`, `**Compare**`). Meanwhile the four terms the lecture actually defines - the risk-sensitive Bellman equation (77), the certainty equivalent (115, 165), the Q-factor (415-424) and optimistic initialization (551-560) - carry no bold at all, and the two correct italic emphases in the file (*minimizes* 555, *below* 557) sit in the one paragraph that gets it right.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 59, 124, 368, 405. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 151, 212, 337, 153. *Example:* 151 closes the signature of `create_rs_inventory_model` at an indent of 4, matching neither column 0 nor the 8-space indent of the arguments above it (E124), and then leaves 152 blank before the body. 212, 254 and 648 unpack the whole `RSModel` and leave locals unused - `p` at 212 and 254, `d_values` and `ϕ_values` at 648 (F841); `T_rs` and `get_greedy_rs` need only six of the eight fields. 337 and 592 call `np.random.seed(seed)` inside a `@numba.jit(nopython=True)` function, mutating numba's global RNG state as a side effect of a simulation call - the copy of this file in `lecture-python.myst` has already been converted to a passed-in `np.random.default_rng` generator (`rng.geometric`, `rng.integers`, `rng.random`), which is both the modern NumPy API and the reason the copies differ. And 153 names a probability *mass* function `demand_pdf`, three lines after `ϕ_values = demand_pdf(p, d_values)` computes a geometric PMF and 58 lines before 111 states 'Here $\phi(d)$ denotes the demand probability mass function'.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 308, 348, 685, 717. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 307, 346, 684, 714. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 557, 559. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 45, 658. *Example:* the roadmap in the Introduction omits half the lecture. 45-47 says 'We show how the model can be solved using value function iteration. We then investigate how risk sensitivity affects the optimal policy' - and stops. Q-learning is in the lecture's title (23), occupies 405-754, and is the part that carries the novel derivation (the Q-factor fixed point at 430-487, where max becomes min and the continuation value becomes a power), yet a reader working from the Introduction has no idea it is coming. Second, 645 sets the wrapper's default to `n_steps=20_000_000` while nothing in the lecture ever runs 20 million steps: 661-663 runs 5 million, 658 says 'We run $n$ = 5 million steps', and 748 reports on 'step 5 million' - so the default is a fourth number that contradicts the three that agree.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 471. *Example:* mid-sentence 'Step'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 376, 370, 167. *Example:* the lecture's central economic claim gets five paragraphs of prose and no picture. 376-402 argues that the variance of profit comes from revenue $\min(x, D)$, that '$\min(x, D) \approx D$' when $x$ is high and '$\min(x, D) \approx x$' when $x$ is low, and that a risk-sensitive agent therefore holds less stock - and every object in that argument is already computed: `ϕ_values` at 157 is the demand PMF, so one panel of $\mathrm{sd}[\min(x, D)]$ against $x$, or two histograms of $\min(x, D)$ at a high and a low $x$, would show the whole mechanism at a glance. Second, all four figures (307, 346, 684, 714) are unnamed, so the prose has to point at them by position - 'The plots above show' (370), 'The panels below show' (707), 'The top panel shows the optimal policy from VFI for reference' (712) - and the claim at 751-754 asks the reader to 'compare with `` {doc}`inventory_q` ``', i.e. with a figure in a different document that cannot be cross-referenced because neither figure has a name. Third, there is not one admonition in 772 lines, and three passages want one: the log-sum-exp stability note at 167-178, the magnitude argument that justifies `q_init=1e-9` at 559-560, and the four-item 'Notice several differences from the risk-neutral case' list at 515-523.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 420. *Example:* the negative thin space `\!` is applied to six `\left(` and `\ln` openings (420, 445, 446, 452, 465, 472) and omitted from the seven structurally identical ones (100-108, 463, 481, 503, 520, 626, 671), so a hand-tuned micro-space is present in about half the displays and absent from the rest with no visible reason for the split. Dropping all six is the simpler and more consistent choice.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 557. *Example:* 2 spaces.


## Strengths

- The derivation of the risk-sensitive Q-factor equation is laid out as two numbered steps that each state their own goal and are each verifiable: 432 says what is to be achieved ('a fixed point equation in $q$ alone, eliminating $v^*$'), Step 1 (434-453) establishes $\exp(-\gamma v^*(x)) = \min_a q(x,a)$ and explains the max-to-min flip by the monotonicity of $\psi^{-1}$ (439-441), Step 2 (455-485) substitutes it back, and 487 confirms the goal was reached.
- The four differences from risk-neutral Q-learning are enumerated explicitly (515-523) rather than left for the reader to spot in the code: positive Q-values, argmin instead of argmax, profit entering through $\exp(-\gamma R_{t+1})$, and the continuation value entering as a power rather than a scaled sum - and each of the four is then visible in the corresponding line of `q_learning_rs_kernel` (577, 626, 626, 626).
- The optimistic-initialization discussion (551-560) is the best passage in the lecture: it notes that the usual logic reverses in sign because the policy minimises, says what 'optimistic' therefore means ('initializing the Q-table *below* the true values'), explains the mechanism ('the update pushes $q$ upward toward reality, making that entry look worse'), and then justifies the actual magnitude - true Q-values around $10^{-8}$ to $10^{-6}$, so `q_init=1e-9` - rather than leaving `1e-9` as a magic number.
- The log-sum-exp trick is stated as an identity before it is coded (167-178), with $m = \max_i(-\gamma z_i)$ named, and the two kernels then implement exactly that identity in the same order (198-202, 239-243), so the numerically-stable form and the mathematical form can be read against each other.
- The comparative statics are set up so the reader can see the mechanism working twice: 297-326 solves the model for $\gamma \in \{0.01, 1.0, 2.0\}$ and plots value and policy on shared axes, then 346-365 simulates all three under the *same* demand seed (`sim_seed = 5678`, 352) so the three inventory paths differ only through the policy.
- The learning-progress figure (714-741) holds the demand sequence fixed across four panels - VFI optimum plus policy snapshots at 10,000, 1,000,000 and 5,000,000 steps - which turns a convergence claim into something visible, and 744-749 reads the three panels off in order.

## Recommended actions

1. Add Q-learning to the Introduction's roadmap at 45-47: it is in the title and it is 350 of the lecture's 772 lines. While there, fix the wrapper default at 645 (`n_steps=20_000_000`) to match the 5 million the lecture actually runs, or drop the default.
2. Reverse the emphasis convention throughout: italicise the nine bold emphases (381, 387, 395-396, 439, 440, 517, 518, 522) and bold the four terms being defined instead - the risk-sensitive Bellman equation (77), the certainty equivalent (115), the Q-factor (415), optimistic initialization (551). The `**Step 1.**` / `**Initialize**` list labels (434, 455, 533, 535, 547, 549) are a label idiom rather than emphasis and can stay, but note that the qe-writing-004 hit at line 471 ('From Step 1') is a consequence of that idiom and is a false positive - do not lowercase it, since it names the bolded label at 434.
3. Draw the variance argument. One extra panel showing $\mathrm{sd}[\min(x, D)]$ as a function of $x$ under the geometric demand already built at 157 would carry 376-402 in a single figure, and it is the one claim in the lecture that currently rests entirely on prose.
4. Name the four figures. Add `mystnb` `figure: name/caption` metadata to the cells at 307, 346, 684 and 714, move the seven embedded titles into those captions (318, 323, 360, 692, 699, 727, 736), and replace the positional references at 370, 707 and 712 with `{numref}` citations - which also gives 751-754 something to point at when it asks the reader to compare with `inventory_q`.
5. Sync the RNG handling from `lecture-python.myst/lectures/rs_inventory_q.md`, which is the only substantive difference between the two copies: it threads an `np.random.default_rng` generator through `sim_inventories` and `q_learning_rs_kernel` instead of calling `np.random.seed` inside jitted functions (337, 592) and using the legacy `np.random.randint` / `np.random.geometric` / `np.random.random` (341, 603, 612, 633, 634). Twenty-eight lines differ and nothing else in the file does.
6. Brace the five `\mathbb E` at 66, 84, 418, 461 and 479 (qe-math-010 (proposed)) - and note that the same operator is already correctly written `\mathbb{E}` at 670, 760 and 768, so the file only needs to be made consistent with itself.
7. Figures: add `lw=2` to the nine line plots (312, 313, 358, 687, 688, 694, 695, 725, 734) and drop the four `figsize=` overrides (308, 348, 685, 717). The two multi-panel `figsize` calls at 348 and 717 scale with `len(γ_values)` / `n_snaps`, so if the height is genuinely needed keep only that argument and drop the fixed width.
8. Sentence-case the four Title Case headings (59 'The model', 124 'Solving via value function iteration', 368 'Interpreting the outcomes', 405 'Q-learning'), split the two two-sentence paragraphs at 557 and 559, clear the double space at 557, rename `demand_pdf` (153) to `demand_pmf`, unpack only the fields used at 212, 254 and 648, and drop the `{contents}` directive at 25-27.
