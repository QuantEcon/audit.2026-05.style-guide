# Summary

Style audit of the **lecture-python-advanced.myst** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-19
- **Corpus snapshot:** `b83d6da399`
- **Lectures audited:** 68
- **Average overall score:** 8.1 / 10
- **Average per-category scores:** writing 7.3, math 5.9, code 9.3, figures 6.2, references 9.0, links 9.6, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
_The series-level reading of these numbers goes here._
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 29    | 42.6% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 21    | 30.9% |
| NONE     | 18    | 26.5% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **59 / 68** lectures, 234 occurrences.
2. **`qe-writing-008`** — Remove excessive whitespace between words — **53 / 68** lectures, 2144 occurrences.
3. **`qe-fig-001`** — Do not set figure size unless necessary — **47 / 68** lectures, 215 occurrences.
4. **`qe-fig-008`** — Use lw=2 for line charts — **46 / 68** lectures, 324 occurrences.
5. **`qe-writing-001`** — Use one sentence per paragraph — **42 / 68** lectures, 155 occurrences.
6. **`qe-ref-001`** — Use correct citation style — **39 / 68** lectures, 139 occurrences.
7. **`qe-fig-003`** — No matplotlib embedded titles — **36 / 68** lectures, 149 occurrences.
8. **`qe-math-002`** — Use \top for transpose notation — **35 / 68** lectures, 941 occurrences.
9. **`qe-math-010`** *(proposed)* — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces — **28 / 68** lectures, 485 occurrences.
10. **`qe-writing-004`** — Avoid unnecessary capitalization in narrative text — **24 / 68** lectures, 109 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-001`** — Use gated syntax for executable code in exercises
- **`qe-admon-002`** — Use dropdown class for solutions
- **`qe-admon-003`** — Use tick count management for nested directives
- **`qe-math-001`** — Prefer UTF-8 unicode for simple parameter mentions, be consistent
- **`qe-math-007`** — Use automatic equation numbering, not manual tags
- **`qe-math-012`** *(proposed)* — Multiplication via \cdot or juxtaposition, never *
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
| 1 | [hs_recursive_models](hs_recursive_models.md) | 3 | 3 | — | — | 8.5 | 10 | — | **6.1** | HIGH |
| 2 | [entropy](entropy.md) | 5.5 | 4 | — | 8.5 | 7.5 | 8.5 | — | **6.8** | HIGH |
| 3 | [match_transport](match_transport.md) | 7 | 7.5 | 7.5 | 3 | 7.5 | 8 | — | **6.8** | HIGH |
| 4 | [asset_pricing_lph](asset_pricing_lph.md) | 5.5 | 3 | 7 | 7.5 | 7.5 | 7.5 | 10 | **6.9** | HIGH |
| 5 | [markov_jump_lq](markov_jump_lq.md) | 8.5 | 3 | 7.5 | 5 | 7.5 | 10 | — | **6.9** | HIGH |
| 6 | [black_litterman](black_litterman.md) | 5 | 3 | 10 | 3.5 | 10 | 8.5 | 10 | **7.1** | HIGH |
| 7 | [knowing_forecasts_of_others](knowing_forecasts_of_others.md) | 4 | 3 | 10 | 9 | 7 | 10 | — | **7.2** | HIGH |
| 8 | [tax_smoothing_1](tax_smoothing_1.md) | 8.5 | 4.5 | 7.5 | 6 | 7 | 10 | — | **7.2** | LOW |
| 9 | [tax_smoothing_2](tax_smoothing_2.md) | 9 | 4 | 8.5 | 4 | 8.5 | 10 | — | **7.3** | HIGH |
| 10 | [BCG_incomplete_mkts](BCG_incomplete_mkts.md) | 5.5 | 5 | 10 | 5 | 9 | 10 | — | **7.4** | LOW |
| 11 | [cons_news](cons_news.md) | 5.5 | 4.5 | 8.5 | 6 | 10 | 10 | — | **7.4** | LOW |
| 12 | [robustness](robustness.md) | 6 | 3 | 9 | 6.5 | 10 | 7.5 | 10 | **7.4** | HIGH |
| 13 | [subjective_beliefs_business_cycles](subjective_beliefs_business_cycles.md) | 4.5 | 3 | 9 | 6.5 | 9 | 10 | 10 | **7.4** | HIGH |
| 14 | [risk_aversion_or_mistaken_beliefs](risk_aversion_or_mistaken_beliefs.md) | 6.5 | 3 | 10 | 3 | 10 | 10 | 10 | **7.5** | HIGH |
| 15 | [additive_functionals](additive_functionals.md) | 9 | 4 | 10 | 3.5 | 8.5 | 8 | 10 | **7.6** | HIGH |
| 16 | [discrete_dp](discrete_dp.md) | 8.5 | 4 | 8 | 6 | 9 | 7.5 | 10 | **7.6** | HIGH |
| 17 | [dovis_accounting_mf](dovis_accounting_mf.md) | 6 | 3 | 10 | 4.5 | 10 | 10 | 10 | **7.6** | HIGH |
| 18 | [tsyrennikov_2013](tsyrennikov_2013.md) | 6.5 | 3 | 9 | 5 | 10 | 10 | 10 | **7.6** | HIGH |
| 19 | [calvo](calvo.md) | 6 | 5.5 | 9 | 6 | 7.5 | 10 | 10 | **7.7** | LOW |
| 20 | [dyn_stack](dyn_stack.md) | 8 | 5 | 8.5 | 4.5 | 10 | 8 | 10 | **7.7** | LOW |
| 21 | [rob_markov_perf](rob_markov_perf.md) | 8 | 4 | 7.5 | 8 | 8.5 | 10 | — | **7.7** | HIGH |
| 22 | [stationary_densities](stationary_densities.md) | 7 | 6.5 | 8.5 | 6 | 8.5 | 7.5 | 10 | **7.7** | LOW |
| 23 | [smoothing](smoothing.md) | 6.5 | 4.5 | 10 | 5.5 | 10 | 10 | — | **7.8** | LOW |
| 24 | [cagan_rational_expectations](cagan_rational_expectations.md) | 9.5 | 3 | 8.5 | 5.5 | 8.5 | 10 | 10 | **7.9** | HIGH |
| 25 | [chang_ramsey](chang_ramsey.md) | 6 | 7.5 | 10 | 5.5 | 8.5 | 10 | — | **7.9** | LOW |
| 26 | [classical_filtering](classical_filtering.md) | 6.5 | 3.5 | 10 | — | 7.5 | 10 | 10 | **7.9** | HIGH |
| 27 | [five_preferences](five_preferences.md) | 6.5 | 10 | 10 | 4 | 7 | 10 | — | **7.9** | HIGH |
| 28 | [opt_tax_recur](opt_tax_recur.md) | 7 | 5 | 10 | 4.5 | 9 | 10 | 10 | **7.9** | LOW |
| 29 | [gorman_heterogeneous_households](gorman_heterogeneous_households.md) | 4 | 8.5 | 8.5 | 5 | 10 | 10 | 10 | **8.0** | HIGH |
| 30 | [growth_in_dles](growth_in_dles.md) | 4.5 | 7.5 | 10 | 7 | 9 | 10 | — | **8.0** | LOW |
| 31 | [orth_proj](orth_proj.md) | 6 | 3 | 10 | 7 | 10 | 10 | 10 | **8.0** | HIGH |
| 32 | [BCG_complete_mkts](BCG_complete_mkts.md) | 6.5 | 7.5 | 9.5 | 5.5 | 10 | 8 | 10 | **8.1** | LOW |
| 33 | [arellano](arellano.md) | 9 | 3.5 | 8.5 | 7 | 9 | 10 | 10 | **8.1** | HIGH |
| 34 | [calvo_machine_learn](calvo_machine_learn.md) | 8 | 3.5 | 7 | 8 | 10 | 10 | 10 | **8.1** | HIGH |
| 35 | [doubts_or_variability](doubts_or_variability.md) | 7 | 3 | 10 | 8 | 8.5 | 10 | 10 | **8.1** | HIGH |
| 36 | [hansen_richard_1987](hansen_richard_1987.md) | 3.5 | 5 | 8.5 | 9.5 | 10 | 10 | 10 | **8.1** | HIGH |
| 37 | [repeat_mh](repeat_mh.md) | 6 | 3 | 9.5 | 8.5 | 10 | 10 | 10 | **8.1** | HIGH |
| 38 | [arma](arma.md) | 8 | 7.5 | 10 | 6 | 9 | 9 | — | **8.2** | LOW |
| 39 | [cattle_cycles](cattle_cycles.md) | 9.5 | 7 | 10 | 5 | 8.5 | 10 | — | **8.3** | LOW |
| 40 | [hs_invertibility_example](hs_invertibility_example.md) | 9 | 7.5 | 10 | 5 | 8.5 | 10 | — | **8.3** | LOW |
| 41 | [tax_smoothing_3](tax_smoothing_3.md) | 9 | 9 | 8.5 | 5 | 8.5 | 10 | — | **8.3** | LOW |
| 42 | [info_projection](info_projection.md) | 8 | 3.5 | 10 | 8 | 9 | 10 | 10 | **8.4** | HIGH |
| 43 | [lqramsey](lqramsey.md) | 9 | 3 | 10 | 6.5 | 10 | 10 | 10 | **8.4** | HIGH |
| 44 | [lucas_asset_pricing_dles](lucas_asset_pricing_dles.md) | 9.5 | 5.5 | 10 | 7 | 8.5 | 10 | — | **8.4** | LOW |
| 45 | [amss](amss.md) | 7 | 7 | 9.5 | 6 | 10 | 10 | 10 | **8.5** | LOW |
| 46 | [atkeson_1991](atkeson_1991.md) | 10 | 5 | 9 | 5.5 | 10 | 10 | 10 | **8.5** | LOW |
| 47 | [chang_credible](chang_credible.md) | 5 | 7.5 | 10 | 8.5 | 10 | 10 | — | **8.5** | LOW |
| 48 | [irfs_in_hall_model](irfs_in_hall_model.md) | 6 | 9 | 10 | 7 | 9 | 10 | — | **8.5** | LOW |
| 49 | [permanent_income_dles](permanent_income_dles.md) | 7 | 7.5 | 10 | 8 | 8.5 | 10 | — | **8.5** | LOW |
| 50 | [smoothing_tax](smoothing_tax.md) | 7 | 8.5 | 10 | 4 | 10 | 10 | 10 | **8.5** | HIGH |
| 51 | [amss3](amss3.md) | 8.5 | 9 | 10 | 5.5 | 7.5 | 10 | 10 | **8.6** | NONE |
| 52 | [calvo_abreu](calvo_abreu.md) | 8 | 9 | 8 | 8 | 8.5 | 10 | — | **8.6** | NONE |
| 53 | [coase](coase.md) | 7.5 | 10 | 7.5 | 7 | 8.5 | 10 | 10 | **8.6** | NONE |
| 54 | [lu_tricks](lu_tricks.md) | 5 | 7 | 10 | 8 | 10 | 10 | 10 | **8.6** | NONE |
| 55 | [matsuyama](matsuyama.md) | 7 | 10 | 9 | 6 | 9 | 9 | 10 | **8.6** | NONE |
| 56 | [amss2](amss2.md) | 8.5 | 10 | 10 | 6 | 8.5 | 10 | — | **8.8** | NONE |
| 57 | [estspec](estspec.md) | 7.5 | 10 | 10 | 5 | 9 | 10 | 10 | **8.8** | NONE |
| 58 | [muth_kalman](muth_kalman.md) | 8.5 | 7.5 | 10 | 5.5 | 10 | 10 | 10 | **8.8** | NONE |
| 59 | [troubleshooting](troubleshooting.md) | 8.5 | — | — | 9 | — | 9 | — | **8.8** | NONE |
| 60 | [mcmc](mcmc.md) | 8.5 | 7 | 10 | 7 | 10 | 10 | 10 | **8.9** | NONE |
| 61 | [rosen_schooling_model](rosen_schooling_model.md) | 7.5 | 10 | 10 | 6 | 9 | 10 | 10 | **8.9** | NONE |
| 62 | [un_insure](un_insure.md) | 8 | 10 | 10 | 5.5 | 8.5 | 10 | 10 | **8.9** | NONE |
| 63 | [hansen_jagannathan_1991](hansen_jagannathan_1991.md) | 10 | 5 | 10 | 8.5 | 10 | 10 | 10 | **9.1** | NONE |
| 64 | [supply_demand_var](supply_demand_var.md) | 10 | 10 | 8.5 | 6 | 10 | 10 | 10 | **9.2** | NONE |
| 65 | [lucas_model](lucas_model.md) | 10 | 10 | 10 | 7.5 | 10 | 9 | 10 | **9.5** | NONE |
| 66 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 67 | [status](status.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 68 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
