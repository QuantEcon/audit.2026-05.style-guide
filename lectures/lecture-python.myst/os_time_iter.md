# os_time_iter

- **Series:** lecture-python.myst
- **File:** `lectures/os_time_iter.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×4; `qe-writing-003` ×4; `qe-writing-002` ×4, +1 more. |
| Math         | 7.5/10 | `qe-math-001` ×2; `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×5; `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-008` ×3. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 318, 366, 369, 397, 410. *Example:* 410-413 assigns four lambdas to module-level names (`u`, `u_prime`, `f`, `f_prime`) and 369 assigns a fifth inside `euler_diff`, all of which PEP8 asks to be `def`s; 318-319 and 333-334 annotate `u_prime: Callable = None`, where the annotation and the default disagree and `Optional[Callable]` is meant; 366 and 392 unpack all ten `Model` fields in both functions when `euler_diff` uses six of them and `K` uses one, leaving four and nine unused names bound; 397 writes `brentq(euler_diff, 1e-10, x-1e-10, args=(σ, x, model))`, dropping the spaces around the minus on a line whose other operators have them; and 546-548 puts `γ = 1.5` immediately against a top-level `def` with no blank line while 284-294 in the same file does leave one. `solve_model_time_iter` also prints on every iteration (467-468) where `os_stochastic`'s `solve_model` took a `print_skip` argument for exactly this.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 68, 161, 215, 237. *Example:* H2 Title Case: 'The Euler Equation' (Equation).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 407, 488, 561. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 423, 427, 431. *Example:* plot() without lw=.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 380, 405. *Example:* unicode `σ` inside a math environment.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 109, 181, 278. *Example:* 178 refers to "the set of all $\sigma \in \Sigma$ that are continuous, strictly increasing and interior" and 181 then introduces a second, differently-fonted symbol for that subset one line later - "Henceforth we denote this set of policies by $\mathscr P$" - so the lecture carries $\Sigma$ and $\mathscr P$ for two nested policy sets in adjacent sentences, and $\mathscr P$ never appears in the code. Line 109 defines the plainer notation in terms of the more decorated one, `(v^*)'(x) = u'(\sigma^*(x)) := (u' \circ \sigma^*)(x)`, and the composition form is then spelled out in full eight more times (144, 145, 153, 154, 190, 210, 354) where $u'(\sigma(\cdot))$ would read directly - the sibling lecture `ifp_egm` states the shorthand the other way round at its line 267. And 278 keeps the $\nu$ of `os_stochastic` for the shock scale in a lecture whose value function is $v^*$ (95, 109, 136), so the two differ by a hairline in the same displays.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 43, 217, 504, 515. *Example:* the lecture makes the same point four times. 37-38 defines time iteration as "iterating on a guess of the optimal policy using the Euler equation", 40-44 says this differs from the value function iteration of `os_stochastic`, 43-47 says it a third time in two sentences of 37 and 32 words ("Time iteration exploits the structure of the Euler equation to find the optimal policy directly, rather than computing the value function as an intermediate step" plus "we can often solve problems faster than with value function iteration"), and 515-517 says it a fourth time in almost the same words. Line 217 opens the subsection "Is the Coleman-Reffett Operator Well Defined?" with "In particular, ...", which has no general statement to particularise - the heading is itself the question. And 504's "Again, the fit is excellent" leans on `os_stochastic` for the "again" while 438-439 has already told the reader the limit "resembles the solution we obtained" there.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 259, 306, 318, 369. *Example:* line 306 says "We use the same `Model` structure from `` {doc}`os_stochastic` ``" and it is not the same: `os_stochastic`'s `Model` (its lines 480-487) has seven fields `u, f, β, μ, ν, x_grid, shocks`, while this one (309-319) has ten - `α`, `u_prime` and `f_prime` are added and `x_grid` is renamed `grid` - so the ten-name unpackings at 366 and 392 would raise against the tuple the sentence points at, and `Model.f` here takes two arguments (`f(x - c, α)` at 372) where the other lecture's `fcd(s)` closed over α. The two functions the whole lecture depends on default to `None` (318-319, 333-334), so `create_model` happily returns a model that fails only later, inside `euler_diff`, with `'NoneType' object is not callable`. Line 259 promises "Examples are given below" for the claim at 250-257 that $K$ is numerically more stable and more efficient than $T$, and no such example ever arrives - 515-517 simply asserts "Time iteration runs faster than value function iteration, as discussed in `` {doc}`os_stochastic` ``", and the file's only timing is a `%%time` at 562 on the CRRA exercise, with nothing to compare it to. And `σ_func = lambda x: np.interp(x, grid, σ)` at 369 names its parameter `x`, shadowing `euler_diff`'s own `x` argument declared three lines above at 358.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 4. *Lines:* 232, 259, 423, 570. *Example:* line 232 names the figure it wants and then asks the reader to draw it: "Sketching these curves and using the information above will convince you that they cross exactly once as $c$ ranges over $(0, x)$." Both sides of `` {eq}`cpi_coledef` `` are one numpy expression each and the argument at 222-230 is entirely about their shapes, so this is the clearest missed figure in the lecture. Second, the conjugacy and stability claims at 239-257 end in "Examples are given below" (259) and are never illustrated - no timing, no side-by-side convergence of $T^n v$ against $K^n \sigma$, though `os_stochastic` supplies the VFI side. Third, the iterate plot at 421-435 encodes iteration order in `plt.cm.jet` colours and neither the prose at 438-439 nor a colorbar says so, where the corresponding figure in `os_stochastic` at least explains the colour scale. Fourth, the CRRA exercise figure at 570-576 plots the approximate policy alone, with no `σ_star` benchmark of the kind 497 supplies for the log case, so the reader has nothing to check it against.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 562. *Example:* %%time.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 194. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.


## Strengths

- The Euler equation is derived, not quoted: 75-78 adds exactly four assumptions to the model of `os_stochastic` and names the last two as the Inada conditions, 99-109 states the three things they buy, 115-125 proves the envelope condition by rewriting the Bellman equation over $k$ and differentiating, and 129-146 combines it with the first-order condition to reach `` {eq}`cpi_euler` `` - with a pointer at 127 to the full proofs in EDTC section 12.1.
- The new operator is introduced through the one the reader already owns: 163-176 recalls the Bellman operator and says that $K$ will do for the Euler equation what $T$ does for the Bellman equation, 183-191 defines $K\sigma(x)$ as the root of a single equation, and 196-197 restates it in words - "the consumption policy that the Euler equation tells you to choose today when your future consumption policy is $\sigma$".
- Well-definedness gets its own subsection before the operator is used (215-235): the monotonicity and the divergence of each side of `` {eq}`cpi_coledef` `` are listed separately (222-230), which is exactly the information the existence-and-uniqueness claim needs, and 234-235 adds that $K$ maps $\mathscr P$ into itself.
- The fixed-point correspondence is argued in both directions: 199-203 states that fixed points of $K$ coincide with solutions of `` {eq}`cpi_euler_func` `` by construction, and 205-213 then verifies the direction that matters by substituting $\sigma^*$ and reading the Euler equation back.
- The comparison with VFI is stated with its own limits attached: 239-248 says $T$ and $K$ are topologically conjugate, so convergence of either implies convergence of the other and the rates agree "at least in theory", and 250-257 then separates that theoretical claim from the numerical one and gives two concrete reasons for the numerical advantage - first-order structure, and lower curvature of policies than of value functions.
- Each mathematical object gets one function and the correspondence is placed next to it: the display `` {eq}`euler_diff` `` at 351-355 sits immediately above `euler_diff` (358-373), whose docstring says which root it is for; `K` (385-400) is only the root-finding step; `solve_model_time_iter` (447-473) is only the iteration.
- The answer is checked against a closed form rather than eyeballed: `v_star` and `σ_star` are transcribed at 284-298, the policy figure at 488-501 overlays `σ_star` as a dashed black line, and 506-512 then prints $\max|\sigma - \sigma^*|$ as an actual number.
- The lecture is explicit that it is a way-station rather than a destination: 49-54 says at the outset that time iteration is *not* the most efficient Euler-based method, names the endogenous grid method and the lecture that covers it, and 519-521 closes by pointing there again - and the `{note}` at 266-270 tells the reader that the code favours clarity over efficiency, so `brentq` inside a Python loop is not read as a recommendation.

## Recommended actions

1. Correct the claim at 306: this `Model` is not `os_stochastic`'s - it adds `α`, `u_prime`, `f_prime` and renames `x_grid` to `grid`, and its `f` takes two arguments where the other lecture's takes one - so say what changed and why the derivatives had to be added.
2. Make `u_prime` and `f_prime` required parameters instead of `None` defaults (318-319, 333-334); every path in the lecture needs them, and omitting them fails later inside `euler_diff` rather than at construction.
3. Draw the curves the text asks the reader to sketch at 232 - the two sides of `` {eq}`cpi_coledef` `` against $c$ on $(0, x)$ - which is the picture the whole well-definedness argument at 222-230 is about.
4. Deliver the examples promised at 259 or drop the promise: the claims at 250-257 and 515-517 that $K$ beats $T$ numerically are never measured, and `os_stochastic`'s `solve_model` is right there for a side-by-side timing and convergence comparison.
5. **Do not "fix" the primes.** All eight `qe-math-002` hits (109, 144, 145, 153, 154, 190, 210, 354) are derivatives of $u$ composed with a policy, `(u' \circ \sigma)`, and are correct as written - see the scanner doubt below; rewriting them as `\top` would be wrong.
6. Settle the policy-set notation: $\Sigma$ at 178 and $\mathscr P$ at 181 name two nested sets one line apart and only one of them is ever used again; and give the shock scale a symbol other than $\nu$ (278), which sits one glyph from the value function $v^*$.
7. Overlay `σ_star` on the CRRA exercise figure (570-576) as 497 does for the log case, and either explain the `plt.cm.jet` iteration colouring at 423-427 in the prose or add a colorbar.
8. Clear the mechanical and code sweep: sentence-case the four flagged headings (68, 161, 215, 237), write `\sigma` rather than unicode `σ` inside the inline maths at 380 and 405 (qe-math-001), add `mystnb figure` name/caption to the three figure cells (407, 488, 561) and `lw=2` at 423, 427 and 431, make 194's citation `{cite:t}`, convert `%%time` at 562 to `qe.Timer()` (qe-code-004), and fix the five lambda assignments (369, 410-413), the shadowed `x` at 369, the ten-name unpackings at 366 and 392, `x-1e-10` at 397, the `Callable = None` annotations, and the missing `print_skip` on `solve_model_time_iter`.
