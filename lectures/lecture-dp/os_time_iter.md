# os_time_iter

- **Series:** lecture-dp
- **File:** `lectures/os_time_iter.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×4; `qe-writing-003` ×3; `qe-writing-007` ×2. |
| Math         | 7.5/10 | `qe-math-001` ×2; `qe-math-009` ×1. |
| Code         | 8/10  | `qe-code-001` ×3; `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-008` ×3. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 68, 161, 215, 237. *Example:* H2 Title Case: 'The Euler Equation' (Equation).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 392, 412, 490. *Example:* (1) `K` unpacks all ten `Model` fields at 392 and uses exactly one of them, `grid` at 395 - nine unused locals, where `euler_diff` at 366 unpacks the same ten and uses six. (2) The lambdas at 412-413 take a parameter named `α` that shadows the global `α` assigned three lines above at 409, and they are then called as `f(x - c, α)` at 372 with the *global* `α`, so the two bindings are silently identical and a reader has no way to know which one is in play. (3) The same unpack is repeated in four consecutive cells: `grid = model.grid` (480), `grid, α, β = model.grid, model.α, model.β` (490), the identical line again at 510, and `grid = model_crra.grid` (564) - all in one notebook session where nothing has invalidated the earlier bindings, each under the comment `# Unpack`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 407, 488, 561. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 423, 427, 431. *Example:* plot() without lw=.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 380, 405. *Example:* unicode `σ` inside a math environment.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 165, 259, 515. *Example:* the lecture's efficiency claim is promised, then attributed to a lecture that does not make it, and never measured. The theory section ends 'Examples are given below' (259) and no comparison with value function iteration appears anywhere in the file - no timing, no accuracy table, no shared figure. What arrives instead is 515-517: 'Time iteration runs faster than value function iteration, as discussed in `` {doc}`os_stochastic` ``', but os_stochastic contains no such discussion; its only remark on efficiency (49-55) says the opposite, that later lectures will explore more efficient methods. The one timing in this file is the `%%time` at 562, inside the CRRA exercise solution, with nothing to compare against. Separately, `` {eq}`fcbell20_coleman` `` (165-172) is recalled and labelled and then never cited or used again - the topological-conjugacy discussion at 239-248, which is the only place it could serve, does not refer to it.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 232, 259. *Example:* the lecture twice names a figure and does not draw it. (1) The well-definedness argument at 215-235 sets out the monotonicity and divergence of each side of `` {eq}`cpi_coledef` `` in two bullet lists and then says 'Sketching these curves and using the information above will convince you that they cross exactly once as $c$ ranges over $(0, x)$' (232) - the reader is asked to draw the two-curve picture the whole argument rests on, and both curves are computable from the code the lecture already has (`euler_diff` at 358-373 is exactly their difference). (2) 'Examples are given below' (259) closes a section comparing $K$ with $T$ on stability and convergence rate, and the natural example - the two operators' errors against iteration count on one axis - never appears; every figure in the file (421-435, 492-501, 570-576) shows time iteration alone.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 562. *Example:* %%time.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 351. *Example:* `` {eq}`euler_diff` `` (351-355) is a labelled *expression* with no relation in it - `u'(c) - \beta \int (u' \circ \sigma)(f(x-c)z) f'(x-c) z \phi(dz)` - and line 379 then says 'We will use a root-finding algorithm to solve `` {eq}`euler_diff` `` for $c$', which is only meaningful with the missing `= 0`. Every other display in the lecture is an equation (`` {eq}`cpi_env` ``, `` {eq}`cpi_foc` ``, `` {eq}`cpi_euler` ``, `` {eq}`cpi_coledef` ``), so this one reads as an equation whose right-hand side has gone missing; writing it as `u'(c) - \beta \int \ldots = 0` says what `brentq` at 397 actually solves, and the label would then not be the name of a Python function as well.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 194. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.


## Strengths

