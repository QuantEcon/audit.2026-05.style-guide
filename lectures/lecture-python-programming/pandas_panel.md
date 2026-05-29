# pandas_panel

- **Series:** lecture-python-programming
- **File:** `lectures/pandas_panel.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10| Five H2 section headings use Title Case; otherwise clean. |
| Math         | N/A   | No math content. |
| Code         | 8/10  | `!pip install --upgrade seaborn` at top with `hide-output` (qe-code-003); PEP8 clean; no Greek identifiers; no benchmarking magics. |
| JAX          | out of scope | — |
| Figures      | 3/10  | Five `plt.title(...)` calls outside any exercise/solution context (lines 395, 414, 425, 482, 618) — repeated qe-fig-003 violation. One static `{figure}` (line 246, Venn diagram) lacks `name:`. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`earlier lecture on pandas <pandas>` `` correctly per qe-link-001. |
| Admonitions  | 9/10  | Two `{exercise-start}` / `{solution-start}` pairs gated; `:class: dropdown` and `:label:` correct per qe-admon-001/qe-admon-002/qe-admon-005; one `{hint}` admonition; one `{note}` admonition. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — Five `plt.title(...)` calls embed titles in matplotlib figures outside exercise/solution context. *Examples:* line 395 `plt.title('Average real minimum wage 2006 - 2016')`, line 414 `plt.title('Average real minimum wage')`, line 425 `plt.title('Average real minimum wage')`, line 482 `plt.title('Real minimum wages in 2015')`, line 618 `plt.title('Employment in Europe (2015)')` (inside solution — exempt). Of these, four are in main-body code cells and are clear violations; line 618 is inside a solution and exempt per qe-fig-003. *Count:* 4 clear violations.

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 72 `## Slicing and Reshaping Data`, line 187 `## Merging Dataframes and Filling NaNs`, line 352 `## Grouping and Summarizing Data`, line 488 `## Final Remarks`, line 497 `## Exercises`. *Count:* 5 occurrences.

### Low severity
- **[qe-fig-005]** — The static `{figure}` at line 246 (Venn diagram) and the embedded `plt.*` plots lack `name:` metadata.
- **[qe-fig-006]** — `plt.xlabel('Country')`, `plt.xlabel('Year')`, `plt.ylabel('2015 USD')`, `plt.ylabel('Percentage of population (%)')` use Title Case (lines 379, 397, 396, 617). "Country" / "Year" should be lowercase per qe-fig-006; "USD" is a proper-noun acronym (acceptable).

## Strengths
- Lecture title uses `{index}` role with Title Case per qe-writing-006.
- One-sentence paragraphs and clean lists.
- Non-Anaconda `seaborn` correctly installed at top with `hide-output` per qe-code-003.
- Good use of `{doc}` cross-references per qe-link-001.
- Exercise/solution pairs use full gated/dropdown/label compliance.

## Recommended actions
1. Remove the four `plt.title(...)` calls in main-body code-cells (lines 395, 414, 425, 482) and migrate to figure-directive captions.
2. Convert H2 headings to sentence case ("Slicing and reshaping data", "Merging dataframes and filling NaNs", "Grouping and summarizing data", "Final remarks").
3. Lowercase `plt.xlabel('country')`, `plt.xlabel('year')`, `plt.ylabel('percentage of population (%)')`.
4. Add `name:` to the Venn-diagram figure (line 246).
