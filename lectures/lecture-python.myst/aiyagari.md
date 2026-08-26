# aiyagari

- **Series:** lecture-python.myst
- **File:** `lectures/aiyagari.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×2; `qe-writing-003` ×2; `qe-writing-002` ×3, +4 more. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×5; `qe-fig-008` ×3; `qe-fig-001` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 376, 434, 499, 564, 666. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 109. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 98. *Example:* H2 Title Case: 'The Economy' (Economy).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 84, 353, 380. *Example:* lines 84-85 bind `I = jnp.identity(n)` and `O = jnp.ones((n, n))`; PEP8 names `l`, `O` and `I` as the three identifiers never to use alone because they are indistinguishable from digits in many fonts, and the ones matrix has no symbol in the surrounding mathematics to inherit. Lines 353 (81 chars) and 831 (86 chars) exceed the 79-character limit, and four lines carry trailing whitespace (380, 526, 589, 592).
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 379, 506, 588. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 380, 508, 677. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 692. *Example:* raw link to dp.quantecon.org.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 57, 391, 560. *Example:* line 374 ("The next plot shows asset accumulation policies at different values of the exogenous state") and line 391 ("The plot shows asset accumulation policies at different values of the exogenous state.") are the same sentence, once before the figure and once after; lines 556-562 spend three paragraphs on one idea ("We can visualize the equilibrium using supply and demand curves" / "The following code draws the aggregate supply and demand curves" / "The intersection gives the equilibrium interest rate and capital"); and line 57 is a list item reading "etc., etc., etc.".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 80, 462. *Example:* `compute_stationary` is defined at 80-88, inside "### Preliminaries" and before the model exists, but is not used until line 424 - 340 lines later - and the only account of what it does is a page reference to an external book, so a reader meets the linear system $(I - P^\top + O)x = \mathbb{1}$ with no explanation of why it yields a stationary distribution. Separately the lecture has two H3s both titled "Equilibrium" (213 under "The Economy", 462 under "Implementation"), which makes the contents directive at 28-30 ambiguous and gives the reader no way to tell which section a reference means.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 78, 692. *Example:* mid-sentence 'Dynamics'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 104, 106, 215. *Example:* 2 spaces.

### Low severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 698. *Example:* line 698 uses bold as a section heading - `**Key concepts you'll need:**` - inside the exercise 3 body; it is neither a definition nor emphasis, and an H4 or a plain lead-in sentence would do the job without borrowing the convention the lecture uses for defined terms (e.g. **stationary rational expectations equilibrium (SREE)** at 215).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 516. *Example:* line 516 asserts a visual fact - "a simple iteration scheme $K_{n+1} = G(K_n)$ will cycle from high to low values, leading to slow convergence" - and points at the figure above it, but that figure (499-512) plots only $G$ and the 45-degree line; the cycling it describes is exactly what a cobweb overlaid on those two curves would show, and it is the whole justification for the damped scheme introduced at 518-522.


## Strengths

- Each piece of the model is followed immediately by the function that implements it, with the equation label and the code side by side - `` {eq}`aiy_rgk` `` at 179-183 then `r_given_k` at 186, `` {eq}`aiy_wgr` `` at 198-202 then `r_to_w` at 205 - so the reader never has to hold an equation in mind across a section boundary.
- The reshape comments in `B` (291-299) annotate every broadcast with its before-and-after index pattern (`a[i] -> a[i, j, ip]`, `Π[j, jp] -> Π[i, j, ip, jp]`), which is the one thing that makes a 4-D vectorised Bellman operator readable.
- The equilibrium algorithm is stated as five numbered steps (466-470), then compressed to $K_{n+1} = G(K_n)$ (474-480), then written as the function `G` (485-494) - three views of the same object, in that order.
- `ψ_a.sum()` at 447 is a deliberate sanity check with the expectation stated in the prose above it ("The distribution should sum to one"), rather than a silently-trusted intermediate.
- The three exercises build on each other in increasing difficulty - bisection instead of damping, comparative statics in $\beta$, then a full Howard policy iteration implementation - and each solution reuses the functions defined in the body rather than restating them.

## Recommended actions

1. Add `mystnb: figure: caption/name` metadata to the five code-cell figures at 376, 434, 499, 564 and 666 so they can be captioned and cross-referenced (qe-fig-005, 5 occurrences).
2. Rename the damping parameter in `compute_equilibrium` (526, 532) and in the display at 521: $\alpha$ is already the capital share, declared at 155 as $\alpha \in (0,1)$ and stored in `Firm` at 173, so "You can try varying $\alpha$" at 552 is ambiguous about which parameter it means.
3. Set `lw=2` on the four plot calls at 380, 508, 597 and 677 (qe-fig-008, 4 occurrences) and drop the three `figsize=` overrides at 379, 506 and 588 (qe-fig-001, 3 occurrences).
4. Rename `value_function_iteration` (331) - it iterates the Bellman operator but returns `get_greedy(v, ...)`, a policy, not a value function, so every caller (493, 573) is reading a policy out of a function whose name promises a value.
5. Give the two "### Equilibrium" H3s (213, 462) distinct titles, and move `compute_stationary` (80-88) down to where it is first needed at 424, with a sentence saying why solving $(I - P^\top + O)x = \mathbb{1}$ returns the stationary distribution.
6. Add a cobweb to the $G$ figure at 499-512 so the cycling claimed at 516 is visible, and lower-case the mid-sentence capitals at 78 ("Dynamics") and 692 (qe-writing-004, 2 occurrences).
7. Sweep the small mechanical items: sentence-case the H2 at 98 to `## The economy` (qe-writing-006), brace `\mathbb E` to `\mathbb{E}` at 109 (qe-math-010 (proposed)), convert the raw `dp.quantecon.org` link at 692 to a `{doc}` reference (qe-link-002), and collapse the double spaces at 104, 106 and 215 (qe-writing-008, 3 occurrences).
