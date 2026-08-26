# Summary

Style audit of the **lecture-python.myst** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-24
- **Corpus snapshot:** `e25fdf2345`
- **Lectures audited:** 145
- **Average overall score:** 7.7 / 10
- **Average per-category scores:** writing 4.5, math 7.0, code 7.6, figures 6.5, references 9.5, links 9.8, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
- **Judgment-review coverage:** all lectures reviewed.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
The largest series at 145 lectures, and the widest spread: 63 lectures need nothing,
40 are HIGH. The average (8.4) sits mid-field, but that average is hiding two different
populations rather than describing a uniform state.

**Math is the binding constraint on the HIGH list** — 21 of the 40 HIGH lectures are
floored by it, against 14 by Writing and 5 by Figures. Two rules do most of that work:
`qe-math-010` *(proposed)* in 50 lectures (521 bare or unbraced expectation operators) and
`qe-math-002` in 49 (661 apostrophe or `^T` transposes). `qe-math-004` is narrower but
intense — 18 lectures carrying 509 bold vectors between them.

Figures are the weakest category by average (6.5) but rarely the floor: `qe-fig-005`
(110 / 145) and `qe-fig-001` (107 / 145) are near-universal and low-weight, so they lower
scores broadly without pushing lectures into HIGH.

`qe-writing-008` deserves a mention for scale alone: **2,569 occurrences** across 89
lectures, the largest single count anywhere in the corpus.
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 81    | 55.9% |
| MEDIUM   | 1     | 0.7% |
| LOW      | 46    | 31.7% |
| NONE     | 17    | 11.7% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **110 / 145** lectures, 446 occurrences.
2. **`qe-fig-001`** — Do not set figure size unless necessary — **107 / 145** lectures, 462 occurrences.
3. **`qe-writing-008`** — Remove excessive whitespace between words — **89 / 145** lectures, 2569 occurrences.
4. **`qe-fig-003`** — No matplotlib embedded titles — **79 / 145** lectures, 329 occurrences.
5. **`qe-writing-006`** — Capitalize lecture titles properly — **71 / 145** lectures, 410 occurrences.
6. **`qe-fig-008`** — Use lw=2 for line charts — **69 / 145** lectures, 393 occurrences.
7. **`qe-writing-001`** — Use one sentence per paragraph — **65 / 145** lectures, 165 occurrences.
8. **`qe-math-010`** *(proposed)* — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces — **60 / 145** lectures, 682 occurrences.
9. **`qe-writing-004`** — Avoid unnecessary capitalization in narrative text — **43 / 145** lectures, 148 occurrences.
10. **`qe-ref-001`** — Use correct citation style — **36 / 145** lectures, 105 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-002`** — Use dropdown class for solutions
- **`qe-admon-003`** — Use tick count management for nested directives
<!-- /qe:series-clean -->

## Series-level recommendations

<!-- qe:series-recommendations -->
1. **`qe-math-010` *(proposed)* and `qe-math-002` together** (50 and 49 lectures,
   1,182 occurrences). The Math floor is what makes 21 lectures HIGH, and these two rules
   are almost all of it. Best done as one careful pass — both are mechanical substitutions
   (`E[·]` → `\mathbb{E}[·]`, `'` and `^T` → `^\top`) but they touch equations, so they
   want review rather than blind `sed`.
2. **`qe-fig-005` — name the figures** (110 / 145, 446 figures). Largest reach in the
   series; a pure sweep.
3. **`qe-fig-001` — drop `figsize=`** (107 / 145, 462 overrides).
4. **`qe-writing-008` — collapse repeated spaces** (89 / 145, 2,569 occurrences). The
   biggest raw count in the corpus and entirely safe to automate.
5. **`qe-fig-003` — plot titles into captions** (79 / 145, 329 calls). Needs a human: each
   `ax.set_title(...)` becomes a caption that has to be written. Titles inside
   `exercise`/`solution` regions are exempt and already excluded from the count.
