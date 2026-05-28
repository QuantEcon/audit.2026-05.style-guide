# Style Audit — lecture-python-intro

- **Audit date:** 2026-05-27
- **Lectures audited:** 51
- **Average overall score:** 8.0 / 10
- **Average writing score:** 8.0 / 10
- **Average math score:** 7.8 / 10 (over 41 lectures containing math)

## Priority distribution

| Priority | Count | % |
|----------|-------|---|
| HIGH     | 1     | 2.0% |
| MEDIUM   | 9     | 17.6% |
| LOW      | 27    | 52.9% |
| NONE     | 14    | 27.5% |

## Top systemic issues across the series

1. **W1** — Multi-sentence paragraphs (style guide requires one-sentence paragraphs) — appears in 47 / 51 lectures. Most are isolated Low-severity occurrences but several lectures have systemic patterns in their Overview sections.
2. **W7** — Random / inconsistent capitalization and quoting (mid-sentence Title Case, double-prime `''...''` quotes, italic style mixing) — appears in 23 / 51 lectures.
3. **W3** — Title Case in H2/H3/H4 section headings where sentence case is required — appears in 19 / 51 lectures, with `money_inflation_nonlinear`, `complex_and_trig`, `geom_series`, `french_rev`, and `supply_demand_foundations_v2` being systemic offenders.

Other notable issues:
- **W2** (lecture title casing / trailing spaces) — 8 lectures.
- **M3** (`\mathbf{1}` instead of `\mathbb{1}` for ones vector / indicator) — 4 lectures (`networks`, `markov_chains_I`, `lln_clt`, `prob_dist`).
- **M2** (`^T` instead of `^\top` for transpose) — 3 lectures (`time_series_with_matrices`, `linear_equations`, `supply_demand_foundations_v2`).
- **M4** (`pmatrix`/`array` instead of `bmatrix`) — 2 lectures (`networks`, `time_series_with_matrices`).
- **M5** (bold for vector spaces, e.g. `{\bf R}^2`) — 2 lectures (`greek_square`, `lln_clt`).

## Lectures ranked by priority (lowest score first)

| # | Lecture | Writing | Math | Overall | Priority |
|---|---------|---------|------|---------|----------|
| 1 | supply_demand_foundations_v2 | 4 | 5 | 4.5 | HIGH |
| 2 | money_inflation_nonlinear | 5 | 6 | 5.5 | MEDIUM |
| 3 | time_series_with_matrices | 7 | 4 | 5.5 | MEDIUM |
| 4 | french_rev | 6 | N/A | 6.0 | MEDIUM |
| 5 | complex_and_trig | 6 | 7 | 6.5 | MEDIUM |
| 6 | geom_series | 6 | 7 | 6.5 | MEDIUM |
| 7 | networks | 8 | 5 | 6.5 | MEDIUM |
| 8 | simple_linear_regression | 6 | 7 | 6.5 | MEDIUM |
| 9 | unpleasant | 6 | 7 | 6.5 | MEDIUM |
| 10 | cagan_ree | 7 | 7 | 7.0 | LOW |
| 11 | greek_square | 8 | 6 | 7.0 | MEDIUM |
| 12 | laffer_adaptive | 7 | 8 | 7.5 | LOW |
| 13 | linear_equations | 8 | 7 | 7.5 | LOW |
| 14 | money_inflation | 7 | 8 | 7.5 | LOW |
| 15 | solow | 8 | 7 | 7.5 | LOW |
| 16 | tax_smooth | 7 | 8 | 7.5 | LOW |
| 17 | about | 8 | N/A | 8.0 | LOW |
| 18 | ar1_processes | 9 | 7 | 8.0 | LOW |
| 19 | cagan_adaptive | 8 | 8 | 8.0 | LOW |
| 20 | cons_smooth | 8 | 8 | 8.0 | LOW |
| 21 | equalizing_difference | 8 | 8 | 8.0 | LOW |
| 22 | inequality | 8 | 8 | 8.0 | LOW |
| 23 | markov_chains_I | 8 | 8 | 8.0 | LOW |
| 24 | schelling | 8 | N/A | 8.0 | LOW |
| 25 | business_cycle | 8 | N/A | 8.5 | LOW |
| 26 | commod_price | 9 | 8 | 8.5 | LOW |
| 27 | eigen_I | 8 | 9 | 8.5 | LOW |
| 28 | eigen_II | 9 | 8 | 8.5 | LOW |
| 29 | inflation_history | 8 | N/A | 8.5 | LOW |
| 30 | intro_supply_demand | 9 | 8 | 8.5 | LOW |
| 31 | lake_model | 8 | 9 | 8.5 | LOW |
| 32 | lln_clt | 9 | 8 | 8.5 | LOW |
| 33 | long_run_growth | 8 | N/A | 8.5 | LOW |
| 34 | lp_intro | 9 | 8 | 8.5 | LOW |
| 35 | monte_carlo | 9 | 8 | 8.5 | LOW |
| 36 | scalar_dynam | 8 | 9 | 8.5 | LOW |
| 37 | supply_demand_heterogeneity | 9 | 8 | 8.5 | LOW |
| 38 | cobweb | 9 | 9 | 9.0 | NONE |
| 39 | heavy_tails | 9 | 9 | 9.0 | NONE |
| 40 | input_output | 9 | 9 | 9.0 | NONE |
| 41 | markov_chains_II | 9 | 9 | 9.0 | NONE |
| 42 | mle | 9 | 9 | 9.0 | NONE |
| 43 | olg | 9 | 9 | 9.0 | NONE |
| 44 | prob_dist | 9 | 9 | 9.0 | NONE |
| 45 | pv | 9 | 9 | 9.0 | NONE |
| 46 | short_path | 9 | 9 | 9.0 | NONE |
| 47 | status | 9 | N/A | 9.0 | NONE |
| 48 | supply_demand_multiple_goods | 9 | 9 | 9.0 | NONE |
| 49 | troubleshooting | 9 | N/A | 9.0 | NONE |
| 50 | intro | 10 | N/A | 10.0 | NONE |
| 51 | zreferences | 10 | N/A | 10.0 | NONE |

