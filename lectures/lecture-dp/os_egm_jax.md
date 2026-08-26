# os_egm_jax

- **Series:** lecture-dp
- **File:** `lectures/os_egm_jax.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-002` ×3; `qe-writing-003` ×1; `qe-writing-007` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 5.5/10 | `qe-code-002` ×7; `qe-code-001` ×3; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-006` ×2; `qe-fig-005` ×2; `qe-fig-008` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 7. *Lines:* 151, 153, 368, 369, 370, 371. *Example:* spelled-out `mu`.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 90, 148, 383. *Example:* `s` is made to carry two unrelated meanings and then shadowed. The `Model` field at 90 is `s: float  # shock scale parameter` - the same quantity os_egm calls `ν` (os_egm.md:175) - while `s_grid` (91) and the loop variable `s` are *savings*. Line 144 unpacks `β, μ, s, s_grid, shocks, α = model` and line 148 immediately rebinds the same name with `def compute_c(s):`, so inside the closure `s` is a savings level and the scale parameter is unreachable. It happens not to matter only because `shocks` was pre-drawn at 114, which is exactly the kind of coincidence a reader should not have to verify. Second point, in the same file: the width kwarg is spelled `lw=2` at 220 and 224 and `linewidth=2` at 383.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['jax', 'quantecon'].
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 217, 377. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 388, 389. *Example:* axis label `State x`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 82, 245, 292. *Example:* three kinds of repetition. (1) The solution copies the body's code rather than parameterising it: `K_crra` (292-321) is `K` (135-162) with `u_prime`/`u_prime_inv` given a `γ` argument, and `solve_model_crra` (326-354) is `solve_model_time_iter` (177-205) with `K_crra` substituted - the inner `condition` and `body` functions at 337-345 are identical to 188-196 line for line. Sixty lines of the lecture exist to change three calls, in a series whose NumPy version already stores the utility callables in `Model` (os_egm.md:179-181). (2) 'Utility and production functions will be defined globally to work with JAX's JIT compiler' (84) is repeated as 'We define utility and production functions globally' (120) with the reason dropped. (3) The speed claim is made four times before it is measured once - 36 ('improved performance'), 132 ('vectorizes the computation'), 173 ('JIT-compiled for speed'), 237 ('very fast thanks to JIT compilation and vectorization') - and then the four-bullet list at 245-250 says it a fifth time.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 237, 377. *Example:* the lecture exists to show that JAX is faster (36, 237, 245-250) and contains no picture or number of that comparison: the `qe.Timer` cell at 240-243 prints one figure with no NumPy counterpart, and both figures in the file (217-228, 377-392) plot consumption policies, which is what os_egm already plots. A run-time bar for NumPy versus JAX, or a curve of solve time against `grid_size`, is the figure this lecture is missing. The second figure has its own visual problem the text works around in prose instead: 395-397 explains that the $\gamma > 1$ curves stop short because each has its own endogenous grid, which plotting against savings $s$ or interpolating onto a shared $x$ grid would simply remove.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 386. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 395, 403. *Example:* the exercise's convergence check contradicts the paragraph immediately above it. Lines 395-397 explain that 'the plots for $\gamma > 1$ do not cover the entire x-axis range' because 'the endogenous grid $x = s + \sigma(s)$ depends on the consumption policy, which varies with $\gamma$' - i.e. each $\gamma$ has its own $x$ grid. Line 399 then promises 'the maximum deviation between the log utility case ($\gamma = 1.0$) and values approaching from above' and line 403 computes `jnp.max(jnp.abs(policies[1.0] - policies[γ]))`, differencing the two arrays index by index. That is the gap between the policies at equal *savings*, not at equal wealth, so it is not the deviation between the two policy functions the prose describes - and 407 reads it as 'confirming convergence'. Either interpolate both onto a common $x$ grid or say that the comparison is at equal $s_i$.


## Strengths

- Each JAX mechanism is named in prose immediately before the code that uses it, so the file reads as a translation rather than a rewrite: `vmap` at 132 ahead of `jax.vmap(compute_c)` (156), `jax.lax.while_loop` at 173 ahead of the `condition`/`body` pair (188-202), and `@jax.jit` at 176.
- `jax.block_until_ready` is called inside the timing block (242) and again in the exercise loop (369) - the one step a JAX benchmark must take to avoid timing asynchronous dispatch rather than the computation.
- Line 82-84 states the structural difference from os_egm as a JAX constraint rather than making it silently: `Model` holds only grids, shocks and parameters (87-93, all arrays and floats, hence a valid pytree) because the callables have to be global for the JIT compiler.
- `K` (135-162) and `K_crra` (292-321) preserve os_egm's signature, comment order and even its `# x_i = s_i + c_i` line (160, 318), so the JAX operator can be diffed against the NumPy one.
- The exercise is posed with the awkwardness of its own design disclosed: the hint at 267 tells the reader to use $\gamma$ near 1 'to ensure the endogenous grids have similar coverage', and 395-397 then explains the truncated curves in the figure instead of leaving them unexplained.
- The accuracy check prints a formatted number rather than a bare repr (233-234, `f"Maximum absolute deviation: {max_dev:.7}"`), and the exercise's per-$\gamma$ loop does the same at 372 and 404.

## Recommended actions

1. Rename the shock scale field from `s` back to `ν` (90, 99, 114, 116, 144) as os_egm has it, so that `s` means savings throughout and `def compute_c(s)` at 148 no longer shadows an enclosing name of a different quantity.
2. Put a NumPy number next to the JAX one: quote or re-run os_egm's solver beside the `qe.Timer` block at 240-243, and use the same timer precision (os_egm uses the default, this uses `precision=8`), otherwise the claims at 36 and 237 rest on a single unanchored figure.
3. Fix the convergence check at 401-405 - interpolate each policy onto a common wealth grid before differencing, or restate 399 as a comparison at equal savings - and plot the exercise figure on an axis where all four policies have the same support.
4. Collapse the duplicated solution code (292-354) by parameterising `K` and `solve_model_time_iter` over the utility callables, as os_egm's `Model` already does, instead of maintaining a second copy of both.
5. Restore the non-convergence signal: os_egm prints 'Warning: maximum iterations reached' (os_egm.md:302-303), whereas `solve_model_time_iter` discards `i` and `error` at 202 and returns silently, so a run that hits `max_iter` looks identical to one that converged.
6. Take the install cell and the RNG fix from the upstream twin `lecture-python.myst/lectures/os_egm_jax.md` rather than patching here: it carries the `!pip install quantecon jax` cell this copy lacks (the whole qe-code-003 finding) and has already replaced the deprecated `jax.random.PRNGKey(seed)` at 113 with `jax.random.key(seed)`.
7. Rename `mu` at 151 and 153 (not to `μ`, which is already the shock location parameter at 89) and `c_gamma`/`x_gamma` at 368-371 to `c_γ`/`x_γ` - the same line already passes `γ`; see scanner_doubts, the latter pair is a detector miss rather than a drafted finding.
8. Mechanical items from the draft: mystnb `name`/`caption` on the two figures (217, 377), lowercase axis labels at 388-389, and `lw=2` on the `else` branch at 386 so both branches of the same plot set a width. Also add the missing blank line between the fence at 129 and the prose at 130.
