# Style Audit — lecture-python-advanced.myst

- **Audit date:** 2026-05-27
- **Lectures audited:** 55
- **Average overall score:** 7.0 / 10
- **Average writing score:** 8.1 / 10
- **Average math score:** 5.6 / 10 (4 lectures have no math content and are excluded from this average)

## Priority distribution

| Priority | Count | % |
|----------|-------|----|
| HIGH     | 6     | 11% |
| MEDIUM   | 25    | 45% |
| LOW      | 17    | 31% |
| NONE     | 7     | 13% |

## Top systemic issues across the series

1. **M7** — Bare `E_t` / `E[...]` for expectation instead of `\mathbb{E}` — appears in 17 / 55 lectures (high/medium-severity finding).
2. **M2** — Prime `'`, `^\prime`, or `^T` used as transpose instead of `^\top` — appears in 15 / 55 lectures.
3. **M9** — `\mathcal{N}` / `\cal N` used as the Normal distribution instead of plain `N` — appears in 14 / 55 lectures.
4. **M4** — `\begin{array}`, `\begin{matrix}`, or `\begin{pmatrix}` used instead of `\begin{bmatrix}` — appears in 14 / 55 lectures.
5. **W4** — Decorative bolding for non-definition keywords (should use italics) — appears in 6 / 55 lectures.
6. **W6** — "i.i.d." / "iid" used in narrative instead of "IID" — appears in 5 / 55 lectures.
7. **M5** — Bold (`\mathbf`, `\boldsymbol`) used for vectors/matrices — appears in 3 / 55 lectures.

## Lectures ranked by priority (lowest score first)

| # | Lecture | Writing | Math | Overall | Priority |
|---|---------|---------|------|---------|----------|
| 1 | hs_recursive_models | 6 | 2 | 4.0 | HIGH |
| 2 | black_litterman | 7 | 2 | 4.5 | HIGH |
| 3 | classical_filtering | 7 | 2 | 4.5 | HIGH |
| 4 | knowing_forecasts_of_others | 6 | 3 | 4.5 | HIGH |
| 5 | robustness | 7 | 2 | 4.5 | HIGH |
| 6 | calvo_machine_learn | 8 | 2 | 5.0 | HIGH |
| 7 | asset_pricing_lph | 7 | 4 | 5.5 | MEDIUM |
| 8 | cons_news | 7 | 4 | 5.5 | MEDIUM |
| 9 | entropy | 7 | 4 | 5.5 | MEDIUM |
| 10 | lucas_asset_pricing_dles | 7 | 4 | 5.5 | MEDIUM |
| 11 | markov_jump_lq | 7.5 | 3.5 | 5.5 | MEDIUM |
| 12 | orth_proj | 8 | 3 | 5.5 | MEDIUM |
| 13 | additive_functionals | 8 | 4 | 6.0 | MEDIUM |
| 14 | cattle_cycles | 8 | 4 | 6.0 | MEDIUM |
| 15 | growth_in_dles | 8 | 4 | 6.0 | MEDIUM |
| 16 | hs_invertibility_example | 8 | 4 | 6.0 | MEDIUM |
| 17 | lu_tricks | 7.5 | 4.5 | 6.0 | MEDIUM |
| 18 | permanent_income_dles | 8 | 4 | 6.0 | MEDIUM |
| 19 | rob_markov_perf | 8 | 4 | 6.0 | MEDIUM |
| 20 | BCG_incomplete_mkts | 7.5 | 6 | 6.5 | MEDIUM |
| 21 | dyn_stack | 8 | 5 | 6.5 | MEDIUM |
| 22 | lqramsey | 8 | 5 | 6.5 | MEDIUM |
| 23 | smoothing_tax | 8 | 5 | 6.5 | MEDIUM |
| 24 | tax_smoothing_1 | 8 | 5 | 6.5 | MEDIUM |
| 25 | tax_smoothing_2 | 8 | 5 | 6.5 | MEDIUM |
| 26 | tax_smoothing_3 | 8 | 5 | 6.5 | MEDIUM |
| 27 | five_preferences | 7.5 | 6.5 | 7.0 | MEDIUM |
| 28 | gorman_heterogeneous_households | 7 | 7 | 7.0 | MEDIUM |
| 29 | irfs_in_hall_model | 8 | 6 | 7.0 | MEDIUM |
| 30 | muth_kalman | 8 | 6 | 7.0 | MEDIUM |
| 31 | smoothing | 8 | 6 | 7.0 | MEDIUM |
| 32 | BCG_complete_mkts | 8 | 7 | 7.5 | LOW |
| 33 | amss | 8.5 | 6.5 | 7.5 | LOW |
| 34 | amss2 | 8.5 | 6.5 | 7.5 | LOW |
| 35 | amss3 | 8.5 | 6.5 | 7.5 | LOW |
| 36 | match_transport | 8 | 7 | 7.5 | LOW |
| 37 | discrete_dp | 8.5 | 7.5 | 8.0 | LOW |
| 38 | opt_tax_recur | 9 | 7 | 8.0 | LOW |
| 39 | rosen_schooling_model | 8.5 | 7.5 | 8.0 | LOW |
| 40 | un_insure | 8.5 | 7.5 | 8.0 | LOW |
| 41 | arma | 9 | 8 | 8.5 | LOW |
| 42 | calvo | 9 | 8 | 8.5 | LOW |
| 43 | chang_credible | 9 | 8 | 8.5 | LOW |
| 44 | chang_ramsey | 9 | 8 | 8.5 | LOW |
| 45 | estspec | 9 | 8 | 8.5 | LOW |
| 46 | lucas_model | 9 | 8 | 8.5 | LOW |
| 47 | stationary_densities | 9 | 8 | 8.5 | LOW |
| 48 | troubleshooting | 8.5 | N/A | 8.5 | LOW |
| 49 | arellano | 9 | 9 | 9.0 | NONE |
| 50 | calvo_abreu | 9 | 9 | 9.0 | NONE |
| 51 | coase | 9.5 | 8.5 | 9.0 | NONE |
| 52 | matsuyama | 9 | 9 | 9.0 | NONE |
| 53 | intro | 9.5 | N/A | 9.5 | NONE |
| 54 | status | 9.5 | N/A | 9.5 | NONE |
| 55 | zreferences | 10 | N/A | 10.0 | NONE |

