# mccall_model_with_separation

- **Series:** lecture-dp
- **File:** `lectures/mccall_model_with_separation.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-003` ×2; `qe-writing-002` ×3; `qe-writing-007` ×2, +1 more. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 7/10  | `qe-code-001` ×5; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 256, 318, 516, 527, 539. *Example:* three docstrings are single-line, single-quoted strings padded with spaces - `" One update of the scalar h. "` (516), `" Compute v_e from h using the closed-form expression. "` (527), `" Iterates to convergence on the Bellman equations. "` (539) - where the other six functions in the file use `"""` (284, 296, 319, 376, 571); `dist = BetaBinomial(n-1, a, b)` (256) drops the spaces around `-` that the same file uses in `1 - γ` (246) and `1 - β` (326); and the closing bracket of `solve_full_model` is indented four spaces against a hanging indent of eight (318, E124).
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 88. *Example:* missing braces: `\mathbb E`.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 37. *Example:* non-Anaconda import with no install cell: ['myst_nb'].
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 354, 678, 696, 714. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 77, 132, 431. *Example:* line 132 defines the second of the model's two value functions as '$v_u(w)$ be maximum lifetime for a worker who who enters the current period unemployed' - the noun is missing (line 130 has 'maximum lifetime value') and 'who' is doubled, in the sentence that introduces the object the rest of the lecture solves for. Line 431 reads 'But we can go further, but eliminating $v_e$ from the above equation' where the second 'but' should be 'by'. Line 77 spends a parenthesis on '(let's say he to save one character)', a note about the authors' typing rather than the model, and the lecture then mixes 'his' (78, 79) with 'their' (109) anyway.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 511, 532. *Example:* the '## Implementation' section presents its two functions in the wrong order and then mis-describes one of them. `update_h` (514-520) is introduced first and its body calls `compute_v_e` at 518, but `compute_v_e` is not shown until 526 - so the reader meets the update rule in terms of a function that does not yet exist, when the sentence at 523 ('Also, we provide a function to compute $v_e$') would work just as well one cell earlier. Then line 532 says of `compute_v_e` 'This function will be applied once convergence is achieved', which the code contradicts twice over: `update_h` calls it on every iteration (518), and `solve_model` calls it again after the loop (561).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 100, 360. *Example:* the figure at 354-366 plots $v_e$ against the flat line $h$ and the prose immediately says 'The reservation wage is the $w$ where these lines meet' (370) - but nothing in the figure marks that point, so line 392 has to hedge with 'This value seems close to where the two lines meet' after the exact value is computed at 388. One `axvline` at `w_bar` would turn a hedge into a demonstration. Separately, '### Timing and decisions' (100-118) describes a two-state chain - employed to unemployed with probability $\alpha$, unemployed to employed on acceptance - which is the lecture's whole structural addition over the baseline model and is given in prose and bullets only.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 308. *Example:* 2 spaces.


## Strengths

- The lecture solves the same model twice on purpose and then checks the two answers against each other: the direct two-vector iteration (262-392) and the scalar reduction (395-583), with 587-594 printing both reservation wages and their difference - so 'the simplified method is far more efficient' (596) rests on a computation the reader watches rather than an assertion.
- The reduction to a single scalar equation is carried out in visible, individually labelled steps - `` {eq}`bell02_mccall` `` (423), `` {eq}`bell01_mccall` `` (445), `` {eq}`v_e_closed` `` (470), `` {eq}`bell_scalar` `` (478) - with every rearrangement displayed (438-472) rather than left as 'it can be shown'. Every equation label in the file is subsequently cited by `{eq}`; there are no orphans.
- The two `{note}` admonitions pre-empt exactly the two objections a reader will have: that search while employed is excluded (120-122, with a forward `{doc}` to `jv` where it is taken up) and that `` {eq}`bell1_mccall` `` has no max in it (185-193, with the reason and the naming convention).
- Definitions are bolded once at the point of definition - **maximum lifetime value** (135), **continuation value** (217), **reservation wage** (226) - and the single italic in the file, *investment* at 54, is genuine emphasis rather than a definition in disguise.
- `glue` is used to put the three comparative-statics figures in the exposition (612, 628, 641) while their generating code sits in the exercise solution (690, 708, 726), and line 603 tells the reader that is what is happening - so the reader sees the answer before being asked to reproduce it.

## Recommended actions

1. Ignore the 5 qe-math-002 findings (156, 181, 214, 480, 498) and do not insert `\top`: every one is `w' \in \mathbb W`, a next-period wage in a summation index, exactly as line 126 declares ('primes denote next period values'). They are the only reason Math scores 5/10. See scanner_doubts.
2. Reorder '## Implementation': show `compute_v_e` (525-530) before `update_h` (514-521), which calls it, and replace the claim at 532 - `compute_v_e` runs on every iteration (518) and once more after convergence (561), not 'once convergence is achieved'.
3. Fix the two sentences that garble the model: line 132 should read 'maximum lifetime value for a worker who enters the current period unemployed', and line 431 'But we can go further, by eliminating $v_e$'.
4. Mark the reservation wage on the figure at 354-366 with a vertical line at `w_bar` and drop the hedge at 392; the value is already computed 20 lines later at 388.
5. Add braces at line 88 - `{\mathbb E}` should be `\mathbb{E}` (qe-math-010 (proposed), proposed) - and add mystnb caption/name metadata to the 4 code-cell figures (354, 678, 696, 714) (qe-fig-005 x4).
6. Add `myst-nb` to the install cell at 37, or drop the `glue` import: the lecture imports `myst_nb` at 68 and the install line covers only `quantecon jax` (qe-code-003). Also clear the double space at 308 (qe-writing-008).
7. Add a state-transition diagram to '### Timing and decisions' (100-118), and tidy the model unpacking: `α, β, γ, c, w, q = model` leaves unused locals in `T_u` (288, α and w), `T_e` (300, c), `solve_full_model` (323, all but β) and `update_h` (517, α, w and q). Note that this file is byte-identical to `lecture-python.myst/lectures/mccall_model_with_separation.md`, so every fix here should be made once, upstream, and it clears both series.
