# information_market_equilibrium

- **Series:** lecture-python.myst
- **File:** `lectures/information_market_equilibrium.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×5; `qe-writing-009` (proposed) ×2; `qe-writing-003` ×2, +4 more. |
| Math         | 5.5/10 | `qe-math-002` ×4; `qe-math-010` (proposed) ×1; `qe-math-009` ×3. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×3; `qe-fig-001` ×9. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 595, 707, 1020, 1080, 1173, 1287, 1396, 1502, 1523. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 4. *Lines:* 59, 61, 234, 245. *Example:* apostrophe transpose `}'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 1567. *Example:* bare expectation `E_h[`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 34, 181, 234, 236, 1199. *Example:* the lecture's bold-for-definition usage is mostly right (**competitive equilibrium** 166, **posterior** 189, **elasticity of substitution** 360, **structural parameter vector** 753, **reduced form** 796, **CARA** 1212), which makes the exceptions conspicuous: 34, 181, 236 and 1199 use bold for pure emphasis - "the **informational role of prices**", "Suppose **agent 1** (the insider)", "**independent of** $\bar{a}$", "the observer's **price expectations** converge" - and 234 does the reverse, italicising the term the `prf:definition` exists to define ("A random variable $\tilde{y}$ is *sufficient* for $\tilde{y}'$") six lines after the same word was bolded at 229.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 1082, 1275, 1389, 1414. *Example:* 1082 pads `palette   = plt.cm.Blues(...)` with extra spaces before `=` to align with the line above (PEP8 E221); 1389 has two spaces after a comma inside a list literal, `[("Easy",  2.0, 1.2), ("Hard", 2.0, 1.8)]` (E241); 1414 leaves a trailing space after `fontsize=11` inside the `set_title` call; and 1275 re-imports `brentq` from `scipy.optimize` in an exercise-solution cell although it is already imported at 112, which is the only import statement in the file that is not in the opening cell.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 1274, 1382, 1459. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 762, 791, 1221. *Example:* three symbols carry unrelated meanings in the same lecture. $P$ is a subjective probability measure ($P^i$, 137), a probability ($P(\bar a = a_s \mid \tilde y = y)$, 192), a probability indexed by structure ($P_\lambda$, 768) and, at 759-762, "any measurable price set $P$" - while the set of realized prices is written $\mathcal{P}$ (286), so the lecture has a plain and a calligraphic $P$ both meaning sets of prices plus $P$ meaning probability. $\mu$ is the insider's posterior over states through the whole first half (186-441) and then, from 791 on, an equivalence class of structural parameters, with $\mu_1$ and $\mu_2$ at 933 being reduced forms rather than posteriors. $W$ is the endowment set $W(P)$ at 762 and agent wealth at 522 and 1221. Each of the three could be renamed once and the collision disappears.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1367. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 213, 322, 478, 783. *Example:* 213 is the first of nine formulaic bridge sentences that carry no content - "To answer that question, we now translate..." (213), "Before turning to invertibility itself, it helps to keep in mind..." (327), "Before stating the theorem, it helps to see..." (363), "With that example in hand, we can compute..." (513), "The numerical plot shows monotonicity, and the next subsection connects..." (632), "The static analysis asks whether... whereas the next section asks..." (731), "The next issue is therefore what an observer can and cannot infer..." (778), "Once that distinction is clear, Bayesian updating can be written down directly" (802), "We can now sharpen the point by..." (1110); 478-483 states the Cobb-Douglas intuition and then 535-539, 616-617, 687-691 and 724-725 state it four more times; 322-325 is a 50-word sentence with three clauses and a report of what "the paper shows formally"; and 783-786 stacks two because-clauses ahead of its main clause across 40 words.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 145, 358. *Example:* 145-162 sets up a production side in detail - the firm's technology $y_1 = f(y_2)$ with $f' < 0$, the profit problem $\pi(p) = \max_{y_2 \leq 0}\{p f(y_2) + y_2\}$, and the shares $\theta^i$ - and 174-177 then discards it ("we will suppress production"); after that, $f$, $y_2$ and $\pi$ never reappear except inside the definition of $W_1$ at 522, so the reader carries three displays of machinery for 350 lines to no purpose. And 358 opens the invertibility section by citing `ime_theorem_invertibility_conditions` for its main claim, but the theorem is not stated until 461, after two lemmas and a first-order condition.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 293, 781. *Example:* 293-296 wants to be a diagram and settles for typesetting one inside `$$`: `\tilde y \longrightarrow \mu_{\tilde y} \longrightarrow p(\mu_{\tilde y})`, with the two arrows then explained in prose at 298-300 as "loses no information" and "the theorem asks when the second arrow also loses no information". Labelling those two arrows in a real figure is the whole logical structure of the price-revelation result on one line. And "### The identification problem" (781-800) partitions $\Lambda$ into equivalence classes under a many-to-one map $\lambda \mapsto g(\cdot \mid \lambda)$ - a mapping diagram - and gets no picture, even though the entire second half of the lecture and the three-panel simulation at 1134-1190 turn on that partition.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 1368, 1372, 1457. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 2. *Lines:* 751, 757. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- The proof apparatus is fully typed and fully wired: `prf:definition` (231), three `prf:lemma` (251, 367, 417), a `prf:proof` (258) and two `prf:theorem` (278, 461, 856), every one labelled, and every one actually reached by `{prf:ref}` from the place that needs it - 299, 318, 358, 435, 608, 633, 660, 1108, 1337, 1435.
- The Cobb-Douglas prediction is tested rather than asserted: 619-626 computes $p^*(q)$ across the whole $q$ grid and prints its range against the analytic $W_1/2$, and 628-630 reports the result, so the flat line in `fig-eq-price-posterior` is corroborated numerically to six decimals.
- The three exercises escalate instead of accumulating: `km_ex1` supplies a case with a closed form so the numerics can be checked against algebra, `km_ex2` quantifies convergence speed by KL divergence and asks for the $T_{0.99} \approx C/D_{KL}$ scaling, and `km_ex3` breaks the convergence theorem's own prior-support assumption and asks what happens instead.
- The non-identification simulation at 1134-1190 is the payoff of the second half and is constructed to make the point unmissable: three structures, two reduced forms, and three panels in which the weight on $\lambda^{(3)}$ is driven to zero while $\lambda^{(1)}$ and $\lambda^{(2)}$ sit at one half apiece forever.
- All five body figures carry `mystnb: figure: caption` and `name` metadata and every line in them is drawn with `lw=2`; citations use the in-text `{cite:t}` form consistently (36, 67, 170, 227, 249, 739, 1330) with no parenthetical misuse.
- The `{note}` at 899-907 adds a genuine logical refinement rather than restating the theorem: positive prior mass on the reduced-form class $\bar\mu$ is strictly weaker than positive mass on $\bar\lambda$, and a prior can satisfy the first while giving the true structure probability zero.

