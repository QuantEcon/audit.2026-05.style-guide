# hansen_richard_1987

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hansen_richard_1987.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×2; `qe-writing-004` ×7; `qe-writing-001` ×8, +2 more. |
| Math         | 4/10  | `qe-math-010` (proposed) ×75; `qe-math-009` ×4; `qe-math-014` (proposed) ×1. |
| Code         | 6.5/10 | `qe-code-001` ×8; `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 98, 426, 449, 653, 681, 848, 1138, 1140. *Example:* 98 imports `pandas as pd` and nothing in the lecture uses it. 426 writes `mu_m = -0.5 * σ_m**2` one line after `σ_m = 0.15`, so the same Greek letter is spelled out and unicode in adjacent lines of one function; the same split runs through the file (`mu_vec` and `Sigma` at 658 against `σ` at 684, `alphas` at 832 against `αs` at 432). 653 drops the spaces from `2*B*frontier_means` four lines after writing `A * C - B**2` at 649. 449 leaves one blank line before the top-level `def objective` where PEP8 asks for two (439 and 656 in the same lecture use two). Assignments are padded to align in seven places - `mu_low  =`, `rets_low  =`, `returns   =`, `w_low  =`, `alphas_dynamic  =` (681-682, 690-692, 696-697, 845-846, 853-854, 866-867, 874-875) - which PEP8 asks not to do. Continuation lines are indented one column past their opening bracket at 848-851 and 870-872. 1138 and 1140 are f-strings with no placeholders. And the SLSQP block at 1133-1135 is a verbatim copy of 454-456, objective, constraint and bounds included, so the exercise solution re-implements the cell the lecture already ran at 450-457.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 75. *Lines:* 74, 87, 111, 150, 202, 260, 268, 292, 299, 323, …. *Example:* bare expectation `E(`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 8. *Lines:* 60, 319, 627, 631, 1055, 1062, 1067, 1072. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 399, 584, 918, 938. *Example:* mid-sentence 'Law'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 311, 949. *Example:* H2 Title Case: 'The Riesz representation: the stochastic discount factor' (Riesz).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 658, 661. *Example:* spelled-out `Sigma`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 65, 383, 500, 907. *Example:* the asterisk is doing three unrelated jobs at once. On $p^*$ (65), $r^*$ (383) and $z^*$ (500) it marks a distinguished element - the benchmark payoff, the benchmark return, the conditional-mean direction. On $w^*$ (558) it marks the solution of an optimisation. And on $\pi^*$ (907) and $P^*$ (907, 916, 925, 941) it marks *unconditional* objects, which is a different idea again - so $\pi^*(p) = E[\pi(p)]$ has a star that means "unconditional" applied to a function whose value is built from $p^*$, whose star means "benchmark". A reader meeting $\pi^*(p) = E(p\,p^*)$ at 934 has to keep two meanings of the same mark apart in one equation. Since the paper's own $r^*$ and $z^*$ are fixed by convention, the two that could move are the unconditional ones - a subscript or an overbar on $\pi$ and $P$ would separate the two ideas at no cost.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 128, 330, 340, 916. *Example:* the same two sentences are written twice, ten lines apart: "The payoff $p^*$ is the **stochastic discount factor** (SDF), also called the **benchmark payoff**." (330-331) and "The payoff $p^*$ is called the **stochastic discount factor** (SDF) or **benchmark payoff**." (340-341), with 337-338 in between restating the theorem the box at 316-328 has just given ("The theorem says that *any* such $\pi$ can be represented concretely as $\pi(p) = E(p\,p^*\mid\mathcal{G})$"). The term **strictly stationary** is likewise defined twice, in the text at 128 and again in the note at 131-136. And 916 is a 35-word sentence that would read better split at its "i.e.": "For $\pi^*$ to be well defined on $P^*$, the benchmark payoff $p^*$ must itself have a finite unconditional second moment, i.e., $p^* \in P^*$", where the two halves are also the two halves of {prf:ref}`hr87_thm41`'s hypothesis at 925.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 482, 543, 620. *Example:* this is a lecture about geometry - orthogonal decompositions, spans, and frontiers - and in 1153 lines it draws exactly one picture: `plt.show()` appears once, at 736. The central construction, $R = \{r^* + w z^* + n\}$ built in stages at 482-531, is an orthogonal decomposition of the return space into a benchmark direction, a conditional-mean direction and a residual space, and it is carried entirely by algebra; one diagram of the three components with the right angle marked would do more than the six displays. The conditional two-fund theorem (543-559) and its unconditional counterpart (591-...) say that the frontier is spanned by $r^*$ and $z^*$ with a *random* weight - again a picture. And the result the lecture is named for, that "a return that is on the conditional frontier [can] fall *off* the unconditional frontier" (81-82, restated at 620-622), gets the one figure it has (716-737), which shows a single star against one curve; the natural version of that figure - two conditional frontiers, one per regime, and the unconditional frontier through the same point cloud - would show the mechanism rather than the symptom. Meanwhile four of the six computational cells report their results as hand-aligned text tables built with f-string padding (444-446, 459-460, 877-879, 1008-1026, 1138-1145), and `pandas` is imported at 98 and never used anywhere in the lecture.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 725. *Example:* figsize=.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 1. *Lines:* 355. *Example:* the lecture follows the convention throughout - braces for events, and every probability statement in it is an event: $\Pr\{\|p_j - p_0\|_{\mathcal{G}} > \varepsilon\}$ (292), $\Pr\{\|p_j - p_k\|_{\mathcal{G}} > \varepsilon\}$ (299), $\Pr\{\|p^*\|_{\mathcal{G}} > 0\}$ (327), $\Pr\{p > 0\}$ (352), $\Pr\{p^* > 0\}$ (370). The one that goes wrong is the no-arbitrage definition at 355, `\Pr\{\pi(p) \leq 0\} \cap \{p > 0\}\} = 0`, which has three closing braces and two opening ones: the intersection of the two events sits outside the probability operator, so the display reads as a probability intersected with a set. It should be $\Pr\{\{\pi(p) \leq 0\} \cap \{p > 0\}\} = 0$ - the delimiters this rule is about, in the definition that the rest of section 3 depends on.


## Strengths

- The formal skeleton is built out of `prf:` directives and then referenced by label rather than by phrase: four assumptions (198-247), three definitions (288, 295, 348), two theorems (316, 922) and four lemmas (389, 543, 591, 776), each cited where it is used - `hr87_assumption_21` at 309 and 480, `hr87_lemma31` at 409, 419 and 490, `hr87_cor31` at 822, 826, 882, 884 and 888 - so a reader who loses the thread can jump to the exact statement being invoked.
- Every theoretical result is followed by a simulation that tests that result and not a neighbouring one: Lemma 3.1's minimum-second-moment claim is checked by minimising $E(r^2)$ over unit-sum portfolio weights and comparing against each individual asset (409-460); the conditional-versus-unconditional gap is produced by a two-regime economy whose weights switch by state (672-713); the single-beta corollary is tested twice over, once with a constant-weight frontier reference and once with the dynamic one (828-879); and the GMM section prices returns that were deliberately generated by a different SDF (988-1039).
- The rejection in the GMM test is explained by the numbers that produced it rather than left as an outcome: 1044 points out that the returns come from a lognormal SDF with $\sigma_m = 0.15$ (set at 425) while the model under test is CRRA with $\gamma = 2$ and $\sigma_c = 0.03$ (1031-1032), "implying far less SDF volatility", and 1048 draws the general lesson from that specific mismatch.
- The `{note}` at 130-144 answers exactly the three questions the definition above it raises - what strict stationarity is, how it differs from weak stationarity, and why it follows here from $S$ being measure-preserving - instead of leaving the reader to look them up.
- 884 anticipates the objection a reader will make to the regression output before they make it: {prf:ref}`hr87_cor31` "guarantees a real zero-beta return $\alpha$, but that $\alpha$ need not be zero -- it equals zero only under an extra normalization or for a specially chosen reference portfolio", which is why 882 can claim success from intercepts that are merely equal across assets.
- The abstract objects are given economic readings where they are introduced: $p^*$ becomes "the **intertemporal marginal rate of substitution** of the numeraire good" once positivity is established (373-375), $R$ and $Z$ are named as returns and excess returns (476-477), and 626-635 converts the conditional-versus-unconditional gap into three concrete consequences - the CAPM's market portfolio, Breeden's consumption CAPM, and portfolio managers who look inefficient when judged on unconditional data.
- The decomposition is assembled one step at a time, each step justified: $r = r^* + z$ because $\pi(r^*) + \pi(z) = 1 + 0$ (482-488), $r^*$ conditionally orthogonal to $Z$ because it has minimum conditional second moment (490-492), $Z = \{wz^* + n\}$ from the defining property of $z^*$ (503-524), and only then the full representation $R = \{r^* + wz^* + n\}$ (529-531).

## Recommended actions

1. Fix the malformed probability at 355 - `\Pr\{\pi(p) \leq 0\} \cap \{p > 0\}\} = 0` has unbalanced braces and puts the intersection outside the operator - since it is the definition the whole no-arbitrage discussion rests on.
2. Add the two figures the argument is asking for: the orthogonal decomposition $R = r^* + wz^* + n$ (482-531) with $r^*$ perpendicular to $Z$, and a two-regime version of the frontier figure at 716-737 showing both conditional frontiers and the unconditional one through the same point cloud.
3. Cut the duplication at 330-344: the SDF is named twice in eleven lines and the Riesz theorem is restated at 337-338 immediately after its own `prf:theorem` box; likewise define **strictly stationary** once (128 or 131, not both).
4. Convert the 75 bare `E(`/`E[` expectations and the `\Pr` probabilities to `\mathbb{E}` and `\mathbb{P}` - at this density the lecture would read as consistently as it is argued, and the conditional forms `E(\cdot \mid \mathcal{G})` would become `\mathbb{E}[\cdot \mid \mathcal{G}]` throughout.
5. Separate the two meanings of the asterisk: keep it for the benchmark objects $p^*, r^*, z^*$ that the paper fixes, and give the unconditional pricing function and payoff space a different mark than the one $\pi^*(p) = E(p\,p^*)$ currently overloads (907, 916, 925, 934, 941).
6. Drop the unused `pandas` import at 98 or use it: the four hand-padded text tables at 444-446, 459-460, 877-879 and 1138-1145 are what it was imported for.
7. Bring the code to one convention: unicode Greek throughout (`mu_m` at 426 sits beside `σ_m` at 425, `Sigma` at 658 beside `σ` at 684, `alphas` at 832 beside `αs` at 432 - see the scanner doubt), factor the shared frontier algebra out of `compute_mv_frontier` (640-655) and `mv_weights` (658-669), reuse the minimisation at 450-457 in place of the copy at 1130-1135, and clear the alignment padding, the two placeholder-free f-strings and the off-by-one continuations at 848 and 870.
8. Sweep the writing items: the 8 two-sentence paragraphs (60, 319, 627, 631, 1055, 1062, 1067, 1072), the 7 capitalised common nouns (399, 584, 918, 938 - "Law of Iterated Expectations", "Assumption 4.1"), and the `figsize=` override at 725.
