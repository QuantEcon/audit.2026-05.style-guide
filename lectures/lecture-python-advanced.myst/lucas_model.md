# lucas_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lucas_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-005` ×6; `qe-writing-003` ×3; `qe-writing-007` ×1. |
| Math         | 9.5/10 | `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×3; `qe-fig-001` ×2; `qe-fig-008` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 429, 443, 448, 395, 546. *Example:* 429 and 443 put a blank line between the `def` line and the docstring (`def operator_factory(tree, parallel_flag=True):` then an empty line then `"""`, and the same inside `def T(f):`), and 435-436 and 445-446 add another blank after it, where the docstring should be the first statement; 393-396 closes the class docstring after a trailing blank line. 448 assigns a lambda to a name, `Af = lambda x: np.interp(x, grid, f)`, which PEP8 asks to be written as a `def`. 546 writes `for β in (.95, 0.98)`, mixing the leading-dot and leading-zero float styles inside one tuple. Minor, but the file is inconsistent with itself: `solve_model` at 465-472 gets the docstring placement right.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 6. *Lines:* 58, 78, 122, 272, 318. *Example:* the file contains no bold at all, and every term it defines is italicised instead: *Pure exchange* and *Representative* in the two bullets that define them (58-61), *consumption endowment* at 78 ("Another way to view $\{y_t\}$ is as a *consumption endowment*"), *ex-dividend* at 122 where the next two bullets spell out what it means, *functional equation* at 272 and again at 299, and *fixed point* at 318. Since italic is never used for emphasis anywhere in the lecture, these six are a straight substitution to bold - and "Lucas operator", named at 313 and used a dozen times after, is currently marked in neither.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 499, 544. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 495, 519, 543. *Example:* {figure} without :name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 30, 36, 40. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 327, 385, 234. *Example:* the space of candidate functions is written $cb\mathbb{R}_+$ (327, 331, 332, 348, 353), which typesets as a product of two italic letters against a blackboard symbol and reads as $c \cdot b \cdot \mathbb{R}_+$; the standard $C_b(\mathbb{R}_+)$, or at least $\mathrm{cb}\mathbb{R}_+$, says the same thing unambiguously. Second, $\alpha$ carries two meanings fifteen lines apart across a section boundary: it is the contraction modulus in `` {eq}`ltbc` `` (342-373, where 373 sets $\alpha := \beta$) and then the autocorrelation of $\ln y$ at 385 and in the class signature at 402, which is what the code uses at 420, 438 and 454. Third, the derivative of the value function with respect to its first argument is written $v_1'$ at 234 and $v'_1$ at 237, 240 and 243 - the prime and the subscript swap places for the same object.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 507, 385, 516. *Example:* 507 reads the figure for a case the lecture never computes: "We see that the price is increasing, even if we remove all serial correlation from the endowment process" - but the only figure above it (495-504) is produced by `LucasTree()` with the default `α=0.90` (402), so serial correlation is fully present and the parenthetical claim has no supporting run. Second, the specialisation at 385-387 changes the shock symbol and skips the step that connects the algebra to the code: 83-86 sets $y_{t+1} = G(y_t, \xi_{t+1})$ with $\{\xi_t\}$ distributed $\phi$, 385 writes $\ln y_{t+1} = \alpha \ln y_t + \sigma\epsilon_{t+1}$ with $\{\epsilon_t\}$ standard normal, and nothing states that this means $G(y, z) = y^\alpha z$ with $z$ lognormal - which is exactly what the code assumes at 415, 420 and 454 (`self.ϕ = lognorm(σ)`, `y**α * self.draws`). Third, 516 describes the static figure as "the orange line ... and the green line", but the exercise that replicates it (543-555) plots two lines with the default matplotlib cycle, so a reader who does the replication gets blue and orange and cannot match the description.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 519. *Example:* static image .png.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 500. *Example:* plot() without lw=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 332. *Example:* the lecture proves that $T$ is a contraction with modulus $\beta$ and that $T^k f$ converges uniformly to $f^*$ from any starting point (329-373), then computes exactly that iteration (482-486), and never plots it. A figure showing three or four successive iterates $f$, $Tf$, $T^2f$, ... approaching $f^*$ from the constant initial guess `np.ones_like(grid)` (480) would turn the contraction-mapping argument - which the `{note}` at 335-337 explicitly invites readers to skip - into something visible, and it costs one extra array per pass through the existing loop. The one figure that does show a comparative static (519) is a pre-baked PNG whose colours the text at 516 describes and the replication code at 543-555 does not reproduce.


## Strengths

- The lecture states its own method before applying it and names it as the general pattern: 162-166 says that in a competitive model one determines consumer behaviour taking $p$ as given and then uses equilibrium conditions to recover $p$, and calls that "the standard way to solve competitive equilibrium models" - so the reader knows at 168 what the next fifty lines are for.
- 200-210 is an unusually honest signpost: it lays out the three-step route a reader would naturally take (solve the two-dimensional dynamic program, impose equilibrium, solve out for $p$), and then says Lucas found a more straightforward way - which both motivates the substitution at 285 and tells the reader why the obvious route is being abandoned.
- The indirect approach is carried out with the return trip stated in advance: 285 defines $f(y) := u'(y)p(y)$, 296-297 isolates $h$ as depending only on primitives, 301 says "the plan is to solve out for $f$ and convert back to $p$ via `` {eq}`ltffp` ``", and 383 and 488 (`price = f * grid**γ`) close the loop in the prose and the code respectively.
- The contraction argument is done in full rather than cited - 355-370 shows $|Tf(y) - Tg(y)| \leq \beta\|f-g\|$ in four displayed steps, with the one non-obvious move flagged inline ("since integrals get larger when absolute values are moved to the inside") - and the `{note}` at 335-337 then gives readers explicit permission to take the two conclusions on trust and jump to `` {ref}`lt_comp_eg` ``.
- The economics of the computed price function is explained rather than described: 507-512 gives the mechanism in three one-sentence paragraphs - a larger endowment lowers marginal utility, so the price must rise to induce the household to consume the whole endowment and satisfy the resource constraint.
- The grid is derived from the model rather than chosen: 407-411 sets it to $[\exp(-4s), \exp(4s)]$ where $s = \sigma/\sqrt{1-\alpha^2}$ is the stationary standard deviation of $\ln y$, with a comment saying that is the intent, so the bounds move correctly when $\alpha$ or $\sigma$ change.
- The small structural details of the consumer problem that usually confuse readers are addressed where they arise: 122-127 spells out what *ex-dividend* buys, and 144-146 explains why the share held at $t$ carries subscript $t$ even though the decision was made at $t-1$.

## Recommended actions

1. Fix the two claims the figures do not support: either add a run with $\alpha = 0$ or drop "even if we remove all serial correlation from the endowment process" at 507, and replace the colour description at 516 with the labels the replication actually produces (543-555 uses the default cycle, and 550 already builds a `$\beta = ...$` label).
2. State the specialisation explicitly at 385-387: that $\ln y_{t+1} = \alpha \ln y_t + \sigma\epsilon_{t+1}$ means $G(y, z) = y^\alpha z$ with $z$ lognormal, which is the form the code uses at 415, 420 and 454 - and keep the shock symbol $\xi$ from 86 rather than switching to $\epsilon$.
3. Rename one of the two $\alpha$'s: the contraction modulus at 342-373 and the endowment autocorrelation at 385 and 402 are different objects fifteen lines apart, and the second is what the code and the class signature carry.
4. Add a figure showing successive iterates of the Lucas operator converging to $f^*$, next to the two claims at 331-333 - the loop at 482-486 already produces them.
5. Write $cb\mathbb{R}_+$ as $C_b(\mathbb{R}_+)$ throughout (327, 331, 332, 348, 353) and settle $v_1'$ against $v'_1$ between 234 and 237-243.
6. Bold the six italicised definitions (58, 59, 78, 122, 272, 318) and mark "Lucas operator" at 313, which is currently the only named object in the lecture with no typographic marker.
7. Replace the three raw URLs with `{doc}` cross-references (30, 36, 40) - note that 36 points at `python.quantecon.org/markov_asset.html` while 30 and 40 point at `python-intro.quantecon.org/markov_asset.html`, so the same lecture is linked under two different hostnames.
8. Clean the PEP8 items: docstring placement at 393-396, 429-436 and 443-446, the assigned lambda at 448, and the mixed float literals at 546; add the missing "us" at 381 ("The preceding discussion tells that we can compute $f^*$").
9. Sweep the figures: `lw=2` at 500, `mystnb: figure: caption/name` metadata on the two code-cell figures (495, 543), a `:name:` on the static figure at 519, and drop the `figsize=(10, 6)` overrides at 499 and 544; and consider generating the $\beta$-comparison figure at 519 in place, since the exercise solution at 543-555 already draws it.
