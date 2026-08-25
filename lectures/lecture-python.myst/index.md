# Summary

Style audit of the **lecture-python.myst** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-24
- **Corpus snapshot:** `e25fdf2345`
- **Lectures audited:** 145
- **Average overall score:** 8.4 / 10
- **Average per-category scores:** writing 6.9, math 7.1, code 9.2, figures 6.5, references 9.5, links 9.8, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
_The series-level reading of these numbers goes here._
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 40    | 27.6% |
| MEDIUM   | 1     | 0.7% |
| LOW      | 41    | 28.3% |
| NONE     | 63    | 43.4% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **110 / 145** lectures, 446 occurrences.
2. **`qe-fig-001`** — Do not set figure size unless necessary — **107 / 145** lectures, 462 occurrences.
3. **`qe-writing-008`** — Remove excessive whitespace between words — **89 / 145** lectures, 2569 occurrences.
4. **`qe-fig-008`** — Use lw=2 for line charts — **80 / 145** lectures, 438 occurrences.
5. **`qe-fig-003`** — No matplotlib embedded titles — **79 / 145** lectures, 329 occurrences.
6. **`qe-writing-006`** — Capitalize lecture titles properly — **77 / 145** lectures, 418 occurrences.
7. **`qe-writing-001`** — Use one sentence per paragraph — **63 / 145** lectures, 161 occurrences.
8. **`qe-code-002`** — Use Unicode symbols for Greek letters in code — **51 / 145** lectures, 388 occurrences.
9. **`qe-math-010`** *(proposed)* — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces — **50 / 145** lectures, 521 occurrences.
10. **`qe-math-002`** — Use \top for transpose notation — **49 / 145** lectures, 661 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-002`** — Use dropdown class for solutions
- **`qe-admon-003`** — Use tick count management for nested directives
- **`qe-fig-009`** — Figure sizing
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
| 1 | [navy_captain](navy_captain.md) | 4.5 | 4.5 | 8.5 | 3 | — | 10 | — | **6.1** | HIGH |
| 2 | [cross_product_trick](cross_product_trick.md) | 6 | 3 | — | — | — | 10 | — | **6.3** | HIGH |
| 3 | [prob_matrix](prob_matrix.md) | 5 | 3 | 7.5 | 5 | — | 10 | 10 | **6.8** | HIGH |
| 4 | [rs_inventory_q](rs_inventory_q.md) | 5 | 4.5 | 10 | 5 | — | 10 | — | **6.9** | MEDIUM |
| 5 | [var_dmd](var_dmd.md) | 3 | 5 | — | — | 7.5 | 9 | 10 | **6.9** | HIGH |
| 6 | [likelihood_ratio_process](likelihood_ratio_process.md) | 4.5 | 3.5 | 7.5 | 3.5 | 10 | 10 | 10 | **7.0** | HIGH |
| 7 | [lagrangian_lqdp](lagrangian_lqdp.md) | 3.5 | 3 | 8.5 | — | 10 | 7.5 | 10 | **7.1** | HIGH |
| 8 | [perm_income_cons](perm_income_cons.md) | 4.5 | 4.5 | 9 | 5.5 | 10 | 9 | — | **7.1** | LOW |
| 9 | [qr_decomp](qr_decomp.md) | 5.5 | 3 | 10 | — | — | 10 | — | **7.1** | HIGH |
| 10 | [two_auctions](two_auctions.md) | 6 | 5.5 | 10 | 3 | 10 | 9 | — | **7.2** | HIGH |
| 11 | [wald_friedman_2](wald_friedman_2.md) | 3 | 6.5 | 8.5 | 5 | 9 | 8.5 | 10 | **7.2** | HIGH |
| 12 | [linear_algebra](linear_algebra.md) | 3 | 5 | 10 | 5.5 | 10 | 7.5 | 10 | **7.3** | HIGH |
| 13 | [mccall_model](mccall_model.md) | 4 | 3 | 10 | 6 | 10 | 8 | 10 | **7.3** | HIGH |
| 14 | [multivariate_normal](multivariate_normal.md) | 5.5 | 3 | 10 | 5.5 | — | 10 | 10 | **7.3** | HIGH |
| 15 | [two_computation](two_computation.md) | 9 | 3 | 9 | 3 | 10 | 10 | — | **7.3** | HIGH |
| 16 | [von_neumann_model](von_neumann_model.md) | 3 | 5.5 | 7 | 7 | 8.5 | 10 | 10 | **7.3** | HIGH |
| 17 | [finite_markov](finite_markov.md) | 3 | 3.5 | 9.5 | 6.5 | 10 | 9 | 10 | **7.4** | HIGH |
| 18 | [ifp_advanced](ifp_advanced.md) | 4.5 | 3 | 8.5 | 7 | 8.5 | 10 | 10 | **7.4** | HIGH |
| 19 | [linear_models](linear_models.md) | 3 | 5 | 10 | 7.5 | — | 9 | 10 | **7.4** | HIGH |
| 20 | [markov_asset](markov_asset.md) | 4 | 4.5 | 10 | 6.5 | 9 | 8 | 10 | **7.4** | HIGH |
| 21 | [likelihood_var](likelihood_var.md) | 8 | 4.5 | 10 | 5 | — | 10 | — | **7.5** | LOW |
| 22 | [perm_income](perm_income.md) | 3.5 | 4.5 | 10 | 6 | 8.5 | 10 | 10 | **7.5** | HIGH |
| 23 | [ge_arrow](ge_arrow.md) | 3 | 3 | 10 | 7.5 | 10 | 10 | 10 | **7.6** | HIGH |
| 24 | [inventory_q](inventory_q.md) | 5.5 | 4 | 10 | 6 | 10 | 10 | — | **7.6** | HIGH |
| 25 | [misspecified_recovery](misspecified_recovery.md) | 6 | 3 | 7.5 | 6.5 | 10 | 10 | 10 | **7.6** | HIGH |
| 26 | [prob_meaning](prob_meaning.md) | 3.5 | 7.5 | 10 | 4.5 | — | 10 | 10 | **7.6** | HIGH |
| 27 | [sargent_surico](sargent_surico.md) | 8 | 5.5 | 6 | 4 | 10 | 10 | 10 | **7.6** | HIGH |
| 28 | [imp_sample](imp_sample.md) | 8 | 5 | 7.5 | 8 | — | 10 | — | **7.7** | LOW |
| 29 | [markov_perf](markov_perf.md) | 5.5 | 5 | 7.5 | 6 | 10 | 10 | 10 | **7.7** | LOW |
| 30 | [lln_clt](lln_clt.md) | 7 | 3 | 7.5 | 7 | 10 | 10 | 10 | **7.8** | HIGH |
| 31 | [lq_inventories](lq_inventories.md) | 5.5 | 3 | 9 | 7 | 10 | 10 | 10 | **7.8** | HIGH |
| 32 | [opt_transport](opt_transport.md) | 4.5 | 3 | 9 | 8 | 10 | 10 | 10 | **7.8** | HIGH |
| 33 | [var_subsets](var_subsets.md) | 8 | 7 | 7 | 5 | — | 10 | 10 | **7.8** | LOW |
| 34 | [affine_risk_prices](affine_risk_prices.md) | 7 | 4 | 10 | 5 | 9 | 10 | 10 | **7.9** | HIGH |
| 35 | [blackwell_kihlstrom](blackwell_kihlstrom.md) | 5.5 | 3.5 | 10 | 7.5 | 9 | 10 | 10 | **7.9** | HIGH |
| 36 | [cass_fiscal](cass_fiscal.md) | 3.5 | 9 | 9 | 4 | 10 | 10 | 10 | **7.9** | HIGH |
| 37 | [cass_koopmans_1](cass_koopmans_1.md) | 4.5 | 5.5 | 10 | 6 | 10 | 9 | 10 | **7.9** | LOW |
| 38 | [likelihood_ratio_process_2](likelihood_ratio_process_2.md) | 5.5 | 10 | 8.5 | 4 | 7.5 | 10 | 10 | **7.9** | HIGH |
| 39 | [lqcontrol](lqcontrol.md) | 8 | 5.5 | 7.5 | 5 | 9 | 10 | 10 | **7.9** | LOW |
| 40 | [mle](mle.md) | 7 | 3 | 10 | 5.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 41 | [odu](odu.md) | 5 | 10 | 7.5 | 5 | 9 | 8.5 | 10 | **7.9** | LOW |
| 42 | [ross_recovery](ross_recovery.md) | 6.5 | 4 | 8.5 | 6 | 10 | 10 | 10 | **7.9** | HIGH |
| 43 | [wald_friedman](wald_friedman.md) | 5 | 9 | 7.5 | 4.5 | 10 | 9 | 10 | **7.9** | LOW |
| 44 | [back_prop](back_prop.md) | 4.5 | 6 | 8.5 | 9 | — | 10 | 10 | **8.0** | LOW |
| 45 | [pandas_panel](pandas_panel.md) | 6.5 | — | 10 | 4.5 | — | 9 | 10 | **8.0** | LOW |
| 46 | [pricing_information](pricing_information.md) | 10 | 3 | 7 | 6 | 10 | 10 | 10 | **8.0** | HIGH |
| 47 | [troubleshooting](troubleshooting.md) | 6 | — | — | 9 | — | 9 | — | **8.0** | LOW |
| 48 | [ifp_egm_transient_shocks](ifp_egm_transient_shocks.md) | 6 | 7.5 | 9 | 5.5 | 8.5 | 10 | 10 | **8.1** | LOW |
| 49 | [ifp_opi](ifp_opi.md) | 6.5 | 10 | 7 | 6 | — | 9 | 10 | **8.1** | LOW |
| 50 | [information_market_equilibrium](information_market_equilibrium.md) | 7 | 3.5 | 8.5 | 7.5 | 10 | 10 | 10 | **8.1** | HIGH |
| 51 | [mccall_q](mccall_q.md) | 7 | 5.5 | 10 | 7 | 9 | 10 | — | **8.1** | LOW |
| 52 | [measurement_models](measurement_models.md) | 4.5 | 5.5 | 7.5 | 9.5 | 10 | 10 | 10 | **8.1** | LOW |
| 53 | [ols](ols.md) | 7.5 | 7.5 | 10 | 5 | 7.5 | 9 | 10 | **8.1** | LOW |
| 54 | [os_stochastic](os_stochastic.md) | 4.5 | 7.5 | 9.5 | 7.5 | 10 | 8 | 10 | **8.1** | LOW |
| 55 | [uncertainty_traps](uncertainty_traps.md) | 5.5 | 6 | 10 | 6.5 | 9 | 10 | 10 | **8.1** | LOW |
| 56 | [ak_aiyagari](ak_aiyagari.md) | 8.5 | 10 | 8.5 | 4 | 8.5 | 10 | — | **8.2** | HIGH |
| 57 | [cass_koopmans_2](cass_koopmans_2.md) | 4.5 | 10 | 10 | 6 | 10 | 7 | 10 | **8.2** | LOW |
| 58 | [hansen_singleton_1983](hansen_singleton_1983.md) | 8 | 3 | 8.5 | 9.5 | 10 | 10 | — | **8.2** | HIGH |
| 59 | [kalman_2](kalman_2.md) | 9 | 7.5 | 10 | 4.5 | — | 10 | — | **8.2** | LOW |
| 60 | [multi_hyper](multi_hyper.md) | 6.5 | 7.5 | 10 | 7 | — | 10 | — | **8.2** | LOW |
| 61 | [samuelson](samuelson.md) | 9.5 | 10 | 7.5 | 5 | 9 | 8 | — | **8.2** | LOW |
| 62 | [svd_intro](svd_intro.md) | 3 | 10 | 10 | 6.5 | — | 10 | 10 | **8.2** | HIGH |
| 63 | [util_rand_resp](util_rand_resp.md) | 5.5 | 5 | 10 | 9.5 | 9 | 10 | — | **8.2** | LOW |
| 64 | [ifp_egm](ifp_egm.md) | 6 | 7.5 | 9 | 6.5 | 9 | 10 | 10 | **8.3** | LOW |
| 65 | [aiyagari_egm](aiyagari_egm.md) | 5.5 | 8.5 | 10 | 5.5 | 9 | 10 | 10 | **8.4** | LOW |
| 66 | [divergence_measures](divergence_measures.md) | 7 | 6.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.4** | LOW |
| 67 | [eig_circulant](eig_circulant.md) | 5.5 | 8 | 10 | 7 | — | 10 | 10 | **8.4** | LOW |
| 68 | [long_run_risk_operator](long_run_risk_operator.md) | 4.5 | 7.5 | 10 | 6.5 | 10 | 10 | 10 | **8.4** | LOW |
| 69 | [merging_of_opinions](merging_of_opinions.md) | 6 | 8 | 8.5 | 7.5 | 9 | 10 | 10 | **8.4** | LOW |
| 70 | [olg_adaptive_money](olg_adaptive_money.md) | 7 | 6.5 | 10 | 5.5 | 10 | 10 | 10 | **8.4** | LOW |
| 71 | [os_time_iter](os_time_iter.md) | 7.5 | 5 | 9.5 | 8 | 9 | 10 | 10 | **8.4** | LOW |
| 72 | [phillips_drifts_volatilities](phillips_drifts_volatilities.md) | 6 | 10 | 8 | 4.5 | 10 | 10 | 10 | **8.4** | LOW |
| 73 | [phillips_lost_conquest](phillips_lost_conquest.md) | 6.5 | 10 | 10 | 4.5 | 7.5 | 10 | 10 | **8.4** | LOW |
| 74 | [phillips_two_stories](phillips_two_stories.md) | 5.5 | 10 | 10 | 5 | 8.5 | 10 | 10 | **8.4** | LOW |
| 75 | [re_with_feedback](re_with_feedback.md) | 3.5 | 9 | 10 | 6 | 10 | 10 | 10 | **8.4** | HIGH |
| 76 | [endogenous_lake](endogenous_lake.md) | 7.5 | 6 | 10 | 6 | 10 | 10 | 10 | **8.5** | LOW |
| 77 | [exchangeable](exchangeable.md) | 6 | 7.5 | 8.5 | 7.5 | 10 | 10 | 10 | **8.5** | LOW |
| 78 | [ifp_discrete](ifp_discrete.md) | 7.5 | 6 | 7.5 | 8.5 | 10 | 10 | 10 | **8.5** | LOW |
| 79 | [kalman](kalman.md) | 9 | 4.5 | 10 | 7 | 9 | 10 | 10 | **8.5** | LOW |
| 80 | [rational_expectations](rational_expectations.md) | 7 | 5.5 | 8.5 | 10 | 8.5 | 10 | 10 | **8.5** | LOW |
| 81 | [stats_examples](stats_examples.md) | 5.5 | 10 | 9 | 6.5 | — | 10 | 10 | **8.5** | LOW |
| 82 | [cass_fiscal_2](cass_fiscal_2.md) | 6 | 10 | 9 | 5.5 | 10 | 10 | 10 | **8.6** | NONE |
| 83 | [mccall_risk](mccall_risk.md) | 10 | 6.5 | 8 | 7 | — | 10 | 10 | **8.6** | NONE |
| 84 | [newton_method](newton_method.md) | 8 | 8.5 | 9 | 6 | — | 10 | 10 | **8.6** | NONE |
| 85 | [os](os.md) | 7 | 5.5 | 10 | 8 | 10 | 10 | 10 | **8.6** | NONE |
| 86 | [os_numerical](os_numerical.md) | 6 | 10 | 10 | 5.5 | — | 10 | 10 | **8.6** | NONE |
| 87 | [sir_model](sir_model.md) | 6.5 | 8 | 10 | 8.5 | — | 10 | — | **8.6** | NONE |
| 88 | [survival_recursive_preferences](survival_recursive_preferences.md) | 9 | 7.5 | 9 | 4.5 | 10 | 10 | 10 | **8.6** | NONE |
| 89 | [wealth_dynamics](wealth_dynamics.md) | 4.5 | 10 | 9.5 | 6.5 | 10 | 10 | 10 | **8.6** | NONE |
| 90 | [aiyagari](aiyagari.md) | 6.5 | 8.5 | 10 | 7 | 10 | 9 | 10 | **8.7** | NONE |
| 91 | [hansen_singleton_1982](hansen_singleton_1982.md) | 8.5 | 5.5 | 8.5 | 8.5 | 10 | 10 | 10 | **8.7** | NONE |
| 92 | [kesten_processes](kesten_processes.md) | 7.5 | 5.5 | 10 | 8 | 10 | 10 | 10 | **8.7** | NONE |
| 93 | [lake_model](lake_model.md) | 9 | 6.5 | 10 | 5.5 | 10 | 10 | 10 | **8.7** | NONE |
| 94 | [ls_learning](ls_learning.md) | 8.5 | 6.5 | 10 | 6 | 10 | 10 | 10 | **8.7** | NONE |
| 95 | [market_diffusion](market_diffusion.md) | 10 | 4.5 | 8.5 | 8 | 10 | 10 | 10 | **8.7** | NONE |
| 96 | [robust_permanent_income](robust_permanent_income.md) | 7.5 | 10 | 7.5 | 6 | 10 | 10 | 10 | **8.7** | NONE |
| 97 | [ak2](ak2.md) | 6.5 | 10 | 10 | 5 | 10 | 10 | 10 | **8.8** | NONE |
| 98 | [ar1_turningpts](ar1_turningpts.md) | 4.5 | 10 | 10 | 8 | 10 | 10 | — | **8.8** | NONE |
| 99 | [chow_business_cycles](chow_business_cycles.md) | 9 | 6.5 | 10 | 6 | 10 | 10 | 10 | **8.8** | NONE |
| 100 | [house_auction](house_auction.md) | 3 | 10 | 10 | — | 10 | 10 | 10 | **8.8** | HIGH |
| 101 | [jv](jv.md) | 6 | 10 | 10 | 6.5 | 9 | 10 | 10 | **8.8** | NONE |
| 102 | [mccall_fitted_vfi](mccall_fitted_vfi.md) | 9 | 8 | 10 | 5.5 | 9 | 10 | 10 | **8.8** | NONE |
| 103 | [phillips_priors](phillips_priors.md) | 9 | 10 | 10 | 5.5 | 7 | 10 | 10 | **8.8** | NONE |
| 104 | [theil_1](theil_1.md) | 9 | 7.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.8** | NONE |
| 105 | [bayes_nonconj](bayes_nonconj.md) | 8 | 10 | 10 | 6.5 | — | 9 | 10 | **8.9** | NONE |
| 106 | [learning_approximation](learning_approximation.md) | 10 | 7.5 | 9 | 6 | 10 | 10 | 10 | **8.9** | NONE |
| 107 | [lq_robust_smoothing](lq_robust_smoothing.md) | 10 | 7.5 | 7 | 7.5 | 10 | 10 | 10 | **8.9** | NONE |
| 108 | [marimon_mcgrattan_sargent](marimon_mcgrattan_sargent.md) | 6 | 10 | 10 | 7.5 | 8.5 | 10 | 10 | **8.9** | NONE |
| 109 | [mccall_model_with_sep_markov](mccall_model_with_sep_markov.md) | 8 | 10 | 10 | 5.5 | — | 10 | 10 | **8.9** | NONE |
| 110 | [mccall_model_with_separation](mccall_model_with_separation.md) | 9.5 | 5 | 9 | 8.5 | 10 | 10 | 10 | **8.9** | NONE |
| 111 | [mix_model](mix_model.md) | 10 | 10 | 7 | 6.5 | — | 10 | 10 | **8.9** | NONE |
| 112 | [os_egm](os_egm.md) | 7 | 7.5 | 8.5 | 9 | 10 | 10 | 10 | **8.9** | NONE |
| 113 | [phillips_escaping_nash](phillips_escaping_nash.md) | 9 | 10 | 10 | 4.5 | 8.5 | 10 | 10 | **8.9** | NONE |
| 114 | [phillips_learning](phillips_learning.md) | 9 | 10 | 10 | 6 | 7 | 10 | 10 | **8.9** | NONE |
| 115 | [theil_2](theil_2.md) | 7.5 | 8 | 8.5 | 8.5 | 10 | 10 | 10 | **8.9** | NONE |
| 116 | [hoist_failure](hoist_failure.md) | 7.5 | 7.5 | 10 | 8 | 10 | 10 | 10 | **9.0** | NONE |
| 117 | [kalman_filter_var](kalman_filter_var.md) | 10 | 8 | 8.5 | 6.5 | 10 | 10 | 10 | **9.0** | NONE |
| 118 | [lq_robust_bewley](lq_robust_bewley.md) | 10 | 5.5 | 10 | 7.5 | 10 | 10 | 10 | **9.0** | NONE |
| 119 | [phillips_credible_policies](phillips_credible_policies.md) | 8.5 | 10 | 10 | 5.5 | 10 | 9 | 10 | **9.0** | NONE |
| 120 | [rational_learning_re](rational_learning_re.md) | 10 | 8.5 | 8.5 | 7 | 10 | 10 | 9 | **9.0** | NONE |
| 121 | [ar1_bayes](ar1_bayes.md) | 10 | 10 | 7.5 | 8 | 10 | 8 | 10 | **9.1** | NONE |
| 122 | [lq_permanent_income](lq_permanent_income.md) | 9.5 | 7.5 | 10 | 6.5 | 10 | 10 | 10 | **9.1** | NONE |
| 123 | [morris_learn](morris_learn.md) | 5 | 10 | 10 | 10 | 8.5 | 10 | 10 | **9.1** | NONE |
| 124 | [organization_capital](organization_capital.md) | 7.5 | 7.5 | 10 | 9 | 10 | 10 | 10 | **9.1** | NONE |
| 125 | [phillips_adaptive](phillips_adaptive.md) | 10 | 10 | 9 | 6.5 | 8.5 | 10 | 10 | **9.1** | NONE |
| 126 | [unemployment_linear](unemployment_linear.md) | 9 | 8.5 | 9 | 8.5 | 9 | 10 | 10 | **9.1** | NONE |
| 127 | [career](career.md) | 8 | 10 | 10 | 6.5 | 10 | 10 | 10 | **9.2** | NONE |
| 128 | [likelihood_bayes](likelihood_bayes.md) | 8.5 | 10 | 8.5 | 7.5 | 10 | 10 | 10 | **9.2** | NONE |
| 129 | [os_egm_jax](os_egm_jax.md) | 10 | 10 | 8.5 | 7 | — | 10 | 10 | **9.2** | NONE |
| 130 | [phillips_credibility](phillips_credibility.md) | 9 | 10 | 10 | 7 | 8.5 | 10 | 10 | **9.2** | NONE |
| 131 | [phillips_misspecified](phillips_misspecified.md) | 10 | 10 | 10 | 6.5 | 8.5 | 10 | 10 | **9.3** | NONE |
| 132 | [phillips_self_confirming](phillips_self_confirming.md) | 10 | 10 | 9 | 6 | 10 | 10 | 10 | **9.3** | NONE |
| 133 | [rand_resp](rand_resp.md) | 6.5 | 10 | 10 | — | 10 | 10 | — | **9.3** | NONE |
| 134 | [bounded_rationality](bounded_rationality.md) | 9.5 | 10 | 10 | 6.5 | 10 | 10 | 10 | **9.4** | NONE |
| 135 | [exchange_rate_learning](exchange_rate_learning.md) | 10 | 10 | 10 | 5.5 | 10 | 10 | 10 | **9.4** | NONE |
| 136 | [genetic_classifier](genetic_classifier.md) | 8.5 | 10 | 10 | 7 | 10 | 10 | 10 | **9.4** | NONE |
| 137 | [harrison_kreps](harrison_kreps.md) | 8 | 8.5 | 10 | — | 10 | 10 | 10 | **9.4** | NONE |
| 138 | [inventory_dynamics](inventory_dynamics.md) | 9 | 10 | 9.5 | 7 | 10 | 10 | 10 | **9.4** | NONE |
| 139 | [lq_bewley_complete_markets](lq_bewley_complete_markets.md) | 9.5 | 10 | 10 | 6 | 10 | 10 | 10 | **9.4** | NONE |
| 140 | [mccall_persist_trans](mccall_persist_trans.md) | 10 | 10 | 10 | 8 | 10 | 10 | 10 | **9.7** | NONE |
| 141 | [status](status.md) | 10 | — | 9 | — | — | 10 | — | **9.7** | NONE |
| 142 | [prospects_bounded_rationality](prospects_bounded_rationality.md) | 10 | 10 | 10 | 8.5 | 10 | 10 | — | **9.8** | NONE |
| 143 | [unemployment_shocks](unemployment_shocks.md) | 10 | 10 | 9 | 10 | — | 10 | 10 | **9.8** | NONE |
| 144 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 145 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
