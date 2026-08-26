# Summary

Style audit of the **lecture-python-advanced.myst** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-19
- **Corpus snapshot:** `b83d6da399`
- **Lectures audited:** 68
- **Average overall score:** 7.4 / 10
- **Average per-category scores:** writing 4.6, math 5.9, code 7.4, figures 6.3, references 9.2, links 9.2, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
- **Judgment-review coverage:** **66 of 68 reviewed** — scores for the unreviewed 2 reflect the 41 measured rules only, so they are not directly comparable with the reviewed ones.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
The weakest series (8.1) and the one with the clearest single cause. **Math scores 5.9 —
the lowest category average anywhere in the corpus** — and it is the floor for **22 of the
29 HIGH lectures**. Figures (4) and Writing (3) account for the rest.

The Math problem is notation debt in the older LQ, filtering and robustness material, and
it is concentrated in two rules: `qe-math-002` in 35 of 68 lectures with **941
occurrences**, and `qe-math-010` *(proposed)* in 28 with 485. Those are the densest
per-lecture counts of either rule in the corpus. `hs_recursive_models` at **5.6** is the
lowest-scoring lecture in all 348.

Everything else here is ordinary: `qe-fig-005` (54 / 68), `qe-writing-008` (53 / 68, 2,144
occurrences) and `qe-fig-001` (47 / 68) look much like the other series. Fix the maths and
this series stops being the outlier.
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 44    | 64.7% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 19    | 27.9% |
| NONE     | 5     | 7.4% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **54 / 68** lectures, 203 occurrences.
2. **`qe-writing-008`** — Remove excessive whitespace between words — **53 / 68** lectures, 2223 occurrences.
3. **`qe-fig-001`** — Do not set figure size unless necessary — **47 / 68** lectures, 215 occurrences.
4. **`qe-fig-008`** — Use lw=2 for line charts — **43 / 68** lectures, 360 occurrences.
5. **`qe-writing-001`** — Use one sentence per paragraph — **42 / 68** lectures, 155 occurrences.
6. **`qe-fig-003`** — No matplotlib embedded titles — **36 / 68** lectures, 149 occurrences.
7. **`qe-ref-001`** — Use correct citation style — **35 / 68** lectures, 93 occurrences.
8. **`qe-math-010`** *(proposed)* — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces — **31 / 68** lectures, 525 occurrences.
9. **`qe-link-002`** — Use doc links for cross-series references — **26 / 68** lectures, 94 occurrences.
10. **`qe-writing-004`** — Avoid unnecessary capitalization in narrative text — **24 / 68** lectures, 109 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-002`** — Use dropdown class for solutions
- **`qe-admon-003`** — Use tick count management for nested directives
- **`qe-math-007`** — Use automatic equation numbering, not manual tags
- **`qe-math-012`** *(proposed)* — Multiplication via \cdot or juxtaposition, never *
<!-- /qe:series-clean -->

## Series-level recommendations

<!-- qe:series-recommendations -->
1. **`qe-math-002` — transpose notation** (35 / 68, **941 occurrences**). The largest
   concentration of any rule in any series. Replace `'` and `^T` with `^\top`. Worth doing
   as one pass over the LQ/filtering cluster rather than lecture by lecture, so the
   notation stays consistent within a topic.
2. **`qe-math-010` *(proposed)* — expectation and probability operators** (28 / 68, 485
   occurrences). `\mathbb{E}` / `\mathbb{P}` / `\mathbb{V}`, with braces. Same cluster,
   same pass.
3. **`qe-math-003` — `bmatrix` for matrices** (15 / 68, 113 blocks) and **`qe-math-011`
   *(proposed)*** — plain `N` rather than `\mathcal{N}` (12 / 68). Both fall out naturally
   while doing items 1–2.
4. **Items 1–3 together should clear most of the 22 Math-floored HIGH lectures**, which is
   three quarters of the series' HIGH list. Nothing else here has comparable leverage.
