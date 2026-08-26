# pandas_panel

- **Series:** lecture-python.myst
- **File:** `lectures/pandas_panel.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×4; `qe-writing-005` ×3; `qe-writing-003` ×4, +3 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-006` ×5; `qe-fig-005` ×8; `qe-fig-003` ×4, +2 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 302, 365, 375, 528, 610, 620. *Example:* 302-304 loops over continent names in a variable called `country`: `replace = ['Central America', 'North America', 'South America']` then `for country in replace:` - the name says country, the values are continents, and the list is named after the method being called on it. The whole loop is one call, `merged.Continent.replace(replace, 'America')`, and its continuation at 304 is indented to column 36 under an opening delimiter at column 48. `matplotlib.pyplot` and `seaborn` are imported at 365-366, three hundred lines after `pandas` at 72 and immediately before their first use, so the file has module-level imports in two places rather than one cell at the top. 371 and 375 both compute `merged.mean().sort_values(ascending=False)`, and 375 runs to 103 characters. Comma spacing is inconsistent within single lines - `columns=['UNIT','AGE', 'SEX', 'INDIC_EM', 'GEO']` at 527 has the space after four of five commas, `swaplevel(0,-1)` at 576, `bbox_to_anchor=(1,0.5)` at 615 - and 528 leaves one space before an inline comment where PEP8 asks for two. 610 writes `palette=("husl")`, which is a parenthesised string rather than the tuple the parentheses suggest, and plots `y=0`, naming the value column by the integer label `reset_index()` happened to give it. And the file's last line, 620, is a closing fence with a leading space, ` ``` `.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 234, 364, 370, 391, 408, 418, 472, 608. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 5. *Lines:* 377, 395, 412, 423, 613. *Example:* axis label `Country`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 60, 175, 344, 484. *Example:* H2 Title Case: 'Slicing and Reshaping Data' (Reshaping, Data).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 393, 410, 421, 478. *Example:* plt.title.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 34. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 508. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 104, 161, 228. *Example:* 104 misspells a pandas class and misplaces a comma in the same sentence: "To more easily filter our time series data, later on, we will convert the index into a `DateTimeIndex`" - the class is `DatetimeIndex`, which is how the lecture spells it correctly at 151, 320, 328 and 336, and the parenthetical commas around "later on" detach it from the clause it modifies. 161 reads "For the rest of lecture", dropping the article. And 228-230 loses a preposition in the sentence that explains the join the whole section turns on: "Here we will pass `how='left'` to keep all countries in `realwage_f`, but discard countries in `worlddata` that do not have a corresponding data entry `realwage_f`" - it should be "entry in `realwage_f`".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 416, 434, 465, 553. *Example:* 419 does more than the prose says. 416 announces "We will drop Australia as a continent for plotting purposes", but `merged = merged.drop('Australia', level='Continent', axis=1)` rebinds `merged` for the rest of the lecture, so every later cell silently excludes Australia: the `.describe()` at 431, the `grouped` object at 449, and `grouped.size()` at 462 - which 456-457 introduces as "the number of countries in our dataset for each continent", and it is no longer the dataset - and the closing kernel-density figure at 472-481, which 51 promised as "kernel density estimates of wages by continent". Second, 465-467 says the density estimate is "of real minimum wages in 2016", while the code at 476 selects `.loc['2015']` and the title at 478 says 2015. Third, 434 ("This is a simplified way to use `groupby`") sits directly under the `.describe()` cell at 430-432, so "This" reads as `.describe()`, which is not a use of `groupby` at all; the intended antecedent is the `merged.T.groupby(...)` calls twenty lines earlier at 403 and 409. Fourth, the second exercise describes its own filter three incompatible ways: 553-554 asks for "employment as a percentage of 'active population'", 592-593 says "percentage employed in the active population", and 596-598 selects `UNIT='Percentage of total population'` with `INDIC_EM='Active population'` - which is the active population as a percentage of the *total* population, the reciprocal framing - and the figure is then titled "Employment in Europe (2015)" at 614.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 89, 91, 436. *Example:* there is not one bold or italic span in the file, and three terms are introduced that the rule would put in bold. 89 introduces "long format" ("The data is currently in long format, which is difficult to analyze when there are several dimensions to the data") and 91 its counterpart "wide format", and these two are the axis the entire first half of the lecture turns on. 436 introduces the `groupby` idiom with single quotes - "Using `groupby` generally follows a 'split-apply-combine' process" - and then defines each of the three steps in the list at 438-440, so it is a definition being marked as a quotation. The same single-quote-for-a-term habit appears at 44 ('panel' and 'data'), 197 ('Country'), 242-246 ('left' / 'right' dataframe) and 240 ('on').
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 232, 408, 472. *Example:* the figures at 408-414 and 418-425 are the same four lines of code and carry the *identical* title, `plt.title('Average real minimum wage')` at 410 and 421, differing only in whether Australia is in the frame - so two adjacent figures are indistinguishable on the page and the one sentence between them (416) is all that tells them apart. The Venn diagram at 234 is a static PNG with an empty `{figure}` body, introduced by "This is illustrated by the red shading in the following diagram" (232): the red region is the entire content of the figure, and nothing in the page text or a caption says which set it is, so a reader who cannot see the image gets nothing. And the kernel-density figure at 472-481 is the lecture's headline deliverable, promised at 51, yet it is the only figure with no interpretive sentence after it - 465-467 explains how it is built and the lecture then moves to "## Final Remarks", so the reader is shown four overlapping densities and told nothing about what they show.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 367. *Example:* style override.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 234. *Example:* static image .png.


