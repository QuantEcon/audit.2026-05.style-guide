# os_numerical

- **Series:** lecture-python.myst
- **File:** `lectures/os_numerical.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×5; `qe-writing-003` ×4; `qe-writing-007` ×3, +1 more. |
| Math         | 9.5/10 | `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×3; `qe-fig-008` ×7. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 76, 171, 227, 259, 302, 533. *Example:* the two analytical solutions space the same expression in opposite ways two lines apart: 76 writes `(1 - β ** (1/γ)) * x` - spaces around `**`, none around `/` - and 81 writes `(1 - β**(1 / γ))**(-γ) * (x**(1-γ) / (1-γ))`, none around `**`, spaces around one `/` and none around the two subtractions. The rule is explicit that exponentiation is written `a**b`, so 76 is the one to change, and 81 needs `1 - γ`. flake8 flags the three `E226` sites (76, 81 twice). Three lambdas are bound to names (E731): `objective = lambda x: -g(x)` at 171, and `vf = lambda x: np.interp(x, x_grid, v)` at 241 and again at 548. Argument order flips between a function and its copy, in both pairs: `B(x, c, v, model)` (227-232) against `extended_B(c, x, v, model)` (542), and `get_greedy(v, model)` (440) against `extended_get_greedy(model, v)` (615) - and every call site passes them positionally (267, 450, 560, 623), so a reader who follows 511 and reuses `B` in the exercise silently swaps state for consumption. Three one-line docstrings are written as padded single-double-quote strings rather than triple-quoted - `" The Bellman operator.  Updates the guess of the value function. "` (259), `" Compute the v-greedy policy on x_grid."` (444), `" The Bellman operator for the extended cake model. "` (556) - with leading and trailing spaces and, at 259, a double space. Also trailing whitespace at 302, a one-space inline comment at 328 (E261), and three lines over 79 characters (533, 544, 631).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 287, 359, 376, 464, 572, 614. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 362, 379, 380, 469, 470, 635, 636. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 55, 86, 106, 125, 411. *Example:* H2 Title Case: 'Reviewing the Model' (Model).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 309, 365, 384. *Example:* .set_title.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 144, 363, 471. *Example:* $\hat v$ is used for two different objects seventy lines apart, and the second use appears in a step that refers back to the first. 95-99 defines $\hat v$ as the Bellman *update*, $\hat v(x) = \max_c\{u(c) + \beta v(x-c)\}$, and 101 tells the reader to "Stop if $\hat v$ is approximately equal to $v$". Then 144-145 defines $\hat v$ as the piecewise-linear *interpolant* of the array $\{v_i\}$, and 146-147 writes $T\hat v(x_i)$ in that second sense - so the same hat means "already updated" in step 3 of the first algorithm and "not yet updated" in step 3 of the second. One of the two wants a different mark. Separately the figures disagree with the text about the case of the value function: the mathematics writes $v$ throughout (64, 112, 215, 250) while `ax.set_ylabel('$V(x)$')` at 363 and 381 writes $V$, and 471 labels the policy axis $\sigma(x)$ where the curve plotted against it is $\sigma^*$, the analytical policy of 419.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 511, 567, 461, 316. *Example:* the exercise gives an instruction that its own solution then breaks. 511 says "Try to reuse as much code as possible", and 514-643 instead clones four functions: `B` (227-244) becomes `extended_B` (542-549), `T` (255-269) becomes `extended_T` (555-561), `compute_value_function` (319-348) becomes `compute_value_function_extended` (573-598) - twenty-six lines duplicated with only the operator name changed - and `get_greedy` (440-452) becomes `extended_get_greedy` (615-625). The only substantive difference in any of them is `vf((x - c)**α)` at 549 in place of `vf(x - c)` at 244; adding an `α` field with default 1 to `Model` would have let all four be reused, which is presumably what the exercise was asking for. Second, the solution clobbers the body's state: 567 rebinds `model` to the extended model, 600 rebinds `v` and 627 rebinds `σ`, while the module-level `β, γ, x_grid = model` unpacked at 279 still points at the baseline - so 630-631 has to re-create `baseline_model = create_cake_eating_model()` to recover what 278 already had, and any reader who re-runs an earlier cell after the exercise gets the wrong model. Third, `(pol_an)=` at 461 labels a paragraph and is referenced nowhere - I grepped all five series and the only occurrences of `pol_an` are this line and its synced twin in lecture-dp - so it is a dead cross-reference target, probably intended for the policy figure at 464-476, which has no `mystnb` name of its own. Fourth, 316 reads "It's task is to iterate" for "Its" .
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 388, 338, 287. *Example:* the lecture's two substantive numerical claims are both made about figures that cannot show them. 388-392 says "The quality of approximation is reasonably good for large $x$, but less so near the lower boundary" from `` {numref} ``-less figure 376-386, which draws `v_analytical` and `v` on the same linear axes where they visibly coincide; the difference the sentence is about is invisible, and `v_analytical` is already in memory (373), so `ax.semilogy(x_grid, np.abs(v - v_analytical))` would show exactly the boundary blow-up the next sentence explains. 478-481 makes the same kind of claim about the policy ("The fit is reasonable but not perfect ... we can improve it by increasing the grid size") against the same kind of plot at 464-476. Second, 121-123 invokes Banach's contraction mapping theorem to say the iterates converge, and `compute_value_function` already computes the error at every step and prints it every 25 (335-339) - plotting that error sequence on a log scale would show the geometric rate the theorem predicts and would cost one array. Third, none of the six figures carries `mystnb` caption or name metadata (qe-fig-005 counts all six), so the prose can only refer to them as "this" (462) or by position, and the orphan label at 461 suggests the author wanted a reference and reached for the wrong mechanism.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 142. *Example:* 2 spaces.


