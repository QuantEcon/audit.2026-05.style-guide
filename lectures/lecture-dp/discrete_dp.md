# discrete_dp

- **Series:** lecture-dp
- **File:** `lectures/discrete_dp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×17; `qe-writing-003` ×2; `qe-writing-002` ×4, +2 more. |
| Math         | 7/10  | `qe-math-010` (proposed) ×1; `qe-math-004` ×1; `qe-math-008` ×1. |
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
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 202. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 17. *Lines:* 139, 144, 164, 165, 171, 172, 173, 175, 177, 179, …. *Example:* the lecture's formal-definition section does the rule exactly backwards: every defined term is italicised rather than bolded. *policies* (139), *stationary Markov policies* (144), *states* (164), *feasible actions* and *feasible state-action pairs* (165), *reward function* (171), *transition probability function* (172), *discount factor* (173), *action space* (175), *policy* (177), *feasible* (179), *controlled chain* (195), *policy value function* (228), *optimal value function* / *value function* (230), *optimal* (239), *Bellman operator* (258), *Bellman equation* (300). These are the terms the rest of the lecture is written in, and none of them is emphasis. Meanwhile the only bold in the file is `**Notes**` at 711, used as a pseudo-heading. There is no formatting left to distinguish a definition from a stressed word.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 454, 865, 925. *Example:* line 454 writes `self.B, self.M, self.α, self.β  = B, M, α, β` with two spaces before the `=` (E221); lines 865 and 925 write `figsize=(8,5)` with no space after the comma (E231), while line 885 in the same file writes `figsize=(8, 10)` correctly and 751 writes `figsize=(14, 4)` - so the file disagrees with itself four times over on one call.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 933, 934. *Example:* spelled-out `beta`.
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 3. *Lines:* 844, 845, 846. *Example:* %timeit.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 751, 865, 885, 925. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 552, 566. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 904. *Example:* .set_title.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 1001. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 727. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 73, 190, 572, 651. *Example:* line 73 reads 'We use dynamic programming many applied lectures, such as' - a preposition is missing; line 190 ends with a stray closing parenthesis, '$r_{\sigma}(s) := r(s, \sigma(s))$)'; line 572 misplaces a comma, 'The `DiscreteDP` class in fact, provides a second interface'; line 651 has unbalanced brackets inside inline code, `grid[a] < f([grid[s])`, which is what the reader is asked to take as the feasibility condition. Line 87's 'minimizing vectorized operators' is a fourth of the same kind - it appears to mean the opposite of what it says, given that line 713-715 warns that vectorization is memory-hungry.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 80, 620. *Example:* the H3 at line 80 is just '### Code' and its first sentence is 'Among other things, it offers' - 'it' has no antecedent anywhere in the section; the subject (the QuantEcon.py `DiscreteDP` implementation) was last named at line 58, two sections earlier, and the four bullets that follow describe an object the reader has to guess at. Second, the exercise/solution structure at 614-620 breaks the reader's expectations for the series: '## Exercises' is a single sentence with no `{exercise}` directive and no label, and '## Solutions' immediately follows with 320 lines of fully visible worked solution - a third of the file. There is nothing to attempt, because the answer starts on the next line.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 183, 285, 543, 951. *Example:* 2 spaces.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 1001. *Example:* ones vector `\mathbf{1}` used 1x with no 'vector of ones' explanation in the prose.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 152. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.


## Strengths

- The formal definition at 160-181 enumerates all five components of a discrete DP as a numbered list and then derives the working notation from them in place - $A$, $\Sigma$, $r_\sigma$, $Q_\sigma$ - so every symbol in the 800 lines that follow has a numbered home the reader can return to.
- Line 211-213 says out loud the identification the whole treatment rests on - 'we're not really distinguishing between functions from $S$ to $\mathbb R$ and vectors in $\mathbb R^n$ ... because they are in one to one correspondence' - which is what licenses the compact operator form $T_\sigma v = r_\sigma + \beta Q_\sigma v$ at 280.
- Both `DiscreteDP` constructor interfaces are demonstrated on the same growth example - the dense $(R, Q, \beta)$ form at 445-501 and the state-action-pair form at 586-609 - so the reader can compare the two set-ups line for line instead of being told the second one exists.
- The discrete solution is checked against the closed form at four levels rather than one: the two-panel overlay at 750-770, the max value error with and without the boundary point (777, 781), the max consumption error (787), and monotonicity of the computed policy (793-804), which the text at 790-791 admits fails - 'not really monotone, but the decrements are quite small'.
- All three solution methods are run on the same instance and their policies compared for exact equality (`np.array_equal(σ, res1.sigma)` at 827 and 838) before any timing is reported at 844-846 - the speed claim at 849-850 rests on having established that the answers agree.
- The appendix at 944-1007 states each algorithm as numbered steps with its exact stopping rule and the guarantee it buys, including the $\varepsilon/2$-versus-$\varepsilon$ distinction between value approximation and policy optimality - it is implementable pseudocode, not a description.
- Notation stays plain and deliberate throughout: $S$, $A$, $\Sigma$, $T$, $T_\sigma$, $\Delta(S)$, and `\mathit{SA}` for the one multi-letter symbol - the correct choice for a two-letter name, and not a decorative face anywhere in the file (qe-math-009 clean).

## Recommended actions

1. Bold the 16 definitions currently in italic (139, 144, 164, 165, 171, 172, 173, 175, 177, 179, 195, 228, 230, 239, 258, 300) and turn `**Notes**` at 711 into a real heading or an admonition. This is the largest editorial change in the file and it affects the section every later section depends on.
2. Gate the exercise and solution at 614-620 with `{exercise}`/`{exercise-end}` and `{solution-start}` with `:class: dropdown`, and give them labels. As written a 320-line solution is fully visible one line after a one-sentence exercise, and the missing directives are also why this lecture scores a clean 10/10 on admonitions.
3. Convert the 10 raw URLs (75, 76, 90, 193, 209, 543, 616, 624, 715, 911). Two of them (`short_path` at 75, `mccall_model` at 76) point at lectures in this same series and want a bare `{doc}` reference; three (`finite_markov` at 193, 209, 543) want `{doc}`intermediate:finite_markov``. Note that 543 reaches for finite_markov on the `python-intro` host and 616/624 reach for optgrowth there while 911 reaches for the same optgrowth lecture on `python.quantecon.org` - so at least three of these are pointing at the wrong site (qe-link-002 x10).
4. Replace the 2 static PNG bar charts at 552 and 566 with the code that draws them (qe-fig-002 x2). The data is already computed one cell earlier at 547 and 561, and the point being made - 'the rightward shift in probability mass' at 564 - is exactly the kind of before/after the reader should be able to re-run at a different $\beta$.
5. Fix the attribute name in the appendix: `iter_max` at 968, 971, 990 and 1007 is `max_iter` in the actual class, as the lecture's own code shows at 527 and 821. Four occurrences, and the appendix is where a reader goes to look it up.
6. Finish the figure work: `:name:` on the 2 `{figure}` directives and mystnb metadata on the 4 plotting cells (552, 566, 750, 862, 882, 916), drop the hand-set `figsize=` at 751, 865, 885 and 925, and move the `set_title(f'{n} value function iterations')` at 904 into a caption (qe-fig-005 x6, qe-fig-001 x4, qe-fig-003 x1).
7. Smaller items: replace the 3 `%timeit` magics at 844-846 with `qe.timeit` (qe-code-005 x3); explain `\mathbf{1}` at 1001 as the vector of ones, or write it as $\mathbb{1}$ per the corpus convention (qe-math-004 x1, qe-math-008 x1); brace the bare `\mathbb E` at 202 (qe-math-010 (proposed), proposed); clear the 4 double spaces at 183, 285, 543 and 951; and fix the prose slips at 73, 190, 572, 651 plus the spacing at 454, 865 and 925. Leave the apostrophes at 247, 264, 273, 305, 319 and 419 alone - they are next-period states.
