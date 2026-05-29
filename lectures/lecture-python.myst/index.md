# Style Audit — lecture-python.myst

- **Audit date:** 2026-05-28
- **Lectures audited:** 110
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Average overall score:** 9.0 / 10
- **Average per-category scores:** writing 8.0 (n=110), math 9.0 (n=105), code 9.2 (n=110), figures 8.7 (n=99), references 9.0 (n=81), links 9.7 (n=98), admonitions 10.0 (n=88)

## Priority distribution

| Priority | Count | % |
|----------|-------|---|
| HIGH   |     2 | 2% |
| MEDIUM |     0 | 0% |
| LOW    |    13 | 12% |
| NONE   |    95 | 86% |

## Top systemic issues across the series

1. **[qe-code-002]** — Unicode Greek letters in code — appears in 94 / 110 lectures.
2. **[qe-writing-006]** — H2+ headings in sentence case (Title Case for H1) — appears in 87 / 110 lectures.
3. **[qe-fig-001]** — Do not set figure size unless necessary — appears in 75 / 110 lectures.
4. **[qe-fig-005]** — Descriptive figure names for cross-referencing — appears in 47 / 110 lectures.
5. **[qe-fig-003]** — No matplotlib embedded titles (`ax.set_title`/`fig.suptitle`) — appears in 44 / 110 lectures.
6. **[qe-fig-008]** — Use `lw=2` for line charts — appears in 37 / 110 lectures.
7. **[qe-writing-009 (proposed)]** — "IID" not "i.i.d." or "iid" — appears in 21 / 110 lectures.
8. **[qe-math-010 (proposed)]** — Blackboard `\mathbb{P}`, `\mathbb{E}`, `\mathbb{V}` — appears in 21 / 110 lectures.
9. **[qe-fig-006]** — Lowercase axis labels — appears in 20 / 110 lectures.
10. **[qe-math-002]** — Use `\top` for transpose — appears in 17 / 110 lectures.
11. **[qe-link-002]** — `{doc}` links for cross-series references — appears in 17 / 110 lectures.
12. **[qe-link-001]** — Markdown links for same-series references — appears in 12 / 110 lectures.
13. **[qe-math-008]** — Explain special notation (`\mathbb{1}` etc.) — appears in 9 / 110 lectures.
14. **[qe-math-004]** — No bold for matrices/vectors — appears in 9 / 110 lectures.
15. **[qe-math-011 (proposed)]** — Distribution names: plain letters, `\mathrm{…}` for multi-letter — appears in 6 / 110 lectures.

## Lectures ranked by priority (lowest score first)