- The Euler equation is derived in five labelled steps that each cite the one before, so nothing appears from nowhere: four numbered assumptions (75-78) including the Inada conditions, the envelope condition `` {eq}`cpi_env` `` with its proof sketch (115-125, 'write the Bellman equation in the equivalent form ... Differentiating with respect to $x$, and then evaluating at the optimum yields'), the first-order condition `` {eq}`cpi_foc` ``, their combination into `` {eq}`cpi_euler` ``, and the functional-equation reading `` {eq}`cpi_euler_func` ``.
- The Coleman-Reffett operator gets a one-sentence economic reading immediately after its formal definition - 'In essence, $K\sigma$ is the consumption policy that the Euler equation tells you to choose today when your future consumption policy is $\sigma$' (196-197) - and 205-213 then checks the fixed-point claim by substituting $\sigma^*$.
- Well-definedness is treated as a question to be answered rather than assumed: '### Is the Coleman-Reffett Operator Well Defined?' (215) asks whether `` {eq}`cpi_coledef` `` has a unique root in $(0,x)$ and answers with the monotonicity and the two divergences of each side (222-230), then notes that $K$ maps $\mathscr P$ into itself (234-235).
- The comparison with value function iteration separates what is true in theory from what matters in practice: conjugacy implies the same convergence rate 'at least in theory' (248), while $K$ is 'more stable *numerically*' (250) for two stated reasons - it uses first-order conditions, and policies near the optimum have less curvature than value functions (255-257).
- `Model` carries `u_prime` and `f_prime` beside `u` and `f` (318-319) because line 304 has just said the method needs them - the data structure is derived from the mathematics rather than inherited.
- `euler_diff`'s docstring states its contract in the lecture's own notation ('the root with respect to c, given x and σ, is equal to Kσ(x)', 360-361), so the root-finding call at 397 needs no further comment.
- The iterates of $K$ are plotted as a colour ramp with the initial condition labelled and the final iterate in black (421-435), which is what makes the 'converges quickly' claim at 438 checkable by eye.

## Recommended actions

1. Deliver the comparison the lecture twice promises (259, 515-517) or drop the claim: solve one model both ways and plot error against iteration count, or time both solvers in one cell. As written the attribution to `` {doc}`os_stochastic` `` is wrong - that lecture makes no efficiency comparison - and the only timing here is the `%%time` in the exercise.
2. Draw the two curves the reader is told to sketch at 232: `euler_diff`'s two terms as functions of $c$ on $(0, x)$ for a fixed $x$, which makes the single crossing visible and reuses code already in the file.
3. Write `` {eq}`euler_diff` `` as an equation with `= 0` (351-355) so that 'solve `` {eq}`euler_diff` `` for $c$' at 379 says something, and consider a label that is not also the name of the Python function.
4. Cite or delete the recalled Bellman operator at 165-172 - the label `fcbell20_coleman` is never referenced.
5. Clean the three code items: unpack only what `K` uses (392), rename the lambda parameter at 412-413 so it does not shadow the global `α` set at 409, and delete the redundant re-unpacks at 480, 490, 510 and 564 (490 and 510 are the same line twice).
6. Mechanical items from the draft: `\sigma` rather than unicode `σ` inside the math at 380 and 405 (qe-math-001 x2), `qe.Timer()` in place of `%%time` at 562 (qe-code-004), `{cite:t}` at 194 where the citations are the sentence's object ('the work of `` {cite}`Coleman1990` `` and `` {cite}`Reffett1996` ``'), sentence-case the four Title-Case headings (68, 161, 215, 237), mystnb `name`/`caption` on the three code-cell figures (407, 488, 561), and `lw=2` on the three plot calls at 423, 427 and 431.
7. The upstream twin `lecture-python.myst/lectures/os_time_iter.md` differs only in already using `np.random.default_rng` at 343-344; make these fixes upstream and re-sync so both copies clear.