## Series-level recommendations

1. **Mass-replace bare expectation symbols.** Run a global pass converting bare `E_t`, `E_0`, `E[...]` to `\mathbb{E}_t`, `\mathbb{E}_0`, `\mathbb{E}[...]` (M7). This single fix would lift many MEDIUM lectures into LOW priority.
2. **Eliminate transpose primes and `^T`.** Replace prime `'`, `^\prime`, and `^T` (when used as transpose) with `^\top` across the series (M2). Be careful to preserve derivative `u'`, `f'`, `v'` and next-period notation `x'`, `B'`, `\theta'`.
3. **Switch distribution notation.** Replace `\mathcal{N}`, `\cal N`, `{\mathcal N}`, `{\cal N}` with plain `N` (M9). For multi-letter distributions use `\mathrm{...}`.
4. **Convert all matrix environments.** Replace `\begin{array}`, `\begin{matrix}`, `\begin{pmatrix}` with `\begin{bmatrix}` (M4). The DLE-class lectures (`growth_in_dles`, `cattle_cycles`, `lucas_asset_pricing_dles`, `permanent_income_dles`, `hs_invertibility_example`) all share this issue.
5. **Reduce decorative bolding.** Many lectures use `**term**` for emphasis rather than definitions; switch to italics (`*term*`) where the intent is emphasis, reserving bold for true definitions (W4/W5).
6. **Standardise "IID".** Replace "i.i.d." and "iid" with "IID" in narrative text (W6).
7. **Treat the 6 HIGH-priority lectures first.** They concentrate the worst Math-conventions scores (math ≤ 3) and would benefit most from mechanical fixes.
