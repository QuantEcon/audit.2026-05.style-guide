# os_egm

- **Series:** lecture-dp
- **File:** `lectures/os_egm.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×4; `qe-writing-005` ×1; `qe-writing-003` ×1, +2 more. |
| Math         | 9.5/10 | `qe-math-009` ×2. |
| Code         | 7.5/10 | `qe-code-002` ×2; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-005` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 55, 77, 98, 214. *Example:* H2 Title Case: 'Key Idea' (Idea).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 241, 243. *Example:* spelled-out `mu`.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['quantecon'].
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 74, 124. *Example:* the same integral is written twice, five lines of prose apart, in two different notations. `` {eq}`egm_coledef` `` (73-75) has `\beta \int (u' \circ \sigma) (f(x - c) z ) f'(x - c) z \phi(dz)` with no spacing macros; `` {eq}`egm_getc` `` (121-126) writes the identical object as `\beta \int (u' \circ \sigma) (f(s_i) z ) \, f'(s_i) \, z \, \phi(dz)` with a `\,` between every factor, and wraps it in `\left\{ \ldots \right\}` as the argument of $(u')^{-1}$ where every other function application in the file uses parentheses ($u'(c)$, $f(s_i)$, $\sigma(x)$, $\phi(dz)$). Curly braces around a function argument also collide with the set notation the file uses two lines below ($\{s_i\}$, $\{x_i\}$, $\{(x_i,c_i)\}$). The code comment at 239 shows the simplest spelling of the same thing, `∫ u'(σ(f(s, α)z)) f'(s, α) z ϕ(z)dz`, without the composition operator at all.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 68, 116. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 318. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 340, 344. *Example:* the lecture's headline claim is the one thing it never measures. Line 344 states 'EGM is faster than time iteration because it avoids numerical root-finding' and 346 repeats it, but the only timing in the file is the bare `with qe.Timer():` at 340-342, which prints one number with nothing to compare it against - the os_time_iter solver is never run here, and the `{note}` at 253-257 has already warned that 'the routine is still not particularly fast because we are using pure Python loops'. So the reader is asked to accept a speed comparison from a cell that contains one half of it, in a lecture that otherwise measures everything (331-334 computes the maximal deviation from `σ_star` rather than asserting accuracy).
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 134. *Example:* line 134 bolds an adverb for emphasis - 'The name EGM comes from the fact that the grid $\{x_i\}$ is determined **endogenously**' - which is the job the rule gives to italics, and the file already does it correctly at 115 ('we fix an *exogenous* grid'). The one legitimate bold is at 36, where **endogenous grid method** is the term being defined; 134 re-bolds the same idea as emphasis, so the two uses are no longer distinguishable.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 128, 318. *Example:* the lecture's single figure (318-328) plots the approximate policy against the true one - the same check every lecture in this series ends with - and the thing that is new here, the endogenous grid itself, is never drawn. `K` computes `x_out = s_grid + c_out` at 246, so the unevenly spaced $\{x_i\}$ that give the method its name are in hand at the end of every iteration and are only ever consumed as an interpolation argument. One panel showing the exogenous $\{s_i\}$ against the resulting $\{x_i\}$ (or the two grids as rug marks on one axis) would make '### Exogenous Grid' (77-95) versus '### Endogenous Grid' (98-134) visible in a way that thirty lines of prose cannot.


## Strengths

- The method is introduced by naming the exact cost it removes and the exact price it pays: 100-104 identifies root-finding as the expensive step, 109-111 states the single new assumption ('the only assumption required is that $u'$ is invertible on $(0,\infty)$') and names $(u')^{-1}$, and 251 closes the loop on the code with 'Note the lack of any root-finding algorithm'.
- The three-step recipe at 113-128 maps line for line onto the operator at 219-248: fix $\{s_i\}$ -> `for i, s in enumerate(s_grid)` (238), get $c_i$ from `` {eq}`egm_getc` `` -> `c_out[i] = u_prime_inv(β * mu)` (243), set $x_i = c_i + s_i$ -> `x_out = s_grid + c_out` (246), the last even carrying `# x_i = s_i + c_i` as its comment.
- Line 130 states the property that makes the whole trick legitimate rather than leaving it to the reader - 'Importantly, each $(x_i, c_i)$ pair constructed in this manner satisfies `` {eq}`egm_coledef` ``' - which is the one thing a sceptical reader would stop to check.
- `Model` is a `NamedTuple` with a one-line comment on each of its eleven fields (170-181) and `create_model` annotates and defaults every parameter (184-198), so the model specification needs no accompanying parameter table.
- The lecture is explicitly positioned in its series: 29-32 lists the two earlier solution methods as `{doc}` links, 61 and 79 and 139 state that the model, terminology and notation are os_time_iter's, and 45 and 348-352 hand off to os_egm_jax - a reader arriving cold knows what to read first and what comes next.
- Accuracy is checked against a closed form rather than asserted: `v_star` and `σ_star` are given at 148-162, the policy plot at 318-328 overlays the true policy, and 331-334 prints the maximal absolute deviation.

## Recommended actions

1. Either measure the speed claim at 344-346 or attribute it: run the os_time_iter solver in the same cell as `qe.Timer()` at 340 so the two numbers appear together, or move the claim to os_egm_jax, which is where the vectorized version actually earns it.
2. Add a figure for the endogenous grid - the exogenous $\{s_i\}$ against the $\{x_i\}$ that come out of `K` - so that the contrast the two H3s at 77 and 98 set up has a picture.
3. Sentence-case the four Title-Case headings: '## Key Idea' (55), '### Exogenous Grid' (77), '### Endogenous Grid' (98), '### The Operator' (214) (qe-writing-006 x4).
4. Rename `mu` at 241 and 243, but not to `μ`: `μ` is already this model's shock location parameter (174, 207), so the two would collide. `mu_bar`, `Emu` or `exp_marginal_u` keeps the qe-code-002 fix from creating a second problem.
5. Take two fixes from the upstream twin, `lecture-python.myst/lectures/os_egm.md`, rather than patching here: it carries the `!pip install quantecon` cell this copy is missing (the whole qe-code-003 finding - `quantecon` is imported at 52), and it has already replaced `np.random.seed(seed)` / `np.random.randn` at 206-207 with `np.random.default_rng(seed)` / `rng.standard_normal`. Fixing upstream and re-syncing clears both copies.
6. Italicise rather than bold 'endogenously' at 134, keeping bold for the definition at 36.
7. Write the two copies of the Euler integral the same way (73-75 and 121-126): one spacing convention, parentheses rather than `\left\{ \right\}` around $(u')^{-1}$'s argument, and either the composition $(u' \circ \sigma)$ or the direct application the code comment at 239 uses - not both.
8. Small mechanical items: give the figure at 318 mystnb `name`/`caption` metadata (qe-fig-005), and remove the double spaces at 68 and 116 (qe-writing-008 x2).