| # | Lecture | Writing | Math | Code | Fig | Ref | Link | Adm | Overall | Priority |
|---|---------|---------|------|------|-----|-----|------|-----|---------|----------|
| 1 | [cross_product_trick](cross_product_trick.md) | 6 | 3 | 10 | N/A | N/A | 10 | N/A | 7.2 | HIGH |
| 2 | [linear_algebra](linear_algebra.md) | 6 | 5 | 8.5 | 9 | 9 | 7 | 10 | 7.8 | LOW |
| 3 | [lagrangian_lqdp](lagrangian_lqdp.md) | 7 | 6 | 9 | N/A | 9 | 7 | 10 | 8 | LOW |
| 4 | [lqcontrol](lqcontrol.md) | 6 | 5 | 8.5 | 9 | 9 | 8.5 | 10 | 8 | LOW |
| 5 | [ar1_turningpts](ar1_turningpts.md) | 6.5 | 8 | 8.5 | 8.5 | 9 | N/A | N/A | 8.1 | LOW |
| 6 | [navy_captain](navy_captain.md) | 7 | 9 | 8.5 | 6.5 | N/A | 10 | N/A | 8.2 | LOW |
| 7 | [rational_expectations](rational_expectations.md) | 5 | 8 | 8.5 | N/A | 9 | 9 | 10 | 8.2 | LOW |
| 8 | [two_auctions](two_auctions.md) | 8 | 7.5 | 9.5 | 6.5 | 9 | 9 | N/A | 8.2 | LOW |
| 9 | [perm_income_cons](perm_income_cons.md) | 6 | 8 | 8.5 | 9.5 | 9 | 9 | N/A | 8.3 | LOW |
| 10 | [linear_models](linear_models.md) | 5 | 10 | 8.5 | 9 | N/A | 8 | 10 | 8.4 | LOW |
| 11 | [markov_perf](markov_perf.md) | 7 | 6 | 8.5 | 8 | 9 | 10 | 10 | 8.4 | LOW |
| 12 | [misspecified_recovery](misspecified_recovery.md) | 8 | 4 | 8.5 | 9.5 | 9 | 10 | 10 | 8.4 | HIGH |
| 13 | [util_rand_resp](util_rand_resp.md) | 6 | 10 | 8.5 | 7 | 9 | 10 | N/A | 8.4 | LOW |
| 14 | [affine_risk_prices](affine_risk_prices.md) | 8 | 5 | 9.5 | 8 | 9 | 10 | 10 | 8.5 | LOW |
| 15 | [prob_meaning](prob_meaning.md) | 7 | 9.5 | 8.5 | 6 | N/A | 10 | 10 | 8.5 | LOW |
| 16 | [kalman_2](kalman_2.md) | 8 | 8.5 | 9.5 | 7 | N/A | 10 | N/A | 8.6 | NONE |
| 17 | [likelihood_var](likelihood_var.md) | 9 | 8.5 | 8.5 | 7 | N/A | 10 | N/A | 8.6 | NONE |
| 18 | [opt_transport](opt_transport.md) | 7 | 5 | 9.5 | 10 | 9 | 10 | 10 | 8.6 | NONE |
| 19 | [two_computation](two_computation.md) | 10 | 7.5 | 8.5 | 5.5 | 9 | 10 | 10 | 8.6 | NONE |
| 20 | [exchangeable](exchangeable.md) | 7 | 9.5 | 8.5 | 8 | 9 | 9 | 10 | 8.7 | NONE |
| 21 | [likelihood_ratio_process](likelihood_ratio_process.md) | 9 | 8.5 | 8.5 | 6 | 9 | 10 | 10 | 8.7 | NONE |
| 22 | [mccall_model](mccall_model.md) | 6 | 9 | 9.5 | 8.5 | 9 | 9 | 10 | 8.7 | NONE |
| 23 | [hansen_singleton_1983](hansen_singleton_1983.md) | 9 | 5.5 | 9.5 | 10 | 9 | 10 | N/A | 8.8 | NONE |
| 24 | [likelihood_ratio_process_2](likelihood_ratio_process_2.md) | 8 | 10 | 8.5 | 6 | 9 | 10 | 10 | 8.8 | NONE |
| 25 | [multivariate_normal](multivariate_normal.md) | 8 | 5.5 | 9.5 | 9.5 | N/A | 10 | 10 | 8.8 | NONE |
| 26 | [odu](odu.md) | 7 | 9.5 | 9.5 | 8 | 9 | 8.5 | 10 | 8.8 | NONE |
| 27 | [perm_income](perm_income.md) | 6 | 10 | 8.5 | 8 | 9 | 10 | 10 | 8.8 | NONE |
| 28 | [cass_koopmans_2](cass_koopmans_2.md) | 6 | 10 | 9.5 | 9.5 | 9 | 8 | 10 | 8.9 | NONE |
| 29 | [ge_arrow](ge_arrow.md) | 6 | 7.5 | 10 | 10 | 9 | 10 | 10 | 8.9 | NONE |
| 30 | [markov_asset](markov_asset.md) | 6 | 10 | 9.5 | 9 | 9 | 8.5 | 10 | 8.9 | NONE |
| 31 | [mle](mle.md) | 10 | 6 | 9.5 | 8.5 | 9 | 9 | 10 | 8.9 | NONE |
| 32 | [re_with_feedback](re_with_feedback.md) | 6 | 10 | 9.5 | 8 | 9 | 10 | 10 | 8.9 | NONE |
| 33 | [samuelson](samuelson.md) | 8 | 10 | 9.5 | 8 | 9 | 8 | 10 | 8.9 | NONE |
| 34 | [svd_intro](svd_intro.md) | 7 | 8 | 8.5 | 10 | N/A | 10 | 10 | 8.9 | NONE |
| 35 | [wald_friedman](wald_friedman.md) | 9 | 9.5 | 8.5 | 7 | 9 | 9 | 10 | 8.9 | NONE |
| 36 | [wald_friedman_2](wald_friedman_2.md) | 7 | 9.5 | 9.5 | 8.5 | 9 | 9 | 10 | 8.9 | NONE |
| 37 | [divergence_measures](divergence_measures.md) | 9.5 | 8 | 8.5 | 8 | 9 | 10 | 10 | 9 | NONE |
| 38 | [hoist_failure](hoist_failure.md) | 8 | 9.5 | 9.5 | 9 | 9 | 8 | 10 | 9 | NONE |
| 39 | [house_auction](house_auction.md) | 6 | 10 | 10 | N/A | 9 | N/A | 10 | 9 | NONE |
| 40 | [jv](jv.md) | 8 | 10 | 8.5 | 8.5 | 9 | N/A | 10 | 9 | NONE |
| 41 | [kalman](kalman.md) | 8 | 9.5 | 8.5 | 8 | 9 | 10 | 10 | 9 | NONE |
| 42 | [likelihood_bayes](likelihood_bayes.md) | 6.5 | 9 | 9.5 | 9 | 9 | 10 | 10 | 9 | NONE |
| 43 | [merging_of_opinions](merging_of_opinions.md) | 8 | 9 | 8.5 | 8.5 | 9 | 10 | 10 | 9 | NONE |
| 44 | [mix_model](mix_model.md) | 7.5 | 10 | 9.5 | 7 | N/A | 10 | 10 | 9 | NONE |
| 45 | [os_stochastic](os_stochastic.md) | 7 | 10 | 8.5 | 9.5 | 9 | 9 | 10 | 9 | NONE |
| 46 | [pandas_panel](pandas_panel.md) | 8 | N/A | 10 | 8 | N/A | 9 | 10 | 9 | NONE |
| 47 | [troubleshooting](troubleshooting.md) | 7 | N/A | 10 | 10 | N/A | 9 | N/A | 9 | NONE |
| 48 | [ak2](ak2.md) | 8 | 10 | 9.5 | 8 | 9 | N/A | 10 | 9.1 | NONE |
| 49 | [blackwell_kihlstrom](blackwell_kihlstrom.md) | 8 | 8 | 9.5 | 9.5 | 9 | 10 | 10 | 9.1 | NONE |
| 50 | [cass_fiscal](cass_fiscal.md) | 6 | 10 | 9.5 | 9 | 9 | 10 | 10 | 9.1 | NONE |
| 51 | [cass_koopmans_1](cass_koopmans_1.md) | 7 | 10 | 9.5 | 9 | 9 | 9 | 10 | 9.1 | NONE |
| 52 | [chow_business_cycles](chow_business_cycles.md) | 9 | 9 | 8.5 | 8.5 | 9 | 10 | 10 | 9.1 | NONE |
| 53 | [finite_markov](finite_markov.md) | 7 | 9 | 9.5 | 10 | 9 | 9 | 10 | 9.1 | NONE |
| 54 | [ifp_egm](ifp_egm.md) | 7 | 10 | 9 | 9 | 9 | 10 | 10 | 9.1 | NONE |
| 55 | [ifp_egm_transient_shocks](ifp_egm_transient_shocks.md) | 7 | 10 | 9 | 8.5 | 9 | 10 | 10 | 9.1 | NONE |
| 56 | [imp_sample](imp_sample.md) | 9.5 | 10 | 8.5 | 7.5 | N/A | 10 | N/A | 9.1 | NONE |
| 57 | [information_market_equilibrium](information_market_equilibrium.md) | 9 | 9.5 | 8.5 | 8 | 9 | 10 | 10 | 9.1 | NONE |
| 58 | [kesten_processes](kesten_processes.md) | 7 | 10 | 8.5 | 9.5 | 9 | 10 | 10 | 9.1 | NONE |
| 59 | [lln_clt](lln_clt.md) | 8 | 10 | 8.5 | 8.5 | 9 | 10 | 10 | 9.1 | NONE |
| 60 | [ols](ols.md) | 9 | 9 | 9.5 | 8 | 9 | 9 | 10 | 9.1 | NONE |
| 61 | [rs_inventory_q](rs_inventory_q.md) | 7 | 9.5 | 9.5 | 9.5 | N/A | 10 | N/A | 9.1 | NONE |
| 62 | [von_neumann_model](von_neumann_model.md) | 7 | 10 | 9.5 | 9 | 9 | N/A | 10 | 9.1 | NONE |
| 63 | [wealth_dynamics](wealth_dynamics.md) | 7 | 10 | 9.5 | 8 | 9 | 10 | 10 | 9.1 | NONE |
| 64 | [aiyagari](aiyagari.md) | 9 | 8 | 9.5 | 9 | 9 | 10 | 10 | 9.2 | NONE |
| 65 | [eig_circulant](eig_circulant.md) | 8 | 9 | 10 | 9 | N/A | 10 | N/A | 9.2 | NONE |
| 66 | [harrison_kreps](harrison_kreps.md) | 7 | 10 | 9.5 | N/A | 9 | 10 | 10 | 9.2 | NONE |
| 67 | [lq_inventories](lq_inventories.md) | 9 | 8 | 8.5 | 10 | 9 | 10 | 10 | 9.2 | NONE |
| 68 | [mccall_q](mccall_q.md) | 8 | 10 | 9.5 | 8.5 | 9 | 10 | N/A | 9.2 | NONE |
| 69 | [newton_method](newton_method.md) | 8 | 10 | 9.5 | 8 | N/A | 10 | 10 | 9.2 | NONE |
| 70 | [os_numerical](os_numerical.md) | 8 | 10 | 9.5 | 8 | N/A | 10 | 10 | 9.2 | NONE |
| 71 | [prob_matrix](prob_matrix.md) | 9 | 9 | 8.5 | 8.5 | N/A | 10 | 10 | 9.2 | NONE |
| 72 | [qr_decomp](qr_decomp.md) | 8 | 9 | 10 | N/A | N/A | 10 | N/A | 9.2 | NONE |
| 73 | [ifp_advanced](ifp_advanced.md) | 7 | 10 | 9.5 | 9.5 | 9 | 10 | 10 | 9.3 | NONE |
| 74 | [inventory_q](inventory_q.md) | 8 | 9.5 | 9.5 | 10 | 9 | 10 | N/A | 9.3 | NONE |
| 75 | [stats_examples](stats_examples.md) | 8 | 10 | 8.5 | 9.5 | N/A | 10 | 10 | 9.3 | NONE |
| 76 | [survival_recursive_preferences](survival_recursive_preferences.md) | 10 | 10 | 8.5 | 7.5 | 9 | 10 | 10 | 9.3 | NONE |
| 77 | [theil_1](theil_1.md) | 9.5 | 10 | 8.5 | 9 | 9 | N/A | 10 | 9.3 | NONE |
| 78 | [theil_2](theil_2.md) | 10 | 9.5 | 8.5 | 9 | 9 | N/A | 10 | 9.3 | NONE |
| 79 | [ar1_bayes](ar1_bayes.md) | 8.5 | 10 | 8.5 | 9.5 | 9 | 10 | 10 | 9.4 | NONE |
| 80 | [career](career.md) | 9 | 10 | 9.5 | 9 | 9 | N/A | 10 | 9.4 | NONE |
| 81 | [endogenous_lake](endogenous_lake.md) | 9 | 10 | 9.5 | 8.5 | 9 | 10 | 10 | 9.4 | NONE |
| 82 | [hansen_singleton_1982](hansen_singleton_1982.md) | 9.5 | 9 | 8.5 | 10 | 9 | 10 | 10 | 9.4 | NONE |
| 83 | [ifp_opi](ifp_opi.md) | 8 | 10 | 9.5 | 9 | N/A | 10 | 10 | 9.4 | NONE |
| 84 | [inventory_dynamics](inventory_dynamics.md) | 9 | 10 | 8.5 | 9 | 9 | 10 | 10 | 9.4 | NONE |
| 85 | [mccall_fitted_vfi](mccall_fitted_vfi.md) | 10 | 10 | 8.5 | 8 | 9 | 10 | 10 | 9.4 | NONE |
| 86 | [measurement_models](measurement_models.md) | 10 | 8.5 | 8.5 | 10 | 9 | 10 | 10 | 9.4 | NONE |
| 87 | [multi_hyper](multi_hyper.md) | 8 | 9.5 | 9.5 | 10 | N/A | 10 | N/A | 9.4 | NONE |
| 88 | [organization_capital](organization_capital.md) | 9.5 | 9.5 | 9.5 | 9 | 9 | N/A | 10 | 9.4 | NONE |
| 89 | [os_egm](os_egm.md) | 8 | 10 | 8.5 | 10 | 9 | 10 | 10 | 9.4 | NONE |
| 90 | [os_time_iter](os_time_iter.md) | 8 | 10 | 9.5 | 9.5 | 9 | 10 | 10 | 9.4 | NONE |
| 91 | [rand_resp](rand_resp.md) | 8 | 10 | 10 | N/A | 9 | 10 | N/A | 9.4 | NONE |
| 92 | [ross_recovery](ross_recovery.md) | 10 | 8 | 9.5 | 9 | 9 | 10 | 10 | 9.4 | NONE |
| 93 | [uncertainty_traps](uncertainty_traps.md) | 9 | 10 | 9.5 | 8 | 9 | 10 | 10 | 9.4 | NONE |
| 94 | [var_dmd](var_dmd.md) | 7.5 | 10 | 10 | N/A | 9 | 10 | 10 | 9.4 | NONE |
| 95 | [ak_aiyagari](ak_aiyagari.md) | 10 | 10 | 9.5 | 8 | 9 | 10 | 10 | 9.5 | NONE |
| 96 | [back_prop](back_prop.md) | 8 | 10 | 10 | 9 | N/A | 10 | 10 | 9.5 | NONE |
| 97 | [bayes_nonconj](bayes_nonconj.md) | 9 | 10 | 8.5 | 9.5 | N/A | 10 | 10 | 9.5 | NONE |
| 98 | [morris_learn](morris_learn.md) | 8 | 10 | 9.5 | 10 | 9 | 10 | 10 | 9.5 | NONE |
| 99 | [os](os.md) | 9 | 10 | 9.5 | 9 | 9 | 10 | 10 | 9.5 | NONE |
| 100 | [sir_model](sir_model.md) | 8 | 10 | 9.5 | 10 | N/A | 10 | N/A | 9.5 | NONE |
| 101 | [status](status.md) | 9 | N/A | 10 | N/A | N/A | N/A | N/A | 9.5 | NONE |
| 102 | [ifp_discrete](ifp_discrete.md) | 9 | 10 | 9.5 | 10 | 9 | 10 | 10 | 9.6 | NONE |
| 103 | [lake_model](lake_model.md) | 10 | 10 | 9.5 | 9 | 9 | 10 | 10 | 9.6 | NONE |
| 104 | [mccall_model_with_sep_markov](mccall_model_with_sep_markov.md) | 9.5 | 10 | 9.5 | 8.5 | N/A | 10 | 10 | 9.6 | NONE |
| 105 | [mccall_model_with_separation](mccall_model_with_separation.md) | 9 | 10 | 9.5 | 9.5 | 9 | 10 | 10 | 9.6 | NONE |
| 106 | [os_egm_jax](os_egm_jax.md) | 10 | 10 | 9.5 | 8 | N/A | 10 | 10 | 9.6 | NONE |
| 107 | [cass_fiscal_2](cass_fiscal_2.md) | 9 | 10 | 10 | 10 | 9 | 10 | 10 | 9.7 | NONE |
| 108 | [mccall_persist_trans](mccall_persist_trans.md) | 10 | 10 | 10 | 9 | 9 | 10 | 10 | 9.7 | NONE |
| 109 | [intro](intro.md) | 10 | N/A | 10 | N/A | N/A | N/A | N/A | 10 | NONE |
| 110 | [zreferences](zreferences.md) | 10 | N/A | 10 | N/A | N/A | N/A | N/A | 10 | NONE |

