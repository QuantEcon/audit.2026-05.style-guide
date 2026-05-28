# Style Audit — lecture-python-intro

- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Lectures audited:** 51
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope across the series)*
- **Average overall score:** 7.6 / 10
- **Average per-category scores:** writing 8.0, math 7.8, code 8.1, figures 6.4, references 7.0, links 7.9, admonitions 9.0

(v1 overall average across writing + math was 8.0; the drop to 7.6 reflects the lower figures and references scores surfaced by the v2 extension.)

## Priority distribution

| Priority | Count | % |
|----------|-------|------|
| HIGH     | 1     | 2.0% |
| MEDIUM   | 9     | 17.6% |
| LOW      | 36    | 70.6% |
| NONE     | 5     | 9.8% |

(v1 had HIGH 1, MEDIUM 9, LOW 27, NONE 14. The v2 extension surfaced more issues in figures/references/links, pulling many `NONE` lectures down into `LOW` and one `LOW` (`inflation_history`) into `MEDIUM`.)

## Top systemic issues across the series

1. **[qe-fig-005]** — Figures lack a descriptive `:name:` for cross-referencing — appears in **36 / 51** lectures. Most matplotlib figures are emitted via `plt.show()` without a `{figure}` directive wrapper, so `numref` cannot target them. **Systemic.**
2. **[qe-fig-001]** — Explicit `figsize=` overrides where `_config.yml` defaults should apply — appears in **26 / 51** lectures (totalling ~80+ individual `figsize=` calls).
3. **[qe-ref-001]** — In-text citations using `{cite}` instead of `{cite:t}` (e.g. "described by {cite}\`X\`", "Chapter 1 of {cite}\`Y\`") — appears in **15 / 51** lectures. **Series-wide pattern: 0 of 51 lectures use `{cite:t}` at all** despite many having clearly in-text citation phrasing. Heaviest in `inflation_history` (10 occurrences), `french_rev` (4), `long_run_growth` (4).
4. **[qe-fig-003]** — `ax.set_title(...)` / `fig.suptitle(...)` outside exercise / solution context — appears in **11 / 51** lectures. Concentrated in `eigen_I` (7), `heavy_tails` (4), `lake_model` (3), `complex_and_trig` (1), `geom_series` (1), `monte_carlo` (1), `schelling` (1), `unpleasant` (1), `greek_square` (2), `inequality` (1).
5. **[qe-fig-006]** — Axis labels starting with an uppercase letter outside acronyms (`"Year"`, `"Date"`, `"Present Value"`, `"Welfare"`, `"Optimal flat tax"`, etc.) — appears in **10 / 51** lectures.
6. **[qe-link-002]** — Cross-series links using direct URLs (e.g. `https://python-programming.quantecon.org/numpy.html`) instead of `{doc}\`programming:numpy\`` — appears in **9 / 51** lectures: `intro_supply_demand` (4), `linear_equations` (5), `time_series_with_matrices` (3), `troubleshooting`, `about`, `markov_chains_I`, `olg`, `schelling`, `lln_clt`.
7. **[qe-fig-007]** — `ax.spines[...].set_visible(False)` / `set_color('none')` removing the figure box — appears in **6 / 51** lectures: `french_rev` (30 calls), `eigen_I` (12), `linear_equations` (6), `complex_and_trig` (3), `scalar_dynam` (3), `lake_model` (2). `french_rev` is the egregious offender.

Carried forward from v1 (writing + math), the top issues remain:

- **qe-writing-001 (was W1)** — Multi-sentence paragraphs — 47 / 51 lectures.
- **qe-writing-004 / qe-writing-006 (was W3 / W7)** — Title-Case headings and random mid-sentence Title Case — 19 / 51 lectures.
- **qe-math-A1 / qe-math-A3 / qe-math-002 (was M3 / M9 / M2)** — Blackboard-bold, distribution-name and transpose conventions — small per-lecture but consistently present.

## Lectures ranked by priority (lowest score first)

