# matplotlib

- **Series:** lecture-python-programming
- **File:** `lectures/matplotlib.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×9; `qe-writing-005` ×4; `qe-writing-004` ×1, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-001` ×5; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-005` ×13; `qe-fig-003` ×3; `qe-fig-007` ×1, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 306, 307, 358, 399, 481. *Example:* `rnormX` and `rnormY` (306-307, used at 308, 311, 314) are camelCase with no mathematical justification, where PEP8 wants `rnorm_x`; line 358 is a whitespace-only line inside a code cell; 399 has trailing whitespace after `cycler('color',` and the continuation at 400 is under-indented; and 481 has both whitespace before a closing bracket, `np.cos(np.pi * θ * x )`, and a space after the unary minus, `np.exp(- x)`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 183, 213, 287, 289, 381, 384, 403, 435. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 13. *Lines:* 59, 82, 103, 114, 123, 132, 157, 181, 201, 236, …. *Example:* {image} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 38, 78, 141, 148, 172, 194, 226, 265, 439. *Example:* H3 Title Case: "Matplotlib's Split Personality" (Split, Personality).

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['cycler'].
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 137, 190, 317. *Example:* .set_title.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 42. *Example:* mid-sentence 'Programming'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 42, 44, 267, 410. *Example:* the lecture contains no bold and no italic anywhere, so the three terms it defines are carried by quotation marks or plain text - the MATLAB-style API (42), the "Pythonic" object-oriented API (44) and style sheets (267) - and at 410 the emphasis on a plain English word is carried by a code span: "These settings are `global`".

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 465. *Example:* static image .png.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 1. *Lines:* 245. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 488. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 265. *Example:* "Style Sheets" runs 265-437, more than a third of the lecture, as an H3 sibling of one-paragraph sections like "3D Plots" (194) - in a section whose own opening says "We mention just a few" (146); and it mutates global `plt.rcParams` at 381-403, which then has to be undone by a reset cell at 430-437.


## Strengths

- The lecture takes a position and argues for it: the MATLAB-style API is shown first (59-68), the same figure is rebuilt in the object-oriented API (82-86), and the recommendation at 46 is backed by the explicit-over-implicit argument at 72-74 with the `import this` pointer.
- Each tweak is a one-line diff on the previous cell - colour, legend, legend location, LaTeX label, ticks (103-139) - so the reader can see exactly which line produced which change.
- `draw_graphs(style=...)` (284-320) is the right abstraction for the style-sheet section: four style sheets are compared through one identical plotting path (327, 333, 339, 345).
- The `{note}` at 408-414 warns that `rcParams` changes are global, and the lecture then actually resets them at 430-437 instead of leaving the notebook in a modified state.
- The custom `subplots` function (237-248) is explained afterwards in three numbered steps (259-263) rather than left for the reader to decode.

## Recommended actions

1. Remove the three embedded matplotlib titles (137, 190, 317) - this is the lecture where readers learn the convention, so demonstrating `set_title` and `suptitle` here teaches against qe-fig-003; use figure captions instead.
2. Add `:name:` and a caption to the 13 figures (59, 82, 103, 114, 123, 132, 157, 181, 201, 236 ...) - in the one lecture where figures are the subject, none is cross-referenceable, and the prose says "the preceding figure" (80).
3. Sentence-case the nine headings (38, 78, 141, 148, 172, 194, 226, 265, 439) and lowercase "Programming" mid-sentence at 42 (qe-writing-004).
4. Drop the eight `figsize=` overrides (183, 213, 287, 289, 381, 384, 403, 435) down to the two that genuinely need a non-default aspect - the 3x2 histogram grid and the 1x4 style comparison.
5. Add the `cycler` install cell at the top of the lecture (qe-code-003): `from cycler import cycler` at 373 is the only non-Anaconda import, and regenerate `matplotlib_ex1.png` (465) from code.
6. Clean the code cells: `rnormX`/`rnormY` to snake_case (306-307), the bracket and unary-minus spacing at 481, the whitespace-only line at 358, the trailing whitespace at 399, and the unused `Axes3D` import at 202.
7. Bold the three terms at first definition (42, 44, 267) and replace the code-span emphasis at 410 with italic; consider splitting "Style Sheets" into its own H2.
