# uncertainty_traps

- **Series:** lecture-python.myst
- **File:** `lectures/uncertainty_traps.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×2; `qe-writing-001` ×4; `qe-writing-005` ×3, +4 more. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×2; `qe-math-004` ×3; `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×6; `qe-fig-002` ×3; `qe-fig-001` ×3, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 237, 249, 251, 258, 435. *Example:* 251 ends the assignment target with a stray comma - `self.num_firms, self.σ_F, self.c, = num_firms, σ_F, c` - which unpacks a 3-tuple into a 3-element target list only by accident of Python's grammar; 237-247 indents all ten `__init__` parameters to 16 columns where the opening paren puts `self,` at 17, so every continuation is off by one; 249 and 254 use decorative banner comments (`# == Record values == #`) while 266 and 268 in the same class use plain `# Simplify names`; 258-259 and 269-270 name the two halves of an exponent `temp1` and `temp2`, which is neither PEP8-meaningful nor the mathematical-notation exception the rule allows - they are $-a(\mu - F)$ and $a^2(1/\gamma + 1/\gamma_x)/2$ from `` {eq}`firm_test` ``; 435 writes the module-level assignment `sim_length=2000` with no spaces round `=`; and 417-418 introduces `label_string` only to pass it to `label=` on the next line.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 147, 302, 321, 408, 471, 482. *Example:* {figure} without :name:.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 169, 195. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 58, 102. *Example:* H2 Title Case: 'The Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 35, 37, 39, 151, 338. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 412, 472, 483. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 147, 302, 321. *Example:* static image .png.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 336, 340, 343. *Example:* \mathbf.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 91, 117, 343. *Example:* the same variance is written two ways in the same lecture: $\gamma_x^{-1}$ and $\gamma^{-1}$ in the body (91, 109) against $1/\gamma_x$ and $1/\gamma$ in the exercise and its solution (337, 339, 343, 351, 365, 371, 373) and in the display at 212 - so `$N(0, \gamma_x^{-1})$` and `$N(\theta, 1/\gamma_x)$` are the same distribution. Line 117 uses blackboard bold for a finite index set, $\mathbb M \subset \{1,\ldots,\bar M\}$, giving the letter M three decorations in three consecutive lines ($\bar M$ at 81, $\mathbb M$ at 117, $M$ at 118) where a plain letter would do and where `\mathbb` is otherwise reserved for $\mathbb E$ at 169 and 195. And the posterior is written with subscript zero in the exercise ($\mu_0$, $\gamma_0$ at 343-351) where the body uses primes for the same update ($\mu'$, $\gamma'$ at 126, 132, declared as the convention at 121), so the solution at 371-379 has to translate between the two.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 336, 358, 404, 426. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 49, 60, 154, 358. *Example:* 49 does not agree with itself - "high aggregate economic activity levels generates valuable information" - and stacks four modifiers before the noun; 60-62 restates line 29, which has already said the lecture studies "a simplified version of an uncertainty traps model of Fajgelbaum, Schaal and Taschereau-Dumouchel", as two further sentences saying the original has many moving parts and this is a simplified version; 154 has no full stop and reads awkwardly ("Thus, if one of these values for $M$ remains fixed, a corresponding steady state is the equilibrium level of precision") where 426-429 says the same thing cleanly; and the solution at 358-362 opens by restating the exercise prompt back to the reader and uses "the stated result" twice in two sentences.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 140, 385, 409, 447. *Example:* the code for the lecture's three body figures is not in the lecture - it is in the solution to exercise 2 (408-423, 434-466, 471-477, 482-502), so the reader who wants to know how the 45-degree diagram at 147 was made must open a dropdown 260 lines later, and the body's narrative at 142-160 is describing a picture whose construction is deliberately hidden. Exercise 2 then asks to "replicate the simulation figures shown above" (385) *modulo randomness*, but its own solution cannot be replicated at all: 447 calls `np.random.default_rng()` with no seed, and 505 concedes "If you run the code above you'll get different plots, of course" - even though `gen_aggregates` was given an `rng` parameter (281) precisely so a seed could be passed in. The `econ` object created at 409 for the 45-degree plot is the same object the simulation mutates in place at 455-456, so re-running the cell at 434-466 without re-running 408 continues from the previous run's `self.μ`, `self.γ`, `self.θ` and silently gives a different series. And 140 points at "Exercise 1" by number rather than `{ref}`uncertainty_traps_ex1``, so the pointer does not resolve to the exercise 190 lines below.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 232, 336, 387. *Example:* 232 and 387 write `__init__` bare in narrative markdown, where the paired double underscores are emphasis delimiters - so "The __init__ method encodes as default values" renders as "The **init** method", producing bold text that is neither a definition nor emphasis (and losing the method name); backticks fix both. Line 336 uses bold as a structural label, `**Fact** Let $\mathbf x = ...$`, running the label straight into the sentence with no punctuation, in a repo that has `{prf:theorem}`/`{prf:lemma}` directives for exactly this. The lecture's two genuine definitions are correctly bold (**precision** 96, **propagation mechanism** 326) and it uses no italic anywhere.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 4. *Lines:* 45, 147, 204, 510. *Example:* the lecture's whole subject is a three-step feedback loop, set out as three bullets at 45-47 (high uncertainty discourages activity, low participation cuts the information flow, less information raises uncertainty) and restated at 49 as a positive externality - and it is never drawn, though a three-node cycle is the one diagram this lecture obviously wants. The three figures it does have (147, 302, 321) are static PNGs with empty caption bodies, so all of the description has to be carried in prose: 142-145 has to say that the image is "a 45 degree diagram, with one curve for each $M \in \{0,\ldots,6\}$" and list the parameter values, and 318-319 has to say what the third one contains. The participation threshold `` {eq}`firm_test` `` at 204-215 is what makes $M$ collapse, and nothing plots $\psi(\mu,\gamma,F_m)$ or the active-set boundary in $(\mu,\gamma)$ space, so the mechanism behind the collapse is never visible. And the lecture carries no admonition at all: 178 (what "pre-visible" means, on which `` {eq}`pref1` `` depends) and 510-512 (the parenthetical about non-Gaussian shocks taking you outside the Kalman filter) are both `{note}` material written as plain paragraphs.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 413. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 60. *Example:* `` {cite} `` in narrative flow: 'in `` {cite} ``'.