6. **`qe-math-004` — un-bold the vectors** (18 / 145, 509 occurrences). Narrow but dense;
   a good single-sitting fix.
7. **Start with the four worst:** `navy_captain` (6.1), `cross_product_trick` (6.3),
   `prob_matrix` (6.8), `rs_inventory_q` (6.9). Note that `cross_product_trick` and
   `rs_inventory_q` are also synced into `lecture-dp` — fixing them here clears both.
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [cross_product_trick](cross_product_trick.md) | 3.5 | 3 | — | — | — | 10 | — | **5.5** | HIGH |
| 2 | [qr_decomp](qr_decomp.md) | 3 | 3 | 7.5 | — | — | 10 | — | **5.9** | HIGH |
| 3 | [navy_captain](navy_captain.md) | 3 | 6.5 | 7.5 | 3 | — | 10 | — | **6.0** | HIGH |
| 4 | [two_auctions](two_auctions.md) | 3 | 4.5 | 6.5 | 3 | 10 | 9 | — | **6.0** | HIGH |
| 5 | [likelihood_var](likelihood_var.md) | 4.5 | 3.5 | 7.5 | 5 | — | 10 | — | **6.1** | HIGH |
| 6 | [prob_matrix](prob_matrix.md) | 3 | 3 | 5.5 | 5 | — | 10 | 10 | **6.1** | HIGH |
| 7 | [rs_inventory_q](rs_inventory_q.md) | 3 | 6.5 | 7.5 | 5 | — | 10 | — | **6.4** | HIGH |
| 8 | [linear_models](linear_models.md) | 3 | 3 | 6 | 8 | — | 9 | 10 | **6.5** | HIGH |
| 9 | [multivariate_normal](multivariate_normal.md) | 3 | 3 | 7.5 | 5.5 | — | 10 | 10 | **6.5** | HIGH |
| 10 | [perm_income_cons](perm_income_cons.md) | 3 | 4 | 7.5 | 5.5 | 10 | 9 | — | **6.5** | HIGH |
| 11 | [two_computation](two_computation.md) | 5.5 | 3 | 7.5 | 3 | 10 | 10 | — | **6.5** | HIGH |
| 12 | [likelihood_ratio_process](likelihood_ratio_process.md) | 3 | 3 | 7 | 3.5 | 10 | 10 | 10 | **6.6** | HIGH |
| 13 | [lagrangian_lqdp](lagrangian_lqdp.md) | 3 | 3 | 7 | — | 10 | 7.5 | 10 | **6.8** | HIGH |
| 14 | [prob_meaning](prob_meaning.md) | 3 | 7.5 | 6 | 4.5 | — | 10 | 10 | **6.8** | HIGH |
| 15 | [ifp_advanced](ifp_advanced.md) | 3 | 3 | 7 | 7 | 8.5 | 10 | 10 | **6.9** | HIGH |
| 16 | [kalman_2](kalman_2.md) | 5 | 7.5 | 7.5 | 4.5 | — | 10 | — | **6.9** | MEDIUM |
| 17 | [linear_algebra](linear_algebra.md) | 3 | 4.5 | 7.5 | 5.5 | 10 | 7.5 | 10 | **6.9** | HIGH |
| 18 | [markov_asset](markov_asset.md) | 3 | 4.5 | 7.5 | 6.5 | 8.5 | 8 | 10 | **6.9** | HIGH |
| 19 | [misspecified_recovery](misspecified_recovery.md) | 3 | 3 | 6 | 6.5 | 10 | 10 | 10 | **6.9** | HIGH |
| 20 | [multi_hyper](multi_hyper.md) | 3.5 | 6.5 | 7.5 | 7 | — | 10 | — | **6.9** | HIGH |
| 21 | [pandas_panel](pandas_panel.md) | 3.5 | — | 7.5 | 4.5 | — | 9 | 10 | **6.9** | HIGH |
| 22 | [stats_examples](stats_examples.md) | 3 | 4.5 | 7 | 7 | — | 10 | 10 | **6.9** | HIGH |
| 23 | [ols](ols.md) | 3 | 7 | 7.5 | 5 | 7.5 | 9 | 10 | **7.0** | HIGH |
| 24 | [perm_income](perm_income.md) | 3 | 4 | 7.5 | 6 | 8.5 | 10 | 10 | **7.0** | HIGH |
| 25 | [phillips_lost_conquest](phillips_lost_conquest.md) | 3.5 | 6 | 7.5 | 4.5 | 7.5 | 10 | 10 | **7.0** | HIGH |
| 26 | [wald_friedman_2](wald_friedman_2.md) | 3 | 6 | 7.5 | 5 | 9 | 8.5 | 10 | **7.0** | HIGH |
| 27 | [finite_markov](finite_markov.md) | 3 | 3.5 | 8 | 6.5 | 10 | 9 | 10 | **7.1** | HIGH |
| 28 | [lln_clt](lln_clt.md) | 3.5 | 3 | 6.5 | 7 | 10 | 10 | 10 | **7.1** | HIGH |
| 29 | [lq_inventories](lq_inventories.md) | 3 | 3 | 7.5 | 7 | 10 | 10 | 10 | **7.2** | HIGH |
| 30 | [mle](mle.md) | 4.5 | 3 | 7.5 | 5.5 | 10 | 10 | 10 | **7.2** | HIGH |
| 31 | [sargent_surico](sargent_surico.md) | 6.5 | 5.5 | 4.5 | 4 | 10 | 10 | 10 | **7.2** | HIGH |
| 32 | [var_subsets](var_subsets.md) | 6.5 | 7 | 5 | 5 | — | 10 | 10 | **7.2** | LOW |
| 33 | [ge_arrow](ge_arrow.md) | 3 | 3 | 7.5 | 7.5 | 10 | 10 | 10 | **7.3** | HIGH |
| 34 | [opt_transport](opt_transport.md) | 3 | 3 | 7 | 8 | 10 | 10 | 10 | **7.3** | HIGH |
| 35 | [pricing_information](pricing_information.md) | 5.5 | 4.5 | 5 | 6 | 10 | 10 | 10 | **7.3** | LOW |
| 36 | [util_rand_resp](util_rand_resp.md) | 4 | 4 | 7.5 | 9.5 | 9 | 10 | — | **7.3** | HIGH |
| 37 | [von_neumann_model](von_neumann_model.md) | 3 | 5 | 7.5 | 7 | 8.5 | 10 | 10 | **7.3** | HIGH |
| 38 | [affine_risk_prices](affine_risk_prices.md) | 4.5 | 4 | 8.5 | 5.5 | 9 | 10 | 10 | **7.4** | HIGH |
| 39 | [blackwell_kihlstrom](blackwell_kihlstrom.md) | 3.5 | 3 | 8.5 | 7.5 | 9 | 10 | 10 | **7.4** | HIGH |
| 40 | [imp_sample](imp_sample.md) | 4.5 | 4 | 10 | 8.5 | — | 10 | — | **7.4** | HIGH |
| 41 | [likelihood_ratio_process_2](likelihood_ratio_process_2.md) | 3 | 9.5 | 7.5 | 4 | 7.5 | 10 | 10 | **7.4** | HIGH |
| 42 | [markov_perf](markov_perf.md) | 4 | 5 | 7 | 6 | 10 | 10 | 10 | **7.4** | HIGH |
| 43 | [mccall_model](mccall_model.md) | 3 | 7.5 | 7 | 6 | 10 | 8 | 10 | **7.4** | HIGH |
| 44 | [odu](odu.md) | 3 | 9 | 7.5 | 5 | 9 | 8.5 | 10 | **7.4** | HIGH |
| 45 | [ross_recovery](ross_recovery.md) | 3.5 | 5.5 | 6.5 | 6 | 10 | 10 | 10 | **7.4** | HIGH |
| 46 | [uncertainty_traps](uncertainty_traps.md) | 3 | 5.5 | 7.5 | 6.5 | 9 | 10 | 10 | **7.4** | HIGH |
| 47 | [inventory_q](inventory_q.md) | 3 | 6 | 10 | 6 | 10 | 10 | — | **7.5** | HIGH |
| 48 | [lqcontrol](lqcontrol.md) | 4.5 | 5 | 7.5 | 5.5 | 10 | 10 | 10 | **7.5** | LOW |
| 49 | [phillips_priors](phillips_priors.md) | 4.5 | 7 | 8.5 | 5.5 | 7 | 10 | 10 | **7.5** | LOW |
| 50 | [samuelson](samuelson.md) | 6.5 | 9.5 | 7.5 | 5 | 8.5 | 8 | — | **7.5** | LOW |
| 51 | [wald_friedman](wald_friedman.md) | 3 | 8.5 | 7.5 | 4.5 | 10 | 9 | 10 | **7.5** | HIGH |
| 52 | [ak_aiyagari](ak_aiyagari.md) | 5 | 10 | 8 | 4 | 8.5 | 10 | — | **7.6** | HIGH |
| 53 | [cass_fiscal](cass_fiscal.md) | 3 | 9 | 7.5 | 4 | 10 | 10 | 10 | **7.6** | HIGH |
| 54 | [hansen_singleton_1983](hansen_singleton_1983.md) | 6 | 3 | 7 | 9.5 | 10 | 10 | — | **7.6** | HIGH |
| 55 | [measurement_models](measurement_models.md) | 3 | 5 | 6 | 9.5 | 10 | 10 | 10 | **7.6** | HIGH |
| 56 | [olg_adaptive_money](olg_adaptive_money.md) | 3.5 | 7.5 | 6.5 | 6 | 10 | 10 | 10 | **7.6** | HIGH |
| 57 | [os_stochastic](os_stochastic.md) | 3 | 7 | 7.5 | 7.5 | 10 | 8 | 10 | **7.6** | HIGH |
| 58 | [ar1_turningpts](ar1_turningpts.md) | 3 | 7.5 | 8.5 | 8 | 9 | 10 | — | **7.7** | HIGH |
| 59 | [cass_koopmans_2](cass_koopmans_2.md) | 3 | 9.5 | 8.5 | 6 | 10 | 7 | 10 | **7.7** | HIGH |
| 60 | [kalman](kalman.md) | 5 | 4.5 | 8.5 | 7 | 9 | 10 | 10 | **7.7** | LOW |
| 61 | [long_run_risk_operator](long_run_risk_operator.md) | 3 | 7 | 7.5 | 6.5 | 10 | 10 | 10 | **7.7** | HIGH |
| 62 | [phillips_learning](phillips_learning.md) | 5 | 7.5 | 8.5 | 6 | 7 | 10 | 10 | **7.7** | LOW |
| 63 | [phillips_two_stories](phillips_two_stories.md) | 3 | 10 | 8.5 | 5 | 7.5 | 10 | 10 | **7.7** | HIGH |
| 64 | [back_prop](back_prop.md) | 3 | 7.5 | 7.5 | 9 | — | 10 | 10 | **7.8** | HIGH |
| 65 | [ifp_opi](ifp_opi.md) | 5 | 10 | 7 | 6 | — | 9 | 10 | **7.8** | LOW |
| 66 | [likelihood_bayes](likelihood_bayes.md) | 5.5 | 4 | 7.5 | 7.5 | 10 | 10 | 10 | **7.8** | HIGH |
| 67 | [ls_learning](ls_learning.md) | 4.5 | 5 | 8.5 | 6.5 | 10 | 10 | 10 | **7.8** | LOW |
| 68 | [mccall_q](mccall_q.md) | 4 | 9.5 | 7 | 7 | 9 | 10 | — | **7.8** | HIGH |
| 69 | [mccall_risk](mccall_risk.md) | 6.5 | 6 | 7 | 7 | — | 10 | 10 | **7.8** | LOW |
| 70 | [newton_method](newton_method.md) | 4 | 9.5 | 7 | 6 | — | 10 | 10 | **7.8** | HIGH |
| 71 | [os_numerical](os_numerical.md) | 4.5 | 9.5 | 7.5 | 5.5 | — | 10 | 10 | **7.8** | LOW |
| 72 | [re_with_feedback](re_with_feedback.md) | 3 | 8.5 | 7 | 6 | 10 | 10 | 10 | **7.8** | HIGH |
| 73 | [sir_model](sir_model.md) | 4.5 | 7.5 | 8.5 | 8.5 | — | 10 | — | **7.8** | LOW |
| 74 | [svd_intro](svd_intro.md) | 3 | 9.5 | 7.5 | 6.5 | — | 10 | 10 | **7.8** | HIGH |
| 75 | [var_dmd](var_dmd.md) | 3 | 9.5 | — | — | 7.5 | 9 | 10 | **7.8** | HIGH |
| 76 | [eig_circulant](eig_circulant.md) | 3 | 7.5 | 10 | 7 | — | 10 | 10 | **7.9** | HIGH |
| 77 | [exchangeable](exchangeable.md) | 3.5 | 7 | 7.5 | 7.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 78 | [ifp_egm](ifp_egm.md) | 3 | 9.5 | 6.5 | 6.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 79 | [information_market_equilibrium](information_market_equilibrium.md) | 4 | 5.5 | 8.5 | 7.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 80 | [kalman_filter_var](kalman_filter_var.md) | 5.5 | 7.5 | 5.5 | 6.5 | 10 | 10 | 10 | **7.9** | LOW |
| 81 | [lake_model](lake_model.md) | 5.5 | 6.5 | 7.5 | 5.5 | 10 | 10 | 10 | **7.9** | LOW |
| 82 | [mccall_fitted_vfi](mccall_fitted_vfi.md) | 6 | 8 | 7 | 5.5 | 9 | 10 | 10 | **7.9** | LOW |
| 83 | [phillips_drifts_volatilities](phillips_drifts_volatilities.md) | 3.5 | 9.5 | 8 | 4.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 84 | [phillips_escaping_nash](phillips_escaping_nash.md) | 5 | 9.5 | 8.5 | 4.5 | 7.5 | 10 | 10 | **7.9** | LOW |
| 85 | [rational_expectations](rational_expectations.md) | 3.5 | 5 | 7.5 | 10 | 9 | 10 | 10 | **7.9** | HIGH |
| 86 | [robust_permanent_income](robust_permanent_income.md) | 3.5 | 9 | 7 | 6 | 10 | 10 | 10 | **7.9** | HIGH |
| 87 | [aiyagari_egm](aiyagari_egm.md) | 3 | 8.5 | 10 | 5.5 | 9 | 10 | 10 | **8.0** | HIGH |
| 88 | [cass_koopmans_1](cass_koopmans_1.md) | 3 | 9.5 | 8.5 | 6 | 10 | 9 | 10 | **8.0** | HIGH |
| 89 | [divergence_measures](divergence_measures.md) | 4.5 | 6.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.0** | LOW |
| 90 | [hansen_singleton_1982](hansen_singleton_1982.md) | 6 | 5 | 5.5 | 9.5 | 10 | 10 | 10 | **8.0** | LOW |
| 91 | [ifp_egm_transient_shocks](ifp_egm_transient_shocks.md) | 4 | 10 | 7.5 | 5.5 | 9 | 10 | 10 | **8.0** | HIGH |
| 92 | [jv](jv.md) | 3 | 10 | 7.5 | 6.5 | 9 | 10 | 10 | **8.0** | HIGH |
| 93 | [marimon_mcgrattan_sargent](marimon_mcgrattan_sargent.md) | 4 | 9.5 | 6.5 | 7.5 | 8.5 | 10 | 10 | **8.0** | HIGH |
| 94 | [market_diffusion](market_diffusion.md) | 6.5 | 7 | 4.5 | 8 | 10 | 10 | 10 | **8.0** | LOW |
| 95 | [mccall_model_with_sep_markov](mccall_model_with_sep_markov.md) | 5.5 | 10 | 7 | 5.5 | — | 10 | 10 | **8.0** | LOW |
| 96 | [mix_model](mix_model.md) | 5 | 9 | 7 | 7 | — | 10 | 10 | **8.0** | LOW |
| 97 | [theil_1](theil_1.md) | 4.5 | 6.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.0** | LOW |
| 98 | [troubleshooting](troubleshooting.md) | 6 | — | — | 9 | — | 9 | — | **8.0** | LOW |
| 99 | [ak2](ak2.md) | 3.5 | 10 | 8.5 | 5 | 10 | 10 | 10 | **8.1** | HIGH |
| 100 | [cass_fiscal_2](cass_fiscal_2.md) | 4 | 10 | 7.5 | 5.5 | 10 | 10 | 10 | **8.1** | HIGH |
| 101 | [chow_business_cycles](chow_business_cycles.md) | 5.5 | 6.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.1** | LOW |
| 102 | [learning_approximation](learning_approximation.md) | 5.5 | 8 | 7 | 6.5 | 10 | 10 | 10 | **8.1** | LOW |
| 103 | [lq_robust_bewley](lq_robust_bewley.md) | 6.5 | 5.5 | 7.5 | 7.5 | 10 | 10 | 10 | **8.1** | LOW |
| 104 | [merging_of_opinions](merging_of_opinions.md) | 4.5 | 7 | 8.5 | 7.5 | 9 | 10 | 10 | **8.1** | LOW |
| 105 | [os_time_iter](os_time_iter.md) | 4.5 | 7.5 | 7.5 | 8 | 9 | 10 | 10 | **8.1** | LOW |
| 106 | [phillips_self_confirming](phillips_self_confirming.md) | 5.5 | 7 | 8.5 | 6 | 10 | 10 | 10 | **8.1** | LOW |
| 107 | [rand_resp](rand_resp.md) | 3.5 | 9.5 | 7.5 | — | 10 | 10 | — | **8.1** | HIGH |
| 108 | [theil_2](theil_2.md) | 4.5 | 7.5 | 6.5 | 8.5 | 10 | 10 | 10 | **8.1** | LOW |
| 109 | [wealth_dynamics](wealth_dynamics.md) | 3 | 9.5 | 8 | 6.5 | 10 | 10 | 10 | **8.1** | HIGH |
| 110 | [aiyagari](aiyagari.md) | 4.5 | 8.5 | 8.5 | 7 | 10 | 9 | 10 | **8.2** | LOW |
| 111 | [bayes_nonconj](bayes_nonconj.md) | 5 | 10 | 8.5 | 6.5 | — | 9 | 10 | **8.2** | LOW |
| 112 | [endogenous_lake](endogenous_lake.md) | 5.5 | 7.5 | 8.5 | 6 | 10 | 10 | 10 | **8.2** | LOW |
| 113 | [mccall_persist_trans](mccall_persist_trans.md) | 6.5 | 6 | 7 | 8 | 10 | 10 | 10 | **8.2** | LOW |
| 114 | [survival_recursive_preferences](survival_recursive_preferences.md) | 5 | 9.5 | 8.5 | 4.5 | 10 | 10 | 10 | **8.2** | LOW |
| 115 | [house_auction](house_auction.md) | 3 | 10 | 7 | — | 10 | 10 | 10 | **8.3** | HIGH |
| 116 | [lq_permanent_income](lq_permanent_income.md) | 5.5 | 7.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.3** | LOW |
| 117 | [hoist_failure](hoist_failure.md) | 5.5 | 6.5 | 8.5 | 8 | 10 | 10 | 10 | **8.4** | LOW |
| 118 | [ifp_discrete](ifp_discrete.md) | 5.5 | 7 | 7.5 | 8.5 | 10 | 10 | 10 | **8.4** | LOW |
| 119 | [kesten_processes](kesten_processes.md) | 5.5 | 5 | 10 | 8 | 10 | 10 | 10 | **8.4** | LOW |
| 120 | [lq_robust_smoothing](lq_robust_smoothing.md) | 5.5 | 7.5 | 8.5 | 7.5 | 10 | 10 | 10 | **8.4** | LOW |
| 121 | [organization_capital](organization_capital.md) | 4.5 | 7 | 8.5 | 9 | 10 | 10 | 10 | **8.4** | LOW |
| 122 | [phillips_adaptive](phillips_adaptive.md) | 5.5 | 9.5 | 8.5 | 6.5 | 8.5 | 10 | 10 | **8.4** | LOW |
| 123 | [phillips_credibility](phillips_credibility.md) | 5 | 9.5 | 9 | 7 | 8.5 | 10 | 10 | **8.4** | LOW |
| 124 | [phillips_misspecified](phillips_misspecified.md) | 5.5 | 9.5 | 8.5 | 6.5 | 8.5 | 10 | 10 | **8.4** | LOW |
| 125 | [rational_learning_re](rational_learning_re.md) | 5.5 | 7.5 | 8.5 | 7 | 10 | 10 | 10 | **8.4** | LOW |
| 126 | [morris_learn](morris_learn.md) | 3 | 9.5 | 8.5 | 10 | 8.5 | 10 | 10 | **8.5** | HIGH |
| 127 | [os_egm](os_egm.md) | 4 | 9.5 | 7 | 9 | 10 | 10 | 10 | **8.5** | HIGH |
| 128 | [phillips_credible_policies](phillips_credible_policies.md) | 6.5 | 9.5 | 8.5 | 6 | 10 | 9 | 10 | **8.5** | LOW |
| 129 | [ar1_bayes](ar1_bayes.md) | 7 | 10 | 7.5 | 8 | 10 | 8 | 10 | **8.6** | NONE |
| 130 | [bounded_rationality](bounded_rationality.md) | 5.5 | 10 | 8.5 | 6.5 | 10 | 10 | 10 | **8.6** | NONE |
| 131 | [career](career.md) | 6 | 9.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.6** | NONE |
| 132 | [exchange_rate_learning](exchange_rate_learning.md) | 5 | 9.5 | 10 | 5.5 | 10 | 10 | 10 | **8.6** | NONE |
| 133 | [lq_bewley_complete_markets](lq_bewley_complete_markets.md) | 6 | 10 | 8.5 | 6 | 10 | 10 | 10 | **8.6** | NONE |
| 134 | [unemployment_linear](unemployment_linear.md) | 6 | 8 | 8.5 | 8.5 | 9 | 10 | 10 | **8.6** | NONE |
| 135 | [os_egm_jax](os_egm_jax.md) | 8 | 10 | 7 | 7 | — | 10 | 10 | **8.7** | NONE |
| 136 | [genetic_classifier](genetic_classifier.md) | 6 | 10 | 8.5 | 7 | 10 | 10 | 10 | **8.8** | NONE |
| 137 | [harrison_kreps](harrison_kreps.md) | 6.5 | 8 | 8.5 | — | 10 | 10 | 10 | **8.8** | NONE |
| 138 | [mccall_model_with_separation](mccall_model_with_separation.md) | 7 | 8.5 | 7.5 | 8.5 | 10 | 10 | 10 | **8.8** | NONE |
| 139 | [os](os.md) | 5.5 | 9.5 | 8.5 | 8 | 10 | 10 | 10 | **8.8** | NONE |
| 140 | [prospects_bounded_rationality](prospects_bounded_rationality.md) | 6.5 | 10 | 7.5 | 8.5 | 10 | 10 | — | **8.8** | NONE |
| 141 | [inventory_dynamics](inventory_dynamics.md) | 5.5 | 10 | 9.5 | 7 | 10 | 10 | 10 | **8.9** | NONE |
| 142 | [unemployment_shocks](unemployment_shocks.md) | 6.5 | 9.5 | 7.5 | 10 | — | 10 | 10 | **8.9** | NONE |
| 143 | [status](status.md) | 10 | — | 9 | — | — | 10 | — | **9.7** | NONE |
| 144 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 145 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
