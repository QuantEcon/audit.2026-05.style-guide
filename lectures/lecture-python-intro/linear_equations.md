# linear_equations

- **Series:** lecture-python-intro
- **File:** `lectures/linear_equations.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×3; `qe-writing-003` ×2; `qe-writing-002` ×4, +2 more. |
| Math         | 6.5/10 | `qe-math-002` ×2; `qe-math-003` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×5; `qe-fig-007` ×3; `qe-fig-008` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 7.5/10 | `qe-link-002` ×5. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 170, 258, 268, 328, 915, 1077, 1081, 1217, 1330. *Example:* continuation lines inside `arrowprops=dict(...)` indented to the outer call rather than the opening paren (170, 258, 268, 328); `plt.plot`/`plt.xlabel` used on the pyplot state machine right after `fig, ax = plt.subplots()`, with f-strings that have no placeholders (915-916, 1374-1375); `h.shape = 2,1` with no space after the comma (1077, against `(3, 1)` at 1210); and imports scattered through the body instead of the imports cell at 44-47 (1081, 1107, 1202-1203, 1217, 1227, 1330-1331) - the cell at 1215 imports `det` for the second time and then calls `inv`, which it never imports.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 155, 242, 315, 912, 1365. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 5. *Lines:* 352, 660, 666, 955, 1388. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 1273. *Example:* `^T` transpose in `A^T`.

### Medium severity
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 3. *Lines:* 163, 250, 323. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 915, 916, 1372, 1373. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 817. *Example:* matrix environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1157. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 525, 947, 1017, 1259. *Example:* two 36-38 word sentences (525, 1259) and two sentences that do not parse: "the $2^{nd}$ row of matrix $A = (2, 6)$ is just a scalar multiple of the $1^{st}$ row of matrix $A = (1, 3)$" (947, where $A$ is the matrix, not the row, and the ordinals are set in math mode) and "You can check yourself that the in {eq}`no_soln` and {eq}`many_solns` with linearly dependent rows are singular matrices" (1017, missing the noun).
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 800, 1384. *Example:* the equilibrium condition changes sign convention between adjacent sections without comment - $(C - D)p = h$ in the two-good case (752, 763), $(D - C)p = e - h$ in the general case (800, 806), then back to $(C-D)^{-1}h$ at 1047 - so the reader has to re-derive which matrix is subtracted from which; and "### Further reading" at 1384 is an H3 placed after the "## Exercises" H2, so it renders as a subsection of the exercises.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 1010, 1024, 1245. *Example:* three definitions are set in italic where the rule asks for bold - "then we say that $A$ is *nonsingular*" (1010), "it possesses an *inverse matrix* $A^{-1}$" (1024) and "$Ax = b$ is called an _inconsistent_ system of equations" (1245, which also switches to underscore emphasis) - while the lecture's other definitions are correctly bolded (**vector** 135, **inner product** 375, **norm** 392, **least squares solution** 1259).

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 963. *Example:* "### No solution" (897) plots the two parallel lines so the reader can see why no intersection exists, but the parallel section "### Many solutions" (963) asks "can you see why?" (989) about linearly dependent rows with no figure at all - the same two-line plot, with the lines coincident, is the obvious counterpart.


## Strengths

- Every one of the eleven labelled equations is cited by `{eq}` somewhere else in the lecture (`two_eq_demand` at 109 and 695, `two_equilibrium` at 689, `la_se` at 836 and 883, `la_se2` at 890/893/991, `la_se_inv` at 1052, `inconsistent` at 1259, `n_eq_sys_la` at 859) - there are no orphan labels and no manual "equation (3)" references.
- The `\color{red}`/`\color{blue}` highlighting of the row and column being combined (378-388, 540-551, 564-584, 1003-1007) is a genuinely effective way to show where each element of a matrix product comes from.
- Transposes are written `^\top` everywhere in the body (378, 396) - only the least-squares formula at 1273 slips to `^T`.
- The lecture builds the same two-good market three times - pencil and paper (59-114), matrix form (687-764), NumPy (1039-1119) - and closes the loop by checking that the numerical answer matches the hand calculation (1102).
- `{index}` entries are attached to each major section (16, 132, 180, 369, 421, 880, 1041), which is rare in this series and makes the lecture searchable.

## Recommended actions

1. Replace `^T` with `^\top` in the least-squares formula at 1273 (two occurrences) so the whole lecture uses one transpose notation.
2. Fix the determinant display at 1001-1008: as written a `bmatrix` is set equal to the scalar $ad - bc$; use `\det` or a `vmatrix`.
3. Fix the two index typos in the matrix-times-vector display {eq}`la_atx`: `a_{i}k` should be `a_{ik}` (567) and the first row of the product reads `a_{11} x_1 + a_{22} x_2` where it should be `a_{12} x_2` (579).
4. Add `mystnb: figure: caption/name` metadata to the five un-named figures (155, 242, 315, 912, 1365), keep the figure spines (161-163, 248-250, 321-323), and set `lw=2` on the four line plots.
5. Bold the three italicised definitions (1010, 1024, 1245), replace `\begin{matrix}` at 817 with an `aligned` block or a bracketed matrix, and settle on one form of `\mathbb R` versus `\mathbb{R}` (both appear, at 142 and 240).
6. Convert the five raw `python-programming.quantecon.org` and `python.quantecon.org` URLs (352, 660, 666, 955, 1388) to `{doc}` cross-series references.
7. Move the scattered `numpy.linalg` imports into the top imports cell, fix the mislabelled third arrow in the vector-addition figure (254 reads `(x1+x2, y1+y2)` where it should be `(x1+y1, x2+y2)`), settle the $(C-D)$ versus $(D-C)$ convention, and promote "Further reading" at 1384 to an H2.
