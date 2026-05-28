# Style Audit — lecture-dp

- **Audit date:** 2026-05-27
- **Lectures audited:** 50
- **Average overall score:** 7.2 / 10
- **Average writing score:** 7.5 / 10
- **Average math score:** 6.7 / 10  (47 files have math content; 3 are non-math)

## Priority distribution

| Priority | Count | % |
|----------|-------|---|
| HIGH     | 7     | 14% |
| MEDIUM   | 18    | 36% |
| LOW      | 17    | 34% |
| NONE     | 8     | 16% |

## Top systemic issues across the series

1. **[M2]** — Apostrophe `'` (and `^\prime`, `^T`) used as transpose instead of `^\top`. Appears in 11 / 50 lectures, often as the dominant math-style violation. Hits hardest in the LQ/DP-derivation lectures (`lqcontrol`, `lagrangian_lqdp`, `perm_income_cons`, `smoothing`, `markov_jump_lq`, `dyn_stack`, `lq_inventories`, `calvo_machine_learn`, `cross_product_trick`, `perm_income`, `mccall_q`).
2. **[W3]** — Section/subsection headings in Title Case rather than sentence case. Appears in 21 / 50 lectures, systemic in the McCall / Optimal-Savings / IFP families and in `lqcontrol`, `mccall_q`, `perm_income`, `perm_income_cons`.
3. **[M7]** — Probability / expectation written as bare `E`, `\mathbb E` (no braces), or `E_0`/`E_t` rather than `\mathbb{E}`. Appears in 17 / 50 lectures, especially the LQ/Ramsey/tax-smoothing/IFP lectures.

Additional cross-cutting issues:
- **[M5]/[W8]** — `\vec`, `\mathbf`, `\mathcal`, `\mathscr`, `\mathsf`, `\cal` used for plain symbols (15 / 50 lectures). Worst in `calvo`, `calvo_abreu`, `chang_credible`, `chang_ramsey`, `calvo_machine_learn`, `dyn_stack`.
- **[M9]** — `{\cal N}` used for the multivariate normal instead of plain `N` (9 / 50 lectures).
- **[M12]** — `\cr` used instead of `\\` for row separators inside `aligned` blocks (7 / 50 lectures).
- **[M4]** — Matrices use `pmatrix`, `array`, or `\left(\begin{matrix}\right)` instead of `bmatrix` (5 / 50 lectures, but very heavy in `lqcontrol` (17 array matrices) and `lq_inventories` (11 array matrices)).
- **[W7]** — Smart quotes ’ “ ” in narrative (20 / 50 lectures).
- **[W1]** — Multi-sentence paragraphs (43 / 50 lectures) — listed as Low-severity everywhere; not driving the priority bucket.

## Lectures ranked by priority (lowest score first)

| #  | Lecture | Writing | Math | Overall | Priority |
|----|---------|---------|------|---------|----------|
| 1  | lqcontrol | 5 | 3 | 4.0 | HIGH |
| 2  | cross_product_trick | 6 | 3 | 4.5 | HIGH |
| 3  | lagrangian_lqdp | 6 | 3 | 4.5 | HIGH |
| 4  | perm_income_cons | 5 | 4 | 4.5 | HIGH |
| 5  | calvo_machine_learn | 7 | 3 | 5.0 | HIGH |
| 6  | lq_inventories | 6 | 4 | 5.0 | HIGH |
| 7  | markov_jump_lq | 7 | 3 | 5.0 | HIGH |
| 8  | dyn_stack | 7 | 4 | 5.5 | MEDIUM |
| 9  | mccall_q | 5 | 6 | 5.5 | MEDIUM |
| 10 | perm_income | 6 | 5 | 5.5 | MEDIUM |
| 11 | smoothing | 8 | 3 | 5.5 | MEDIUM |
| 12 | mccall_model | 5 | 7 | 6.0 | MEDIUM |
| 13 | odu | 6 | 7 | 6.5 | MEDIUM |
| 14 | os_numerical | 6 | 7 | 6.5 | MEDIUM |
| 15 | os_stochastic | 6 | 7 | 6.5 | MEDIUM |
| 16 | cons_news | 7 | 7 | 7.0 | MEDIUM |
| 17 | ifp_advanced | 7 | 7 | 7.0 | MEDIUM |
| 18 | ifp_egm | 7 | 8 | 7.0 | MEDIUM |
| 19 | ifp_egm_transient_shocks | 7 | 8 | 7.0 | MEDIUM |
| 20 | ifp_opi | 7 | 8 | 7.0 | MEDIUM |
| 21 | jv | 6 | 8 | 7.0 | MEDIUM |
| 22 | opt_tax_recur | 8 | 6 | 7.0 | MEDIUM |
| 23 | os_time_iter | 7 | 8 | 7.0 | MEDIUM |
| 24 | tax_smoothing_1 | 8 | 6 | 7.0 | MEDIUM |
| 25 | tax_smoothing_2 | 8 | 6 | 7.0 | MEDIUM |
| 26 | amss | 8 | 7 | 7.5 | LOW |
| 27 | career | 7 | 8 | 7.5 | LOW |
| 28 | chang_credible | 8 | 7 | 7.5 | LOW |
| 29 | chang_ramsey | 8 | 7 | 7.5 | LOW |
| 30 | ifp_discrete | 7 | 8 | 7.5 | LOW |
| 31 | os_egm | 7 | 8 | 7.5 | LOW |
| 32 | smoothing_tax | 8 | 7 | 7.5 | LOW |
| 33 | tax_smoothing_3 | 8 | 7 | 7.5 | LOW |
| 34 | un_insure | 8 | 7 | 7.5 | LOW |
| 35 | calvo | 8 | 8 | 8.0 | LOW |
| 36 | calvo_abreu | 8 | 8 | 8.0 | LOW |
| 37 | lqramsey | 8 | 8 | 8.0 | LOW |
| 38 | amss2 | 9 | 8 | 8.5 | LOW |
| 39 | discrete_dp | 9 | 8 | 8.5 | LOW |
| 40 | mccall_fitted_vfi | 9 | 8 | 8.5 | LOW |
| 41 | mccall_model_with_sep_markov | 8 | 9 | 8.5 | LOW |
| 42 | mccall_model_with_separation | 9 | 8 | 8.5 | LOW |
| 43 | amss3 | 9 | 9 | 9.0 | NONE |
| 44 | mccall_persist_trans | 9 | 9 | 9.0 | NONE |
| 45 | os | 9 | 9 | 9.0 | NONE |
| 46 | os_egm_jax | 9 | 9 | 9.0 | NONE |
| 47 | short_path | 9 | 9 | 9.0 | NONE |
| 48 | intro | 10 | N/A | 10.0 | NONE |
| 49 | status | 10 | N/A | 10.0 | NONE |
| 50 | zreferences | 10 | N/A | 10.0 | NONE |

