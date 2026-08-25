# discrete_dp

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/discrete_dp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-005` ×16; `qe-writing-001` ×1; `qe-writing-008` ×4. |
| Math         | 4/10  | `qe-math-002` ×6; `qe-math-010` (proposed) ×1; `qe-math-004` ×1, +1 more. |
| Code         | 6.5/10 | `qe-code-002` ×2; `qe-code-001` ×3; `qe-code-005` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×6; `qe-fig-003` ×1; `qe-fig-002` ×2, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 7/10  | `qe-link-002` ×10. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 552, 566, 750, 862, 882, 916. *Example:* {figure} without :name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 10. *Lines:* 75, 76, 90, 193, 209, 543, 616, 624, 715, 911. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 247, 264, 273, 305, 319, 419. *Example:* apostrophe transpose `s'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 202. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 16. *Lines:* 144, 164, 165, 171, 172, 173, 175, 177, 179, 195, …. *Example:* the lecture's whole formal apparatus is defined in italic rather than bold - *stationary Markov policies* (144), *states* (164), *feasible actions* and *feasible state-action pairs* (165), *reward function* (171), *transition probability function* (172), *discount factor* (173), *action space* (175), *policy* (177), *feasible* (179), *controlled chain* (195), *policy value function* (228), *optimal value function* / *value function* (230), *optimal* (239), *Bellman operator* (258), *Bellman equation* (300) - which is the exact reversal the rule warns about; the file contains one bold span in 1010 lines and it is `**Notes**` at 711, used as a pseudo-heading rather than for a definition or an emphasis.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 631, 865, 925. *Example:* line 631 binds a lambda to a name (`f = lambda k: k**α`) where PEP8 asks for `def` (E731); lines 865 and 925 write `figsize=(8,5)` with no space after the comma, while the same file writes `figsize=(14, 4)` at 751 and `figsize=(8, 10)` at 885 - the spacing is inconsistent within the lecture, not just against PEP8.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 933, 934. *Example:* spelled-out `beta`.
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 3. *Lines:* 844, 845, 846. *Example:* %timeit.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 751, 865, 885, 925. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 552, 566. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 904. *Example:* .set_title.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 1001. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 727. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 183, 285, 543, 951. *Example:* 2 spaces.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 1001. *Example:* ones vector `\mathbf{1}` used 1x with no 'vector of ones' explanation in the prose.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 152. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- The formal definition at 160-175 gives every object in a discrete DP an explicit type signature - $r\colon \mathit{SA} \to \mathbb{R}$, $Q\colon \mathit{SA} \to \Delta(S)$, $\sigma\colon S \to A$ - so the later `DiscreteDP(R, Q, β, s_indices, a_indices)` call reads as a direct transcription of the mathematics.
- The discrete solution is checked against the closed form of the continuous model: `v_star` and `c_star` are coded at 740-748 from the analytical constants at 736-738 and then overlaid on the computed policy, so the reader sees the discretization error rather than being told about it.
- "How to read this lecture" (71-79) states the prerequisite lecture and what background is assumed before any notation appears, and the appendix at 945-1010 gives the three algorithms as numbered pseudo-code with the $\varepsilon$-optimality definition (951) they all reference.
- The three solution methods are not just described - 817-847 runs all three on the same `ddp`, checks `np.array_equal(σ, res1.sigma)` and `np.array_equal(σ, res2.sigma)` to confirm they agree, and then times them.
- Code uses Unicode Greek (`α`, `β`, `σ`) consistently from 630 onward, matching the $\alpha$, $\beta$, $\sigma$ of the model statement.

## Recommended actions

1. Bold each defined term at the 15 places listed above and keep italic for the genuine emphases (*policies* at 139, *indices* at 727) - this is the single most systematic style deviation in the file.
2. Gate the exercise and its solution: the exercise at 614-618 is plain prose and the 320-line "## Solutions" section at 620 is an ordinary H2 full of executable cells, so it is neither an `{exercise-start}` block nor a `{solution-start}` / `{solution-end}` pair with `:class: dropdown` (qe-admon-001, qe-admon-002 and qe-admon-005 all have nothing to attach to here).
3. Fix the unbalanced brackets in the feasibility condition at 651 - `grid[a] < f([grid[s])` should read `grid[a] < f(grid[s])`.
4. Delete or convert the cell at 699-703: all three of its lines are commented out, so the cell executes nothing while claiming to show "the most efficient way to create the `Q` matrix"; if the code is worth keeping, put it in a `{note}` as a code block rather than a live cell.
5. Add `:name:` to the six figures at 552, 566, 750, 862, 882 and 916 and reference them with `{numref}` (qe-fig-005, 6 occurrences), regenerate the two static PNGs at 552 and 566 as code cells (qe-fig-002), drop the four `figsize=` overrides at 751, 865, 885, 925 (qe-fig-001) and move the embedded title at 904 into a caption (qe-fig-003).
6. Turn the ten raw quantecon URLs at 75, 76, 90, 193, 209, 543, 616, 624, 715 and 911 into `{doc}` references (qe-link-002), and disambiguate "the lecture" at 854 and 858-859 - it means the optimal growth lecture, not this one, and a `{doc}` reference would say so.
7. Sweep the remaining single-instance items: brace the expectation at 202 (`\mathbb{E}`, qe-math-010 (proposed) proposed), replace `\mathbf{1}` at 1001 with a plain $1$ and explain the ones-vector notation where it is introduced (qe-math-004, qe-math-008), swap the three `%timeit` calls at 844-846 for `qe.tic`/`qe.toc` (qe-code-005), rename the loop variable `beta` at 933-934 to `β` (the `ddp0.beta` attribute name itself has to stay), split the two-sentence paragraph at 727 and collapse the four double spaces at 183, 285, 543, 951.