## Strengths

- The feedback loop is stated before any mathematics: 43-47 gives the three steps of the trap and 49 names the externality that drives it, so a reader knows what the model is for before meeting $\gamma$.
- Precision, not variance, is made the primitive and the choice is justified where it is introduced - 96-98 defines $\gamma_x$ as the shock precision and says immediately why it matters ("the higher is the precision, the more informative $x_m$ is about the fundamental") - which is what makes the additive updating rule `` {eq}`update_prec` `` readable.
- The Kalman step is not asserted: the standard scalar-Gaussian result it rests on is quoted in full as exercise 1 (333-352) with a page reference to `` {cite}`young2005` ``, and the solution at 376-379 supplies the missing half - pushing the posterior through $\rho\theta + \sigma_\theta w$ to get $\mu'$ and $\gamma'$.
- The 45-degree diagram is used to do real work: 151-160 reads the fixed points off it as steady-state precisions indexed by $M$, states the comparative static in both directions, and then says at 160 that $M$ will in fact fluctuate - which sets up the whole simulation.
- The class carries exactly the state the model has and nothing else - parameters plus $(\theta, \mu, \gamma)$ at 250-255 - and each method is one law of motion: `update_beliefs` is `` {eq}`update_mean` `` and `` {eq}`update_prec` `` (262-273), `update_θ` is the fundamental process of 68-70 (275-279), and `ψ` is `` {eq}`firm_test` `` (257-260).
- `gen_aggregates` (281-293) handles the case the economics makes possible and the algebra does not: when no firm is active it sets $X = 0$ rather than averaging an empty array, which is exactly the degenerate branch an uncertainty trap produces.
- The results section reads the simulation the way the model predicts: 306-316 identifies the trap episodes by two symptoms (low precision, few firms), and 324-326 makes the one claim the exercise is set up to check - that traps follow a run of bad fundamental draws, which is a propagation mechanism rather than an impulse.

## Recommended actions

1. Move the figure-generating code out of the exercise 2 solution and into the body where the figures are described: 408-423 belongs next to 142-149, and 434-502 next to 300-322, which also removes the need for three static PNGs (qe-fig-002 at 147, 302, 321).
2. Seed the simulation - `np.random.default_rng(seed)` at 447 - so that "replicate the simulation figures shown above" (385) is possible and 505 can be deleted; and give the 45-degree cell its own `UncertaintyTrapEcon()` so the simulation at 434-466 does not depend on the mutated state of the `econ` created at 409.
3. Wrap `__init__` in backticks at 232 and 387, where the bare double underscores currently render as bold "init", and convert the `**Fact**` label at 336 into a `{prf:theorem}` or `{prf:lemma}`.
4. Draw the feedback loop of 43-49 as a three-node diagram, and add a plot of the participation threshold $\psi$ from `` {eq}`firm_test` `` so the collapse in $M$ has a picture.
5. Settle on either $\gamma^{-1}$ or $1/\gamma$ throughout - 91 and 109 use the first, 212, 337, 339, 343, 351, 365, 371 and 373 the second - and replace $\mathbb M$ at 117-118 with a plain letter.
6. Clear the mechanical list: sentence-case the two headings at 58 and 102, replace `\mathbf x` with plain $x$ at 336, 340 and 343 (qe-math-004), brace the two `\mathbb E [` at 169 and 195, give the three `{figure}` directives captions and `:name:` fields (147, 302, 321) plus the three code-cell figures (408, 471, 482), remove the five double spaces (35, 37, 39, 151, 338), and make 60's citation `{cite:t}`.
7. Fix the code items: the stray comma at 251, the off-by-one parameter indent at 237-247, the banner comments at 249 and 254, `temp1`/`temp2` at 258-259 and 269-270, `sim_length=2000` at 435, the redundant `label_string` at 417, and the six `fontsize=` overrides (419, 420, 421, 475, 488, 499) together with the three `figsize` overrides (412, 472, 483).