## Recommended actions

1. Rename one member of each of the three colliding symbol families: the price set at 759-768 (call it $B$ or $\mathcal{B}$, freeing $P$ for probability), the reduced-form equivalence classes from 791 on (call them $\mathcal{C}$ or $R$, freeing $\mu$ for the insider's posterior), and the endowment set $W(P)$ at 762 (freeing $W$ for wealth). This is the single change that most improves the lecture, because $\mu$ currently means two unrelated things across its two halves.
2. Add braces to the bare expectation at 1567 (`E_h[\log L_t]` -> `\mathbb{E}_h`) and replace `\Pr(` with `\mathbb{P}` in the two axis labels at 601 and 1295 (qe-math-010 (proposed)); write "IID" at 751 and 757 (qe-writing-009 (proposed)), dropping the bold on it at 751.
3. Cut roughly 350 lines of scaffolding down: delete or shorten the production block at 145-162 that 174-177 then suppresses, keep one statement of the Cobb-Douglas intuition instead of the five at 478, 535, 616, 687 and 724, and delete the nine bridge sentences listed above - the argument reads faster without them.
4. Replace the arrow display at 293-296 with a real diagram of the two-step chain, with the arrows labelled by what each step preserves, and add a mapping diagram for the $\lambda \mapsto g(\cdot \mid \lambda)$ partition at 781-800.
5. Add `mystnb: figure: caption`/`name` metadata to the three exercise-solution figures (1274, 1382, 1459) so they match the five in the body, and move the four embedded `set_title` calls in those cells (1297, 1411, 1510) into those captions.
6. Move the statement of `ime_theorem_invertibility_conditions` (461) ahead of the two supporting lemmas, or drop the forward citation at 358 - and drop `figsize=` from the five single-panel figures (595, 707, 1080, 1287, 1523), keeping it on the four multi-panel ones (1020, 1173, 1396, 1502) where the grid needs the width.
7. Switch the four bold emphases (34, 181, 236, 1199) to italic, bold *sufficient* at 234 so the definition matches 229, split the two-sentence paragraph at 1367, close the three double spaces (1368, 1372, 1457), fix the trailing space at 1414 and the alignment padding at 1082, and drop the duplicate `brentq` import at 1275.
