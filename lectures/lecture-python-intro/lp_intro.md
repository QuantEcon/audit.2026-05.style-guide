# lp_intro

- **Series:** lecture-python-intro
- **File:** `lectures/lp_intro.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-005` ×5; `qe-writing-004` ×3; `qe-writing-001` ×4, +3 more. |
| Math         | 6.5/10 | `qe-math-002` ×9. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 115, 116, 123, 127, 128, 129. *Example:* missing space after commas in `ax.set_xlim(0,15)` and `ax.set_ylim(0,10)` (115-116), in the polygon vertex list `[[0, 0],[0, 6],[2.5, 5],[5, 0]]` (123) and in the three iso-revenue plot calls `label="...",color='k',linewidth=0.75` (127-129). The column alignment inside the numeric matrix and bounds literals (462, 468-472, 680-682, 741-742) is deliberately matrix-like and is covered by the rule's own mathematical-notation exception, so it is not counted here.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 9. *Lines:* 287, 305, 380, 562, 564, 598, 637. *Example:* apostrophe transpose `c'`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 47, 242, 254, 509, 548. *Example:* the same three terms are bolded as if newly defined each time they recur: **dual** at 33, again at 47, again at 509, again at 548; **standard form** at 43, again at 242, again at 254; **primal** at 31, again at 509 - after the first definition these are emphasis, which the rule assigns to italic.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 36. *Lines:* 27, 31, 70, 80, 160, 166, 168, 170, 172, 176, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 118, 119, 132. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 193, 200, 208, 419. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 166, 168, 170, 178. *Example:* the three investment options are stated as 36-43 word run-ons, each packing two or three separate rules into one sentence - the annuity terms plus the must-keep-investing condition (166), the deposit terms plus the borrowing limit plus the repayment terms (168), and the bond availability plus the cap plus the payout (170-172) - and the variable list at 178 is a 32-word sentence that also contains the typo "the amount of put in the annuity".
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 240, 405, 513. *Example:* mid-sentence 'Example'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 109. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 550. *Example:* the duality section opens with "Let's develop these ideas using the production problem from Example 1" (513) and the dual it builds at 550-557 has exactly two variables, so it could be drawn with the same feasible-set-plus-iso-line figure the primal gets at 109-138; instead the two shadow prices are only asserted numerically (608) and verified by re-solving (616-624), and the reader never sees the dual feasible region or that the two optimal values meet.


## Strengths

- The lecture earns its computational turn: the graphical solution at 109-148 is explicitly shown not to scale (150-154), which is what motivates the standard form and the solver.
- The duality section is built from an economic story rather than an algebraic identity - the outside investor pricing material and labor (528-546) - and then the shadow prices are verified numerically by relaxing the material constraint from 30 to 31 and recovering exactly 0.625 (616-624).
- Both examples are carried all the way through: stated (86, 223), transformed to standard form (315, 356), and solved with `linprog` (409, 454), so the reader can see the same problem in three representations.
- The note at 628 points out that `res_ex1.ineqlin.marginals` gives the shadow prices directly, and then explains the sign convention (637-639) rather than leaving the reader to puzzle over the negative numbers.
- Every matrix is written with `bmatrix` (272-280) and the `{seealso}` at 51 uses an intersphinx `{doc}` reference to the optimal transport lecture rather than a raw URL.

## Recommended actions

1. Replace the nine apostrophe transposes with `^\top` - `c'x` (287, 380, 562), `b'y` and `A'y` (564), `c'x \le b'y` (598), `-c'x` (637) - the single largest fix in this lecture.
2. Plot the dual feasible region and iso-cost lines alongside the primal figure so strong duality can be seen rather than only computed.
3. Break the three investment-option paragraphs at 166-172 into one sentence per rule, and split the four multi-sentence paragraphs at 193, 200, 208 and 419.
4. Add `mystnb: figure: caption/name` metadata to the graphical-solution figure at 109 - it is the only figure in the lecture and the prose refers to it as "The following graph" (105) and "The blue region" (140).
5. Either cite the equation labelled `lpproblem` (291) somewhere with `{eq}` or drop the label - as it stands it is the lecture's only labelled equation and nothing references it.
6. Replace the 13 uses of `\mbox{subject to }` with `\text{subject to }`, set `lw=2` on the three constraint lines (118, 119, 132), and strip the 36 runs of double spaces.
7. Use italic for the recurring emphasis on primal/dual/standard form after their first bolded definition, and fix the index slip at 305 where a free variable is introduced as $x_i$ and then split into $x_j^+$ and $x_j^-$.
