# likelihood_bayes

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_bayes.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×4; `qe-writing-003` ×3; `qe-writing-002` ×4, +2 more. |
| Math         | 4/10  | `qe-math-010` (proposed) ×31; `qe-math-015` (proposed) ×4; `qe-math-014` (proposed) ×4. |
| Code         | 6.5/10 | `qe-code-001` ×5; `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×6; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 322, 577, 832, 853, 951. *Example:* 322 names a parameter `l` (`def update(π, l)`), which PEP8 E741 singles out as ambiguous, and uses it again at 326; 577 and 156-157 bind lambdas to names (E731); 832-834, 845-846, 853, 899, 932 and 951-954 index without a space after the comma - `np.empty((N,T+1))`, `π_path[:,0]`, `π_path[:,t]`, `π_path[j,:]` (E231) - where the rest of the file writes `[i, :]`; 853 runs to 98 characters (E501); 951-954 and 370-371 and 410-411 indent continuation lines four spaces from the statement start rather than aligning under the opening bracket (E128); and 848-850 and 854-856 separate top-level defs by one blank line instead of two (E302). Line 844 also recomputes `f(w)/g(w)` twice in one expression.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 50, 874, 896, 929, 948, 1005. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 31. *Lines:* 202, 217, 218, 226, 229, 230, 233, 247, 288, 300, …. *Example:* non-blackboard `{\rm Prob}`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 65. *Lines:* 96, 105, 107, 143, 229, 230, 242, 262, 271, 274, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 56, 152. *Example:* spelled-out `gamma`.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 4. *Lines:* 247, 288, 446, 669. *Example:* the lecture states the convention itself and then breaks it. 236-242 defines the events with braces - `A = \{q=f\}`, `B = \{w^{t+1}\}` - and says outright "where braces $\{\cdot\}$ are our shorthand for 'event'". Five lines later 247 writes `{\rm Prob}(q=f |w^{t+1})` with parentheses around exactly that event, and the same parenthesised form recurs at 288, 300, 446, 472 and 669, plus `\pi_0 = {\rm Prob}(q=f|\emptyset)` at 217-218. The one place the braces survive is inside `{\rm Prob}({a = f | w_0})` at 669, where they are typed inside the parentheses rather than replacing them. Written as `\mathbb{P}\{q = f \mid w^{t+1}\}` throughout, the notation would match the convention the lecture announces at 242.
- **[qe-math-015 (proposed)]** *(reviewer)* — Lowercase for densities/PMFs, uppercase for CDFs. *Count:* 4. *Lines:* 637, 678, 946, 1037. *Example:* from section 623 onward the lecture switches to uppercase $F$ and $G$ for the two objects it has called densities $f$ and $g$ for six hundred lines - "successive draws of his wage are drawn from either $F$ or $G$" (637), "the probability that $w_{t+1}$ is being drawn from distribution $F$" (678), "pushes the subjective distribution to draw from $F$ more frequently" (946), "almost sure that $w_t$ is drawn from $F$, or is almost sure it is drawn from $G$" (1037) - while the surrounding mathematics keeps using $f(w_0)$, $g(w_0)$, $\ell(w_t) = f(w_t)/g(w_t)$ and the code keeps using `F_a, F_b` as beta parameters of the *density*. Neither $F$ nor $G$ is ever a CDF anywhere in the lecture, so the uppercase is not the case distinction proposed qe-math-015 (proposed) reserves it for; 669-678 has both forms four lines apart.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 331, 467, 618, 640. *Example:* 331-334 repeats 274-279 almost word for word and says so ("As mentioned above, formula {eq}`eq_Bayeslaw1033` shows the key role that the likelihood ratio process ... plays in determining the posterior probability $\pi_{t+1}$"), so two consecutive sentences appear twice fifty lines apart; 618-621 states the same forward reference twice in a row ("This topic is taken up in {doc}`mix_model`" then "We explore how to learn the true mixing parameter $x$ in the exercise of {doc}`mix_model`"); 640 announces its own redundancy ("We'll review and reiterate and rearrange some formulas that we have encountered above"); and 467 is a single 47-word sentence carrying a negation, an equation reference and a restatement of the alternative timing protocol. The closing section at 1039-1042 also repeats line 46 verbatim.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 636, 648, 938. *Example:* 636 introduces "a McCall worker" and wage draws with no transition, three sections into a lecture about a statistician observing $w_t$ - the worker never appears again except at 657-678 and 1037; 648 and 657 silently change the prior's index from $\pi_0$, used from 193 to 612, to $\pi_{-1}$, and both then coexist for the rest of the lecture while the code keeps calling the same quantity `π0` (856, 869, 924), so 973-977 describes a table of $\pi_{-1}$ values produced by a function whose parameter is `π0s`; and the histogram at 929-937 for $\pi_0 = 0.3$ is plotted and then never mentioned, with 940 returning to the $\pi_0 = 0.5$ ensemble.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 29, 33, 710, 718. *Example:* the lecture bolds two definitions - **likelihood ratio process** (109) and **recursion** / **multiplicative decomposition** (128-129) - and italicises at least six others: *likelihood ratio processes* and *Bayesian learning* in the opening sentence (29), *prior* and *posterior* at 33, *martingale* at 710, *bounded martingale* at 712, *sufficient statistic* at 718, *martingale convergence theorem* at 723. All six are terms being introduced, which the rule assigns to bold; the file's many other italics (*some* 142, *same* and *different* 339, *permanent* 451, *not* 467, *before* 657, *subjective* 720) are correct emphasis, so the marker is doing both jobs at once.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 538. *Example:* figsize=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 971. *Example:* 971 promises "We'll use our simulations to generate a histogram of this distribution" and 979-982 delivers a `pandas` DataFrame instead - eleven rows of $\pi_{-1}$ against the fraction of paths converging to 0 and to 1. The claim being checked (985: "The fraction of simulations for which $\pi_t$ had converged to $1$ is indeed always close to $\pi_{-1}$") is that one column equals the index, which is a 45-degree line: plotting the realized fraction against $\pi_{-1}$ with the identity line drawn would verify the martingale prediction of 810-812 in one picture, where the table asks the reader to compare eleven pairs of rounded numbers by eye.


## Strengths

- The lecture states the braces-for-events convention explicitly at 236-242 - `A = \{q=f\}`, `B = \{w^{t+1}\}`, "where braces $\{\cdot\}$ are our shorthand for 'event'" - which is more than most lectures in the corpus do, and it is exactly the distinction proposed qe-math-014 (proposed) is about.
- Both Bayes formulas are derived rather than quoted: 229-268 gets the batch form {eq}`eq_Bayeslaw1033` from the product rule, 285-310 gets the recursion {eq}`eq_recur1` the same way, and 426-437 then checks numerically that iterating the recursion reproduces the closed form to within 1e-10 - the algebra is verified in code, not asserted.
- The martingale argument at 700-812 is carried all the way through: $E(\pi_t \mid \pi_{t-1}) = \pi_{t-1}$ is computed explicitly, boundedness is noted, the convergence theorem is applied, the only admissible limits are shown to be 0 and 1, and iterated expectations then pins $\mathbb{P}\{\pi_\infty = 1\} = \pi_{-1}$ - and 968-985 tests that prediction across eleven priors.
- The mixture section (444-621) is a real misspecification experiment with a full explanation: $\pi_t \to 1$ under an $x$-mixture is displayed (531-559), then attributed to $KL(m,f) < KL(m,g)$ with the divergences actually computed (572-597), then closed with $\lim_{z\to\infty} h(z) = 1$ at 606-612 - three steps, none of them hand-waved.
- The `{note}` at 480-482 names the object that will explain the coming surprise (a KL divergence with respect to the mixture) before the surprise is shown, and the `{note}` at 509-511 flags what the same simulated path will be reused for later.
- The twin-axis figures at 367-381 and 407-421 put the two posterior paths and $\log L(w^t)$ on one set of axes so the reader can see the prior being overwhelmed, and 386 warns explicitly that the two $y$ scales differ.
- 943-946 supplies the mechanism behind the split limits rather than only the picture: early luck of the draw makes the subjective distribution sample from $F$ more often, which pushes $\pi_t$ further up - a self-reinforcing loop the reader would not infer from the plot alone.

## Recommended actions

1. Replace the 31 bare probability operators - 26 `{\rm Prob}` and 5 `\textrm{Prob}` - with `\mathbb{P}`, and put the events in braces as 242 says they should be: `\mathbb{P}\{q = f \mid w^{t+1}\}`. Do the same for the five bare expectations `E(\pi_t\mid\pi_{t-1})` (703), `E_t` (774) and `E_{-1}` (780, 786, 801), and for the conditional variance written `\sigma^2(\pi_t \mid \pi_{t-1})` at 995. The file currently contains no `\mathbb` at all.
2. Settle on lowercase $f$ and $g$ for the two densities throughout, replacing the uppercase $F$ and $G$ introduced at 637 and used at 678, 946 and 1037 - neither is a CDF, and the switch happens in the middle of a sentence at 669-678.
3. Close the 65 double spaces (96, 105, 107, 143, 229, 230, 242, 262, 271, 274 and 55 more) - they are the file's single largest mechanical defect and they cluster in the derivation at 229-315.
4. Add `mystnb: figure: caption`/`name` metadata to the five un-named figures (874, 896, 929, 948, 1005); the prose currently refers to them as "The above graph" (884), "the following graph" (894) and "the plot above" (614), and the two twin-axis figures at 360 and 400 share the identical caption "Posterior paths and log likelihood".
5. Replace the table at 979-982 with the scatter of realized limit fraction against $\pi_{-1}$ that 971 promises, or keep both - the table is the evidence, the 45-degree plot is the argument.
6. Pick one index for the prior: either $\pi_0$ as at 193-612 or $\pi_{-1}$ as at 648-812, and make the code agree (`π0`, `π0s` at 856, 869, 924). Then either develop the McCall worker introduced at 636 or drop the framing and keep the statistician of the first half.
7. Delete the duplicated passages (331-334 against 274-279, 620-621 against 618, 1041-1042 against 46), discuss or drop the $\pi_0 = 0.3$ histogram at 929-937, bold the six italicised definitions (29, 33, 710, 712, 718, 723), rename the `l` parameter at 322, and fix the E231/E128/E501 items listed above.
