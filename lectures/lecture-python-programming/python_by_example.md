# python_by_example

- **Series:** lecture-python-programming
- **File:** `lectures/python_by_example.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×10; `qe-writing-005` ×3; `qe-writing-002` ×2, +3 more. |
| Math         | 9/10  | `qe-math-012` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×11; `qe-fig-008` ×10. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 7.5/10 | `qe-admon-003` ×2. |

## Issues

### Critical
- **[qe-admon-003]** — Use tick count management for nested directives. *Count:* 2. *Lines:* 499, 549. *Example:* {exercise-start} fence (3 ticks) is never closed — the directive swallows the rest of the block.

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 391, 420, 641, 660, 721. *Example:* inline-comment and unary-operator spacing in a lecture that itself teaches PEP8 indentation: `i == ts_length #the ending condition for the while loop` has one space before the hash and none after it (391); one space before the inline comment where PEP8 asks for two (420, 721); and a space after the unary minus in `abs_x = - x[t]` (641) and `abs_x = - x[t] if x[t] < 0 else x[t]` (660).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 11. *Lines:* 46, 61, 179, 209, 374, 417, 481, 524, 576, 632, …. *Example:* {figure} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 67, 182, 217, 382, 426, 491, 534, 586, 646, 663. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 39, 99, 147, 174, 195, 204, 294, 338, 364, 399. *Example:* H2 Title Case: 'The Task: Plotting a White Noise Process' (Task, White, Noise, Process).

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 445. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 349, 513. *Example:* 'Once you get used to it, this is a good thing: It' (349) ends on a dangling pronoun that the two following bullets have to finish, so the sentence cannot be read on its own; and the exercise-2 hint at 513 - 'For the legend, noted that suppose `var = 42`, the expression `f'foo{var}'` evaluates to `'foo42'`' - is ungrammatical, in the one place a stuck reader goes for help.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 224, 225, 239. *Example:* the lecture bolds its definitions correctly almost everywhere - **package** (118), **modules** (120), **subpackage** (141), **method** (263), **code block** (309) - but the two terms introduced in the bullet list at 221-227 are italicised instead: 'an empty *list* called `ϵ_values`' (224) and 'The statement `# empty list` is a *comment*' (225), the latter a textbook definition set in emphasis. The fuller definition of a list at 239 ('Lists are a native Python data structure used to group a collection of objects') then carries no emphasis at all.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 124, 397, 445. *Example:* 2 spaces.

### Low severity
- **[qe-math-012 (proposed)]** — Multiplication via \cdot or juxtaposition, never *. *Count:* 1. *Lines:* 693. *Example:* * as multiplication.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 56. *Example:* '## Version 1' (56) is the only numbered section in the lecture and there is no Version 2 - the second attempt arrives 140 lines later as '## Alternative Implementations' (195). The numbering promises a sequence the lecture never continues, and a reader scanning the contents cannot tell that 195 is the continuation of 56.


## Strengths

- The white-noise program is written three times - vectorised (61-69), with a `for` loop (209-219) and with a `while` loop (374-384) - and the first two carry labels that later prose actually cites by `{ref}` (197, 299, 371), so 'let's do this another way' is always a link rather than a description.
- Unicode Greek is used from the very first code cell (`ϵ_values`, 66) through to the last exercise (`α_values`, 525); qe-code-002 has nothing to report.
- The indentation rule is introduced where it is first needed (307-315) and then given its own section (338-362) that ends on something concrete: 'The Python standard is 4 spaces, and that's what you should use'.
- Every exercise is a labelled `exercise-start`/`exercise-end` pair with a `:class: dropdown` solution, and two carry `{hint}` dropdowns (509, 686) so the help is opt-in.
- 'IID' is written in the correct form at 197, 461 and 692 - no 'i.i.d.' anywhere.

## Recommended actions

1. Close the two `{exercise-start}` fences at 499 and 549 (qe-admon-003, critical, 2 occurrences): each opens a 3-tick block that is never closed, so the exercise body swallows the `{hint}` and the `{exercise-end}` that follow it.
2. Lower-case the 10 Title Case headings (39, 99, 147, 174, 195, 204, 294, 338, 364, 399) - qe-writing-006, 10 occurrences and the largest routine fix here.
3. Add `:name:`/caption metadata to the 11 figures (46, 61, 179, 209, 374, 417, 481, 524, 576, 632, 652) and set `lw=2` on the 10 plots (67, 182, 217, 382, 426, 491, 534, 586, 646, 663) - qe-fig-005 and qe-fig-008.
4. Rewrite the exercise-2 hint at 513 as a sentence, and finish the sentence at 349 before the bullet list starts.
5. Bold the two definitions at 224-225 and the definition sentence at 239, matching 118, 120, 141, 263 and 309.
6. Fix the PEP8 items above (391, 420, 641, 660, 721) and replace `*` with `\cdot` in the circle-area hint at 693 (qe-math-012 (proposed), proposed, 1 occurrence).
7. Either rename '## Version 1' (56) or add the Version 2 it implies, and correct 'There are no withdraws over the time period' to 'withdrawals' (405).
