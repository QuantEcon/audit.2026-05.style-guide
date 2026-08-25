# pandas_panel

- **Series:** lecture-python-programming
- **File:** `lectures/pandas_panel.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×4; `qe-writing-005` ×3; `qe-writing-003` ×2, +3 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-006` ×5; `qe-fig-005` ×8; `qe-fig-003` ×4, +2 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 38, 246, 372, 393, 412, 422, 476, 612. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 5. *Lines:* 379, 397, 416, 427, 617. *Example:* axis label `Country`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 72, 187, 352, 488. *Example:* H2 Title Case: 'Slicing and Reshaping Data' (Reshaping, Data).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 531, 532, 580, 619. *Example:* missing spaces after commas in `columns=['UNIT','AGE', 'SEX', ...]` at 531 (inconsistent within the same list), `swaplevel(0,-1)` at 580 and `bbox_to_anchor=(1,0.5)` at 619 (E231); and one space before the inline comment at 532 where PEP8 wants two (E262).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 395, 414, 425, 482. *Example:* plt.title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 512. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 173, 242, 470. *Example:* 173 reads "For the rest of lecture"; 240-242 drops the preposition - "countries in `worlddata` that do not have a corresponding data entry `realwage_f`"; and 469-471 is a 30-word sentence that also states the wrong year, promising "real minimum wages in 2016" where the code at 480 selects `.loc['2015']` and the plot title at 482 says 2015.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 420, 438. *Example:* "This is a simplified way to use `groupby`." (438) sits directly after the `.describe()` example at 431-436 and refers to the `groupby(level='Continent')` call 30 lines earlier at 407, so as placed it tells the reader that `.describe()` is a simplified `groupby`; and 420-423 drops Australia from `merged` in place "for plotting purposes", after which every later cell - `.describe()` (435), `grouped` (453), `grouped.size()` (466) and the kernel densities (480) - silently excludes it, without the text noting that the summary statistics have changed.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 101, 124, 440. *Example:* the file contains no bold and no italic anywhere, so its three defined terms are carried by plain text or code spans - long format versus wide format (101-103), "multiple levels of indexing, known as a `MultiIndex`" (123-124) and the 'split-apply-combine' process (440) - and quotation marks do the work bold should be doing at 56 ('panel' and 'data'), 209 ('Country') and 253-256 ('left', 'right').

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 41. *Example:* style override.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 246. *Example:* static image .png.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 148. *Example:* "Slicing and Reshaping Data" (72-185) is the section that most needs a picture and has none: `.stack()` is described as rotating "the lowest level of the column `MultiIndex` to the row index" with `.unstack()` left as "try it out" (148-150), and `xs` on a three-level index follows at 182-183. A before/after schematic of one stack and one unstack would settle in one figure what 40 lines of prose and output tables attempt - and the lecture proves it knows this, because the join semantics do get the Venn diagram at 246.


## Strengths

- The Venn diagram at 246 is the right visual in the right place: the four join types are listed (233-236) and then the one the lecture uses is shown shaded.
- The `MultiIndex` is built rather than handed over - long format shown first (97-99), then `pivot_table` with a list of columns (110-113), then the level names printed (135) so the hierarchy is visible before it is used.
- The three missing continents are found by filtering on `.isnull()` (271-273) rather than asserted, then fixed with a dictionary and `.fillna`, with an explanation of why `.map` alone would overwrite the column (293-299).
- 'split-apply-combine' is named and decomposed (440-447) before `groupby` is used in earnest, and `grouped.size()` (466) shows what the intermediate `DataFrameGroupBy` object actually holds.
- The lecture states its three deliverables at 59-63 and delivers exactly those three - summary statistics, the average-wage time series, and the by-continent kernel densities.

## Recommended actions

1. Lowercase the five axis labels (379, 397, 416, 427, 617) and move the four matplotlib titles (395, 414, 425, 482) into figure captions (qe-fig-006 ×5, qe-fig-003 ×4).
2. Add `:name:` and captions to the eight figures (38, 246, 372, 393, 412, 422, 476, 612) and regenerate `venn_diag.png` (246) from code.
3. Sentence-case the four headings (72, 187, 352, 488).
4. Add a before/after schematic for `.stack()` and `.unstack()` (145-171) - the operation the section is named for is currently described in words and left as an exercise for the reader.
5. Move "This is a simplified way to use `groupby`." (438) back to the example at 407 it describes.
6. Reconsider dropping Australia in place at 423, or say in the text that everything downstream - including `.describe()` at 435 and the kernel densities at 480 - now excludes it.
7. Fix 470 (2016 where the code and title say 2015), 173, and the missing preposition at 242; settle `DateTimeIndex` (116) against `DatetimeIndex` (163, 328, 336, 344); bold the three definitions at 101-103, 124 and 440.