## Series-level recommendations

### Writing & math issues
1. **Address `qe-writing-006` (sentence case for H2+) systemically.** Still the most common deviation — affects roughly 4 out of every 5 lectures. A find-and-replace pass converting H2/H3 headings to sentence case (preserving proper nouns and acronyms) would lift writing scores across the series.
2. **Adopt `\top` for transpose everywhere (`qe-math-002`).** Older lectures (notably `lqcontrol`, `linear_algebra`, `lagrangian_lqdp`, `markov_perf`, `rational_expectations`, `perm_income_cons`, `cross_product_trick`) still use prime `'` or `^T` heavily.
3. **Remove `\mathbf`/`\boldsymbol` from vectors (`qe-math-004`).** Concentrated in `hansen_singleton_1983`, `mle`, `misspecified_recovery`, `multivariate_normal`, `opt_transport`, `theil_2`, `two_auctions`, `likelihood_var`, `likelihood_ratio_process`.
4. **Standardise probability notation (`qe-math-010 (proposed)`): `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}` with braces.** Notable offenders include `kalman_2`, `multivariate_normal`, `misspecified_recovery`, `navy_captain`.
5. **Replace "i.i.d."/"iid" with "IID" (`qe-writing-009 (proposed)`).** Trivial global-replace across ~20 lectures.
6. **Replace `\mathcal{N}` with `N` for the normal distribution (`qe-math-011 (proposed)`).** Concentrated in `affine_risk_prices`, `merging_of_opinions`, `likelihood_var`.
7. **Fix Critical: `\begin{align}` inside `$$` in `divergence_measures.md` (`qe-math-006`).** Build-risk.