| # | Lecture | W | M | C | F | R | L | A | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | supply_demand_foundations_v2 | 4 | 5 | N/A | 7 | N/A | N/A | N/A | 5.4 | HIGH |
| 2 | time_series_with_matrices | 7 | 4 | 9 | 7 | 8 | 4 | N/A | 5.9 | MEDIUM |
| 3 | french_rev | 6 | N/A | 7 | 4 | 5 | 9 | 9 | 6.0 | MEDIUM |
| 4 | geom_series | 6 | 7 | 7 | 4 | N/A | N/A | 9 | 6.4 | MEDIUM |
| 5 | inflation_history | 8 | N/A | 8 | 5 | 4 | 8 | 9 | 6.6 | MEDIUM |
| 6 | money_inflation_nonlinear | 5 | 6 | 8 | 7 | 8 | 9 | 9 | 6.6 | MEDIUM |
| 7 | unpleasant | 6 | 7 | 8 | 6 | 8 | 9 | 9 | 6.6 | MEDIUM |
| 8 | complex_and_trig | 6 | 7 | 8 | 5 | 6 | N/A | 8 | 6.7 | MEDIUM |
| 9 | greek_square | 8 | 6 | 8 | 5 | 7 | 9 | 9 | 6.7 | MEDIUM |
| 10 | networks | 8 | 5 | 8 | 7 | 7 | N/A | 9 | 7.0 | MEDIUM |
| 11 | cagan_ree | 7 | 7 | 8 | 6 | 8 | 9 | 9 | 7.0 | LOW |
| 12 | long_run_growth | 8 | N/A | 8 | 6 | 4 | 9 | N/A | 7.0 | LOW |
| 13 | simple_linear_regression | 6 | 7 | 8 | 8 | N/A | N/A | N/A | 7.1 | LOW |
| 14 | lake_model | 8 | 9 | 8 | 5 | N/A | N/A | 8 | 7.3 | LOW |
| 15 | cons_smooth | 8 | 8 | 8 | 6 | 7 | 9 | 9 | 7.4 | LOW |
| 16 | laffer_adaptive | 7 | 8 | 8 | 6 | 6 | 9 | 9 | 7.4 | LOW |
| 17 | linear_equations | 8 | 7 | 8 | 7 | N/A | 4 | 9 | 7.4 | LOW |
| 18 | money_inflation | 7 | 8 | 8 | 6 | 7 | 9 | 9 | 7.4 | LOW |
| 19 | solow | 8 | 7 | 8 | 6 | N/A | N/A | 9 | 7.4 | LOW |
| 20 | tax_smooth | 7 | 8 | 9 | 6 | 7 | 9 | 9 | 7.4 | LOW |
| 21 | cagan_adaptive | 8 | 8 | 8 | 6 | 7 | N/A | 9 | 7.6 | LOW |
| 22 | eigen_I | 8 | 9 | 8 | 5 | N/A | 8 | 9 | 7.6 | LOW |
| 23 | heavy_tails | 9 | 9 | 8 | 5 | 7 | 6 | 9 | 7.6 | LOW |
| 24 | intro_supply_demand | 9 | 8 | 8 | 8 | N/A | 5 | 9 | 7.6 | LOW |
| 25 | lln_clt | 9 | 8 | 8 | 6 | N/A | 6 | 9 | 7.6 | LOW |
| 26 | markov_chains_I | 8 | 8 | 8 | 8 | 7 | 8 | 9 | 7.6 | LOW |
| 27 | about | 8 | N/A | N/A | N/A | N/A | 7 | N/A | 7.7 | LOW |
| 28 | equalizing_difference | 8 | 8 | 9 | 7 | 7 | N/A | 9 | 7.7 | LOW |
| 29 | inequality | 8 | 8 | 8 | 7 | 8 | 9 | 9 | 7.7 | LOW |
| 30 | lp_intro | 9 | 8 | 8 | 8 | 6 | 9 | 9 | 7.7 | LOW |
| 31 | schelling | 8 | N/A | 8 | 6 | 8 | 6 | 9 | 7.7 | LOW |
| 32 | short_path | 9 | 9 | 8 | 5 | N/A | N/A | 9 | 7.7 | LOW |
| 33 | troubleshooting | 9 | N/A | N/A | 7 | N/A | 7 | N/A | 7.7 | LOW |
| 34 | ar1_processes | 9 | 7 | 8 | 7 | 7 | N/A | 9 | 7.9 | LOW |
| 35 | olg | 9 | 9 | 8 | 6 | 8 | 6 | 9 | 7.9 | LOW |
| 36 | scalar_dynam | 8 | 9 | 8 | 7 | N/A | 9 | 9 | 8.0 | LOW |
| 37 | monte_carlo | 9 | 8 | 9 | 7 | N/A | 9 | 9 | 8.1 | LOW |
| 38 | prob_dist | 9 | 9 | 8 | 5 | N/A | N/A | 9 | 8.1 | LOW |
| 39 | cobweb | 9 | 9 | 8 | 7 | 8 | N/A | 9 | 8.3 | LOW |
| 40 | business_cycle | 8 | N/A | 8 | 8 | N/A | N/A | N/A | 8.4 | LOW |
| 41 | eigen_II | 9 | 8 | 9 | N/A | 7 | N/A | 9 | 8.4 | LOW |
| 42 | input_output | 9 | 9 | 8 | 7 | 8 | 9 | 9 | 8.4 | LOW |
| 43 | markov_chains_II | 9 | 9 | 9 | 8 | 7 | 9 | 9 | 8.4 | LOW |
| 44 | pv | 9 | 9 | 8 | 7 | N/A | 9 | 9 | 8.4 | LOW |
| 45 | supply_demand_heterogeneity | 9 | 8 | 8 | N/A | N/A | 9 | N/A | 8.4 | LOW |
| 46 | supply_demand_multiple_goods | 9 | 9 | 7 | N/A | N/A | 9 | 9 | 8.4 | LOW |
| 47 | commod_price | 9 | 8 | 9 | 9 | 8 | N/A | N/A | 8.7 | NONE |
| 48 | mle | 9 | 9 | 9 | 8 | N/A | N/A | 9 | 8.7 | NONE |
| 49 | status | 9 | N/A | 9 | N/A | N/A | N/A | N/A | 9.0 | NONE |
| 50 | intro | 10 | N/A | N/A | N/A | N/A | N/A | N/A | 10.0 | NONE |
| 51 | zreferences | 10 | N/A | N/A | N/A | N/A | N/A | N/A | 10.0 | NONE |