## Series-level recommendations

1. **Transpose convention (M2)** — Run a sweep across the LQ and DP-derivation lectures (`lqcontrol`, `lagrangian_lqdp`, `perm_income_cons`, `smoothing`, `dyn_stack`, `markov_jump_lq`, `lq_inventories`, `calvo_machine_learn`, `cross_product_trick`, `mccall_q`, `perm_income`, `tax_smoothing_1`) replacing every `'`, `^\prime`, and `^T` used as transpose with `^\top`. This is the single biggest math-style win for the series.

2. **Heading case (W3)** — Convert all H2/H3/H4 headings in the McCall (`mccall_model`, `mccall_q`), Optimal-Savings (`os_numerical`, `os_stochastic`, `os_time_iter`, `os_egm`), IFP (`ifp_discrete`, `ifp_opi`, `ifp_egm`, `ifp_egm_transient_shocks`, `ifp_advanced`), perm-income (`perm_income`, `perm_income_cons`), `lqcontrol`, `odu`, `lagrangian_lqdp`, `lq_inventories`, and `cross_product_trick` from Title Case to sentence case. Proper nouns (McCall, Bellman, Markov, Stackelberg, Riccati, etc.) stay capitalised.

3. **Expectation/probability notation (M7)** — Standardise to `\mathbb{E}` and `\mathbb{P}` with braces throughout. Replace bare `E`, `E_0`, `E_t`, `\mathbb E_t` with `\mathbb{E}_t` etc. Affects most LQ, Ramsey, IFP, and smoothing lectures.

4. **Vector/matrix decoration (M5/W8)** — Drop `\vec` arrows from sequence/vector symbols, drop `\mathbf` from matrices, drop `\mathcal`/`\mathscr`/`\mathsf`/`\cal` from sets where unambiguous. Affects `calvo`, `calvo_abreu`, `chang_credible`, `chang_ramsey`, `calvo_machine_learn`, `dyn_stack`, `lqramsey`, `os_time_iter`, `ifp_advanced`, `ifp_discrete`, `ifp_egm`, `ifp_egm_transient_shocks`, `mccall_fitted_vfi`, `opt_tax_recur`.

5. **Distribution naming (M9)** — Replace `{\cal N}` / `\mathcal{N}` with plain `N` for the normal distribution in `smoothing`, `markov_jump_lq`, `tax_smoothing_1`, `tax_smoothing_2`, `tax_smoothing_3`. Replace `\text{Beta}`/`\operatorname{Beta}` with `\mathrm{Beta}` in `jv` and `odu`.

6. **Matrix brackets (M4)** — Replace `pmatrix`, `array`, and `\left(\begin{matrix}\right)` constructions with `\begin{bmatrix}...\end{bmatrix}` in `lqcontrol`, `lq_inventories`, `lagrangian_lqdp`, `opt_tax_recur`, `amss`, `cross_product_trick`.

7. **Indicator/ones vector (M3)** — Replace `\mathbf{1}` indicator/ones notation with `\mathbb{1}` and introduce the convention. Affects `mccall_model`, `odu`, `discrete_dp`, `calvo_machine_learn`, and `cross_product_trick`.

8. **Sustain compliance** — The Optimal-Savings lectures `os`, `os_egm_jax`, `short_path`, `mccall_persist_trans`, `amss3`, and `mccall_model_with_separation` are good models of the target style. Use them as templates when refactoring weaker lectures.
