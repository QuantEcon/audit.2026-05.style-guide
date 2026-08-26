# Summary

Style audit of the **lecture-dp** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-07
- **Corpus snapshot:** `c30490a2f4`
- **Lectures audited:** 52
- **Average overall score:** 8.0 / 10
- **Average per-category scores:** writing 5.6, math 6.9, code 8.5, figures 6.4, references 9.3, links 9.5, admon 10.0
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
- **Judgment-review coverage:** **31 of 52 reviewed** — scores for the unreviewed 21 reflect the 41 measured rules only, so they are not directly comparable with the reviewed ones.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
A mid-field series (8.2) with the same shape as `lecture-python-advanced.myst` but less
of it. Math and Figures tie as the weakest categories (6.4 each), and **Math is the floor
for 12 of the 15 HIGH lectures**.

`qe-math-002` is the story: 31 of 52 lectures, **509 occurrences** — the second-densest
transpose debt in the corpus after `lecture-python-advanced.myst`. Beyond it the Math
findings thin out quickly (`qe-math-010` *(proposed)* 16 / 52 but only 63 occurrences), so this is one
rule rather than a cluster.

**A caveat specific to this series.** 31 of these 52 lectures share a filename with a
lecture in `lecture-python.myst` — but only **6 are byte-identical** today
(`cross_product_trick`, `ifp_discrete`, `ifp_opi`, `lq_inventories`,
`mccall_model_with_separation`, `os_numerical`). The other 25 share an origin and have
since diverged. So the two situations need different handling: for the identical 6, a
finding here and a finding there are the same finding, and one upstream fix clears both;
for the diverged 25, the same defect often appears in both copies but each needs its own
fix. `cross_product_trick` (6.3) is in the identical set. `rs_inventory_q` (6.9) is not —
it has drifted from its upstream namesake, so it needs fixing here.
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 28    | 53.8% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 10    | 19.2% |
| NONE     | 14    | 26.9% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **42 / 52** lectures, 164 occurrences.
2. **`qe-writing-008`** — Remove excessive whitespace between words — **40 / 52** lectures, 1578 occurrences.
3. **`qe-fig-008`** — Use lw=2 for line charts — **39 / 52** lectures, 252 occurrences.
4. **`qe-fig-001`** — Do not set figure size unless necessary — **31 / 52** lectures, 102 occurrences.
5. **`qe-fig-003`** — No matplotlib embedded titles — **30 / 52** lectures, 105 occurrences.
6. **`qe-writing-001`** — Use one sentence per paragraph — **23 / 52** lectures, 44 occurrences.
7. **`qe-writing-006`** — Capitalize lecture titles properly — **22 / 52** lectures, 146 occurrences.
8. **`qe-ref-001`** — Use correct citation style — **20 / 52** lectures, 45 occurrences.
9. **`qe-math-010`** *(proposed)* — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces — **18 / 52** lectures, 108 occurrences.
10. **`qe-link-002`** — Use doc links for cross-series references — **15 / 52** lectures, 53 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
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
1. **`qe-math-002` — transpose notation** (31 / 52, 509 occurrences). The dominant
   finding and the floor under most of the HIGH list. `lqcontrol` alone carries 85.