5. **`qe-fig-005` — name the figures** (54 / 68, 203 figures) and **`qe-writing-008`**
   (53 / 68, 2,144 occurrences). Routine sweeps, best kept in separate commits from the
   maths so the notation diff stays reviewable.
6. **Start with `hs_recursive_models`** (5.6, the corpus minimum), then
   `knowing_forecasts_of_others` and `match_transport` (6.9 each) and `asset_pricing_lph`
   (7.0).
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [hs_recursive_models](hs_recursive_models.md) | 3 | 3 | — | — | 8.5 | 8 | — | **5.6** | HIGH |
| 2 | [markov_jump_lq](markov_jump_lq.md) | 5 | 3 | 5 | 5.5 | 8.5 | 9 | — | **6.0** | HIGH |
| 3 | [smoothing](smoothing.md) | 3 | 3 | 7.5 | 5 | 10 | 7.5 | — | **6.0** | HIGH |
| 4 | [tax_smoothing_1](tax_smoothing_1.md) | 4 | 4.5 | 5.5 | 6 | 7.5 | 9 | — | **6.1** | HIGH |
| 5 | [five_preferences](five_preferences.md) | 3 | 6 | 7 | 4 | 7 | 10 | — | **6.2** | HIGH |
| 6 | [knowing_forecasts_of_others](knowing_forecasts_of_others.md) | 3 | 3 | 7 | 9 | 7.5 | 8 | — | **6.2** | HIGH |
| 7 | [match_transport](match_transport.md) | 3 | 9.5 | 5 | 3 | 8.5 | 8 | — | **6.2** | HIGH |
| 8 | [tax_smoothing_2](tax_smoothing_2.md) | 5 | 3.5 | 6.5 | 4 | 8.5 | 10 | — | **6.2** | HIGH |
| 9 | [cons_news](cons_news.md) | 3 | 4.5 | 7 | 6 | 10 | 7.5 | — | **6.3** | HIGH |
| 10 | [entropy](entropy.md) | 3 | 3 | — | 8.5 | 8.5 | 8.5 | — | **6.3** | HIGH |
| 11 | [asset_pricing_lph](asset_pricing_lph.md) | 3 | 3 | 5.5 | 7.5 | 8.5 | 7.5 | 10 | **6.4** | HIGH |
| 12 | [rob_markov_perf](rob_markov_perf.md) | 3.5 | 4 | 6.5 | 8 | 9 | 7.5 | — | **6.4** | HIGH |
| 13 | [black_litterman](black_litterman.md) | 3 | 3 | 7 | 4 | 10 | 8.5 | 10 | **6.5** | HIGH |
| 14 | [additive_functionals](additive_functionals.md) | 5.5 | 3.5 | 7 | 3.5 | 9 | 7.5 | 10 | **6.6** | HIGH |
| 15 | [dyn_stack](dyn_stack.md) | 3.5 | 4 | 6.5 | 4.5 | 10 | 7.5 | 10 | **6.6** | HIGH |
| 16 | [robustness](robustness.md) | 3 | 3 | 7 | 6.5 | 10 | 7.5 | 10 | **6.7** | HIGH |
| 17 | [cagan_rational_expectations](cagan_rational_expectations.md) | 5.5 | 3 | 6.5 | 5.5 | 8.5 | 10 | 10 | **7.0** | HIGH |
| 18 | [calvo](calvo.md) | 3 | 5.5 | 7 | 7 | 8.5 | 8 | 10 | **7.0** | HIGH |
| 19 | [smoothing_tax](smoothing_tax.md) | 4 | 4.5 | 7.5 | 4 | 10 | 9 | 10 | **7.0** | HIGH |
| 20 | [BCG_incomplete_mkts](BCG_incomplete_mkts.md) | 3 | 7.5 | 7.5 | 4.5 | 10 | 10 | — | **7.1** | HIGH |
| 21 | [calvo_machine_learn](calvo_machine_learn.md) | 3.5 | 3 | 5.5 | 8 | 10 | 10 | 10 | **7.1** | HIGH |
| 22 | [stationary_densities](stationary_densities.md) | 4 | 6 | 7 | 6 | 9 | 7.5 | 10 | **7.1** | HIGH |
| 23 | [hs_invertibility_example](hs_invertibility_example.md) | 5.5 | 7 | 7.5 | 5 | 8.5 | 10 | — | **7.2** | LOW |
| 24 | [lucas_asset_pricing_dles](lucas_asset_pricing_dles.md) | 5.5 | 4 | 8.5 | 7 | 8.5 | 10 | — | **7.2** | HIGH |
| 25 | [permanent_income_dles](permanent_income_dles.md) | 4 | 7.5 | 7.5 | 8 | 8.5 | 8 | — | **7.2** | HIGH |
| 26 | [subjective_beliefs_business_cycles](subjective_beliefs_business_cycles.md) | 3 | 3 | 8.5 | 7 | 9 | 10 | 10 | **7.2** | HIGH |
| 27 | [amss](amss.md) | 4 | 4 | 7 | 6 | 10 | 10 | 10 | **7.3** | HIGH |
| 28 | [growth_in_dles](growth_in_dles.md) | 3 | 7.5 | 7.5 | 7 | 9 | 10 | — | **7.3** | HIGH |
| 29 | [tax_smoothing_3](tax_smoothing_3.md) | 5.5 | 8.5 | 6.5 | 5 | 8.5 | 10 | — | **7.3** | LOW |
| 30 | [BCG_complete_mkts](BCG_complete_mkts.md) | 3 | 7.5 | 7 | 6 | 10 | 8 | 10 | **7.4** | HIGH |
| 31 | [classical_filtering](classical_filtering.md) | 4.5 | 3.5 | 10 | — | 8.5 | 8 | 10 | **7.4** | HIGH |
| 32 | [discrete_dp](discrete_dp.md) | 6 | 7 | 6.5 | 6 | 9 | 7 | 10 | **7.4** | LOW |
| 33 | [lqramsey](lqramsey.md) | 4 | 3 | 7.5 | 7 | 10 | 10 | 10 | **7.4** | HIGH |
| 34 | [opt_tax_recur](opt_tax_recur.md) | 4.5 | 5.5 | 8.5 | 4.5 | 9 | 10 | 10 | **7.4** | LOW |
| 35 | [orth_proj](orth_proj.md) | 4 | 3 | 10 | 7 | 10 | 8 | 10 | **7.4** | HIGH |
| 36 | [risk_aversion_or_mistaken_beliefs](risk_aversion_or_mistaken_beliefs.md) | 5 | 3 | 10 | 3.5 | 10 | 10 | 10 | **7.4** | HIGH |
| 37 | [amss3](amss3.md) | 3.5 | 8.5 | 7.5 | 5.5 | 7.5 | 10 | 10 | **7.5** | HIGH |
| 38 | [arma](arma.md) | 4.5 | 7.5 | 8.5 | 6.5 | 10 | 8 | — | **7.5** | LOW |
| 39 | [chang_ramsey](chang_ramsey.md) | 3 | 9 | 8.5 | 6 | 8.5 | 10 | — | **7.5** | HIGH |
| 40 | [gorman_heterogeneous_households](gorman_heterogeneous_households.md) | 3 | 8 | 6.5 | 5 | 10 | 10 | 10 | **7.5** | HIGH |
| 41 | [irfs_in_hall_model](irfs_in_hall_model.md) | 3 | 8.5 | 7.5 | 7 | 9 | 10 | — | **7.5** | HIGH |
| 42 | [tsyrennikov_2013](tsyrennikov_2013.md) | 4.5 | 5.5 | 7.5 | 5 | 10 | 10 | 10 | **7.5** | LOW |
| 43 | [amss2](amss2.md) | 3.5 | 10 | 7.5 | 6 | 8.5 | 10 | — | **7.6** | HIGH |
| 44 | [calvo_abreu](calvo_abreu.md) | 4 | 8.5 | 5.5 | 9 | 8.5 | 10 | — | **7.6** | HIGH |
| 45 | [doubts_or_variability](doubts_or_variability.md) | 4 | 3 | 8.5 | 9 | 9 | 10 | 10 | **7.6** | HIGH |
| 46 | [dovis_accounting_mf](dovis_accounting_mf.md) | 4 | 4.5 | 10 | 4.5 | 10 | 10 | 10 | **7.6** | HIGH |
| 47 | [hansen_richard_1987](hansen_richard_1987.md) | 3 | 4 | 6.5 | 9.5 | 10 | 10 | 10 | **7.6** | HIGH |
| 48 | [cattle_cycles](cattle_cycles.md) | 7 | 7 | 9 | 5 | 8.5 | 10 | — | **7.8** | LOW |
| 49 | [lu_tricks](lu_tricks.md) | 3 | 6.5 | 8.5 | 8.5 | 10 | 8 | 10 | **7.8** | HIGH |
| 50 | [info_projection](info_projection.md) | 4.5 | 5 | 8.5 | 8 | 9 | 10 | 10 | **7.9** | LOW |
| 51 | [repeat_mh](repeat_mh.md) | 4 | 6 | 7 | 8.5 | 10 | 10 | 10 | **7.9** | HIGH |
| 52 | [un_insure](un_insure.md) | 4.5 | 9.5 | 7.5 | 5.5 | 9 | 10 | 10 | **8.0** | LOW |
| 53 | [arellano](arellano.md) | 5.5 | 8.5 | 6.5 | 7 | 9 | 10 | 10 | **8.1** | LOW |
| 54 | [coase](coase.md) | 6 | 9 | 6 | 7 | 8.5 | 10 | 10 | **8.1** | LOW |
| 55 | [estspec](estspec.md) | 5 | 9.5 | 7.5 | 5 | 10 | 10 | 10 | **8.1** | LOW |
| 56 | [muth_kalman](muth_kalman.md) | 6 | 6 | 10 | 5.5 | 10 | 9 | 10 | **8.1** | LOW |
| 57 | [atkeson_1991](atkeson_1991.md) | 5.5 | 9.5 | 7 | 5.5 | 10 | 10 | 10 | **8.2** | LOW |
| 58 | [matsuyama](matsuyama.md) | 5 | 10 | 7 | 6.5 | 10 | 9 | 10 | **8.2** | LOW |
| 59 | [hansen_jagannathan_1991](hansen_jagannathan_1991.md) | 6.5 | 5 | 7.5 | 9 | 10 | 10 | 10 | **8.3** | LOW |
| 60 | [mcmc](mcmc.md) | 7 | 5.5 | 7.5 | 8 | 10 | 10 | 10 | **8.3** | LOW |
| 61 | [rosen_schooling_model](rosen_schooling_model.md) | 5.5 | 10 | 7.5 | 6 | 9 | 10 | 10 | **8.3** | LOW |
| 62 | [lucas_model](lucas_model.md) | 6 | 9.5 | 7.5 | 7.5 | 10 | 8 | 10 | **8.4** | LOW |
| 63 | [chang_credible](chang_credible.md) | 3 | 10 | 8.5 | 9.5 | 10 | 10 | — | **8.5** | HIGH |
| 64 | [supply_demand_var](supply_demand_var.md) | 8 | 10 | 6.5 | 6 | 10 | 10 | 10 | **8.6** | NONE |
| 65 | [troubleshooting](troubleshooting.md) | 8.5 | — | — | 9 | — | 9 | — | **8.8** | NONE |
| 66 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 67 | [status](status.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 68 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
