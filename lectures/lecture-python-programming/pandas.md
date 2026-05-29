# pandas

- **Series:** lecture-python-programming
- **File:** `lectures/pandas.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Heading Title Case throughout the H3 layer. |
| Math         | N/A   | No math content. |
| Code         | 8/10  | `!pip install --upgrade wbgapi` and `!pip install --upgrade yfinance` at top with `hide-output` (qe-code-003); PEP8 clean; one `import yfinance` deferred to inside an exercise (line 637) — borderline qe-code-003 nit (used as a per-exercise import for clarity, not a runtime install). |
| JAX          | out of scope | — |
| Figures      | 7/10  | Two `figsize=(10,8)` (line 726), `figsize=(10, 8)` (line 797); one `ax.set_title(index_name)` (line 803) is inside `solution-start`/`solution-end` per qe-fig-003 exception; two static `{image}` for example plot screenshots (lines 685, 752) used inside exercises per qe-fig-011; one static `{figure}` (line 46) for pandas-popularity screenshot (qe-fig-002 acceptable for SO trends). |
| References   | N/A   | No citations. |
| Links        | 8/10  | Uses external doc links for `wbgapi`, `yfinance`, FRED — appropriate; no improper cross-series URLs. The `[QuantEcon.py](https://github.com/...)` etc. are external repos, not lectures — not a violation. |
| Admonitions  | 9/10  | Two `{exercise-start}` / `{solution-start}` pairs gated; `:class: dropdown` on solutions; `:label:` cross-linked; `{note}` admonition used. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 144 `## DataFrames`, line 181 `### Select Data by Position`, line 209 `### Select Data by Conditions`, line 294 `### Apply Method`, line 347 `### Make Changes in DataFrames`, line 427 `### Standardization and Visualization`, line 495 `## On-Line Data Sources`, line 514 `### Accessing Data with requests`, line 593 `### Using wbgapi and yfinance to Access Data`, line 627 `## Exercises`. *Count:* 10 occurrences.

### Medium severity
- **[qe-fig-001]** — Two explicit `figsize=(10, 8)` in code-cells inside solution blocks (lines 726, 797). Inside `solution-start`/`solution-end` qe-fig-003 has an exception but qe-fig-001 does not — these are weak style nits.
- **[qe-fig-005]** — Code-generated plots (e.g., bar plots at lines 473, 489, 583) lack `name:` metadata.

### Low severity
- **[qe-writing-004]** — "On-Line" capitalized at line 495 — modern usage prefers "online".
- **[qe-code-003]** — `import yfinance as yf` placed inside an exercise body (line 637); pedagogically motivated (only needed for that exercise) but the install at the top makes it available globally.

## Strengths
- Lecture title "Pandas" follows qe-writing-006.
- Some headings already use sentence case (e.g., "Series").
- Clean code-cell usage, inline backtick code, one-sentence paragraphs.
- Non-Anaconda `wbgapi` and `yfinance` correctly installed at top with `hide-output` per qe-code-003.
- All axis labels are lowercase or use proper-noun acronyms (e.g., 'GDP per capita', '%') per qe-fig-006.
- The one `ax.set_title(...)` use is inside `solution-start`/`solution-end` so qualifies for the qe-fig-003 exception.
- Exercise/solution pairs use gated syntax per qe-admon-001 with `:class: dropdown` per qe-admon-002 and `:label:` per qe-admon-005.

## Recommended actions
1. Convert section headings to sentence case ("DataFrames", "Select data by position", "Select data by conditions", "Apply method", "Make changes in DataFrames", "Standardization and visualization", "Online data sources", "Accessing data with `requests`", "Using `wbgapi` and `yfinance` to access data").
2. Drop the `figsize=` overrides in the solution blocks unless visually necessary.
3. Add `name:` metadata to a few representative code-generated bar plots.
