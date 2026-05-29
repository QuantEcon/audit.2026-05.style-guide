# Style Audit — french_rev

- **Series:** lecture-python-intro
- **File:** `lectures/french_rev.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.0 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Many H2 sections in Title Case (W3); long multi-sentence bullets in Overview. |
| Math         | N/A   | minimal math notation |
| Code         | 7/10  | Standard Anaconda imports; spelled-out `alpha=` only as matplotlib kwarg (acceptable). |
| JAX          | out of scope | — |
| Figures      | 4/10  | Heavy `plt.gca().spines['top'/'right'].set_visible(False)` pattern (30 spine calls); 3 `ax.set_title` in solution blocks (OK by exception); `figsize=` on 1035, 1190; many axis labels with uppercase first letter (Date, Monthly inflation, Real balances). |
| References   | 5/10  | 20 `{cite}` usages; ~4+ are clearly in-text and should be `{cite:t}` (e.g. "described by", "assembled by", "appear in", "adopted by"). |
| Links        | 9/10  | `{doc}` links used (9 occurrences). |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
- **W3** — Several H2 section headings use Title Case. *Examples:* "## Data Sources" (57), "## Government Expenditures and Taxes Collected" (78), "## Hyperinflation Ends" (973), "## Underlying Theories" (984). *Count:* 4+ headings.
- **[qe-fig-007]** — `plt.gca().spines['top'/'right'].set_visible(False)` pattern repeated throughout. *Examples:* lines 117–118, 162, etc. *Count:* 30 spine-removal calls across multiple figures.
- **[qe-ref-001]** — Multiple in-text citations using `{cite}` instead of `{cite:t}`. *Examples:* line 19 ("described by {cite}\`sargent_velde1995\`"), 59 ("assembled by {cite}\`sargent_velde1995\`"), 84 ("appear in {cite}\`sargent_velde1995\`"), 626 ("adopted by {cite}\`Cagan\`"). *Count:* 4+ occurrences.

### Medium severity
- **W1** — Very long bullet items in Overview that contain multiple sentences (lines 28–53).
- **W7** — Random Title Case mid-prose: "The Twelve Members" (line 53), "Committee of Public Safety", "Napoleon Bonaparte" — some proper-noun OK; "Wealth of Nations" italicized OK.
- **W2** — H1 has trailing space.
- **[qe-fig-006]** — Multiple axis labels begin with uppercase. *Examples:* "Date" (line 1045), "Monthly inflation (log change)" (1046), "Monthly inflation rate $\\pi_t$" (1130), "Real balances (millions of livres)". *Count:* 5+ occurrences.

### Low severity
- **W7** — Typo "adminstered" (line 53), "wary" (line 30) probably "war".
- **[qe-fig-001]** — `figsize=` on lines 1035, 1190. *Count:* 2 occurrences.
- **[qe-fig-005]** — No figures use `{figure}` with `:name:`.

## Strengths
- H1 Title Case OK.
- Bold for definitions / key terms (**tax-smoothing**, **unpleasant monetarist arithmetic**, **assignats**, **gold**/**silver standard**, etc.).
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert all Title Case H2 headings to sentence case per qe-writing-006.
2. Remove the 30 `plt.gca().spines[...].set_visible(False)` calls per qe-fig-007.
3. Convert in-text `{cite}` usages to `{cite:t}` (lines 19, 59, 84, 626).
4. Lowercase axis labels (Date, Monthly inflation, Real balances).
5. Break long multi-sentence bullets into shorter ones.
6. Fix typos.
