# career

- **Series:** lecture-python.myst
- **File:** `lectures/career.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-003` ×2; `qe-writing-006` ×1; `qe-writing-002` ×1, +2 more. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×6; `qe-fig-001` ×5; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 175, 320, 337, 424, 547. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 170, 313, 336, 373, 396, 542. *Example:* {image} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 64. *Example:* H3 Title Case: 'Model Features' (Features).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 231, 244, 504. *Example:* line 231 has a single space before the inline `# III` comment where PEP8 asks for two (and where the two lines above it align theirs); lines 244-245 pad with extra spaces both before `=` and inside the `in_axes` tuples (`_B_j  = jax.vmap(_B,   in_axes=(None, None, None, 0))`), which PEP8 explicitly discourages even for alignment; line 504 is 82 characters.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 178, 429, 430. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 359, 508. *Example:* line 359 is a lone bullet ("Sometimes a good job must be sacrificed...") dangling two prose paragraphs after the list it belongs to at 349-353, so it reads as a list of one; and the exercise 2 solution at line 508 calls `median_passage_time(cw, greedy_star, ...)` using `cw` and `greedy_star` that are bound inside the exercise 1 solution cell (419-421) and `draw` defined there at 397 - the second solution silently depends on the first, and both are behind `:class: dropdown`.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 373. *Example:* static image .png.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 117. *Example:* the three continuation values are named $I$, $II$ and $III$ (117, 126-128, 132, 217-218); in math mode `$II$` typesets as two adjacent italic capital I's and `$III$` as three, so each reads as a product of copies of $I$ rather than as a label - $v_1, v_2, v_3$ is both simpler and unambiguous, and the code already calls them `stay_put`, `new_job` and `new_life`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 1. *Lines:* 303. *Example:* the note at 303-305 is a 43-word sentence that carries the readability claim, the scaling claim, three examples of what it scales to, and the GPU claim in one span.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 508. *Example:* exercise 2 sets up a random variable $T^*$, defines it twice (450, 460), asks for 25,000 draws of it, and then the solution reports a single median at 508 and another at 519; the 25,000 first-passage times are already in `times` at line 504, so the distribution the exercise is about is computed and then thrown away without a histogram - the natural companion to the "about 7 and 14 respectively" claim at 522.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 74. *Example:* 2 spaces.


## Strengths

- The three continuation values are coded for a single state first (`_B` at 224-232, with `# I`, `# II`, `# III` marking the correspondence to `` {eq}`eyes` ``) and only then vectorised with two `jax.vmap` calls at 244-245 - the code sits next to the equation instead of next to the array shapes, and lines 220-221 say that is the intent.
- The Bellman operator and the greedy policy are derived from the same `B(v, cw)` array as its max and argmax (259-268), so the policy cannot drift out of step with the value function.
- The note at 300-309 justifies the choice of JAX for a problem that does not need it, and points at the specific place where the choice pays off (`` {ref}`career_ex2` ``, 25,000 simulated careers).
- `solve_model` returns the iteration count and the final error alongside the value function (278-297) and line 318 prints them, so convergence is visible rather than assumed.
- The optimal-policy contour plot is annotated in place with `ax.text` naming the three regions (343-345), and the prose at 349-359 reads the figure back to the reader region by region.

## Recommended actions

1. Add `:name:` to the `{image}` at 373 and `mystnb: figure: caption/name` metadata to the five code-cell figures at 170, 313, 336, 396 and 542 so every figure is captionable and `{numref}`-referenceable (qe-fig-005, 6 occurrences).
2. Drop the five `figsize=` overrides at 175, 320, 337, 424 and 547 and let the theme set the size (qe-fig-001, 5 occurrences).
3. Replace the static PNG at 373 with the code that generates it - the exercise 1 solution at 396-435 already produces that figure, so the target image can be generated rather than shipped as `/\_static/lecture_specific/career/career_solutions_ex1_py.png` (qe-fig-002).
4. Rename $I$, $II$, $III$ to $v_1$, $v_2$, $v_3$ (117, 126-128, 132, 217-218), and give the Beta function at 153 a name other than $B$ - $B$ is already the grid upper bound (139-142) and is also the name of the Bellman option-value array in the code (249), so one letter carries three meanings.
5. Plot the 25,000 first-passage times in the exercise 2 solution instead of reducing them to a median, and make the exercise 2 solution self-contained rather than depending on names bound in the exercise 1 solution.
6. Set `lw=2` on the three plot calls at 178, 429 and 430 (qe-fig-008, 3 occurrences).
7. Sweep the small mechanical items: sentence-case the H3 at line 64 to `### Model features` (qe-writing-006), collapse the double space at line 74 (qe-writing-008), delete the two `\nonumber` commands at 127-128 which do nothing inside `aligned`, fix "overall feasible" to "over all feasible" at line 111, and tidy the PEP8 spacing at 231 and 244-245.
