# french_rev

- **Series:** lecture-python-intro
- **File:** `lectures/french_rev.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×5; `qe-writing-001` ×2; `qe-writing-005` ×4, +5 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-007` ×30; `qe-fig-004` ×19; `qe-fig-006` ×6, +3 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 103, 108, 229, 267, 433, 469, 515, 578, 647. *Example:* nine `pd.read_excel(` calls open with an argument on the first line and then indent the continuation to an arbitrary column - 8 spaces at 104-105 and 109-110, 12 at 230 and 232, 10 at 268, 20 at 434, 8 at 470, 9 at 516, 10 at 579-581, 8 at 648-650 - none of which matches the visual indent of the opening parenthesis; the call at 152-153 in the same lecture is aligned correctly, so the fix is already demonstrated in the file.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 19. *Lines:* 95, 144, 221, 273, 425, 461, 507, 570, 639, 733, …. *Example:* Title Case caption (Spending).
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 6. *Lines:* 124, 1049, 1050, 1134, 1214, 1215. *Example:* axis label `Millions of livres`.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 30. *Lines:* 119, 120, 164, 165, 249, 250, 295, 296, 440, 441, …. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 28. *Lines:* 244, 585, 586, 745, 749, 752, 800, 803, 806, 831, …. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 39, 313, 340, 405, 981. *Example:* `` {cite} `` in narrative flow: '     `` {cite} ``'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 57, 80, 342, 979, 990. *Example:* H2 Title Case: 'Data Sources' (Sources).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 89. *Lines:* 19, 22, 24, 30, 32, 34, 36, 43, 45, 47, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 70, 1039, 1194. *Example:* style override.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 1033, 1125, 1193. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 142, 615. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 30, 36, 563, 763. *Example:* the Overview's theory list opens with a 70-word single sentence at line 30 (the whole tax-smoothing prescription, war-time debt, roll-over and post-war taxes, chained with semicolons) and a 46-word sentence at 36 (the real-bills theory plus its backing mechanism); line 563 "These led to outcomes that vary over time and that illustrate the playing out in practice of theories that guided the Revolutionaries' monetary policy decisions" says almost nothing in 24 words; and 763-768 repeats 683-689 verbatim - the same two sentences about the three clouds of points, 80 lines apart.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 683, 409, 976. *Example:* lines 683-689 interpret `{numref}`fr_fig104`` 50 lines before the cell that creates it at 733-738, and then the identical paragraph reappears at 763 in its right place - so the reader meets the conclusion before the evidence and again after it; line 409 restarts the narrative with "In 1789 the French Revolutionaries formed a National Assembly and set out to remake French fiscal policy", which is where line 344 already started; and line 976 attributes the reversed regression to `fr_fig104e`, the figure discussed at 942, instead of `fr_fig104f` directly above it.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 366. *Example:* mid-sentence 'Wealth'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 36, 366, 368, 417. *Example:* the six theories listed in the Overview are bolded - **tax-smoothing** (28), **unpleasant monetarist arithmetic** (32), **gold** / **silver standard** (43), **inflation-tax** (47), **legal restrictions** / **financial repression** (51) - but *real bills* at 36 is italicised instead; **The Wealth of Nations** at 366 is bold for a book title, where italic is wanted; and the two explicit definitions are italic where bold is wanted, "Adam Smith defined a *real bill* as a paper money note that is backed by..." at 368 and "*tax farming*" at 417, defined on the line below.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 979. *Example:* the "Hyperinflation Ends" section (979-988) asserts that the government "abruptly ended the inflation" in 1797 and lists the four measures, with no figure - in a lecture where every other empirical claim is a plotted series, and where the price-level series in fr_fig9 stops at mid-1796, just short of the stabilisation the section is about.


## Strengths

- Twelve of the thirteen figures carry `mystnb: figure:` metadata with a stable `name`, and the prose then cites them by `{numref}` rather than "the figure above" - fr_fig4 at 137 and 140, fr_fig2 at 180, 185, 191, 201, 210, fr_fig1 at 259, fr_fig3 at 304, fr_fig5 at 451, fr_fig11 at 502, fr_fig24 at 539, fr_fig9 and fr_fig8 at 609.
- The three monetary regimes are each assigned a named theory at 623-625 and then each theory is tested against its own regression - real bills at 850, legal restrictions at 895, Cagan hyperinflation at 942 - so the historical narrative and the empirical section answer each other item by item.
- The `{note}` at 627-633 states Cagan's operational definition of hyperinflation (50 percent per month, ending a year clear of it) and dates the assignat episode by it, so the word carries a criterion rather than rhetoric.
- Data provenance is fully traceable: the three source spreadsheets are linked at 59-62 and every `pd.read_excel` names its sheet, its column range and its row offsets, so each figure can be tied back to specific cells.
- The three exercises go beyond replication - fr_ex1 tests the lecture's own 1795 hyperinflation dating against Cagan's threshold, fr_ex2 re-estimates $\alpha$ log-linearly and compares it with the value used in `cagan_ree`, and fr_ex3 asks the reader to collapse the five scatter plots into one figure.

## Recommended actions

1. Collapse the six near-identical scatter figures - fr_fig104, fr_fig104b, fr_fig104c, fr_fig104d, fr_fig104e, fr_fig104f at 733, 788, 819, 864, 911, 945 - into one or two. They plot the same three clouds and differ only in which regression line is drawn, and all six carry the identical caption "Inflation and Real Balances"; the lecture's own exercise fr_ex3 (1159-1220) already shows the consolidated version.
2. Squash the 89 runs of two and three spaces in the prose; they are spread over the whole file but densest at 19-55 and 130-220 (qe-writing-008 x89).
3. Lower-case the five Title Case section headings - "Data Sources" (57), "Government Expenditures and Taxes Collected" (80), "Nationalization, Privatization, Debt Reduction" (342), "Hyperinflation Ends" (979), "Underlying Theories" (990) - and the 19 Title Case figure captions, plus the 6 capitalised axis labels at 124, 1049, 1050, 1134, 1214, 1215 (qe-writing-006 x5, qe-fig-004 x19, qe-fig-006 x6).
4. Remove the duplicated material: the regression cell at 776-786 is identical to 721-731, and the paragraph at 763-768 is identical to 683-689 - keep each once, in the position after the figure it describes. While there, fix the `{numref}` at 976 (it names fr_fig104e but discusses fr_fig104f), the sentence broken by a full stop at 137-138, and the empty list bullet at 626.
5. Break up the two long Overview bullets at 30 and 36, and restore the figure box on the 30 despined axes plus set an explicit `lw` on the 28 default-width line plots (qe-fig-007 x30, qe-fig-008 x28).
6. Fix the emphasis: italicise *The Wealth of Nations* at 366, bold **real bill** at 368 and **tax farming** at 417 where they are defined, and make **real bills** at 36 match the five bolded theory names around it.
7. Align the nine `pd.read_excel` continuation lines on the pattern already used at 152-153, drop the duplicate `import pandas as pd` at 1034 (pandas is imported at 66), and move the five `{cite}` calls at 39, 313, 340, 405 and 981 out of the middle of their sentences (qe-ref-001 x5).