## Series-level recommendations

1. **Fix `supply_demand_foundations_v2.md` (HIGH).** It is missing a proper Title Case H1 at the top of the file (the file begins with `## Elements of Supply and Demand` and the first H1 `# Multiple goods` appears 145 lines in, with lowercase 'goods'). Restructure the file so a single, Title Case H1 sits at the top; convert all Title Case H2 headings to sentence case; normalize transpose to `\top`; and fix typos ("compeitive", "simulataneous", "It we solve", "we'll can").

2. **Sweep Title Case section headings to sentence case across the series (W3).** Highest-impact targets: `money_inflation_nonlinear` (6+ headings), `complex_and_trig` (8+), `geom_series` (3+), `french_rev` (4+), `networks` (2 H3s), `supply_demand_foundations_v2` (6+). One pass with a global replace can fix these.

3. **One-sentence-paragraph pass on Overview sections (W1).** Almost every lecture has compound paragraphs in its Overview. A series-wide pass that splits any paragraph containing more than one sentence (especially in `cagan_ree`, `cons_smooth`, `cagan_adaptive`, `laffer_adaptive`, `money_inflation`, `unpleasant`) would significantly improve readability.

4. **Standardize matrix and operator notation (M2, M3, M4).** Replace `^T` → `^\top` in `linear_equations`, `time_series_with_matrices`, and `supply_demand_foundations_v2`. Replace `\mathbf{1}` → `\mathbb{1}` (with explanation) in `networks`, `markov_chains_I`, `lln_clt`. Replace `\begin{pmatrix}` / `\begin{array}` → `\begin{bmatrix}` in `networks` and `time_series_with_matrices`.

5. **Quote style (W7).** Replace TeX-style double-prime quotes `` ``...'' `` (and double-single `''...''`) with straight double quotes throughout — they appear in many monetarist/inflation lectures (`cagan_adaptive`, `laffer_adaptive`, `unpleasant`, `cons_smooth`, `equalizing_difference`, `scalar_dynam`).

6. **Trim trailing whitespace from H1s (W2).** Multiple lectures have a trailing space in their H1 (`laffer_adaptive`, `unpleasant`, `inflation_history`, `cobweb`, `french_rev`, `eigen_I`, `pv`, `markov_chains_I`).

7. **Treat data/history lectures as text-only.** Lectures without math content (`about`, `business_cycle`, `french_rev`, `inflation_history`, `intro`, `long_run_growth`, `schelling`, `status`, `troubleshooting`, `zreferences`) should be evaluated and refined on writing style alone. Most are already clean; `french_rev` is the main offender and worth a dedicated editing pass.