## Strengths

- The lecture states why it is doing numerical work on a problem that is already solved, and the reason is the one that matters: 25-35 says the analytical case exists precisely so the numerical methods can be checked against a known answer, and every section then does that check - the value function against `v_star` at 372-386 and the policy against `c_star` at 464-476.
- Both algorithms are written out as numbered steps before any code appears - value function iteration at 92-102 and its fitted variant at 140-150 - and 152 names the one implementation choice the steps leave open ('In step 2 we'll use piecewise linear interpolation').
- The Bellman right-hand side is factored into its own function $B(x, c, v)$ with the mathematics displayed first (212-222) and the code immediately after (226-244), so `T` (255-269) and `get_greedy` (440-452) are visibly the same maximisation differing only in which of the two outputs of `maximize` they keep - `_, v_new[i]` against `σ[i], _`.
- `maximize` (162-175) is a three-line helper whose docstring states the trick it relies on ('the maximizer of g on any interval is also the minimizer of -g'), so the sign flip is documented rather than left for the reader to reverse-engineer.
- The two `{note}` admonitions are used for exactly what admonitions are for: 38-44 sets expectations about code that aims for clarity over speed, and 394-408 names the fix for the boundary approximation error (a nonlinear grid), says the lecture will not take it, and says what it will do instead - iterate on the policy - which is then delivered by the pointer to `` {doc}`os_time_iter` `` at 488.
- The iteration is shown converging rather than only reported: 287-311 plots twelve successive iterates coloured by iteration index with the initial and final guesses labelled, so the reader sees $T^n v$ rising toward its limit before any convergence criterion is discussed.
- Parameters live in a `NamedTuple` with a keyword-only factory carrying inline comments for each default (185-202), including the reason for the one non-obvious choice, `x_grid_min: float = 1e-3,  # exclude zero for numerical stability`.
- Bold is used only for the five terms the lecture defines - **value function iteration** (88), **successive approximation** (90), **Bellman operator** (108), **iterating with the Bellman operator** (118), **greedy policy** (430) - so qe-writing-005 has nothing to report.

## Recommended actions

1. Make the exercise solution do what 511 asks: give `Model` an `α` field defaulting to 1 and reuse `B`, `T`, `compute_value_function` and `get_greedy` instead of cloning them at 542, 555, 573 and 615 - the only real change is `vf((x - c)**α)` for `vf(x - c)`. If the clones stay, at least give them the same argument order as the originals: `extended_B(c, x, ...)` reverses `B(x, c, ...)` and `extended_get_greedy(model, v)` reverses `get_greedy(v, model)`.
2. Plot the approximation error. 388-392 and 478-481 both assert something a linear overlay of two near-identical curves cannot show; `v_analytical` (373) and `c_analytical` (465) are already computed, so one `semilogy` of the absolute difference turns both claims into evidence - and it is the figure the boundary-steepness explanation at 391-392 needs.
3. Stop the exercise solution from clobbering the body's state: 567, 600 and 627 rebind `model`, `v` and `σ`, leaving the globals unpacked at 279 pointing at the baseline model, which is why 630-631 has to rebuild it. Use `ext_model`, `v_ext`, `σ_ext`.
4. Fix the two spacings of the same expression: 76 should be `β**(1/γ)` per the rule's `a**b`, and 81 should read `β**(1/γ)` and `x**(1-γ) / (1 - γ)` consistently - as written the two lines disagree on both operators.
5. Either reference `(pol_an)=` (461) or delete it: it is defined here and in the lecture-dp copy and referenced nowhere in any of the five series. If a reference is wanted, give the figure at 464-476 `mystnb` caption and name metadata and point `{numref}` at that.
6. Replace the three `lambda` bindings with `def` (171, 241, 548), and rewrite the three padded one-line docstrings as triple-quoted (259, 444, 556).
7. Rename one of the two $\hat v$'s - the Bellman update at 95 or the interpolant at 144 - and make the figure labels at 363 and 381 use $v(x)$, matching the mathematics at 64, 112 and 215.
8. Sweep the mechanical items: the five Title-Case headings (55, 86, 106, 125, 411), the six figures with no `mystnb` metadata (287, 359, 376, 464, 572, 614), the seven `plot()` calls with no `lw=2` (362, 379, 380, 469, 470, 635, 636), the three embedded titles (309, 365, 384), the eleven `fontsize=12` overrides (307, 308, 363, 364, 381, 382, 605, 606, 638, 639, 641), the double space at 142, the trailing whitespace at 302, the `E261` at 328, the three lines over 79 characters (533, 544, 631), and 'It's task' at 316.
