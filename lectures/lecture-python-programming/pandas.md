# pandas

- **Series:** lecture-python-programming
- **File:** `lectures/pandas.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×8; `qe-writing-002` ×5; `qe-writing-004` ×2, +3 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 7/10  | `qe-code-001` ×12. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×8; `qe-fig-002` ×3; `qe-fig-001` ×2, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 12. *Lines:* 329, 330, 371, 384, 408, 420, 620, 625, 675, 704, …. *Example:* `complexCondition` (329, used at 339 and 345) is camelCase with no mathematical justification; trailing whitespace at 330 and 675 (W291); `row.POP<= 10000` missing a space before the operator at 371 (E225); `lambda x : round(x,2)` with a space before the colon and none after the comma at 384 (E203/E231); a double space after `return` at 408 (E271); `df.iloc[:,2:8]` at 420 and `economy=['USA','AUS'], time=range(2005,2016)` at 620 missing spaces after commas (E231); a trailing semicolon at 625 (E703); `#Get the first set of prices` with no space after the hash at 704, 705 and 770 (E265); `figsize=(10,8)` at 727 (E231); and `fontsize = 12` at 803 (E251) two lines after 728-729 write `fontsize=12` correctly.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 46, 473, 489, 583, 624, 686, 726, 753. *Example:* {figure} without :name:.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 184, 230, 334, 430, 592. *Example:* 430-432 repeats 278-280 word for word - "Let's imagine that we're only interested in the population (`POP`) and total GDP (`tcgdp`). One way to strip the data frame `df` down to only these variables..." - 150 lines apart; "of our interests" appears twice as a noun phrase (184, 212); "Take one more example," (230); "returns a series of boolean values rows that satisfies the condition" (334); and "methods that we can use to read, excel, json, parquet or plug straight into a database server" (592).
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 182, 210, 295, 348, 428, 496, 515, 594. *Example:* H3 Title Case: 'Select Data by Position' (Data, Position).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 727, 798. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 46, 686, 753. *Example:* static image .png.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 329, 428. *Example:* the `complexCondition` cell at 329-332 assigns a two-element tuple, not a boolean series - the trailing `, ['country', 'year', ...]` sits outside the `df.apply(...)` call - and 334-336 then describes that as something `df.apply()` returned ("In addition, it also defines a subset of variables of interest"); `df.loc[complexCondition]` at 345 happens to work because `.loc` accepts a (rows, columns) tuple, which is not what the text says is happening. And "Standardization and Visualization" (428) does no standardizing, reopens with the duplicated paragraph at 430-432, and operates on the `df` already mutated by the imputation section above (395, 420), so the plotted numbers are the imputed ones without comment.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 86, 387. *Example:* mid-sentence 'Series'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 272, 353, 387. *Example:* bold is used for structure rather than for definitions throughout: "**Application: Subsetting Dataframe**" (272) and "**Application: Missing Value Imputation**" (387) are section headings written as bold paragraphs, and "**1.**" through "**4.**" (353, 359, 366, 380) are bold numerals standing in for an ordered list; meanwhile `Series` and `DataFrame` (75-79), the two types the lecture is about, are introduced with no bold at all.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 802. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 75. *Example:* 2 spaces.


## Strengths

- Selection is taught in the order a user needs it - by position (182-208), by condition (210-270) - and the `query` alternative is shown as a labelled equivalent to each `[]` form (239, 254) rather than as a separate topic.
- The `.loc[condition, columns]` form is explained argument by argument (264-266) instead of being left to be inferred from the example that follows.
- The FRED section works upward from the raw HTTP response (524-554) to `pd.read_csv(url, parse_dates=True)` (562-563), so the reader sees what `read_csv` is saving them from.
- Both exercises show the target figure before asking for it (686, 753), and the second reuses `read_data` from the first, which is how a reader would actually work.
- The `{note}` at 319-324 puts the `axis=0`/`axis=1` convention - the thing everyone forgets - in a callout rather than in running prose, and gives the default.

## Recommended actions

1. Sentence-case the eight headings (182, 210, 295, 348, 428, 496, 515, 594) and lowercase "Series" mid-sentence at 86 and 387 (qe-writing-004).
2. Rewrite the `complexCondition` cell (329-332) so the code and the prose agree - as written it builds a tuple, and 334-336 describes something else.
3. Delete the duplicated paragraph at 430-432 and either rename "Standardization and Visualization" or add the standardization it promises.
4. Add `:name:` and captions to the eight figures (46, 473, 489, 583, 624, 686, 726, 753) and regenerate the three static PNGs (46, 686, 753) from code.
5. Run the code cells through pycodestyle - `complexCondition` to snake_case (329), 371, 384, 408, 420, 620, 625, 704-705, 727, 770, 803 and the trailing whitespace at 330 and 675.
6. Fix the broken sentences at 230, 334 and 592, and replace "of our interests" (184, 212).
7. Replace the bold pseudo-headings at 272 and 387 with real headings and the bold numerals at 353-380 with an ordered list; extract the 600-character FRED URL to one variable instead of pasting it twice (525, 543).
