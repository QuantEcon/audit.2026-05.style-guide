# lqramsey

- **Series:** lecture-dp
- **File:** `lectures/lqramsey.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-003` ×4; `qe-writing-002` ×4; `qe-writing-008` ×7. |
| Math         | 3/10  | `qe-math-010` (proposed) ×11; `qe-math-002` ×8; `qe-math-009` ×2. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-006` ×3; `qe-fig-008` ×12; `qe-fig-001` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 590, 670, 716, 728, 827, 939. *Example:* line 670 is `nx, nx = A.shape` - the same name bound twice, which works only because the matrix is square and silently hides the second dimension. Lines 716 and 722 call `sys.exit(0)` from inside `compute_paths` when the parameters admit no Ramsey equilibrium: in a notebook that raises SystemExit rather than returning, and the status code says success. `l = (Sl @ x).flatten()` (728) is the ambiguous single-character name PEP8 forbids (E741), and it is also a `Path` field. Continuation lines are misaligned throughout: 590 is indented 20 against a visual indent of 21, 600 is 16 against 18, and the same off-by-two or off-by-three appears at 907, 939, 945, 956 and 1019 (E128). `bbox = (0., 1.02, 1., .102)` is written twice, identically, at 826 and 827. Add the missing spaces around `-` in `temp[:T-1]` (741), `R[:T-1]` (755), `x[:, t-1]` (681) and around `*` in `mg*(1-ρ)` (1005).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 787, 788, 789, 794, 795, 796, 801, 806, 807, 808, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 8. *Lines:* 401, 404, 408, 410, 411, 430. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 11. *Lines:* 117, 128, 206, 262, 275, 331, 336, 359, 365, 401, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 53, 59, 382, 541, 572, 860. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 775, 824. *Example:* figsize=.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 780, 835, 842. *Example:* axis label `Time`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 274, 497. *Example:* the expectation operator is written four ways in one lecture: `\mathbb E` (117, 128, 206, 262, 275, 331, 336, 359, 365, 401, 426), `\mathbb E_t` (472, 481, 513), a bare `E_t` (497, 505, 547 twice, 562) and `\tilde E_t` for the distorted measure (555, 558, 568). The bare `E_t` is the problem case - at 497 and 505 it is the same conditional expectation that 472 and 481 write as `\mathbb E_t`, sixteen lines apart, in a derivation the reader is meant to follow line by line. Separately, the Ramsey Lagrangian at 274 is `\mathscr L`, a script font used exactly once in the file, where a plain $L$ or `\mathcal{L}` would do and would match the rest of the series.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 185, 238, 536, 539. *Example:* line 536 drops a symbol from a displayed quantity: the bullet explaining $\pi_{t+1}$ writes '$R_t [B_t + g_t - \tau_t ]$' where the definition twelve lines above has $R_t[B_t - (\tau_t \ell_t - g_t)]$ (524) and the sentence six lines below has '$B_t + g_t - \tau_t \ell_t$' (542) - the $\ell_t$ is missing in the middle version only. Line 539 is a bare `> ` blockquote marker with nothing in it. Line 238 reads 'the first-conditions for the household's problem' and line 185 'Gaussian with identify covariance matrix'. Line 576 puts a plain English phrase in code backticks: 'the `excess payoff` $\{\Pi_t\}$'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 279, 359, 850, 853. *Example:* four symbols are reused for unrelated objects inside one argument. $\mu$ is the Lagrange multiplier on the household budget constraint (241), $\mu_t$ is the multiplier on feasibility in the Ramsey Lagrangian (279), and $\mu_g$ is the mean of government spending (886-889). $\pi^0_t(x^t)$ is a probability density (145-146) while $\pi_{t+1}$ is the excess payout on state-contingent debt (524) and $\Pi_t$ its cumulation (530), against $P$ the Markov transition matrix (184). Worst is $b_0$: line 245 normalises 'at $\mu = b_0 - c_0$', where $b_0$ is the time-0 value of the preference process $b_t = S_b x_t$ (138, 175), and then line 359 defines '$b_0 := \mathbb E\{\sum \beta^t (b_t - \bar c_t)(g_t + s_t)\}$' - a completely different quantity - and line 374 solves for $\nu$ using the second meaning while {eq}`lq_hfoc` at 251 still uses the first. Separately, '### Comments on the code' (848-867) describes code that is not there: `var_quadratic_sum` is 'imported from `quadsums`' (850) when line 85 imports it from `quantecon`, and the two namedtuples are 'Below the definition of the function' (853) when they are defined at 589 and 599, above `compute_paths` at 616.

### Low severity
_None found._


## Strengths

- The solution procedure is stated as a three-step plan (224-232) and then executed in exactly that order, with every step's equation labelled and cited where it is used - {eq}`lq_hfoc` into {eq}`lq_gc` giving {eq}`lq_gc2` (256-264), then the Lagrangian {eq}`lq_rp`, then {eq}`lq_lcex`, then {eq}`lq_gc22` - so a reader can navigate a 250-line derivation without losing the thread.
- The two exogenous specifications are labelled once at `(lq_twospec)=` (183) and then reached by `{ref}` three times (406, 418, 876) instead of being restated, and the code branches on exactly that distinction (`econ.discrete` at 659, 665, 692, 734) so the mathematics and the implementation are partitioned the same way.
- The martingale result is assembled in visible stages: the two objects are defined (524-531), each term of $\pi_{t+1}$ is given a verbal reading (533-542), the change of measure is derived through the likelihood ratio $m^t_{t+1}$ (547-563), the conclusion is drawn (565-572), and then it is contrasted with Barro's random-walk result (574-576) - the contrast being the reason the lecture exists.
- The discrete-case identity is stated and then implemented recognisably: '{eq}`lq_ise` is in fact equal to the $j$-th element of the vector $(I - \beta P)^{-1} h$' (446-447), and line 694 is `F = scipy.linalg.inv(eye(ns) - β * P)` used at 695, 697 and 736.
- Parameter failures are handled rather than left to crash: the discriminant is tested before the square root (710-716) and the sign of the multiplier after it (719-722), each with a message naming which primitive is at fault - and the joke in `warning_msg` is at least memorable.
- Both figure functions share one styling contract - `legend_args` and `p_args` dictionaries splatted into every call (782-783, 828-829) - so all six panels across the two figures get identical line widths, alpha and legend placement.

## Recommended actions

1. Brace every blackboard operator and settle on one spelling. The scanner reports 11 (117, 128, 206, 262, 275, 331, 336, 359, 365, 401, 426) but that is an undercount: `\mathbb E_t` at 472, 481 and 513 is the same defect and is silently missed, and the bare `E_t` at 497, 505, 547 and 562 is the same operator with no blackboard at all. See scanner_doubts; the true figure is closer to twenty.
2. Rename one of the two $b_0$'s. As written, $b_0$ is the time-0 preference parameter at 245 and an expected discounted sum at 359, and both are used in the same chain of reasoning - a reader checking {eq}`lq_hfoc` against line 374 will get nonsense. The same applies less acutely to the three $\mu$'s (241, 279, 886) and to $\pi^0_t$ against $\pi_{t+1}$ (145, 524).
3. Replace `sys.exit(0)` at 716 and 722 with a `raise ValueError(...)`: inside a notebook the current code raises SystemExit from the middle of `compute_paths` and reports success while doing it. While there, fix `nx, nx = A.shape` (670) and rename `l` (728, E741).
4. Convert the 6 transposes to `^\top` (401, 404, 408, 410, 411, 430) - the reported count of 8 double-counts two of them, see scanner_doubts - and replace `\mathscr L` at 274 with `L` or `\mathcal{L}`.
5. Correct '### Comments on the code' (848-867): `var_quadratic_sum` comes from `quantecon`, not `quadsums` (850), and the namedtuples are above `compute_paths`, not below it (853). As it stands the one section devoted to orienting the reader in the code describes a different file.
6. Do not act on the 12 qe-fig-008 findings (787-808, 833, 840): every one of those `plot` calls already carries `lw=2`, supplied through `**p_args` (defined at 783 and 829). They are the larger half of the Figures deduction - see scanner_doubts. What the figures do need is the 2 hand-set `figsize` removed (775, 824) and the 3 'Time' axis labels lowercased (780, 835, 842) (qe-fig-006 x3).
7. Fix the prose items: the missing $\ell_t$ at 536, the empty blockquote at 539, 'first-conditions' at 238, 'identify' at 185, the backticked phrase at 576; then clear the 7 double spaces (53, 59, 382, 541, 572, 860) and the continuation-indent and operator-spacing items listed above.
