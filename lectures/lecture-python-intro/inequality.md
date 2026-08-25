# inequality

- **Series:** lecture-python-intro
- **File:** `lectures/inequality.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-004` ×3; `qe-writing-001` ×2; `qe-writing-005` ×3, +3 more. |
| Math         | 9/10  | `qe-math-012` (proposed) ×1. |
| Code         | 6.5/10 | `qe-code-001` ×16; `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×5; `qe-fig-004` ×4; `qe-fig-003` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 16. *Lines:* 285, 555, 575, 673, 700, 725, 760, 768, 936, 982, …. *Example:* PEP8 spacing is loose throughout the data-handling cells: whitespace before a closing paren (285), missing space after a comma in `('YR','')`, `['USA','GBR', ...]`, `range(min_year,max_year,5)`, `[0,1],[0,1]`, `reshape((k,1))` (555, 575, 673, 700, 725, 760, 982, 1110), spaces around `=` in the plotly keyword arguments (768-773), `σ ** 2` where the rule explicitly prefers `σ**2` and where line 490 already writes it that way (936), lambdas bound to names instead of `def` (1013), missing space after an operator in `return 1- t(1 - p)` (1014), a backslash line-continuation inside parentheses with a 3-space hanging indent (1031-1032), `gini_coefficients =[]` (1119) and a 5-space indent (1121).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 766, 945, 960, 975, 1023. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 322, 323, 324, 325, 500, 636, 876, 878, 880, 982, …. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 715. *Example:* H3 Title Case: 'Gini Coefficient and GDP per capita (over time)' (Coefficient).

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 482, 1118. *Example:* %%time.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 504. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 666, 692. *Example:* caption of 9 words.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 578, 1124. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 152, 210. *Example:* 149-154 says the same thing twice - "First let us construct a `lorenz_curve` function that we can use in our simulations below" followed by "It is useful to construct a function that translates an array of income or wealth data into the cumulative share of individuals (or households) and the cumulative share of income (or wealth)" (32 words, restating the docstring at 158-163); 210-212 is a 35-word sentence carrying both the interpretation of the axes and the reading of the dashed lines.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 246, 426, 533. *Example:* mid-sentence 'Consumer'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 100, 343, 795. *Example:* the lecture contains no bold and no italic at all, so the three terms it exists to define - the Lorenz curve (100, formalised at 107), the Gini coefficient (343, formalised at 353) and top shares (795, formalised at 804) - are introduced in plain text; the `prf:definition` blocks hold only the formula, not the term.

### Low severity
- **[qe-math-012 (proposed)]** — Multiplication via \cdot or juxtaposition, never *. *Count:* 1. *Lines:* 31. *Example:* * as multiplication.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 118. *Example:* 2 spaces.


## Strengths

- Definitions are placed in `prf:definition` blocks with labels (`define-lorenz`, `define-gini`, `top-shares`) and the equation label `topshares` is genuinely cited later, in exercise 2 at line 997.
- Nearly every generated figure carries `mystnb: figure: caption/name` metadata and is referenced with `{numref}` in the prose that follows (368, 400, 567, 602).
- The plotly figure at 766 is paired with an `{only} latex` fallback at 779 that points LaTeX readers at the web version - a genuinely thoughtful accessibility touch.
- Greek variables in code use Unicode (`σ_vals`, `μ`) in the simulation cells, matching the mathematical notation in the surrounding prose.
- All three exercises use gated `exercise` / `solution-start` / `solution-end` with `:class: dropdown`, and exercise 3 cross-references the in-lecture code block by label (`code:gini-coefficient`).

## Recommended actions

1. Add `mystnb: figure: caption/name` metadata to the five figures that only have an `image: alt:` key (766, 945, 960, 975, 1023) so they can be captioned and cross-referenced like the rest.
2. Move the three embedded matplotlib titles out of the code (504 via the `title=` argument of `plot_inequality_measures`, 985, 1037) and into figure captions.
3. Bold each term at its point of definition - the Lorenz curve, the Gini coefficient, top shares - and reserve italic for emphasis; the lecture currently uses neither.
4. Run the code cells through a PEP8 formatter to fix the 16 spacing items listed above, and replace the remaining spelled-out Greek names at 230, 231, 383, 413, 414 with Unicode letters.
5. Give the two identically-captioned Norway figures (666, 692) distinct captions - the second one is the forward-filled version - and shorten them to under eight words.
6. Lower-case the H3 at 715 to `### Gini coefficient and GDP per capita (over time)`.
7. Split the two-sentence paragraphs at 578 and 1124, cut the redundant lead-in at 152, and escape the currency signs at 31, 33 and 35 (`\$100,000,000`, `\$100`) - as written the unescaped `$` pairs open a math span that swallows the bullet list.
