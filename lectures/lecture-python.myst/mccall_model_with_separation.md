# mccall_model_with_separation

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model_with_separation.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-002` ×2; `qe-writing-003` ×1; `qe-writing-008` ×1, +1 more. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-001` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 256, 318, 516, 527, 539, 388, 684, 702, 720. *Example:* `BetaBinomial(n-1, a, b)` at 256 omits the spaces around `-` that the neighbouring lines keep; the closing bracket of the `solve_full_model` signature sits at column 4 (318) - matching neither the opening line nor the 8-space hanging indent of its arguments; three one-line docstrings are written as padded single-quoted strings, `" One update of the scalar h. "` (516) and likewise 527 and 539, although the other five docstrings in the file use triple quotes (284, 296, 319, 376, 571); and four top-level definitions are followed by only one blank line before the next statement (388, 684, 702, 720) where PEP8 asks for two.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 88. *Example:* missing braces: `\mathbb E`.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 354, 678, 696, 714. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 132, 431. *Example:* two sentences are garbled: line 132 reads '$v_u(w)$ be maximum lifetime for a worker who who enters the current period unemployed' - the noun 'value' is missing from 'maximum lifetime' and 'who' is doubled, in the very sentence that defines one of the lecture's two value functions; line 431 reads 'But we can go further, but eliminating $v_e$ from the above equation', where the second 'but' should be 'by'.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 518. *Example:* `update_h` at 515-520 calls `compute_v_e`, which is not defined until 526, and the prose introduces it afterwards at 523 ('Also, we provide a function to compute $v_e$'). A reader following the code in order meets the call before the function and before the sentence that motivates it; swapping the two cells costs nothing.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 360. *Example:* the figure at 360-365 exists to locate the reservation wage - 370 says 'The reservation wage is the $w$ where these lines meet' - but it draws only $v_e$ and $h$, marks nothing, and carries no axis labels, so after computing $\bar w$ the lecture can say only that 'This value seems close to where the two lines meet' (392). A vertical line at `w_bar_full`, or a marker at the crossing, would turn that hedge into a check.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 308. *Example:* 2 spaces.


## Strengths

- Every labelled equation is referred to later, and the references are what carry the derivation: bell2_mccall is cited at 170, 219, 237 and 407, bell1_mccall at 195, 200, 237 and 442, defh_mm at 348, 407, 420 and 436, and v_e_closed at 485 and 523 - there is not a single dead label in the lecture.
- The scalar reduction is not just derived but tested: the simplified solver is run against the two-vector solver on the same model and the two reservation wages are printed side by side with their difference (587-594).
- The note at 185-193 pre-empts the objection that `` {eq}`bell1_mccall` `` is not a Bellman equation because it contains no max, and says why the name is kept anyway.
- `Model` is a `NamedTuple` with a default and a one-line comment for each of the six fields (263-269), and every function unpacks it with the identical `α, β, γ, c, w, q = model` line, so the parameter set is declared in exactly one place.
- The three comparative-statics figures are generated inside the exercise solutions and pulled into the narrative with `glue` (612, 628, 641 against 690, 708, 726), and line 603 tells the reader that is what is happening - the result is shown first, then set as the exercise.

## Recommended actions

1. Fix the two broken sentences at 132 ('maximum lifetime value', and drop the doubled 'who') and 431 ('by eliminating', not 'but eliminating') - 132 is one of the two definitions the whole lecture rests on.
2. Mark $\bar w$ on the figure at 360 and give it axis labels, so that 392 can state the agreement instead of saying the value 'seems close'.
3. Add `mystnb: figure: caption/name` metadata to the four un-named figure cells (354, 678, 696, 714) - the three glued figures are referenced by key but none of the four has a caption (qe-fig-005, 4 occurrences).
4. Move the `compute_v_e` cell (525-530) ahead of the `update_h` cell (514-521) so no function is called before it is defined.
5. Brace the blackboard operator at 88, `{\mathbb E}` -> `\mathbb{E}` (qe-math-010 (proposed), proposed, 1 occurrence), and close the double space at 308 (qe-writing-008, 1 occurrence).
6. Give the three one-line docstrings triple quotes (516, 527, 539) to match the other five, space `n-1` at 256, and add the second blank line after the top-level definitions at 388, 684, 702 and 720.
7. Rename the two code sections so they are distinguishable: '## Code' at 234 holds the two-vector solver and '## Implementation' at 509 holds the scalar solver, and nothing in the titles says which is which.
