# lq_inventories

- **Series:** lecture-python.myst
- **File:** `lectures/lq_inventories.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×2; `qe-writing-001` ×4; `qe-writing-005` ×4, +4 more. |
| Math         | 3/10  | `qe-math-002` ×15; `qe-math-003` ×17. |
| Code         | 7/10  | `qe-code-001` ×7; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×4; `qe-fig-008` ×10; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 298, 299, 315, 322, 333, 335, 743. *Example:* `c2 * Q_path ** 2` (298) and `d2 * (S_path - I_path) ** 2` (299) put spaces around `**`, which qe-code-001 names explicitly as the one operator that should be written closed up; `set_ylim(0-span*1.1, 0+span*1.1)` (315, 322) drops the spaces around `-`, `+` and `*` in the same expression; the two plot labels at 333-336 are continued with a backslash inside the string literal, which both violates PEP8's preference for parenthesised continuation and injects a run of spaces into the rendered legend text; and `A22 =[[1,  0,  0],` (743) has no space after `=` and continues at column 10 under an opening bracket at column 6. Three inline comments also sit one space from the code rather than two (646, 680, 753).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 306, 307, 308, 312, 326, 327, 328, 332, 333, 335. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 15. *Lines:* 131, 137, 148, 149, 151, 153, 661, 720. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 17. *Lines:* 114, 150, 151, 154, 157, 158, 161, 164, 165, 168, …. *Example:* array used as matrix.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 417, 448. *Example:* H2 Title Case: 'Inventories Not Useful' (Not, Useful).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 310, 316, 330, 338. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 489, 716, 722, 769. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 481, 71, 564. *Example:* line 481-487 is one 75-word sentence describing three production paths and their three colours, and it is ungrammatical in the middle ('as well with an optimal production path'); the bullet at 71-72 says the same object is two different things - '$c(Q_t) = c_1 Q_t + c_2 Q_t^2$, be a cost of production function, where $c_1>0, c_2>0$, be an inventory cost function' - so the definition of the production cost function reads as a definition of the inventory cost function; and 564-571 packs the stability caveat, the optimal output level, its economic meaning and an aside about negative production into a single 48-word sentence with two nested parentheticals.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 417, 481. *Example:* the two alternative-technology models are given their own H2 sections, 'Inventories Not Useful' (417) and 'Inventories Useful but are Hardwired to be Zero Always' (448), which sit between '## Example 1' (353) and '## Example 2' (517) at the same heading level - so the Example 1..6 sequence is broken in the middle by two sections that are not examples. Worse, the discussion inside the second of them (481-511) is about the bottom-right panel of Example 1's figure and ends by re-running Example 1 at 514, so Example 1's analysis is completed under a heading about a different model. The two concepts are also introduced a third time, at 404-415, before either section defines them.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 565, 590, 592, 685. *Example:* bold is used for emphasis throughout the later sections, and the lecture uses italic for emphasis nowhere: **stability** (565) emphasises a term that is not being defined here, **run a Ponzi scheme** (590) and **going short in** / **borrowing** (592-593) are rhetorical emphasis, and **season** (685) marks a word in an ordinary sentence. The genuine definitions earlier in the lecture, **state** (98) and **control** (104), are bolded correctly - it is the emphasis that has taken the wrong markup.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 56, 62, 432, 507. *Example:* 2 spaces.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 278. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 304. *Example:* figsize=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 304. *Example:* all twelve figures in the lecture come from one hard-coded four-panel layout inside `SmoothingExample.simulate` (304-340), the same four panels whatever the example is about, and none of them is captioned or named. The prose is therefore forced to navigate by position - 'The figures above' (391), 'The lower right panel' (404), 'The bottom right panel' (481), 'the following figures confirm' (595) - and Example 4's point, that inventories run down without limit, has to be found in one panel of a 15x10 grid. Example 6 then prints four more of the same four-panel figures (681, 689, 694, 699) that differ only in the initial season, with nothing in or around them saying which is which.


## Strengths

- The reduction of the firm's profit function to the LQ matrices is shown rather than asserted: the `\underset{...}{\underbrace{...}}` annotations at 148-149 tag each group of terms with the matrix it lands in, and 150-171 then displays $R$, $Q$ and $N$ with the same tags, so every entry can be traced back to a primitive.
- The lecture warns the reader about the two notation collisions it cannot avoid - that $Q_t$ is production while $Q$ is the control cost matrix (129-132), and that the cross-product matrix is called $N$ in the QuantEcon library (177-178).
- The six examples change exactly one feature of the environment each - AR(1) shock (353), no randomness (517), $d_1 = 0$ (535), $d_1 = d_2 = 0$ (554), linear trend (614), deterministic seasonal (650) - and all of them go through keyword arguments to a single class, so any difference between figures is attributable to the stated change.
- Example 4 teaches a failure instead of hiding it: switching off both inventory costs violates the stability conditions, and the lecture follows the absurd optimum through the law of motion (573-590) and then shortens the horizon to $T = 30$ so the divergence is visible (607-611).

## Recommended actions

1. Convert the seventeen `array` environments used as matrices to `bmatrix` (114, 150-171, 364-376, 626-634) - the profit-function display at 150-171 is where a reader most needs the brackets to read the block structure (qe-math-003, 17 occurrences).
2. Replace every transpose with `^\top`: the apostrophes at 131, 137 and 661 and the `^\prime` forms at 148, 149, 151, 153 and 720 (qe-math-002, 15 occurrences, a very-high-weight rule).
3. Fix the section structure: move 'Inventories Not Useful' (417) and 'Inventories Useful but are Hardwired to be Zero Always' (448) ahead of Example 1 (or demote them under it), and return the Example 1 discussion at 481-514 to the Example 1 section, so the numbered examples run without interruption.
4. Give the figures identities: have `simulate` take a caption/name, or wrap each call in a cell with `mystnb: figure:` metadata, and replace 'the lower right panel' (404), 'The bottom right panel' (481) and 'The figures above' (391) with `` {numref} `` references - twelve figures currently have no name at all.
5. Drop the four `set_title` calls (310, 316, 330, 338) in favour of captions, set `lw=2` on the ten `plot` calls (306-335), and drop `figsize=(15, 10)` at 304 (qe-fig-003 x4, qe-fig-008 x10, qe-fig-001 x1).
6. Repair the prose: rewrite the 75-word sentence at 481, fix the contradictory bullet at 71-72, split the four two-sentence paragraphs at 489, 716, 722 and 769 (qe-writing-001, 4 occurrences), lowercase the H2 headings at 417 and 448 (qe-writing-006, 2 occurrences), close the double spaces at 56, 62, 432 and 507 (qe-writing-008, 4 occurrences), and change the four emphasis-bolds at 565, 590, 592 and 685 to italic.
7. Clean the code: close up `Q_path**2` (298, 299), space the arithmetic at 315 and 322, replace the backslash string continuations at 333-336 with parenthesised strings, fix `A22 =[[` at 743, rename the exercise-solution `ex1` at 751 so it does not overwrite Example 1's `ex1` from 385, and replace the mathematical-italic nu in `𝜈_path` (292) with the ordinary Greek ν.
