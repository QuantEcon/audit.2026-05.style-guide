# calvo_machine_learn

- **Series:** lecture-dp
- **File:** `lectures/calvo_machine_learn.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×5; `qe-writing-002` ×6; `qe-writing-003` ×2, +2 more. |
| Math         | 3/10  | `qe-math-002` ×13; `qe-math-004` ×4; `qe-math-013` (proposed) ×1, +1 more. |
| Code         | 6/10  | `qe-code-003` ×4; `qe-code-001` ×4; `qe-code-002` ×1, +1 more. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×4; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 13. *Lines:* 860, 862, 865, 867, 870, 879, 880, 881. *Example:* `^T` transpose in `\vec{\beta}^T`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 46, 391, 417, 1184, 1191, 1328. *Example:* line 46 has 'money growh rates'; line 391 has 'answers will agree with those found obtained by other more structured methods'; line 417 doubles a clause - 'compare the results we obtain here to those that we obtain in those obtained in this quantecon lecture'; line 1184 reads 'it will worthwhile to study the reasoning that let Chang `` {cite}`chang1998credible` `` to choose' (missing 'be', and 'let ... to choose' for 'led ... to choose'); line 1191 has 'inflation at time $t$ is determined $\{\mu_s\}_{s=t}^\infty$' with the preposition missing; line 1328 has 'the peak of the function quadratic function'. Line 1163 is a seventh of the same kind and a notation slip besides - 'both of them converge from above to the same constant $\vec \mu$' uses the vector symbol for what the rest of the lecture calls $\bar\mu$.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 18, 24, 59, 72, 389. *Example:* five concept names are wrapped in double backticks and so render as inline code rather than as defined terms: ``machine learning`` (18 and again 389), ``dynamic programming squared`` (24), ``gradient descent`` (59), ``artificial intelligence`` (72). None is a code identifier. The file itself shows what these should look like - '**machine learning** approach' at 48, '**human intelligence**' and '**artificial intelligence**' at 1167 - so the same terms appear in two different formats within one lecture, and the code font wrongly suggests the reader should look for a function of that name.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 193. *Lines:* 18, 19, 21, 24, 27, 29, 31, 36, 39, 43, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 556, 591, 602, 1131. *Example:* line 556 writes `λ ** jnp.arange(T + 1)` with spaces around the exponentiation operator while line 563 seven lines below writes `λ**(T - jnp.arange(T))` and 574 writes `α**2` tight - the rule asks for the tight form; line 560 writes `λ_powers[:T-t]` unspaced. Line 591 runs to about 89 characters (E501). Line 602 puts one space before an inline comment and the comment says nothing: `print(...) # good!` (E261). Lines 1131, 1133 and 1317 write `max(Ts)*0.07` unspaced immediately after a spaced `+` in the same expression. Trailing whitespace is scattered through the JAX cells (554, 557, 561, 564, 566, 576, 578, 582, 584, 587, 589, 592).
- **[qe-code-003]** — Package installation at lecture top. *Count:* 4. *Lines:* 399. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 656, 941. *Example:* %%time.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 1035, 1221, 1262, 1308. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 1223, 1264, 1313. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 4. *Lines:* 865, 867, 870, 872. *Example:* \mathbf.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 865, 870, 872. *Example:* the diagonal matrix built from $\vec\beta$ is written as a vector times an identity: $B^{T}(h_2 \cdot \vec{\beta} \cdot \mathbf{I})B$ at 865, $(\frac{c}{2} \cdot \vec{\beta} \cdot \mathbf{I})$ at 870, and again at 872. A vector dotted with an identity matrix is not a defined product, and the object meant - $\operatorname{diag}(\vec\beta)$ - is both simpler to read and correct. Fixing this also removes three of the four `\mathbf` uses the mechanical check flags.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1151. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 383, 843. *Example:* line 383 sends the reader to a formula that does not exist: 'where $\tilde \theta_t, \ t = 0, 1, \ldots, T-1$ satisfies formula (1)'. Nothing in this lecture is numbered (1) - its equations carry labels (`eq_grad_old1`, `eq:inflation101`, `eq:Ramseyvalue`, `eq:valueformula101`), and the intended target is presumably `` {eq}`eq:inflation101` ``. Second, the truncated objective is written two incompatible ways within the same lecture: at 379-380 the tail term is $(h_0 + h_1\bar\mu + h_2\bar\mu^2 - \frac{c}{2}\bar\mu^2)$, while at 841-845 the same tail is $(h_0 + h_1\theta_T + h_2\theta_T^2 - \frac{c}{2}\mu_T^2)$; then 860, 865, 870 and 878 equate infinite sums $\sum_{t=0}^\infty$ to finite $(T+1)$-dimensional quadratic forms. A reader following the affine-quadratic derivation - the whole point of the second, 'less lazy' approach - has to guess which convention is in force at each step.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 454. *Example:* spelled-out `beta`.
- **[qe-math-013 (proposed)]** — Reference equations via `` {eq}`label` ``. *Count:* 1. *Lines:* 383. *Example:* manual reference 'formula (1)'.


