# market_diffusion

- **Series:** lecture-python.myst
- **File:** `lectures/market_diffusion.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-005` ×6; `qe-writing-002` ×1; `qe-writing-007` ×1. |
| Math         | 7/10  | `qe-math-010` (proposed) ×2; `qe-math-014` (proposed) ×2. |
| Code         | 6/10  | `qe-code-001` ×22; `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×1; `qe-fig-004` ×1; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 22. *Lines:* 165, 247, 250, 251, 260, 275, 277, 349, 350, 418, …. *Example:* exponentiation is written with spaces on fourteen lines - `n ** 2` (165), `mkt.mu_H ** 2` (247, 277), `mkt.sigma ** 2` (251, 277), `... ) ** 2` (260, 349, 350, 418, 419, 424, 425, 569, 571, 635) - where qe-code-001 asks for `a**b`; two lambdas are bound to names (600, 860) rather than written as `def`s; the title at 527 concatenates `f'single crossing at '`, an f-string with no placeholder, to a second string with `+`; and six code lines run past 79 characters (250, 275, 277, 682, 795, 872 - the longest is 87).
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 143, 184. *Example:* non-blackboard `\Pr`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 6. *Lines:* 64, 116, 202, 294, 381, 491. *Example:* bold is used for emphasis in six places where the lecture's own practice is italic: **excessive** and **insufficient** (64-65, two bolds in one sentence), **unknown** (116), **linear in $n$** (202), **undiscounted** (294), **more** (381) and **established** (491). None of these is a term being defined - the lecture's real definitions are bolded correctly at 215 (**log likelihood ratio**) and 308 (**value of information**) - and italic emphasis is used correctly nine times elsewhere (*owned* 37, *want* 58, *aggregate* 171, *exact* 231, *exactly* 458, *more* 461, *competitors* 720, *identical* 735, *not* 1004). Line 461 even italicises *more* for the same kind of emphasis that 381 bolds.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 154, 156, 159. *Example:* spelled-out `sigma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 92, 509, 608, 968. *Example:* style override.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 2. *Lines:* 143, 184. *Example:* (proposed) both probability statements are events - logical conditions on the random quality $\mu$ - but are written with square brackets: `\Pr[\mu = \mu_H]` (143) and `\Pr[\mu = \mu_H \mid \mathcal F_t]` (184). Under qe-math-014 (proposed) an event takes braces, so these should read $\mathbb{P}\{\mu = \mu_H\}$ and $\mathbb{P}\{\mu = \mu_H \mid \mathcal F_t\}$. This is separate from the qe-math-010 (proposed) hit on the same two lines, which is about `\Pr` rather than `\mathbb{P}`; fixing the operator and the delimiter together is one edit.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 592. *Example:* caption of 9 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 963. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 1. *Lines:* 812. *Example:* the sentence at 812-815 runs to about 50 words and carries four separate claims - that the efficient allocation is at a corner, what that allocation is at each quality level, that the interior formula no longer applies, and that the efficiency comparison of the proposition therefore breaks down. It is the one long sentence in a lecture that otherwise holds to one claim per paragraph throughout (the scanner found no qe-writing-001 violations at all), and it sits at the point of the solution where the reader most needs the steps separated.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 112. *Example:* the Hotelling structure is the geometric heart of the model and is never drawn. Lines 100-113 give the two value schedules $s_n = s + nh$ and $\mu_n = \mu + (1-n)h$ and then describe the picture in words - 'buyers near $n = 0$ are naturally drawn to the new product and buyers near $n = 1$ to the established one' - and line 388 describes it again through the indifference condition of the marginal buyer. One panel showing the two lines crossing over $n \in [0,1]$, with the marginal buyer marked and condition `` {eq}`eq:md_condition4` `` shown as the ordering $s-h < \mu_L < s < \mu_H < s+h$ on the same axis, would do the work of both passages. The lecture is otherwise well illustrated, with four captioned figures, so the gap is in the setup only.


## Strengths

- Every analytical claim is checked numerically at the point it is made: the belief martingale and its variance formula by Monte Carlo (258-286), the agreement of $n^*$ with the full-information share at $\alpha \in \{0,1\}$ (366-370), the single crossing by counting sign changes of the gap (531-532), the inflection at $\hat\alpha = 1/3$ against the simulated growth peak (628-637), and all six martingale predictions in one table (672-692).
- The belief dynamics are obtained twice - once as the standard filtering result with a citation to Liptser and Shiryaev (187-198), once from first principles as a log-likelihood-ratio increment (208-229) - and the code implements the second, which the lecture points out gives an exact Bayesian update rather than a discretization of an SDE (231-233).
- The three results promised in the Overview (56-69) are each delivered by a named section with a proposition and a figure, and the closing remarks (704-739) place the lecture against its two companions and its two source papers rather than summarising itself.
- Exercise 1 part 3 takes the parameter values Bergemann and Valimaki use for their own diffusion figures, shows they violate the paper's condition (4) at both ends, and then works out precisely which of the lecture's results survive and which do not (810-822) - a rare and genuinely instructive exercise.
- Exercise 2 walks the reader from a bisection to a guessed closed form for the crossing belief, verifies it to 1e-16 across six parameter sets (885-892), and then deliberately breaks the symmetry assumption to show the formula is knife-edge (916-926).

## Recommended actions

1. Fix the comparison at line 453: it prints `max |p2 - p2_myopic|` but computes `np.abs(p2(mkt, A_int) - p2(mkt, A_int)).max()`, the difference of `p2` with itself, so the zero it reports is a tautology - and it is the only evidence offered for the claim at 458 that the new firm's price is exactly its myopic price. There is no `p2_myopic` function in the lecture (440-445 define `p1_myopic` and `n_myopic` only); add it and compare against it.
2. Write the two probabilities as $\mathbb{P}\{\cdot\}$ at 143 and 184 - blackboard operator with braces, braces because both arguments are events (qe-math-010 (proposed) x2 and qe-math-014 (proposed) x2, both proposed).
3. Add a figure of the Hotelling line for the setup section: the two value schedules over $n \in [0,1]$, the marginal buyer, and the ordering that condition `` {eq}`eq:md_condition4` `` imposes.
4. Change the six emphasis-bolds to italic (64, 65, 116, 202, 294, 381, 491) so the bold in the lecture marks only the two definitions at 215 and 308.
5. Rename the spelled-out Greek parameters `mu_L`, `mu_H` and `sigma` to unicode in the `Market` constructor and its attributes (154, 156, 159 and their uses) (qe-code-002, 3 occurrences).
6. Close up the fourteen spaced `**` operators, turn the two named lambdas at 600 and 860 into `def`s, collapse the concatenated f-string at 527, and bring the six over-length lines under 79 characters.
7. Add `mystnb: figure: caption/name` metadata to the figure cell at 963, shorten the 9-word caption at 592 (qe-fig-004), and drop the `figsize` overrides at 509, 608, 968 and the global `plt.rcParams['figure.figsize']` at 92 unless the wide aspect is deliberate (qe-fig-001, 4 occurrences).