2. **Check whether a lecture is still identical to its upstream namesake before fixing
   it.** `cross_product_trick` is byte-identical to the `lecture-python.myst` copy, so its
   malformed `` {eq}`eq:Kalman102} `` reference at line 133 should be fixed upstream — a
   fix here would be overwritten by the next sync. `rs_inventory_q` and `ifp_advanced`
   have diverged, so they need fixing in this repo as well; `ifp_advanced:158` carries a
   raw `\label{}` inside `$$` in **both** copies, and each needs its own edit.
3. **`qe-fig-005` — name the figures** (42 / 52, 164 figures) and **`qe-fig-008` — `lw=2`**
   (39 / 52, 252 calls). Routine sweeps.
4. **`qe-writing-008` — collapse repeated spaces** (40 / 52, 1,578 occurrences).
5. **`qe-fig-001` — drop `figsize=`** (31 / 52) and **`qe-fig-003` — titles into captions**
   (30 / 52, 105 calls). The second needs a reading pass.
6. **Start with `lqcontrol`** (6.6) — it is the largest genuine (non-synced) Math debt in
   the series, then `cons_news` (7.0).
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [cross_product_trick](cross_product_trick.md) | 4 | 3 | — | — | — | 10 | — | **5.7** | HIGH |
| 2 | [markov_jump_lq](markov_jump_lq.md) | 5 | 3 | 7.5 | 5.5 | 8.5 | 9 | — | **6.4** | HIGH |
| 3 | [cons_news](cons_news.md) | 3 | 4.5 | 8.5 | 6 | 10 | 7.5 | — | **6.6** | HIGH |
| 4 | [lagrangian_lqdp](lagrangian_lqdp.md) | 3 | 3 | 7 | — | 10 | 7.5 | 10 | **6.8** | HIGH |
| 5 | [dyn_stack](dyn_stack.md) | 4 | 5 | 7.5 | 4.5 | 10 | 7.5 | 10 | **6.9** | HIGH |
| 6 | [ifp_advanced](ifp_advanced.md) | 3 | 3 | 6.5 | 7 | 8.5 | 10 | 10 | **6.9** | HIGH |
| 7 | [smoothing](smoothing.md) | 6.5 | 3 | 10 | 5 | 10 | 7.5 | — | **7.0** | HIGH |
| 8 | [discrete_dp](discrete_dp.md) | 4 | 7 | 6.5 | 6 | 9 | 7 | 10 | **7.1** | HIGH |
| 9 | [lqcontrol](lqcontrol.md) | 4 | 3 | 10 | 4.5 | 10 | 8 | 10 | **7.1** | HIGH |
| 10 | [calvo](calvo.md) | 3 | 5.5 | 8.5 | 7 | 8.5 | 8 | 10 | **7.2** | HIGH |
| 11 | [inventory_q](inventory_q.md) | 4 | 5.5 | 7.5 | 6 | 10 | 10 | — | **7.2** | HIGH |
| 12 | [perm_income_cons](perm_income_cons.md) | 4.5 | 4.5 | 10 | 5.5 | 10 | 9 | — | **7.2** | LOW |
| 13 | [amss](amss.md) | 3.5 | 3.5 | 8 | 6 | 10 | 10 | 10 | **7.3** | HIGH |
| 14 | [rs_inventory_q](rs_inventory_q.md) | 5 | 6.5 | 10 | 5 | — | 10 | — | **7.3** | LOW |
| 15 | [calvo_machine_learn](calvo_machine_learn.md) | 4 | 3 | 6.5 | 8 | 10 | 10 | 10 | **7.4** | HIGH |
| 16 | [lq_inventories](lq_inventories.md) | 4 | 3 | 7.5 | 7 | 10 | 10 | 10 | **7.4** | HIGH |
| 17 | [tax_smoothing_1](tax_smoothing_1.md) | 8.5 | 4.5 | 9 | 6 | 7.5 | 9 | — | **7.4** | LOW |
| 18 | [perm_income](perm_income.md) | 3.5 | 4.5 | 10 | 6 | 8.5 | 10 | 10 | **7.5** | HIGH |
| 19 | [mccall_q](mccall_q.md) | 3 | 9.5 | 7 | 7 | 9 | 10 | — | **7.6** | HIGH |
| 20 | [tax_smoothing_2](tax_smoothing_2.md) | 9 | 4 | 10 | 4 | 8.5 | 10 | — | **7.6** | HIGH |
| 21 | [amss3](amss3.md) | 3.5 | 9 | 8.5 | 5.5 | 7.5 | 10 | 10 | **7.7** | HIGH |
| 22 | [chang_ramsey](chang_ramsey.md) | 3 | 10 | 8.5 | 6 | 8.5 | 10 | — | **7.7** | HIGH |
| 23 | [lqramsey](lqramsey.md) | 6.5 | 3 | 7.5 | 7 | 10 | 10 | 10 | **7.7** | HIGH |
| 24 | [amss2](amss2.md) | 3.5 | 10 | 8.5 | 6 | 8.5 | 10 | — | **7.8** | HIGH |
| 25 | [ifp_egm_transient_shocks](ifp_egm_transient_shocks.md) | 3.5 | 9.5 | 7.5 | 5.5 | 9 | 10 | 10 | **7.9** | HIGH |
| 26 | [mccall_model](mccall_model.md) | 4 | 7 | 10 | 6 | 10 | 8 | 10 | **7.9** | HIGH |
| 27 | [smoothing_tax](smoothing_tax.md) | 7 | 5 | 10 | 4 | 10 | 9 | 10 | **7.9** | HIGH |
| 28 | [calvo_abreu](calvo_abreu.md) | 4 | 9 | 7.5 | 9 | 8.5 | 10 | — | **8.0** | HIGH |
| 29 | [ifp_egm](ifp_egm.md) | 3 | 9 | 7.5 | 6.5 | 10 | 10 | 10 | **8.0** | HIGH |
| 30 | [ifp_opi](ifp_opi.md) | 5 | 10 | 8 | 6 | — | 9 | 10 | **8.0** | LOW |
| 31 | [jv](jv.md) | 3.5 | 9.5 | 7.5 | 6.5 | 9 | 10 | 10 | **8.0** | HIGH |
| 32 | [mccall_model_with_sep_markov](mccall_model_with_sep_markov.md) | 5 | 10 | 7.5 | 5.5 | — | 10 | 10 | **8.0** | LOW |
| 33 | [mccall_fitted_vfi](mccall_fitted_vfi.md) | 7 | 8 | 7.5 | 5.5 | 9 | 10 | 10 | **8.1** | LOW |
| 34 | [odu](odu.md) | 5 | 10 | 10 | 5 | 9 | 8 | 10 | **8.1** | LOW |
| 35 | [opt_tax_recur](opt_tax_recur.md) | 7 | 6 | 10 | 4.5 | 9 | 10 | 10 | **8.1** | LOW |
| 36 | [os_stochastic](os_stochastic.md) | 4.5 | 7.5 | 9.5 | 7.5 | 10 | 8 | 10 | **8.1** | LOW |
| 37 | [chang_credible](chang_credible.md) | 3 | 10 | 8.5 | 9.5 | 10 | 10 | — | **8.5** | HIGH |
| 38 | [ifp_discrete](ifp_discrete.md) | 6 | 7 | 8 | 8.5 | 10 | 10 | 10 | **8.5** | LOW |
| 39 | [os_numerical](os_numerical.md) | 6 | 10 | 10 | 5.5 | — | 10 | 10 | **8.6** | NONE |
| 40 | [tax_smoothing_3](tax_smoothing_3.md) | 9 | 9 | 10 | 5 | 8.5 | 10 | — | **8.6** | NONE |
| 41 | [mccall_model_with_separation](mccall_model_with_separation.md) | 6.5 | 8.5 | 7.5 | 8.5 | 10 | 10 | 10 | **8.7** | NONE |
| 42 | [mccall_persist_trans](mccall_persist_trans.md) | 9.5 | 6.5 | 7 | 8 | 10 | 10 | 10 | **8.7** | NONE |
| 43 | [career](career.md) | 8 | 9.5 | 8.5 | 6.5 | 10 | 10 | 10 | **8.9** | NONE |
| 44 | [os](os.md) | 6 | 9 | 9 | 8 | 10 | 10 | 10 | **8.9** | NONE |
| 45 | [os_time_iter](os_time_iter.md) | 7.5 | 8 | 9.5 | 8 | 9 | 10 | 10 | **8.9** | NONE |
| 46 | [un_insure](un_insure.md) | 8 | 10 | 10 | 5.5 | 9 | 10 | 10 | **8.9** | NONE |
| 47 | [os_egm](os_egm.md) | 7 | 10 | 7.5 | 9 | 10 | 10 | 10 | **9.1** | NONE |
| 48 | [os_egm_jax](os_egm_jax.md) | 10 | 10 | 7.5 | 7 | — | 10 | 10 | **9.1** | NONE |
| 49 | [short_path](short_path.md) | 10 | 10 | 10 | 8 | — | 10 | 10 | **9.7** | NONE |
| 50 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 51 | [status](status.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
| 52 | [zreferences](zreferences.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