## Strengths

- Every transformation is shown one step at a time with its own cell and its own `head()`, so the reader can see the frame change shape: long to wide by `pivot_table` (97-102), the index to datetime (106-109), the `MultiIndex` levels named and inspected (118-124), a top-level selection (129-131), `.stack()` with and without an explicit level (140-149), a year selected and the two lower levels stacked into a cross-section (157-159), and finally `.xs` down to the hourly 2015-dollar frame (169-173).
- The merge is set up by explaining the choice before making it: 218-224 lists all four join types in one four-item list, 226 says what `merge` does by default, 228-230 says which one is being used and why, and 238-246 then explains each of the two key arguments in terms of where the country name actually lives in each frame (`left_index=True` because it is the index on the left, `right_on='Country'` because it is a column on the right).
- Missing data is handled as a teaching moment rather than swept away: 257-262 checks for it with `.isnull()`, 264 states the count out loud ("We have three missing values!"), 266-280 builds the repair dictionary and shows what `.map()` alone produces, and 282-285 then explains precisely why `.fillna()` is used instead of assignment - "only fills in `NaN` values ... while leaving other values in the column unchanged" - which is the mistake a reader would otherwise make.
- The `groupby` section is structured around the split-apply-combine idea and then walks the three steps in order: 436-443 names them and says which one `groupby` itself performs, 448-451 creates and displays the `DataFrameGroupBy` object without aggregating so the reader sees what it is, 453-463 applies `.size()` as the simplest possible aggregation, and 465-481 then applies a real one.
- Both exercises use data of a genuinely different shape from the body's - a five-level Eurostat `MultiIndex` (`UNIT`, `AGE`, `SEX`, `INDIC_EM`, `GEO`) - and the solutions teach transferable idioms: enumerating every level's values with a loop over `employ.columns.names` (541-544), promoting a level with `swaplevel` and re-sorting (575-578), and filtering out non-country `GEO` entries with a list comprehension on the level values (585-590).
- The lecture is honest about what it is not: 486-491 names what was covered and points at `xarray` for the N-dimensional case rather than implying pandas is the end of the road, and 34 links the prerequisite pandas lecture in the first sentence.
- Both exercises are gated with `{exercise-start}` / `{exercise-end}`, both solutions carry `:class: dropdown` (520, 569), the second exercise's `{hint}` is a dropdown with exactly the one fact needed (559-563, "`GEO` includes both areas and countries"), and all five admonition rules measure zero.

## Recommended actions

1. Scope the Australia drop to the figure that needs it - 419 rebinds `merged`, so `.describe()` (431), `grouped.size()` (462) and the closing density plot (476) all quietly exclude a continent that 456-457 and 51 tell the reader is in the dataset; plot from a local `merged.drop(...)` instead.
2. Fix 465-467 to say 2015, matching `.loc['2015']` at 476 and the title at 478; and rewrite the exercise-2 filter description so 553-554, 592-593 and the `UNIT` / `INDIC_EM` pair at 596-598 all describe the same quantity.
3. Give the two average-wage-by-continent figures (408-414, 418-425) distinct titles - "including Australia" and "excluding Australia" - and add a sentence after the density figure at 481 saying what the four curves show.
4. Replace the loop at 302-304 with the single `merged.Continent.replace(replace, 'America')` call it amounts to, and rename `country` (it holds continents) and `replace` (it holds the values to be replaced).
5. Move `matplotlib.pyplot` and `seaborn` (365-366) into one import cell with `pandas` near the top of the lecture, and bind `merged.mean().sort_values(ascending=False)` once instead of recomputing it at 371 and 375.
6. Bold the three terms the lecture defines - long format (89), wide format (91), split-apply-combine (436) - instead of leaving them plain or in single quotes.
7. Fix the accuracy items in the prose: `DateTimeIndex` at 104 (the class is `DatetimeIndex`), "For the rest of lecture" at 161, and the missing "in" at 230.
8. Sweep the mechanical items: the four Title-Case H2s (60, 175, 344, 484), the `{doc}` link for the cross-series pandas reference at 34, the four `plt.title` calls moved into `mystnb` captions (393, 410, 421, 478) along with the `title=` argument at 372, lower-case axis labels at 377, 395, 412, 423 and 613, `mystnb` caption/name metadata for the eight unnamed figures, a caption for the Venn diagram at 234, and the leading space on the closing fence at 620.