### Code, figures, references, links & admonitions issues
8. **`qe-fig-001` (do not set `figsize=`):** the single most common new-category finding — set in 75 / 110 lectures, with extreme offenders (`chow_business_cycles`, `likelihood_ratio_process`, `likelihood_ratio_process_2`, `two_computation`, `organization_capital`) setting it 10+ times. A series-wide pass removing `figsize=` would benefit nearly every lecture.
9. **`qe-code-002` (Unicode Greek in code):** 94 / 110 lectures use spelled-out Greek (alpha, beta, …) in code cells; 83 of these also mix in unicode (α, β, …) inconsistently within the same lecture. The style guide prefers unicode. Pick a convention per lecture and apply it consistently.
10. **`qe-fig-003` (no embedded matplotlib titles):** 44 lectures use `ax.set_title()` or `fig.suptitle()` outside exercise blocks. Worst offenders: `navy_captain` (13), `likelihood_ratio_process` (8), `prob_meaning` (7), `survival_recursive_preferences` (6), `likelihood_ratio_process_2` (6), `likelihood_var` (6).
11. **`qe-fig-006` (lowercase axis labels):** 20 lectures have capitalised `set_xlabel`/`set_ylabel` strings. Worst offenders: `two_computation` (46 instances), `two_auctions` (14), `affine_risk_prices` (15), `kalman_2` (6).
12. **`qe-link-002` (cross-series `{doc}` links):** 17 lectures use direct URLs to other QuantEcon series; convert to `{doc}` intersphinx form. Notable offenders: `linear_algebra` (6 URLs), `lagrangian_lqdp` (3), `cass_koopmans_2` (2 same-series + 2 cross-series).
13. **`qe-link-001` (same-series links):** 12 lectures use full python.quantecon.org URLs for same-series refs; switch to plain markdown `[](label)` links. Notable: `odu` (4), `wald_friedman_2` (2), `cass_koopmans_2` (2).
14. **`qe-fig-005` (descriptive figure names):** most lectures with figures lack `:name: fig-…` fields, missing the opportunity for `{numref}` cross-referencing. Only 17 lectures use the convention systematically; consider applying it series-wide.
15. **`qe-code-003` (install-cell `hide-output` tag):** `hoist_failure.md` has a `!pip install tabulate` cell without the `tags: [hide-output]` annotation. Low-risk fix.
16. **`qe-code-004` / `qe-code-005` (use `qe.Timer` / `qe.timeit`):** `ifp_egm.md`, `ifp_egm_transient_shocks.md` use manual `time.time()` timing; `lagrangian_lqdp.md` uses `%%timeit` magic. Migrate to `quantecon.Timer` / `quantecon.timeit`.
17. **`qe-fig-010` (plotly + `{only} latex`):** `back_prop.md` uses Plotly figures but lacks the `{only} latex` directive required for PDF compatibility.

### Methodology notes

- Code, Figures, References, Links, and Admonitions are all scored. JAX is out of scope; 23 / 110 lectures use JAX.
- New-category scoring is mechanical: regex/AST signals on lecture source. References (`qe-ref-001`) is judgment-only and scored conservatively at 9 unless an LLM check is performed; consider a follow-up audit pass that adjudicates each `{cite}` vs `{cite:t}` call in context.
- Admonitions scored 10.0 across the series because the mechanical checks (`qe-admon-001`, `qe-admon-003`, `qe-admon-004`) found no violations; `qe-admon-002` (dropdown class) is followed almost universally. A judgment-level review of admonition usage may surface additional issues.
