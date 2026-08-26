# aiyagari_egm

- **Series:** lecture-python.myst
- **File:** `lectures/aiyagari_egm.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×5; `qe-writing-005` ×3; `qe-writing-003` ×2, +3 more. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×5; `qe-fig-005` ×3; `qe-fig-001` ×3, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 383, 393, 574, 609, 619. *Example:* .set_title.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 99. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 88, 400, 483, 581, 629. *Example:* H2 Title Case: 'The Economy' (Economy).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 375, 563, 598. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 367, 549, 597. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 696. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 634, 650, 651. *Example:* the summary at 629-658 restates the overview rather than closing it. "avoids costly root-finding by working backwards from the Euler equation" (634) and "EGM avoids the root-finding required by value function iteration" (649) are the third and fourth statements of the claim first made at 258; "simulation is more flexible (works with continuous shocks, non-linear policies)" (650) repeats line 406 nearly verbatim; and 651 repeats 641, itself a repeat of 583. The section adds three lists (631-641, 647-658, 662-667) where one would do.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 138, 585. *Example:* the Euler equation at 133-136 is written in terms of $s$, "the optimal savings policy function" (138), and $s$ then never appears again - the operator implemented at 276-308 works on a *consumption* policy $\sigma$ (280-281), and nothing bridges the two, so the reader has to work out for themselves that `σ` is not the $s$ of the display above it. Separately line 585 says "We reuse the cross-section simulated at equilibrium prices", but the cell that follows (587-590) re-solves the household problem and re-runs the 50,000-household, 1,000-period simulation from scratch; nothing is reused.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 51, 647, 654. *Example:* the lecture uses bold for eight different jobs and italic for none. Line 51 bolds **simulation** for contrast, not definition ("We compute aggregate capital by **simulation** rather than an algebraic technique"); lines 647 and 654 use `**Advantages:**` and `**Disadvantages:**` as section headings; and line 50 re-bolds **endogenous grid method**, already bolded and defined eight lines earlier at 42.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 569. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 64. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 258. *Example:* the endogenous grid - the one idea the lecture exists to teach - is never drawn. Section "The EGM operator" (256-308) explains in a three-step recipe that the exogenous $a'$ grid is mapped back to an *irregular* implied grid $a_{ij} = (c_{ij} + a_i - w z_j)/(1+r)$ and then interpolated back onto the regular grid, and step 3 mentions "handling the borrowing constraint where it binds"; a plot of `a_endo` against `a_grid`, or of the $(a_{endo}, c_{endo})$ points before and after interpolation, would show both the irregular spacing and the binding region that lines 298-303 handle in code.


## Strengths

- The EGM operator is checked, not assumed: line 361 measures the fixed-point residual `max|K_egm(σ_star) - σ_star|` and prints it, so the reader sees that `solve_household` actually converged rather than just returning.
- Every array in `K_egm` carries its shape as an inline comment (288, 291, 307, 308: `# (a_size, z_size)`, `# (z_size, a_size)`), which is what makes the two transposes at 288 and 308 followable.
- The borrowing-constraint branch is explained where it happens: the comment at 298-300 says why `a_grid < a_endo[0, j]` is the binding region and what the household does there, rather than leaving `jnp.where` unexplained.
- Line 509 states why a fixed random key is passed to every `G` evaluation - the root finder needs a deterministic excess-demand function - which is the kind of trap that silently breaks bisection on a simulated objective.
- The lecture is honest about the cost of its method: the disadvantages list at 654-658 names Monte Carlo noise and lower precision than the analytical stationary distribution, rather than presenting simulation as free.

## Recommended actions

1. Move the ten embedded matplotlib titles into figure captions - `ax.set_title` at 383, 393, 574, 609 and 619 (qe-fig-003, 5 occurrences) - and add `mystnb: figure: caption/name` metadata to the three code-cell figures at 367, 549 and 597 (qe-fig-005, 3 occurrences).
2. Add a figure showing the endogenous grid against the exogenous grid; without it the lecture's title method is described but never seen.
3. Write solutions for the four exercises at 671-713, or mark them as unsolved deliberately - every other lecture in the series pairs `{exercise}` with `{solution-start}`, and exercise 1 in particular asks the reader to time EGM against the VFI code from `` {doc}`aiyagari` ``, which is not available in this notebook.
4. Fix `\mathbb{E_z}` at line 126: the subscript is inside the braces, so the whole token `E_z` renders in blackboard bold; it should be `\mathbb{E}_z`.
5. Reconcile the math with the code: either write the Euler equation at 133-136 in terms of the consumption policy the code implements, or say explicitly that $\sigma$ is consumption while $s$ was savings.
6. Cut the summary at 629-667 down to the parts that are not already in the overview, and fix the claim at 649 - the standard Aiyagari lecture solves the household problem by `argmax` over a discretised grid, not by root-finding.
7. Sweep the mechanical items: sentence-case the five Title Case H2s at 88, 400, 483, 581 and 629 (qe-writing-006, 5 occurrences), drop the three `figsize=` overrides at 375, 563 and 598 plus the hard-coded `fontsize=` arguments at 572-575 and 607-620 (qe-fig-001, 3 occurrences), brace `\mathbb E` at 99 (qe-math-010 (proposed), proposed), set `lw=2` at 569 (qe-fig-008), move the mid-narrative `{cite}` at 64 (qe-ref-001), split the two-sentence paragraph at 696 (qe-writing-001), and drop the unused `z_dist` binding at 590.
