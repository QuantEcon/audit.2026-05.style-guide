# markov_chains_I

- **Series:** lecture-python-intro
- **File:** `lectures/markov_chains_I.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-003` ×3; `qe-writing-002` ×3; `qe-writing-001` ×1, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×15; `qe-math-004` ×7; `qe-math-003` ×1. |
| Code         | 7/10  | `qe-code-001` ×9; `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×2; `qe-fig-002` ×2; `qe-fig-008` ×1. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 9/10  | `qe-admon-001` ×1. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 270, 836, 850, 948, 969, 978, 1197, 1217, 1228. *Example:* `ψ_t[0 ]= ψ_0` - whitespace inside the subscript and no space before `=` (836); missing space after commas in `add_edge(node_start,node_end, ...)` (270), `['blue','red', 'green']` (850), `['red','yellow', ...]` (948), `Poly3DCollection(faces,alpha=0.05)` (969), `color=colors[idx],linewidth=0.75` (978) and `matrix_power(P,3)` (1197); a `##` block comment where PEP8 asks for a single `#` (1217); and spaces around the keyword-argument `=` in `color = 'black'` (1228).
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 7. *Lines:* 1258, 1259, 1261. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 145, 165, 332, 333, 343, 546, 547, 548, 620, 1008, …. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 15. *Lines:* 30, 38, 47, 70, 80, 97, 103, 336, 555, 1003, …. *Example:* 2 spaces.

### Medium severity
- **[qe-admon-001]** — Use gated syntax for executable code in exercises. *Count:* 1. *Lines:* 1165. *Example:* code cell inside non-gated {exercise}.
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 490, 494. *Example:* %time.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 105, 1122. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 261, 1206. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 487. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 237. *Example:* array used as matrix.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 231. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 236, 571, 1164. *Example:* the six-state Imam-Temple matrix is printed three times in twenty lines - as a LaTeX `array` (236-247), as a Python list (249-257), and again as a `bmatrix` (292-302) - and then twice more in the exercises (1164, 1190); and the rule that postmultiplication shifts a distribution forward is stated four times in twenty-five lines (571, 573, 575, 589) with two labelled equations, `mdfmc` and `mdfmc2`, that say the same thing, prefaced by "This is very important, so let's repeat it" (581).
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 828, 990, 1122. *Example:* line 828 introduces three initial distributions as $\psi_1, \psi_2, \psi_3$, but $\psi$ with a numeric subscript already means the distribution at that date everywhere else in the lecture ($\psi_t$, $\psi_0$, $\psi_{t+1}$ at 534-596), so "$\psi_i P^t$" at 897 reads as a distribution at date $i$; line 990 tells the reader "The blue dot represents the unique stationary distribution", but the code at 937-948 defines four initial distributions and four colours, so blue is $\psi_4 = (1/3,1/3,1/3)$ and no stationary distribution is plotted in that figure at all - the colour convention also contradicts the adjacent Hamilton animation, where yellow is $\psi^*$ (884); and exercise 1 answers part 1 ("visualize the transition matrix") with a static PNG at 1122 rather than the network-graph code the lecture body uses at 261-288.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1223. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 711. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- Definitions are bolded exactly once at the point of definition and never re-bolded - probability mass function (75), stochastic matrix and Markov matrix (80), states (111), state space and state values (320), distribution (322), Markov chain and Markov property (324), stationary and invariant (700), asymptotic stationarity and global stability (808) - and italic is reserved for genuine emphasis (336, 632, 659).
- Probability events use braces throughout - `\mathbb P\{X_{t+1} = 0 \,|\, X_t = 1\}` (145), `\mathbb P\{X_{t+1} = y \,|\, X_t\}` (332) - satisfying the proposed qe-math-014 convention without exception.
- Three worked examples (Hamilton's economic states, the unemployment chain, the Imam-Temple political chain) are each given a label at first appearance and then re-used by `{ref}` in later sections (630, 655, 743, 895) rather than restated.
- The two 3D simplex animations (844-891, 934-985) are a genuinely good pedagogical pairing: the same figure shows convergence for Hamilton's chain and cycling for the periodic chain, so the reader sees exactly what the positivity condition buys.
- The lecture writes its own simulator first (419-441) and only then introduces `qe.MarkovChain`, and times the two against each other (490, 494) so the reader sees why the library version exists.

## Recommended actions

1. Add braces to the 15 blackboard operators - `\mathbb P` -> `\mathbb{P}`, `\mathbb E` -> `\mathbb{E}`, `\mathbb N` -> `\mathbb{N}`, `\mathbb R` -> `\mathbb{R}` (qe-math-010, proposed).
2. Replace `\mathbf 1` with a non-bold ones vector in the exercise 3 solution (1258, 1259, 1261 - seven occurrences) and say in the prose that it denotes a column of ones.
3. Fix the figure description at 986-994: the four colours are four initial distributions, and the periodic-chain figure plots no stationary distribution; either plot $\psi^*$ as the Hamilton figure does or correct the text.
4. Rename the three initial distributions at 828 and 847-849 (for example $\psi^a, \psi^b, \psi^c$) so the subscript on $\psi$ keeps meaning time throughout.
5. Print the Imam-Temple matrix once: keep the `bmatrix` at 292-302, drop the `array` at 236-247 (which is also the only `array` environment in the file) and let the code cell at 249 be the machine-readable copy.
6. Replace the two static PNGs (105, 1122) with code-generated figures, add `mystnb: figure: caption/name` metadata to the four un-named figures (261, 844, 934, 1206), and convert the code cell inside the non-gated `{exercise}` at 1165 to gated syntax.
7. Convert the author-position citations at 711 to `{cite:t}`, swap the two `%time` magics for `qe.Timer()` (490, 494), fix the set notation at 380 ($S = \{0, \ldots, n-1\}$), rename the loop variable `nodes` at 280 which shadows the state list defined at 250, and clean up the PEP8 items above.
