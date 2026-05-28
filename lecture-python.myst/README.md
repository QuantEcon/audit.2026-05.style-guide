# Style Audit — lecture-python.myst

- **Audit date:** 2026-05-27
- **Lectures audited:** 110
- **Average overall score:** 8.5 / 10
- **Average writing score:** 8.0 / 10
- **Average math score:** 9.0 / 10 (over 105 lectures with math content)

## Priority distribution

| Priority | Count | % |
|----------|-------|---|
| HIGH     |     2 | 2% |
| MEDIUM   |    10 | 9% |
| LOW      |    40 | 36% |
| NONE     |    58 | 53% |

## Top systemic issues across the series

1. **W3** — Section/subsection headings in Title Case rather than sentence case — appears in 87 / 110 lectures.
2. **W6** — "i.i.d." / "iid" used in text instead of "IID" — appears in 21 / 110 lectures.
3. **M7** — Bare `E[]`, `\Pr()`, `\Var()` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}` — appears in 21 / 110 lectures.
4. **M2** — Transpose uses prime `'` or `^T` rather than `\top` — appears in 17 / 110 lectures.
5. **M3** — Ones vector typeset with `\mathbf{1}` instead of `\mathbb{1}` — appears in 9 / 110 lectures.
6. **M5** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` — appears in 9 / 110 lectures.
7. **M9** — Normal distribution written as `\mathcal{N}` rather than `N` — appears in 6 / 110 lectures.
8. **M4** — Matrices use `pmatrix`/`matrix` rather than `bmatrix` — appears in 3 / 110 lectures.
9. **M11** — Multiplication uses `*` instead of `\cdot`/juxtaposition — appears in 3 / 110 lectures.
10. **W1** — Multi-sentence paragraphs (style asks for one-sentence paragraphs) — appears in 2 / 110 lectures.

## Lectures ranked by priority (lowest score first)

| # | Lecture | Writing | Math | Overall | Priority |
|---|---------|---------|------|---------|----------|
| 1 | cross_product_trick | 6 | 3 | 4.5 | HIGH |
| 2 | linear_algebra | 6 | 5 | 5.5 | MEDIUM |
| 3 | lqcontrol | 6 | 5 | 5.5 | MEDIUM |
| 4 | misspecified_recovery | 8 | 4 | 6.0 | HIGH |
| 5 | opt_transport | 7 | 5 | 6.0 | MEDIUM |
| 6 | affine_risk_prices | 8 | 5 | 6.5 | MEDIUM |
| 7 | lagrangian_lqdp | 7 | 6 | 6.5 | MEDIUM |
| 8 | markov_perf | 7 | 6 | 6.5 | MEDIUM |
| 9 | rational_expectations | 5 | 8 | 6.5 | MEDIUM |
| 10 | ge_arrow | 6 | 7.5 | 6.8 | MEDIUM |
| 11 | multivariate_normal | 8 | 5.5 | 6.8 | MEDIUM |
| 12 | perm_income_cons | 6 | 8 | 7.0 | MEDIUM |
| 13 | troubleshooting | 7 | N/A | 7.0 | LOW |
| 14 | ar1_turningpts | 6.5 | 8 | 7.2 | LOW |
| 15 | hansen_singleton_1983 | 9 | 5.5 | 7.2 | LOW |
| 16 | linear_models | 5 | 10 | 7.5 | LOW |
| 17 | mccall_model | 6 | 9 | 7.5 | LOW |
| 18 | svd_intro | 7 | 8 | 7.5 | LOW |
| 19 | likelihood_bayes | 6.5 | 9 | 7.8 | LOW |
| 20 | two_auctions | 8 | 7.5 | 7.8 | LOW |
| 21 | blackwell_kihlstrom | 8 | 8 | 8.0 | LOW |
| 22 | cass_fiscal | 6 | 10 | 8.0 | LOW |
| 23 | cass_koopmans_2 | 6 | 10 | 8.0 | LOW |
| 24 | finite_markov | 7 | 9 | 8.0 | LOW |
| 25 | house_auction | 6 | 10 | 8.0 | LOW |
| 26 | markov_asset | 6 | 10 | 8.0 | LOW |
| 27 | mle | 10 | 6 | 8.0 | LOW |
| 28 | navy_captain | 7 | 9 | 8.0 | LOW |
| 29 | pandas_panel | 8 | N/A | 8.0 | LOW |
| 30 | perm_income | 6 | 10 | 8.0 | LOW |
| 31 | re_with_feedback | 6 | 10 | 8.0 | LOW |
| 32 | util_rand_resp | 6 | 10 | 8.0 | LOW |
| 33 | exchangeable | 7 | 9.5 | 8.2 | LOW |
| 34 | kalman_2 | 8 | 8.5 | 8.2 | LOW |
| 35 | odu | 7 | 9.5 | 8.2 | LOW |
| 36 | prob_meaning | 7 | 9.5 | 8.2 | LOW |
| 37 | rs_inventory_q | 7 | 9.5 | 8.2 | LOW |
| 38 | wald_friedman_2 | 7 | 9.5 | 8.2 | LOW |
| 39 | aiyagari | 9 | 8 | 8.5 | LOW |
| 40 | cass_koopmans_1 | 7 | 10 | 8.5 | LOW |
| 41 | eig_circulant | 8 | 9 | 8.5 | LOW |
| 42 | harrison_kreps | 7 | 10 | 8.5 | LOW |
| 43 | ifp_advanced | 7 | 10 | 8.5 | LOW |
| 44 | ifp_egm | 7 | 10 | 8.5 | LOW |
| 45 | ifp_egm_transient_shocks | 7 | 10 | 8.5 | LOW |
| 46 | kesten_processes | 7 | 10 | 8.5 | LOW |
| 47 | lq_inventories | 9 | 8 | 8.5 | LOW |
| 48 | merging_of_opinions | 8 | 9 | 8.5 | LOW |
| 49 | os_stochastic | 7 | 10 | 8.5 | LOW |
| 50 | qr_decomp | 8 | 9 | 8.5 | LOW |
| 51 | von_neumann_model | 7 | 10 | 8.5 | LOW |
| 52 | wealth_dynamics | 7 | 10 | 8.5 | LOW |
| 53 | divergence_measures | 9.5 | 8 | 8.8 | NONE |
| 54 | hoist_failure | 8 | 9.5 | 8.8 | NONE |
| 55 | inventory_q | 8 | 9.5 | 8.8 | NONE |
| 56 | kalman | 8 | 9.5 | 8.8 | NONE |
| 57 | likelihood_ratio_process | 9 | 8.5 | 8.8 | NONE |
| 58 | likelihood_var | 9 | 8.5 | 8.8 | NONE |
| 59 | mix_model | 7.5 | 10 | 8.8 | NONE |
| 60 | multi_hyper | 8 | 9.5 | 8.8 | NONE |
| 61 | two_computation | 10 | 7.5 | 8.8 | NONE |
| 62 | var_dmd | 7.5 | 10 | 8.8 | NONE |
| 63 | ak2 | 8 | 10 | 9.0 | NONE |
| 64 | back_prop | 8 | 10 | 9.0 | NONE |
| 65 | chow_business_cycles | 9 | 9 | 9.0 | NONE |
| 66 | ifp_opi | 8 | 10 | 9.0 | NONE |
| 67 | jv | 8 | 10 | 9.0 | NONE |
| 68 | likelihood_ratio_process_2 | 8 | 10 | 9.0 | NONE |
| 69 | lln_clt | 8 | 10 | 9.0 | NONE |
| 70 | mccall_q | 8 | 10 | 9.0 | NONE |
| 71 | morris_learn | 8 | 10 | 9.0 | NONE |
| 72 | newton_method | 8 | 10 | 9.0 | NONE |
| 73 | ols | 9 | 9 | 9.0 | NONE |
| 74 | os_egm | 8 | 10 | 9.0 | NONE |
| 75 | os_numerical | 8 | 10 | 9.0 | NONE |
| 76 | os_time_iter | 8 | 10 | 9.0 | NONE |
| 77 | prob_matrix | 9 | 9 | 9.0 | NONE |
| 78 | rand_resp | 8 | 10 | 9.0 | NONE |
| 79 | ross_recovery | 10 | 8 | 9.0 | NONE |
| 80 | samuelson | 8 | 10 | 9.0 | NONE |
| 81 | sir_model | 8 | 10 | 9.0 | NONE |
| 82 | stats_examples | 8 | 10 | 9.0 | NONE |
| 83 | status | 9 | N/A | 9.0 | NONE |
| 84 | ar1_bayes | 8.5 | 10 | 9.2 | NONE |
| 85 | hansen_singleton_1982 | 9.5 | 9 | 9.2 | NONE |
| 86 | information_market_equilibrium | 9 | 9.5 | 9.2 | NONE |
| 87 | measurement_models | 10 | 8.5 | 9.2 | NONE |
| 88 | wald_friedman | 9 | 9.5 | 9.2 | NONE |
| 89 | bayes_nonconj | 9 | 10 | 9.5 | NONE |
| 90 | career | 9 | 10 | 9.5 | NONE |
| 91 | cass_fiscal_2 | 9 | 10 | 9.5 | NONE |
| 92 | endogenous_lake | 9 | 10 | 9.5 | NONE |
| 93 | ifp_discrete | 9 | 10 | 9.5 | NONE |
| 94 | inventory_dynamics | 9 | 10 | 9.5 | NONE |
| 95 | mccall_model_with_separation | 9 | 10 | 9.5 | NONE |
| 96 | organization_capital | 9.5 | 9.5 | 9.5 | NONE |
| 97 | os | 9 | 10 | 9.5 | NONE |
| 98 | uncertainty_traps | 9 | 10 | 9.5 | NONE |
| 99 | imp_sample | 9.5 | 10 | 9.8 | NONE |
| 100 | mccall_model_with_sep_markov | 9.5 | 10 | 9.8 | NONE |
| 101 | theil_1 | 9.5 | 10 | 9.8 | NONE |
| 102 | theil_2 | 10 | 9.5 | 9.8 | NONE |
| 103 | ak_aiyagari | 10 | 10 | 10.0 | NONE |
| 104 | intro | 10 | N/A | 10.0 | NONE |
| 105 | lake_model | 10 | 10 | 10.0 | NONE |
| 106 | mccall_fitted_vfi | 10 | 10 | 10.0 | NONE |
| 107 | mccall_persist_trans | 10 | 10 | 10.0 | NONE |
| 108 | os_egm_jax | 10 | 10 | 10.0 | NONE |
| 109 | survival_recursive_preferences | 10 | 10 | 10.0 | NONE |
| 110 | zreferences | 10 | N/A | 10.0 | NONE |

## Series-level recommendations

1. **Address W3 (section headings in Title Case) systemically.** This is by far the most common deviation, affecting roughly 4 out of every 5 lectures. A simple find-and-replace pass to convert H2/H3/H4 headings to sentence case (preserving proper nouns and acronyms) would lift the writing score across the entire series.
2. **Adopt `\top` for transpose everywhere (M2).** Older lectures (notably lqcontrol, linear_algebra, lagrangian_lqdp, markov_perf, rational_expectations, perm_income_cons) still use prime `'` heavily. A targeted sweep replacing prime transpose with `^\top` in math expressions would substantially improve math-convention scores.
3. **Remove `\mathbf` / `\boldsymbol` from vectors (M5).** A small number of lectures (hansen_singleton_1983, mle, misspecified_recovery, multivariate_normal, opt_transport, theil_2, two_auctions, likelihood_var, likelihood_ratio_process) account for most violations, but they are heavy in those files.
4. **Standardize probability notation (M7).** Use `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}` rather than bare `E[]` / `\Pr()` / `\operatorname{Var}`. Notable offenders include kalman_2, multivariate_normal, misspecified_recovery, navy_captain.
5. **Replace "i.i.d." / "iid" with "IID" (W6).** A trivial global-replace covering ~20 lectures.
6. **Replace `\mathcal{N}` with `N` for the normal distribution (M9).** Mostly concentrated in affine_risk_prices, merging_of_opinions, likelihood_var, plus single occurrences in measurement_models, ross_recovery, wald_friedman.
7. **Fix one M12 rendering risk** in `divergence_measures.md` (line 134): `\begin{align}` inside `$$` should be `\begin{aligned}` to avoid PDF build failures.
