# career

- **Series:** lecture-dp
- **File:** `lectures/career.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-006` ×1; `qe-writing-008` ×2. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×6; `qe-fig-001` ×5; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 176, 318, 335, 420, 529. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 166, 312, 334, 372, 395, 523. *Example:* {image} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 60. *Example:* H3 Title Case: 'Model Features' (Features).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 168, 410, 485. *Example:* line 485 writes `i, j  = qe.random.draw(F), qe.random.draw(G)` with two spaces before the `=` (pycodestyle E221); the identical line at 414 has one. Line 168 `np.zeros(n+1)` and line 179 `list(range(0, n+1))` omit the spaces around `+` that the rest of the file uses (`k + a`, `n - k + b` at 170). Line 410 is the substantive one: inside `gen_path` the branch reads `elif greedy_star[i, j] == 2` - the module-level array - where the sibling branch at 407 reads the `optimal_policy` parameter, so the function silently ignores its own argument.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 179, 423, 424. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 70, 275. *Example:* 2 spaces.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 372. *Example:* static image .png.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 113. *Example:* the three continuation values are named with Roman numerals - `$v(\theta, \epsilon) = \max\{I, II, III\}$` at 113, defined at 121-124, and referred to again at 128 and 219-220. $I$ is the conventional symbol for an identity matrix, and $II$ / $III$ read as products of it. The lecture's own code writes the same three quantities as `v1`, `v2`, `v3` (244-246, 259-261), so $v_1, v_2, v_3$ in the math would be both simpler and a direct match to the implementation.


## Strengths

- The three regimes are named once and then labelled identically everywhere: 'stay put' / 'new job' / 'new life' at 81-85, in the interpretation at 128, as `ax.text` annotations placed inside the policy regions at 341-343, and as the trailing comments on the code branches at 244-246 and 407-413 - so the math, the figure and the code use one vocabulary.
- Only the two real definitions are bold - **career** at 69 and **job** at 70 - and the distinction they draw (a career spans many jobs) is exactly what makes the three-option choice set at 78-85 non-obvious, so the bold is doing definitional work rather than decoration.
- Both labelled equations are cited: `exw` (99) at 107 and `eyes` (119) at 220, the latter tying the Bellman operator in code back to the display that defines it - no orphan labels and no manual 'equation (2)' references.
- The Beta-binomial family is motivated before it is used: pmf at 147-151, a three-line generative interpretation at 155-157, and then a figure at 166-182 that shows what the shape parameters actually do to the mass - so the `F_a`/`F_b`/`G_a`/`G_b` arguments of `CareerWorkerProblem` mean something by the time they appear at 196-199.
- Density and CDF case is used correctly throughout: lowercase $p(k \mid n, a, b)$ for the pmf at 148, uppercase $F$ and $G$ for the distributions at 90-91, and `F = np.cumsum(cw.F_probs)` at 396 is in fact the CDF (qe-math-015 (proposed) clean).

## Recommended actions

1. Fix the two defects in `gen_path` (402-417): line 410 reads the global `greedy_star` instead of the `optimal_policy` parameter that line 407 reads, and the parameter `t=20` is shadowed by the loop variable at `for t in range(t)` - the function happens to give the right answer here only because the caller at 422 passes `greedy_star`.
2. Give the 6 figure sites names and mystnb metadata (166, 312, 334, 372, 395, 523) so the surface plot, the two policy contour plots and the sample-path panel can be cross-referenced (qe-fig-005 x6).
3. Replace the static PNG at 372 with the code that generates it (qe-fig-002) - the solution at 395-429 already draws that exact figure, so the exercise can `{ref}` the solution's figure instead of shipping a bitmap.
4. Drop the 5 hand-set `figsize=` arguments (176, 318, 335, 420, 529) and add `lw=2` to the 3 default-width line plots (179, 423, 424) (qe-fig-001 x5, qe-fig-008 x3).
5. Rename the Roman-numeral continuation values to $v_1$, $v_2$, $v_3$ at 113, 121-124, 128 and 219-220, matching the `v1`/`v2`/`v3` already used in the code.
6. Sentence-case the H3 at line 60 ('Model features'), and clear the 2 double spaces at 70 and 275 (qe-writing-006 x1, qe-writing-008 x2).
7. Small cleanups: 'the maximum of `` {eq}`exw` `` overall feasible (career, job) policies' at 107 should read 'over all'; the `\nonumber` markers at 123 and 124 do nothing inside an `aligned` block in a labelled `{math}` directive; the `Axes3D` import at 56 is unused with current matplotlib; and even out the operator spacing at 168, 179 and 485.
