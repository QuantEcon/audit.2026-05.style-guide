# Summary

Style audit of the **lecture-python-intro** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-23
- **Corpus snapshot:** `a12d17c0ef`
- **Lectures audited:** 56
- **Average overall score:** 8.7 / 10
- **Average per-category scores:** writing 7.5, math 8.7, code 9.3, figures 6.3, references 9.0, links 9.7, admon 9.9
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
_The series-level reading of these numbers goes here._
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 7     | 12.5% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 16    | 28.6% |
| NONE     | 33    | 58.9% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **49 / 56** lectures, 208 occurrences.
2. **`qe-fig-008`** — Use lw=2 for line charts — **42 / 56** lectures, 292 occurrences.
3. **`qe-writing-008`** — Remove excessive whitespace between words — **39 / 56** lectures, 710 occurrences.
4. **`qe-fig-001`** — Do not set figure size unless necessary — **30 / 56** lectures, 91 occurrences.
5. **`qe-writing-001`** — Use one sentence per paragraph — **30 / 56** lectures, 53 occurrences.
6. **`qe-ref-001`** — Use correct citation style — **19 / 56** lectures, 73 occurrences.
7. **`qe-writing-004`** — Avoid unnecessary capitalization in narrative text — **18 / 56** lectures, 40 occurrences.
8. **`qe-fig-004`** — Caption formatting conventions — **17 / 56** lectures, 69 occurrences.
9. **`qe-fig-003`** — No matplotlib embedded titles — **15 / 56** lectures, 36 occurrences.
10. **`qe-writing-006`** — Capitalize lecture titles properly — **15 / 56** lectures, 33 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-003`** — Use tick count management for nested directives
- **`qe-code-005`** — Use quantecon timeit for benchmarking
- **`qe-fig-009`** — Figure sizing
- **`qe-fig-010`** — Plotly figures require latex directive
- **`qe-math-006`** — Use aligned environment correctly for PDF compatibility
- **`qe-math-007`** — Use automatic equation numbering, not manual tags
- **`qe-math-011`** *(proposed)* — Distribution names in plain letters, not \mathcal / \mathbb
- **`qe-math-013`** *(proposed)* — Reference equations via {eq}`label`
<!-- /qe:series-clean -->

## Series-level recommendations

<!-- qe:series-recommendations -->
_generated_
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [heavy_tails](heavy_tails.md) | 6 | 5.5 | 6.5 | 5 | 9 | 9 | 10 | **7.3** | LOW |
| 2 | [inflation_history](inflation_history.md) | 3 | 10 | 6 | 4.5 | 8.5 | 10 | 10 | **7.4** | HIGH |
| 3 | [french_rev](french_rev.md) | 3.5 | 10 | 10 | 3 | 7.5 | 10 | 10 | **7.7** | HIGH |
| 4 | [bivariate_dist](bivariate_dist.md) | 6.5 | 5.5 | 7.5 | 5 | 10 | 10 | 10 | **7.8** | LOW |
| 5 | [inequality](inequality.md) | 4 | 9 | 6.5 | 5 | 10 | 10 | 10 | **7.8** | HIGH |
| 6 | [markov_chains_I](markov_chains_I.md) | 8 | 3 | 9.5 | 7.5 | 8.5 | 9 | 9 | **7.8** | HIGH |
| 7 | [networks](networks.md) | 6 | 6.5 | 9 | 5.5 | 7.5 | 10 | 10 | **7.8** | LOW |
| 8 | [ar1_processes](ar1_processes.md) | 6 | 7.5 | 6 | 7 | 9 | 10 | 10 | **7.9** | LOW |
| 9 | [geom_series](geom_series.md) | 5.5 | 8.5 | 10 | 4 | — | 10 | 10 | **8.0** | HIGH |
| 10 | [linear_equations](linear_equations.md) | 9 | 6.5 | 10 | 5.5 | — | 7.5 | 10 | **8.1** | LOW |
| 11 | [eigen_I](eigen_I.md) | 6 | 10 | 10 | 3 | — | 10 | 10 | **8.2** | HIGH |
| 12 | [lln_clt](lln_clt.md) | 10 | 4 | 10 | 7 | — | 9 | 9 | **8.2** | HIGH |
| 13 | [money_inflation_nonlinear](money_inflation_nonlinear.md) | 4.5 | 8.5 | 10 | 5.5 | 9 | 10 | 10 | **8.2** | LOW |
| 14 | [time_series_with_matrices](time_series_with_matrices.md) | 5 | 7.5 | 10 | 7 | 10 | 8 | 10 | **8.2** | LOW |
| 15 | [bayes_intro](bayes_intro.md) | 7.5 | 9.5 | 7.5 | 5.5 | — | 10 | 10 | **8.3** | LOW |
| 16 | [equalizing_difference](equalizing_difference.md) | 8.5 | 8 | 7.5 | 5.5 | 8.5 | 10 | 10 | **8.3** | LOW |
| 17 | [input_output](input_output.md) | 7.5 | 10 | 6.5 | 6 | 8.5 | 10 | 10 | **8.4** | LOW |
| 18 | [mobility](mobility.md) | 7 | 7.5 | 10 | 7.5 | 7 | 10 | 10 | **8.4** | LOW |
| 19 | [money_inflation](money_inflation.md) | 7 | 7 | 10 | 5.5 | 9 | 10 | 10 | **8.4** | LOW |
| 20 | [monte_carlo](monte_carlo.md) | 8 | 5.5 | 9 | 8 | — | 10 | 10 | **8.4** | LOW |
| 21 | [about](about.md) | 8 | — | — | — | — | 9 | — | **8.5** | LOW |
| 22 | [business_cycle](business_cycle.md) | 8 | — | 9 | 7 | — | 10 | — | **8.5** | LOW |
| 23 | [greek_square](greek_square.md) | 6 | 8 | 10 | 6.5 | 9 | 10 | 10 | **8.5** | LOW |
| 24 | [complex_and_trig](complex_and_trig.md) | 4.5 | 10 | 10 | 5.5 | 10 | 10 | 10 | **8.6** | NONE |
| 25 | [cons_smooth](cons_smooth.md) | 7 | 10 | 10 | 6 | 7.5 | 10 | 10 | **8.6** | NONE |
| 26 | [long_run_growth](long_run_growth.md) | 7.5 | — | 10 | 5.5 | 8.5 | 10 | 10 | **8.6** | NONE |
| 27 | [supply_demand_multiple_goods](supply_demand_multiple_goods.md) | 6.5 | 10 | 8.5 | 6.5 | — | 10 | 10 | **8.6** | NONE |
| 28 | [unpleasant](unpleasant.md) | 5.5 | 8.5 | 10 | 6 | 10 | 10 | 10 | **8.6** | NONE |
| 29 | [intro_supply_demand](intro_supply_demand.md) | 7.5 | 10 | 10 | 6.5 | — | 8 | 10 | **8.7** | NONE |
| 30 | [lp_intro](lp_intro.md) | 6 | 6.5 | 10 | 8.5 | 10 | 10 | 10 | **8.7** | NONE |
| 31 | [laffer_adaptive](laffer_adaptive.md) | 8 | 10 | 10 | 6 | 7.5 | 10 | 10 | **8.8** | NONE |
| 32 | [prob_dist](prob_dist.md) | 9.5 | 7.5 | 7.5 | 8 | — | 10 | 10 | **8.8** | NONE |
| 33 | [scalar_dynam](scalar_dynam.md) | 7.5 | 10 | 8.5 | 7 | — | 10 | 10 | **8.8** | NONE |
| 34 | [simple_linear_regression](simple_linear_regression.md) | 7.5 | 9 | 10 | 6.5 | — | 10 | 9.5 | **8.8** | NONE |
| 35 | [solow](solow.md) | 7.5 | 8.5 | 10 | 6.5 | — | 10 | 10 | **8.8** | NONE |
| 36 | [troubleshooting](troubleshooting.md) | 8.5 | — | — | 9 | — | 9 | — | **8.8** | NONE |
| 37 | [lake_model](lake_model.md) | 8.5 | 10 | 10 | 5 | — | 10 | 10 | **8.9** | NONE |
| 38 | [tax_smooth](tax_smooth.md) | 6 | 10 | 10 | 6 | 10 | 10 | 10 | **8.9** | NONE |
| 39 | [cagan_adaptive](cagan_adaptive.md) | 8.5 | 10 | 10 | 6 | 8.5 | 10 | 10 | **9.0** | NONE |
| 40 | [markov_chains_II](markov_chains_II.md) | 9 | 10 | 10 | 6.5 | 8.5 | 10 | 9 | **9.0** | NONE |
| 41 | [pv](pv.md) | 7 | 10 | 10 | 7 | — | 10 | 10 | **9.0** | NONE |
| 42 | [cagan_ree](cagan_ree.md) | 7 | 10 | 10 | 6.5 | 10 | 10 | 10 | **9.1** | NONE |
| 43 | [msy_fishery](msy_fishery.md) | 7.5 | 10 | 10 | 6.5 | 10 | 10 | 10 | **9.1** | NONE |
| 44 | [olg](olg.md) | 9.5 | 10 | 10 | 6.5 | 10 | 8 | 10 | **9.1** | NONE |
| 45 | [cobweb](cobweb.md) | 10 | 10 | 10 | 6 | 8.5 | 10 | 10 | **9.2** | NONE |
| 46 | [eigen_II](eigen_II.md) | 7 | 10 | 10 | — | 8.5 | 10 | 10 | **9.2** | NONE |
| 47 | [mle](mle.md) | 7.5 | 10 | 10 | 7.5 | — | 10 | 10 | **9.2** | NONE |
| 48 | [observed_distributions](observed_distributions.md) | 8.5 | 10 | 10 | 7 | 10 | 10 | 10 | **9.4** | NONE |
| 49 | [schelling](schelling.md) | 9.5 | 10 | 10 | 7 | 10 | 9 | 10 | **9.4** | NONE |
| 50 | [commod_price](commod_price.md) | 10 | 10 | 8.5 | 8 | 10 | 10 | 10 | **9.5** | NONE |
| 51 | [supply_demand_heterogeneity](supply_demand_heterogeneity.md) | 9 | 10 | 8.5 | — | — | 10 | 10 | **9.5** | NONE |
| 52 | [fitting_distributions](fitting_distributions.md) | 10 | 10 | 10 | 8 | — | 10 | 10 | **9.7** | NONE |
| 53 | [short_path](short_path.md) | 10 | 10 | 10 | 8 | — | 10 | 10 | **9.7** | NONE |
| 54 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 55 | [status](status.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 56 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
