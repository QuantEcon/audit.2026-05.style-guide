# Summary

Style audit of the **lecture-python-intro** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-23
- **Corpus snapshot:** `a12d17c0ef`
- **Lectures audited:** 56
- **Average overall score:** 8.4 / 10
- **Average per-category scores:** writing 6.3, math 8.7, code 8.2, figures 6.5, references 9.3, links 9.7, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
- **Judgment-review coverage:** **33 of 56 reviewed** — scores for the unreviewed 23 reflect the 41 measured rules only, so they are not directly comparable with the reviewed ones.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
This series is in the best shape of the five, and its problems are shallow: no lecture
scores below 7.2, and 23 of 56 need nothing at all. What holds the average down is not
a hard spot but a pair of habits applied almost everywhere — `qe-fig-005` (46 of 56
lectures have a figure with no `name:`) and `qe-writing-008` (710 runs of extra
whitespace across 39 lectures).

The 11 HIGH lectures are all triggered by a single category floor rather than a low
overall: **Writing** in 6 of them, Figures in 3, Math in 2. Math is barely a factor here —
`qe-math-002` appears in only 6 lectures, against 35 in `lecture-python-advanced.myst`.
So the whole series is reachable with figure metadata and a prose sweep; there is no
notation debt to work through.
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 12    | 21.4% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 21    | 37.5% |
| NONE     | 23    | 41.1% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **46 / 56** lectures, 174 occurrences.
2. **`qe-fig-008`** — Use lw=2 for line charts — **39 / 56** lectures, 266 occurrences.
3. **`qe-writing-008`** — Remove excessive whitespace between words — **39 / 56** lectures, 710 occurrences.
4. **`qe-fig-001`** — Do not set figure size unless necessary — **30 / 56** lectures, 91 occurrences.
5. **`qe-writing-001`** — Use one sentence per paragraph — **30 / 56** lectures, 53 occurrences.
6. **`qe-writing-004`** — Avoid unnecessary capitalization in narrative text — **18 / 56** lectures, 40 occurrences.
7. **`qe-fig-004`** — Caption formatting conventions — **17 / 56** lectures, 69 occurrences.
8. **`qe-fig-003`** — No matplotlib embedded titles — **15 / 56** lectures, 36 occurrences.
9. **`qe-ref-001`** — Use correct citation style — **15 / 56** lectures, 48 occurrences.
10. **`qe-writing-006`** — Capitalize lecture titles properly — **15 / 56** lectures, 33 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-003`** — Use tick count management for nested directives
- **`qe-code-005`** — Use quantecon timeit for benchmarking
- **`qe-fig-010`** — Plotly figures require latex directive
- **`qe-math-006`** — Use aligned environment correctly for PDF compatibility
- **`qe-math-007`** — Use automatic equation numbering, not manual tags
- **`qe-math-013`** *(proposed)* — Reference equations via {eq}`label`
<!-- /qe:series-clean -->

## Series-level recommendations

<!-- qe:series-recommendations -->
1. **`qe-fig-005` — name the figures** (46 / 56, 174 figures). The single highest-return
   fix in the series, and a pure sweep: add `name:` under the `mystnb.figure` metadata of
   each figure-producing cell. Unlocks `{numref}` cross-referencing as a side effect.
2. **`qe-writing-008` — collapse repeated spaces** (39 / 56, 710 occurrences). Entirely
   safe to automate, and it is the largest raw count in the series.
3. **`qe-fig-008` — `lw=2` on line plots** (39 / 56, 266 calls). Scriptable, though worth
   a glance where a plot deliberately uses a thin line.
4. **`qe-fig-001` — drop `figsize=`** (30 / 56, 91 overrides). Let the series
   `_config.yml` defaults apply; keep an override only where a plot needs a different
   aspect ratio.
5. **`qe-writing-001` — one sentence per paragraph** (30 / 56, 53 blocks). A reading pass,
   not a sweep: splitting a paragraph changes its rhythm, so it wants an editor.
6. **Figures and Writing together clear 9 of the 11 HIGH lectures.** Start with
   `linear_equations` (7.2), then `business_cycle`, `heavy_tails` and `inflation_history`
   (7.4 each).
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [geom_series](geom_series.md) | 3 | 8.5 | 7.5 | 4 | — | 10 | 10 | **7.2** | HIGH |
| 2 | [linear_equations](linear_equations.md) | 5.5 | 6.5 | 7.5 | 6 | — | 7.5 | 10 | **7.2** | LOW |
| 3 | [french_rev](french_rev.md) | 3 | 10 | 7.5 | 3 | 7.5 | 10 | 10 | **7.3** | HIGH |
| 4 | [business_cycle](business_cycle.md) | 6 | — | 6.5 | 7 | — | 10 | — | **7.4** | LOW |
| 5 | [eigen_I](eigen_I.md) | 3.5 | 10 | 7.5 | 3.5 | — | 10 | 10 | **7.4** | HIGH |
| 6 | [heavy_tails](heavy_tails.md) | 6 | 5.5 | 6.5 | 5 | 10 | 9 | 10 | **7.4** | LOW |
| 7 | [inflation_history](inflation_history.md) | 3 | 10 | 6 | 4.5 | 8.5 | 10 | 10 | **7.4** | HIGH |
| 8 | [markov_chains_I](markov_chains_I.md) | 6 | 3 | 7 | 7.5 | 9 | 9 | 10 | **7.4** | HIGH |
| 9 | [equalizing_difference](equalizing_difference.md) | 5 | 8 | 6 | 5.5 | 9 | 10 | 10 | **7.6** | LOW |
| 10 | [greek_square](greek_square.md) | 4 | 7.5 | 7 | 6.5 | 9 | 10 | 10 | **7.7** | HIGH |
| 11 | [bivariate_dist](bivariate_dist.md) | 6.5 | 5.5 | 7.5 | 5 | 10 | 10 | 10 | **7.8** | LOW |
| 12 | [inequality](inequality.md) | 4 | 9 | 6.5 | 5 | 10 | 10 | 10 | **7.8** | HIGH |
| 13 | [intro_supply_demand](intro_supply_demand.md) | 4.5 | 10 | 7.5 | 6.5 | — | 8 | 10 | **7.8** | LOW |
| 14 | [lln_clt](lln_clt.md) | 8 | 4 | 7.5 | 8 | — | 9 | 10 | **7.8** | HIGH |
| 15 | [long_run_growth](long_run_growth.md) | 5 | — | 7.5 | 6 | 8.5 | 10 | 10 | **7.8** | LOW |
| 16 | [ar1_processes](ar1_processes.md) | 6 | 7.5 | 6 | 7 | 9 | 10 | 10 | **7.9** | LOW |
| 17 | [complex_and_trig](complex_and_trig.md) | 3 | 9.5 | 7 | 5.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 18 | [laffer_adaptive](laffer_adaptive.md) | 4 | 10 | 7 | 6 | 8.5 | 10 | 10 | **7.9** | HIGH |
| 19 | [lake_model](lake_model.md) | 4.5 | 10 | 7.5 | 5.5 | — | 10 | 10 | **7.9** | LOW |
| 20 | [networks](networks.md) | 6 | 6.5 | 9 | 5.5 | 8.5 | 10 | 10 | **7.9** | LOW |
| 21 | [lp_intro](lp_intro.md) | 3.5 | 6.5 | 7.5 | 8.5 | 10 | 10 | 10 | **8.0** | HIGH |
| 22 | [cons_smooth](cons_smooth.md) | 4.5 | 10 | 7.5 | 6 | 9 | 10 | 10 | **8.1** | LOW |
| 23 | [time_series_with_matrices](time_series_with_matrices.md) | 5 | 6.5 | 10 | 7 | 10 | 8 | 10 | **8.1** | LOW |
| 24 | [cagan_adaptive](cagan_adaptive.md) | 5 | 10 | 7 | 6.5 | 9 | 10 | 10 | **8.2** | LOW |
| 25 | [mle](mle.md) | 5 | 10 | 7 | 7.5 | — | 10 | 10 | **8.2** | LOW |
| 26 | [bayes_intro](bayes_intro.md) | 7.5 | 9.5 | 7.5 | 5.5 | — | 10 | 10 | **8.3** | LOW |
| 27 | [eigen_II](eigen_II.md) | 4.5 | 9.5 | 7.5 | — | 9 | 10 | 10 | **8.4** | LOW |
| 28 | [input_output](input_output.md) | 7.5 | 10 | 6.5 | 6 | 8.5 | 10 | 10 | **8.4** | LOW |
| 29 | [markov_chains_II](markov_chains_II.md) | 6.5 | 10 | 7.5 | 6.5 | 8.5 | 10 | 10 | **8.4** | LOW |
| 30 | [mobility](mobility.md) | 7 | 7.5 | 10 | 7.5 | 7 | 10 | 10 | **8.4** | LOW |
| 31 | [monte_carlo](monte_carlo.md) | 8 | 5.5 | 9 | 8 | — | 10 | 10 | **8.4** | LOW |
| 32 | [about](about.md) | 8 | — | — | — | — | 9 | — | **8.5** | LOW |
| 33 | [cagan_ree](cagan_ree.md) | 4 | 10 | 8.5 | 7 | 10 | 10 | 10 | **8.5** | HIGH |
| 34 | [unpleasant](unpleasant.md) | 5.5 | 8.5 | 10 | 6 | 10 | 10 | 10 | **8.6** | NONE |
| 35 | [money_inflation](money_inflation.md) | 7 | 8 | 10 | 6 | 10 | 10 | 10 | **8.7** | NONE |
| 36 | [money_inflation_nonlinear](money_inflation_nonlinear.md) | 4.5 | 10 | 10 | 6.5 | 10 | 10 | 10 | **8.7** | NONE |
| 37 | [prob_dist](prob_dist.md) | 9.5 | 7.5 | 7.5 | 8.5 | — | 10 | 10 | **8.8** | NONE |
| 38 | [simple_linear_regression](simple_linear_regression.md) | 7.5 | 9 | 10 | 6.5 | — | 10 | 9.5 | **8.8** | NONE |
| 39 | [supply_demand_multiple_goods](supply_demand_multiple_goods.md) | 6.5 | 10 | 8.5 | 7.5 | — | 10 | 10 | **8.8** | NONE |
| 40 | [troubleshooting](troubleshooting.md) | 8.5 | — | — | 9 | — | 9 | — | **8.8** | NONE |
| 41 | [solow](solow.md) | 7.5 | 8.5 | 10 | 7.5 | — | 10 | 10 | **8.9** | NONE |
| 42 | [tax_smooth](tax_smooth.md) | 6 | 10 | 10 | 6 | 10 | 10 | 10 | **8.9** | NONE |
| 43 | [cobweb](cobweb.md) | 7.5 | 10 | 9 | 6.5 | 10 | 10 | 10 | **9.0** | NONE |
| 44 | [commod_price](commod_price.md) | 7.5 | 10 | 7.5 | 8 | 10 | 10 | 10 | **9.0** | NONE |
| 45 | [pv](pv.md) | 7 | 10 | 10 | 7 | — | 10 | 10 | **9.0** | NONE |
| 46 | [fitting_distributions](fitting_distributions.md) | 6.5 | 10 | 10 | 8 | — | 10 | 10 | **9.1** | NONE |
| 47 | [msy_fishery](msy_fishery.md) | 7.5 | 10 | 10 | 6.5 | 10 | 10 | 10 | **9.1** | NONE |
| 48 | [olg](olg.md) | 9.5 | 10 | 10 | 6.5 | 10 | 8 | 10 | **9.1** | NONE |
| 49 | [scalar_dynam](scalar_dynam.md) | 7.5 | 10 | 8.5 | 8.5 | — | 10 | 10 | **9.1** | NONE |
| 50 | [observed_distributions](observed_distributions.md) | 8.5 | 10 | 10 | 7 | 10 | 10 | 10 | **9.4** | NONE |
| 51 | [supply_demand_heterogeneity](supply_demand_heterogeneity.md) | 9 | 10 | 8.5 | — | — | 10 | 10 | **9.5** | NONE |
| 52 | [schelling](schelling.md) | 9.5 | 10 | 10 | 8.5 | 10 | 9 | 10 | **9.6** | NONE |
| 53 | [short_path](short_path.md) | 10 | 10 | 10 | 8 | — | 10 | 10 | **9.7** | NONE |
| 54 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 55 | [status](status.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 56 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
