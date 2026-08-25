# inflation_history

- **Series:** lecture-python-intro
- **File:** `lectures/inflation_history.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-001` ×5; `qe-writing-002` ×7; `qe-writing-004` ×2, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 6/10  | `qe-code-001` ×8; `qe-code-003` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-006` ×9; `qe-fig-004` ×9; `qe-fig-005` ×4, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 238, 271, 280, 284, 721, 724, 728, 789. *Example:* `if type(entry) == str` instead of `isinstance(entry, str)` (238); backslash line-continuations where the enclosing parentheses already allow implicit continuation (271, 280, 284); and alignment padding that PEP8 rules out - extra spaces after the dict colons at 721 and 789 and two spaces before `=` at 724 and 728.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 9. *Lines:* 98, 174, 412, 432, 460, 480, 506, 549, 591. *Example:* caption of 8 words.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 117, 118, 189, 323, 324, 339, 743, 817, 894. *Example:* axis label `Index  1913 = 100`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 5. *Lines:* 79, 227, 502, 661, 765. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 7. *Lines:* 76, 162, 164, 207, 401, 666, 932. *Example:* seven sentences of 34-57 words, each carrying two or more ideas: 76 (39w, definition of hard currency plus the mechanics of coin valuation), 162 (35w), 164 (39w, announces a figure, names the historical turning point and cites the source in one breath), 207 (42w), 401 (34w), 666 (57w, four countries' stabilisation ratios in a single sentence - a table would carry this better), 932 (37w).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 76, 153, 502, 668, 765. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 2. *Lines:* 22, 30. *Example:* non-Anaconda import with no install cell: ['packaging'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 110, 810, 890, 910. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 538, 701, 786, 871. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 69, 646, 668, 672. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 164, 454. *Example:* 164-174 announces {numref}`lrpl_lg`, then describes what it shows (166), then interrupts with a note about logarithms (168) and an unrelated sentence about 1914 (172) before the figure finally appears at 174; and line 452 promises "We'll see similar patterns in the next three episodes that we'll study now", but the Hungary, Poland and Germany sections (454-630) contain six figures and not one sentence of interpretation - the reader gets no commentary again until 632.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 502. *Example:* mid-sentence 'Price'.

### Low severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 153. *Example:* "issuing **limited supplies** of paper currency" - bold used for emphasis inside a bullet, where the rule reserves bold for definitions and italic for emphasis; contrast line 49, where **inflation** is correctly bolded as a definition.


## Strengths

- The two plotting helpers `pe_plot` and `pr_plot` (297-351) are defined once and reused across all four country sections, so the eight country figures are guaranteed to share axes, log scaling and date formatting.
- Every figure that has a caption also has a `name`, and the prose actually cites them with `{numref}` (126, 166, 197, 446).
- Data provenance is unusually careful: each country section names the source table and page from {cite}`sargent2013rational`, and the note at 501 documents exactly how the three Polish price series were spliced.
- `{note}` and `{tip}` admonitions are used well to park side material (the warehouse-certificate aside at 78, the treasury-bill aside at 660, the PPP pointer at 640) instead of interrupting the narrative.
- The three exercises added at 678-937 are genuine quantitative follow-ups on the lecture's own claims, each with a gated dropdown solution that re-uses the lecture's dataframes.

## Recommended actions

1. Fix the left/right mix-up at line 401: `pe_plot` puts the price level on the left axis (`ax`, ylabel at 323) and the exchange rate on the right (`ax1 = ax.twinx()`, ylabel at 324), which is the reverse of what the prose tells the reader to look at.
2. Fix the formula at line 403: the prose defines the plotted series as $(p_{t-1} + p_t + p_{t+1})/3$, but `pr_plot` (334-338) computes a three-period rolling mean of $\Delta \log p_t$; write the moving average of the log-difference.
3. Lower-case the nine axis labels ('Index  1913 = 100', 'Year', 'Price level', 'Exchange rate', 'Inflation rate', and the four in the exercise solutions) and shorten the nine over-long figure captions.
4. Add `mystnb: figure: caption/name` metadata to the four un-named figures (538, 701, 786, 871) - the Poland price/exchange-rate figure at 538 is the only one of the eight country figures that cannot be cross-referenced.
5. Convert the four narrative-position citations to `{cite:t}` (69, 646, 668, 672) - "Chapter 3 of {cite:t}`sargent2002big`" rather than `{cite}`.
6. Break the seven over-long sentences listed above, split the five multi-sentence paragraphs (79, 227, 502, 661, 765) and strip the six runs of double spaces.
7. Add a paragraph of interpretation to each of the Hungary, Poland and Germany sections, in the manner of the Austria discussion at 446-450, and italicise the emphasis at 153.