## Strengths

- The lecture states its own methodological bet plainly and defends the label it uses for it: 39-41 says it will proceed 'without knowing the mathematical structure imparted by dynamic programming squared' and simply pick two infinite sequences, and 48 explains that it is called machine learning precisely because it discards structure and proliferates parameters - which is honest about the point being made rather than dressing the approach up.
- The two approaches are ordered by the mental effort they require, with the trade stated (56-61: the first 'is really lazy' and hands the objective to a gradient-descent optimiser; the second 'exerts enough mental effort' to write the objective as an affine quadratic form and solve the first-order conditions), and each is checked numerically against the dynamic-programming answer - `np.abs(V_val - clq.J_series[0])` at 602 and `np.linalg.norm(optimized_μ - clq.μ_series)` at 669.
- 'Adding some human intelligence' (1156-1330) delivers exactly what the introduction promised at 65-72: three regressions recover the three objects `` {doc}`calvo` `` derives analytically - the policy function $\mu_t = b_0 + b_1\theta_t$, the law of motion $\theta_{t+1} = d_0 + d_1\theta_t$, and the quadratic continuation value in $\theta_t$ - and 1177-1179 names the human contribution precisely ('we are free to regress anything on anything else. Human intelligence tells us what regressions to run').
- The awkward diagnostic is reported rather than hidden: the third regression's high condition number is flagged at 1297, attributed at 1299-1300 to $\theta_t$ and $\theta_t^2$ being nearly collinear along the Ramsey path, and then checked with `np.corrcoef(θs, θs**2)` at 1303.
- The `{note}` at 1150-1153 replaces a piece of received jargon with a description: what some call 'the value of a Ramsey plan under a time-less perspective' is, more usefully, 'the value of the worst continuation Ramsey plan' - and that renaming is what makes the ordering $v_0 > V^{CR} > v_T$ at 1145-1147 interpretable.
- Figures are named and cross-referenced properly with `{numref}` (1142, 'Figure `` {numref}`continuation_values` `` shows interesting patterns'), and the reader is told what to look for in the scatter before seeing it (1230-1232: the time-0 pair at the upper right, later pairs moving to the lower left and converging on $(\bar\mu, \bar\mu)$).

## Recommended actions

1. Replace the copied `ChangLQ` class at 427-506 with a `:load:` of a shared file. This is the third verbatim copy of the same class in this series - calvo.md 904-1015, calvo_abreu.md 395-506 and here - and lines 419-422 admit it ('we copy the class ChangLQ used in that lecture. We hide the cell that copies the class'). All three copies carry the same stale comments '(41.16)', '(41.17)', '(41.18)' (457, 461, 464), which refer to an equation numbering none of the three lectures has.
2. Clear the 193 double spaces (qe-writing-008) - the largest mechanical item, and note that many of the affected lines are also extremely long (48 is a single 246-character paragraph, 70 is 205, 39 is 174), so this is a good moment to break those sentences up as well.
3. Replace the 13 `^T` transposes with `^\top` at 860, 862, 865, 867, 870, 879, 880 and 881 (qe-math-002 x13) and write the four `\mathbf{I}` occurrences as $\operatorname{diag}(\vec\beta)$ per the note above (qe-math-004 x4) - together these are the whole of the file's math debt and they sit in the one derivation the lecture asks the reader to follow closely.
4. Add `jax` to the install cell at 399-405. It installs `quantecon`, `optax` and `statsmodels` but the very next cell imports `jax.numpy` and `jax.jit`/`grad` (410-411), so a fresh environment fails at the import (qe-code-003 x4).
5. Stop hand-writing regression output into the prose. Lines 1209 and 1219 quote '$\mu_t = .0645 + 1.5995 \theta_t$' as literal text, but those coefficients come from the fit executed at 1195-1203 - change $\beta$, $c$ or $T$ and the prose silently becomes wrong. Print them from `results1.params`, or state the relation symbolically as $\mu_t = b_0 + b_1\theta_t$ and let the regression supply the numbers.
6. Fix the two pointers and the notation clash: 'formula (1)' at 383 should be `` {eq}`eq:inflation101` ``, and the tail term of the truncated objective needs one consistent form across 379-380 and 841-845, with $\sum_{t=0}^\infty$ at 860, 865, 870 and 878 replaced by the finite sums the quadratic forms actually represent.
7. Finish the small items: the five concept names in double backticks (18, 24, 59, 72, 389) become bold or italic; the 2 `%%time` magics at 656 and 941 become `qe.Timer` (qe-code-004 x2); mystnb `name`/`caption` metadata goes on the 4 figure cells at 1035, 1221, 1262 and 1308 and `lw=2` on the 3 line plots at 1223, 1264 and 1313 (qe-fig-005 x4, qe-fig-008 x3); and the typos at 46, 391, 417, 1163, 1184, 1191 and 1328 plus the code slips at 556, 560, 591, 602 and 1131 get cleaned up.
