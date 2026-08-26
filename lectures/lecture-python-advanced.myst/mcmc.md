# mcmc

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/mcmc.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-002` ×5; `qe-writing-005` ×1. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×2; `qe-math-005` ×3; `qe-math-009` ×2. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×2; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 773, 783, 820, 986, 1008, 1011, 1082. *Example:* trivial but inconsistent within the file. Three one-line docstrings are written with single double-quotes - 773 (`"Build the log unnormalized posterior from a log prior and data."`), 820 and 986 - while the multi-line docstring at 795-798 uses triple quotes as PEP257 asks. And the blank-line counts around top-level definitions are irregular: 783 and 1011 put one blank line between the end of a `def` and the following module-level statement where PEP8 asks for two, and 1008 and 1082 open a `def` after a single blank line, while 779-780 correctly leaves two.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 158, 322. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 45, 626, 827, 829, 831. *Example:* the same point about probabilistic programming libraries is made four times with the same two links. 45 says the lecture prepares the reader for NumPyro and BlackJAX, "which we will use in later lectures: the implementation below is, in essence, what happens under the hood when such libraries run"; then 827 repeats that libraries "such as [NumPyro](...) and [BlackJAX](...) organize their MCMC computations" this way, 829 repeats "what runs under the hood", and 831 repeats "We will meet these libraries in later lectures". Three consecutive paragraphs carry one idea. Separately, 626 runs to 55 words across four clauses ("A clean sufficient condition for aperiodicity (defined in `` {ref}`mcmc_ergo` ``) is that the chain can *remain in place*: if $P(\theta,\{\theta\}) > 0$ on a set of positive $\pi$-measure, then, combined with irreducibility, the chain is aperiodic, because a state that can be revisited at two consecutive times cannot belong to a nontrivial cycle") - the one definition-plus-justification in the lecture that is not broken into its own sentences.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1158, 1205. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 3. *Lines:* 107, 313, 591. *Example:* parenthesised sequence.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 149, 166. *Example:* the letters $N$ and $n$ each carry two meanings, and the two clashes are the same clash twice over. $N$ is the Markov kernel from 149 through 313 ($N(\theta, A)$, $N^t$, $\pi N$), and from 705 onwards it is the normal distribution ($y_i \mid \theta \sim N(\theta, \sigma_y^2)$ at 705, $\theta \sim N(\mu_0,\sigma_0^2)$ at 709, $\pi = N(\mu_n, \sigma_n^2)$ at 718, $N(0,\sigma_m^2)$ at 1074). Its lowercase twin does the same: $n$ is the sample size at 71 and again at 720-726 and in code at 734, but is the conditional density of the kernel at 166-175 and in the detailed balance equation at 230-237. Since qe-math-011 (proposed) requires the plain letter $N$ for the normal distribution, the kernel is the symbol that should move - a $K$ or $Q$ would free both letters at once, and the density $n$ with it.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 1161. *Example:* figsize=.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 1145. *Example:* the lecture's use of bold for definitions is otherwise exemplary and systematic - **posterior distribution** (73), **unnormalized posterior** (98), **Markov kernel** (149), **admit a density representation** (166), **stationary** (183), **reversible** / **satisfy detailed balance** (205), **detailed balance equation** (230), **$\pi$-irreducible** (298), **periodic** / **aperiodic** (306), **proposal kernel** (356), **symmetric** (363), **burn-in** (833) - and italic is reserved for emphasis (*remain in place* 626, *every* 668, *is* 929, *any* 975, *shape* 1066). The single exception is 1145, where the term the exercise is introducing is italicised: "plot the first 2,000 elements of the chain (a *trace plot*)".


## Strengths

- The theory is assembled from labelled `prf:` blocks that are then actually used by reference: `` {prf:ref}`mcmc_thm_stat` `` (245) is invoked at 352 and 499, `` {prf:ref}`mcmc_eg_rw` `` (373) at 589 and 786, `` {prf:ref}`mcmc_algo_mh` `` (411) at 425, 438 and 790, `` {prf:ref}`mcmc_thm_ergodic` `` (310) at 591, 674 and 891 - so at every point where a result is needed the reader is sent to the exact statement rather than to a remembered paragraph.
- The lecture declares its level and audience before the reader invests anything: 47-51 states plainly that it is intentionally high level, freely uses advanced probability theory, and targets strong-math students and researchers.
- Nothing in the numerical section is trusted before it is checked against something already known: the conjugate posterior is derived in closed form (715-724) and the sampler is validated against it (877-886), then the quadrature routine is validated against the same closed form (992-998), and only then is quadrature used as the ground truth for the two non-conjugate priors (1043, 1119).
- The two halves of the ergodic theorem get two separate pictures and the lecture says which is which: 891-893 splits irreducibility (time averages) from aperiodicity (distributional convergence); 895-921 draws the first along a single trajectory with the burn-in deliberately not discarded and 899-901 says why; 923-965 draws the second with 10,000 chains launched from $\theta_0 = -10$ precisely because "the transient *is* the object of interest" (929).
- The proof of `` {prf:ref}`mcmc_thm_mhstat` `` confronts the atom instead of assuming it away: 501-509 splits $\Lambda$ into $\Lambda_{\mathrm{ac}}$ and $\Lambda_{\mathrm{diag}}$ with `\underbrace` labels naming each piece, 513-521 handles the diagonal part on its own terms, and 546-560 verifies detailed balance by showing both sides equal $\min(\pi(\theta),\pi(\theta'))$ including the degenerate $\pi(\theta)=0$ case set up by the convention at 403.
- The JAX design choice is argued rather than asserted: 812-816 explains that a Markov chain is inherently sequential and therefore a poor accelerator workload, and that the idiomatic fix is to transform rather than rewrite, so `mh_ensemble` (819-825) arrives as a consequence and the burn-in accounting at 833-839 follows from it.
- The three prior experiments each change exactly one thing and each figure is read back in the text: Gaussian to Student-t holding "the *same location and scale*" (1003) with the three readings at 1054-1060, then a mixture that changes only the *shape* (1066) with the three readings at 1127-1133.
- The probability notation is right where the two proposed rules would look: 158 writes the event with braces, $\mathbb P \{\theta_{t+1} \in A \mid \theta_t = \theta\}$, which is exactly the form qe-math-014 (proposed) asks for, and every density in the lecture is lowercase - $p$, $\pi$, $\tilde p$, $n$, $q$, $\phi$ - as qe-math-015 (proposed) asks.

## Recommended actions

1. Rename the Markov kernel from $N$ to a letter not already carrying a meaning: $N$ is the normal distribution from 705 onwards and $n$ is the sample size, so one rename at 149 (and its uses through 313) clears both collisions and leaves the distribution name in the plain form qe-math-011 (proposed) requires.
2. Cut the NumPyro/BlackJAX point to one place: 45 already makes it, and 827-831 makes it three more times with the same two links - the surviving version belongs at 827 where `mh_ensemble` has just been defined.
3. Write the three sequences with curly brackets - `(\theta_t)_{t \geq 0}` at 107, 313 and 591 - to match `\{\theta_t\}_{t=1}^T` as the lecture already writes it at 416 and 676 and `\{\theta_t^i\}_{i=1}^{10000}` at 941 (qe-math-005).
4. Brace the two blackboard operators: `\mathbb P` at 158 and `\mathbb E_\pi` at 322 should be `\mathbb{P}` and `\mathbb{E}_\pi` (qe-math-010 (proposed)).
5. Split the aperiodicity condition at 626 into the condition and the reason, one sentence each.
6. Bold *trace plot* at 1145, which is a definition rather than emphasis.
7. Tidy the PEP8 trivia: triple-quote the one-line docstrings at 773, 820 and 986, and fix the blank-line counts at 783, 1008, 1011 and 1082.
8. Give the two exercise-solution figures the `mystnb: figure: caption/name` metadata the five main-text figures already carry (1158, 1205), move the `set_title` at 1169-1170 into that caption, and drop the `figsize=(10, 9)` override at 1161.
9. Consider one sketch of the mixed kernel `` {eq}`mcmc_fullkernel` `` - a continuous density plus a point mass at the current state - since that two-part structure is what forces the two-part proof at 511-523 and is the hardest object in the lecture to picture.
