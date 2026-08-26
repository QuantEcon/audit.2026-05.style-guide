# lake_model

- **Series:** lecture-python.myst
- **File:** `lectures/lake_model.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×2; `qe-writing-003` ×3; `qe-writing-002` ×2, +2 more. |
| Math         | 6.5/10 | `qe-math-003` ×4; `qe-math-001` ×2. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×8; `qe-fig-003` ×3; `qe-fig-008` ×8, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 229, 317, 334, 424, 589. *Example:* 334, 339 and 400 each unpack the whole model with `λ, α, b, d, A, R, g = model` and then use exactly one of the seven names (`A` at 335, `R` at 340 and 401), leaving eighteen unused bindings across three short functions where `model.A` and `model.R` would do; 317 declares `def update_wrapper(state, t)` and never uses `t`; 229 leaves a trailing space after `A: jnp.ndarray` in the NamedTuple body; 424 binds `e, f = jnp.linalg.eigvals(model.R)`, where `e` is the employment rate everywhere else in the lecture (352, 168) and `f` is `generate_path`'s callable parameter (297); and 589-590 mis-indents the continuation of the `P` literal by one column so the two matrix rows do not line up, with alignment padding inside the row itself. 332-337 and 461-470 also separate top-level defs by one blank line rather than two (E302), and 690, 798 and 816 pass `figsize` as a list where every other call passes a tuple.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 364, 433, 473, 610, 690, 708, 798, 816. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 350, 430, 460, 573, 689, 707, 793, 815. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 692, 695, 698, 713, 800, 803, 806, 821. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 97, 128, 148, 173, 380. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 369, 442, 620. *Example:* .set_title.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 267. *Example:* unicode `α` inside a math environment.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 4. *Lines:* 148, 192, 195, 499. *Example:* matrix environment.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 123, 628. *Example:* 123 duplicates a word - "Of the mass of workers $U_t$ workers who are currently unemployed" - where the parallel sentence at 118 reads correctly; and 628 ("In this case it takes much of the sample for these two objects to converge") gives no magnitude for a claim the figure above it can be read off precisely, in a section headed "### Convergence rate" whose opening question at 567 asks exactly how long.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 66, 68, 448. *Example:* the Overview makes two promises the lecture does not keep: 66 says "Later, we'll determine some of these transition rates endogenously using the `` {doc}`McCall search model <mccall_model>` ``" and nothing after it does - $\lambda$ and $\alpha$ stay exogenous through to the last exercise; and 68-70 says the ergodicity material "will help us build an equilibrium model of ex-ante homogeneous workers whose different luck generates variations in their ex post experiences", but no equilibrium model appears. Separately, exercise `model_ex1` sits at 448-481, immediately after "### Rate dynamics" and 180 lines before the "## Exercises" heading at 632 that holds `model_ex2` and `model_ex3`, so one of the three exercises is outside the section that collects them.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 45, 168. *Example:* the file contains no bold at all, and the term it exists to define is italicised instead: "This lecture describes what has come to be called a *lake model*" (45), where the rule asks for bold on a definition - the two other italics in the file, *cross-sectional* and *long run time series* at 68, are correct emphasis. The employment and unemployment rates are then defined in plain text at 168-169, as is the aggregate-versus-rate capitalisation convention at 171, which is the one piece of notation a reader most needs to find again.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 56, 495. *Example:* the lecture is named after a picture it never draws. 56-61 sets out the metaphor in bullets - two "lakes", the pools of employed and unemployed, with "flows" between them caused by firing and hiring and by entry and exit from the labor force - and that is a two-box diagram with four labelled arrows whose weights are exactly the $\lambda$, $\alpha$, $b$, $d$ of 99-102 and the entries of $A$ at 153-157. Drawing it would let the reader read the transition matrix off the figure. Second, "## Dynamics of an individual worker" (484-527) puts up the two-state transition matrix $P$ at 497-504 and reasons about $\psi_{t+1} = \psi_t P$ and $\psi^*[0] = \alpha/(\alpha+\lambda)$ with no state-transition diagram, in a lecture that already spends eight figures on time paths.

### Low severity
_None found._


## Strengths

- `generate_path` is written once as a higher-order `lax.scan` wrapper (296-326) and then drives every simulation in the lecture - stocks and rates in the body (361, 435) and in both exercise solutions (682, 683, 775, 776, 785, 787) - so eight simulations share one implementation and one `jax.jit` boundary.
- 288-293 says plainly why the JAX idiom is needed ("iteratively generating time series is somewhat nontrivial in JAX because arrays are immutable") and then tells the reader they may skip to the end of the function - an honest signpost around a technical digression rather than an unexplained wrapper.
- The capital-for-aggregates, lowercase-for-rates convention is stated outright at 171 and then held without exception, in the mathematics ($E_t, U_t, N_t, X_t$ against $e_t, u_t, x_t$) and in the code (`X_path` against `x_path`, `X_0` against `x_0`, `U_0` against `u_0`).
- The `rate_steady_state` docstring (392-399) gives the Perron-Frobenius reason why the eigenvector of the largest eigenvalue is the steady state, so the `jnp.argmax` at 405 is justified where a reader would look for the justification rather than left as a trick.
- The convergence condition is checked rather than asserted: 417-425 prints both eigenvalue moduli of $R$ to confirm the second is below one before the convergence plot at 430-445 is shown.
- 561-563 is the payoff the Overview promises: observing that $P = R^\top$ when $b = d = 0$ ties the cross-sectional steady state to a single worker's long-run time averages, and the simulation at 573-623 then confirms it against the dashed stationary line.
- Parameter values are sourced rather than chosen: 264-265 attributes $\alpha$ and $\lambda$ to `` {cite}`davis2006flow` `` and links the CDC birth and death tables behind $b$ and $d$; and `\mathbb 1\{\cdot\}` is defined in the parenthetical at 547, right after its first two uses.

## Recommended actions

1. Add `mystnb: figure: caption`/`name` metadata to all eight figures (350, 430, 460, 573, 689, 707, 793, 815) and move the three `set_title` calls that duplicate captions (369, 442, 620) - none of the eight figures is currently citable, and the prose refers to them only as "the dashed line" (626) and "below".
2. Draw the lake diagram for section 56-61 - two pools, four arrows labelled $\lambda$, $\alpha$, $b$, $d$ - and a two-state transition diagram for $P$ at 497-504; the first would let a reader read $A$ off the figure and the second is the standard picture for the Markov section.
3. Either deliver the two things the Overview promises - endogenous transition rates via the McCall model (66) and the equilibrium model of ex-ante identical workers (68-70) - or remove those sentences and point to the lecture that does.
4. Replace the seven-way unpacking in `stock_update`, `rate_update` and `rate_steady_state` (334, 339, 400) with `model.A` / `model.R`, and drop the unused `t` in `update_wrapper` (317); the three functions currently create eighteen unused local names.
5. Convert the four `matrix` environments to `bmatrix` (148, 192, 195, 499), which also removes the `\left( ... \right)` scaffolding around them, and write `$\alpha$` rather than the unicode `$α$` inside math at 267 (qe-math-001).
6. Move exercise `model_ex1` (448-481) down into the "## Exercises" section at 632, and replace the four hand-written three-panel plotting blocks in the solutions (689-703, 707-719, 798-811, 815-827) with the `zip` loop already used at 367-369 - the same figure is currently coded out four times.
7. Add `lw=2` to the eight line plots in the exercise solutions (692, 695, 698, 713, 800, 803, 806, 821) to match the body, bold the definitions at 45 and 168-169, fix the duplicated word at 123, give a number for "much of the sample" at 628, and close the six double spaces (97, 128, 148, 173, 380).
