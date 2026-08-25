# Summary

Style audit of the **lecture-dp** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-07
- **Corpus snapshot:** `c30490a2f4`
- **Lectures audited:** 52
- **Average overall score:** 8.2 / 10
- **Average per-category scores:** writing 7.0, math 6.4, code 9.0, figures 6.4, references 9.3, links 9.5, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
_The series-level reading of these numbers goes here._
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 15    | 28.8% |
| MEDIUM   | 2     | 3.8% |
| LOW      | 16    | 30.8% |
| NONE     | 19    | 36.5% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **42 / 52** lectures, 164 occurrences.
2. **`qe-writing-008`** — Remove excessive whitespace between words — **40 / 52** lectures, 1578 occurrences.
3. **`qe-fig-008`** — Use lw=2 for line charts — **39 / 52** lectures, 252 occurrences.
4. **`qe-fig-001`** — Do not set figure size unless necessary — **31 / 52** lectures, 102 occurrences.
5. **`qe-math-002`** — Use \top for transpose notation — **31 / 52** lectures, 509 occurrences.
6. **`qe-fig-003`** — No matplotlib embedded titles — **30 / 52** lectures, 105 occurrences.
7. **`qe-writing-001`** — Use one sentence per paragraph — **23 / 52** lectures, 44 occurrences.
8. **`qe-ref-001`** — Use correct citation style — **22 / 52** lectures, 49 occurrences.
9. **`qe-writing-006`** — Capitalize lecture titles properly — **22 / 52** lectures, 141 occurrences.
10. **`qe-code-002`** — Use Unicode symbols for Greek letters in code — **21 / 52** lectures, 56 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-001`** — Use gated syntax for executable code in exercises
- **`qe-admon-002`** — Use dropdown class for solutions
- **`qe-admon-003`** — Use tick count management for nested directives
- **`qe-fig-004`** — Caption formatting conventions
- **`qe-fig-007`** — Keep figure box and spines
- **`qe-fig-010`** — Plotly figures require latex directive
- **`qe-link-001`** — Use markdown style links for lectures in same lecture series
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
| 1 | [cross_product_trick](cross_product_trick.md) | 6 | 3 | — | — | — | 10 | — | **6.3** | HIGH |
| 2 | [lqcontrol](lqcontrol.md) | 4 | 3 | 7.5 | 4.5 | 9 | 8 | 10 | **6.6** | HIGH |
| 3 | [rs_inventory_q](rs_inventory_q.md) | 5 | 4.5 | 10 | 5 | — | 10 | — | **6.9** | MEDIUM |
| 4 | [cons_news](cons_news.md) | 5.5 | 4.5 | 8.5 | 6 | 10 | 7.5 | — | **7.0** | MEDIUM |
| 5 | [markov_jump_lq](markov_jump_lq.md) | 8.5 | 3 | 7.5 | 5.5 | 8.5 | 9 | — | **7.0** | HIGH |
| 6 | [lagrangian_lqdp](lagrangian_lqdp.md) | 3.5 | 3 | 8.5 | — | 10 | 7.5 | 10 | **7.1** | HIGH |
| 7 | [perm_income_cons](perm_income_cons.md) | 4.5 | 4.5 | 9 | 5.5 | 10 | 9 | — | **7.1** | LOW |
| 8 | [ifp_advanced](ifp_advanced.md) | 4.5 | 3 | 7.5 | 7 | 8.5 | 10 | 10 | **7.2** | HIGH |
| 9 | [smoothing](smoothing.md) | 6.5 | 4.5 | 10 | 5 | 10 | 7.5 | — | **7.2** | LOW |
| 10 | [tax_smoothing_1](tax_smoothing_1.md) | 8.5 | 4.5 | 7.5 | 6 | 7.5 | 9 | — | **7.2** | LOW |
| 11 | [mccall_model](mccall_model.md) | 4 | 3 | 10 | 6 | 10 | 8 | 10 | **7.3** | HIGH |
| 12 | [tax_smoothing_2](tax_smoothing_2.md) | 9 | 4 | 8.5 | 4 | 8.5 | 10 | — | **7.3** | HIGH |
| 13 | [discrete_dp](discrete_dp.md) | 8.5 | 4 | 8 | 6 | 9 | 7 | 10 | **7.5** | HIGH |
| 14 | [perm_income](perm_income.md) | 3.5 | 4.5 | 10 | 6 | 8.5 | 10 | 10 | **7.5** | HIGH |
| 15 | [dyn_stack](dyn_stack.md) | 8 | 5 | 8.5 | 4.5 | 10 | 7.5 | 10 | **7.6** | LOW |
| 16 | [inventory_q](inventory_q.md) | 5.5 | 4 | 10 | 6 | 10 | 10 | — | **7.6** | HIGH |
| 17 | [mccall_q](mccall_q.md) | 4 | 5.5 | 10 | 7 | 9 | 10 | — | **7.6** | HIGH |
| 18 | [calvo](calvo.md) | 6 | 5.5 | 9 | 7 | 8.5 | 8 | 10 | **7.7** | LOW |
| 19 | [lq_inventories](lq_inventories.md) | 5.5 | 3 | 9 | 7 | 10 | 10 | 10 | **7.8** | HIGH |
| 20 | [odu](odu.md) | 5 | 10 | 7.5 | 5 | 9 | 8 | 10 | **7.8** | LOW |
| 21 | [opt_tax_recur](opt_tax_recur.md) | 7 | 5 | 10 | 4.5 | 9 | 10 | 10 | **7.9** | LOW |
| 22 | [chang_ramsey](chang_ramsey.md) | 6 | 7.5 | 10 | 6 | 8.5 | 10 | — | **8.0** | LOW |
| 23 | [calvo_machine_learn](calvo_machine_learn.md) | 8 | 3.5 | 7 | 8 | 10 | 10 | 10 | **8.1** | HIGH |
| 24 | [ifp_egm_transient_shocks](ifp_egm_transient_shocks.md) | 6 | 7.5 | 9 | 5.5 | 8.5 | 10 | 10 | **8.1** | LOW |
| 25 | [ifp_opi](ifp_opi.md) | 6.5 | 10 | 7 | 6 | — | 9 | 10 | **8.1** | LOW |
| 26 | [os_stochastic](os_stochastic.md) | 4.5 | 7.5 | 9.5 | 7.5 | 10 | 8 | 10 | **8.1** | LOW |
| 27 | [ifp_egm](ifp_egm.md) | 6 | 7.5 | 9 | 6.5 | 9 | 10 | 10 | **8.3** | LOW |
| 28 | [tax_smoothing_3](tax_smoothing_3.md) | 9 | 9 | 8.5 | 5 | 8.5 | 10 | — | **8.3** | LOW |
| 29 | [lqramsey](lqramsey.md) | 9 | 3 | 10 | 7 | 10 | 10 | 10 | **8.4** | HIGH |
| 30 | [os_time_iter](os_time_iter.md) | 7.5 | 5 | 9.5 | 8 | 9 | 10 | 10 | **8.4** | LOW |
| 31 | [smoothing_tax](smoothing_tax.md) | 7 | 8.5 | 10 | 4 | 10 | 9 | 10 | **8.4** | HIGH |
| 32 | [amss](amss.md) | 7 | 7 | 9.5 | 6 | 10 | 10 | 10 | **8.5** | LOW |
| 33 | [ifp_discrete](ifp_discrete.md) | 7.5 | 6 | 7.5 | 8.5 | 10 | 10 | 10 | **8.5** | LOW |
| 34 | [amss3](amss3.md) | 8.5 | 9 | 10 | 5.5 | 7.5 | 10 | 10 | **8.6** | NONE |
| 35 | [os](os.md) | 7 | 5.5 | 10 | 8 | 10 | 10 | 10 | **8.6** | NONE |
| 36 | [os_numerical](os_numerical.md) | 6 | 10 | 10 | 5.5 | — | 10 | 10 | **8.6** | NONE |
| 37 | [chang_credible](chang_credible.md) | 5 | 7.5 | 10 | 9.5 | 10 | 10 | — | **8.7** | NONE |
| 38 | [os_egm](os_egm.md) | 7 | 7.5 | 7.5 | 9 | 10 | 10 | 10 | **8.7** | NONE |
| 39 | [amss2](amss2.md) | 8.5 | 10 | 10 | 6 | 8.5 | 10 | — | **8.8** | NONE |
| 40 | [calvo_abreu](calvo_abreu.md) | 8 | 9 | 8 | 9 | 8.5 | 10 | — | **8.8** | NONE |
| 41 | [jv](jv.md) | 6 | 10 | 10 | 6.5 | 9 | 10 | 10 | **8.8** | NONE |
| 42 | [mccall_fitted_vfi](mccall_fitted_vfi.md) | 9 | 8 | 10 | 5.5 | 9 | 10 | 10 | **8.8** | NONE |
| 43 | [mccall_model_with_sep_markov](mccall_model_with_sep_markov.md) | 8 | 10 | 10 | 5.5 | — | 10 | 10 | **8.9** | NONE |
| 44 | [mccall_model_with_separation](mccall_model_with_separation.md) | 9.5 | 5 | 9 | 8.5 | 10 | 10 | 10 | **8.9** | NONE |
| 45 | [un_insure](un_insure.md) | 8 | 10 | 10 | 5.5 | 9 | 10 | 10 | **8.9** | NONE |
| 46 | [career](career.md) | 8 | 10 | 8.5 | 6.5 | 10 | 10 | 10 | **9.0** | NONE |
| 47 | [os_egm_jax](os_egm_jax.md) | 10 | 10 | 7.5 | 7 | — | 10 | 10 | **9.1** | NONE |
| 48 | [mccall_persist_trans](mccall_persist_trans.md) | 10 | 10 | 10 | 8 | 10 | 10 | 10 | **9.7** | NONE |
| 49 | [short_path](short_path.md) | 10 | 10 | 10 | 8 | — | 10 | 10 | **9.7** | NONE |
| 50 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 51 | [status](status.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 52 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