## Series-level recommendations

1. **Adopt `{cite:t}` for in-text citations across the series (qe-ref-001).** 0 / 51 lectures currently use `{cite:t}`, but at least 15 have clear in-text patterns ("described by {cite}", "Chapter X of {cite}", "proven by {cite}", "by {cite:t}\`Author\`"). Priority sweep targets: `inflation_history` (10 occurrences), `french_rev` (4), `long_run_growth` (4), `markov_chains_I`/`II` (2 each), `eigen_II`, `tax_smooth`, `lp_intro`, `cagan_adaptive`, `laffer_adaptive`, `complex_and_trig`, `equalizing_difference`, `greek_square`, `ar1_processes`, `networks`.

2. **Series-wide figure refactor (qe-fig-001, qe-fig-003, qe-fig-005, qe-fig-006, qe-fig-007).**
   - Remove the ~80+ `figsize=` overrides (26 lectures); rely on `_config.yml` defaults per qe-fig-001.
   - Move `ax.set_title(...)` content outside exercise/solution blocks into mystnb metadata or `{figure}` captions (11 lectures, ~25 calls).
   - Wrap key matplotlib outputs in `{figure}` directives with `:name: fig-...` to enable `numref` cross-referencing (36 lectures).
   - Lowercase axis labels (10 lectures, ~25 labels); keep acronyms (GDP, CPI, YoY) and proper nouns.
   - Drop `ax.spines[...].set_visible(False)` / `set_color('none')` patterns — particularly in `french_rev` (30 calls) and `eigen_I` (12 calls).

3. **Cross-series link cleanup (qe-link-002).** Replace direct `python-programming.quantecon.org/*.html`, `python.quantecon.org/*.html` URLs with `{doc}\`programming:foo\`` / `{doc}\`intermediate:foo\`` form. 9 lectures affected; heaviest in `intro_supply_demand` (4 SciPy refs), `linear_equations` (5 NumPy/linalg refs), `time_series_with_matrices` (3 refs).

4. **Fix `supply_demand_foundations_v2.md` (HIGH).** Still the worst-scoring lecture (5.4). The v1 issues (missing top-level H1, Title Case sections, mixed transpose) remain. In addition the lecture has no executable `{code-cell}` blocks and no exercises/solutions, making it inconsistent with the rest of the series.

5. **Convert remaining Title Case section headings to sentence case (qe-writing-006).** Highest-impact targets unchanged from v1: `money_inflation_nonlinear` (6+), `complex_and_trig` (8+), `geom_series` (3+), `french_rev` (4+), `networks` (2 H3s), `supply_demand_foundations_v2` (6+).

6. **Sweep `\mathbf 1` → `\mathbb{1}` for ones / indicator (M3).** Affects `networks`, `markov_chains_I`, `lln_clt`, `prob_dist`.

7. **Treat data/history lectures (`about`, `business_cycle`, `french_rev`, `inflation_history`, `intro`, `long_run_growth`, `schelling`, `status`, `troubleshooting`, `zreferences`) as text-only and refine on writing + links + references.** `french_rev` and `inflation_history` are the main offenders.
