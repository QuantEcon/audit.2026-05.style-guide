# inflation_history

- **Series:** lecture-python-intro
- **File:** `lectures/inflation_history.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 sentence case (country names retained as proper nouns); one-sentence paragraphs. |
| Math         | N/A   | trivial price-level notation only |
| Code         | 8/10  | `!pip install` on lines 25, 37 — line 25 has `hide-output` (tagged on line 23) but line 37 is a stray mid-lecture install; standard Anaconda imports otherwise. |
| JAX          | out of scope | — |
| Figures      | 5/10  | `figsize=` on lines 110, 810, 890, 910; 4 `ax.set_title(...)` inside solution blocks (OK by exception); axis labels with leading capitals throughout ("Year", "Index 1913 = 100", "Logs of price levels...", "Price level", "Exchange rate", "Inflation rate"). |
| References   | 4/10  | 10 `{cite}` usages, **all in-text** (e.g. "on page 35 of {cite}", "from chapter 3 of {cite}") — all should be `{cite:t}`. |
| Links        | 8/10  | `{doc}` cross-series links used (5 occurrences). |
| Admonitions  | 9/10  | 7 admonitions (note/warning) used; 3 solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
- **[qe-ref-001]** — Multiple in-text citations using `{cite}` instead of `{cite:t}`. *Examples:* line 69 ("page 35 of {cite}\`sargent2002big\`"), 164 ("page 35 of {cite}\`sargent2002big\`"), 215 ("from chapter 3 of {cite}\`sargent2013rational\`"), 225, 227, 502, 565, 646, 668, 672. *Count:* 10 occurrences. **Systemic.**
- **[qe-fig-001]** — `figsize=` overrides on lines 110, 810, 890, 910. *Count:* 4 occurrences.
- **[qe-fig-006]** — Multiple axis labels begin with uppercase: "Year", "Index 1913 = 100" (lines 117, 189), "Logs of price levels...", "Price level", "Exchange rate", "Inflation rate". *Count:* 5+ occurrences.

### Medium severity
- **W1** — Some multi-sentence paragraphs (lines 138–143).
- **[qe-code-003]** — Stray `!pip install` on line 37 should be merged with the install block at line 25.

### Low severity
- **W2** — H1 has trailing whitespace "Price Level Histories ".
- **W7** — Mid-sentence capitalization for events ("Civil War", "French Revolution") — proper nouns, acceptable.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Section headings comply with W2/W3.
- Clean prose, one-sentence paragraphs mostly maintained.
- Bold for definition (**inflation**).
- `{doc}` cross-series links used (qe-link-002 OK).
- Solutions gated, dropdown, linked.

## Recommended actions
1. Convert all 10 in-text `{cite}` usages to `{cite:t}` — they all start with "page X of" or "chapter X of" etc.
2. Remove `figsize=` overrides on lines 110, 810, 890, 910.
3. Lowercase axis labels.
4. Merge the stray `!pip install` on line 37 into the install cell at the top.
5. Trim trailing whitespace in H1.
