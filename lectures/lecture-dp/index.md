# Style Audit — lecture-dp

- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Lectures audited:** 50
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions  *(JAX out of scope)*
- **Average overall score:** 7.5 / 10
- **Average per-category scores:** writing 7.5, math 6.7, code 7.3, figures 6.9, references 7.8, links 7.7, admonitions 8.7

## Priority distribution

| Priority | Count | % |
|----------|-------|---|
| HIGH     | 17    | 34% |
| MEDIUM   | 5     | 10% |
| LOW      | 21    | 42% |
| NONE     | 7     | 14% |

The HIGH count rises sharply from 7 in the v1 audit (writing+math only) to 17 in v2. The extra HIGH lectures are pushed there primarily by **figures** (embedded matplotlib titles, Title-Case axis labels), **references** (no use of `{cite:t}`), **links** (raw markdown cross-series URLs), or **code** (mid-lecture `pip install`, `time.time()` benchmarking, binary-package installs without notes) — i.e. they have a single in-scope category ≤ 4 even when their writing/math is acceptable.

## Top systemic issues across the series

### From the 5 new categories

1. **[qe-ref-001]** — Author-name narrative citations using parenthetical `{cite}` instead of textual `{cite:t}`. **Zero `{cite:t}` uses across the entire series.** Affects ~22 lectures (calvo×12, smoothing_tax×8, calvo_machine_learn×8, calvo_abreu×7, amss2×5, smoothing×4, chang_credible×3, chang_ramsey×3, lqramsey×3, perm_income×3, perm_income_cons×2, cons_news×2, tax_smoothing_1, mccall_model, career, os_egm, etc.). Hits hardest in the Calvo/Chang/Ramsey/AMSS/smoothing/tax-smoothing families where authors are routinely named in the surrounding prose.

2. **[qe-link-002]** — Raw markdown links to other QuantEcon series (`python.quantecon.org`, `python-intro.quantecon.org`, `python-advanced.quantecon.org`, `python-programming.quantecon.org`) used where `{doc}` intersphinx references are required. Affects ~14 lectures; worst in `discrete_dp` (10×), `cons_news` (7×), `smoothing` (6×), `dyn_stack` (5×), `calvo` (4×), `odu` (4×), `lagrangian_lqdp` (4×), `lqcontrol` (2×).

3. **[qe-fig-003]** — Embedded matplotlib titles via `ax.set_title(...)`, `fig.suptitle(...)`, `plt.title(...)`. Affects ~20 lectures with at least one violation; concentrated in `markov_jump_lq` (6), `cons_news` (4), `dyn_stack` (3), `os_numerical` (3), `smoothing_tax` (3), `mccall_model` (2), `chang_ramsey` (2), `mccall_fitted_vfi` (2), `un_insure` (2), `calvo` (2). Captions should be in MyST `{figure}` blocks, not embedded in the plot.

### Other cross-cutting issues from the new categories

- **[qe-fig-006]** — Title-Case axis labels (`'Time'`, `'Periods'`, `'Gross Interest Rate'`, etc.). Worst in `tax_smoothing_2` (9×), `tax_smoothing_3` (4×), `lqcontrol` (4×), `smoothing` (4×), `lqramsey` (3×), `dyn_stack` (3×), `smoothing_tax` (5×), plus single-occurrence violations in `os_egm_jax`, `opt_tax_recur`, `ifp_egm_transient_shocks`, `perm_income`, `odu`. Should be sentence case / all lowercase.
- **[qe-fig-001]** — Unnecessary `figsize=` declarations. Heavy in `odu` (7×), `calvo` (5×), `career` (5×), `chang_ramsey` (5×), `lqcontrol` (5×), `mccall_q` (5×), `mccall_fitted_vfi` (5×), `mccall_model_with_sep_markov` (5×), `opt_tax_recur` (5×). Most plots do not need an explicit `figsize`.
- **[qe-fig-002]** — Static PNG figures bundled instead of generated from code. In `lqcontrol` (5×), `short_path` (4×), `amss3` (3×), `discrete_dp` (2×), `career` (1×).
- **[qe-code-003]** — Pip install not at top of lecture: `tax_smoothing_1:162`, `calvo_machine_learn:402-404`, `calvo` has duplicate (lines 33 + 82), `calvo_abreu:278`, `mccall_model_with_separation` installs build-time `myst-nb`.
- **[qe-code-004]** — `time.time()` used for benchmarking instead of `quantecon.Timer`: 6 occurrences each in `ifp_egm` and `ifp_egm_transient_shocks`.
- **[qe-code-005]** — `%timeit` / `%%timeit` magics instead of `quantecon.timeit`: `discrete_dp` (3×), `lagrangian_lqdp` (2×).
- **[qe-code-006]** — Binary scientific-Python packages installed without notes: `chang_credible` (`polytope`), `chang_ramsey` (`polytope cvxopt`), `odu` (`interpolation`), `calvo_machine_learn` (`optax`).

### Carried-forward issues from v1 (writing + math)

- **[qe-math-002]** — Apostrophe `'` (and `^\prime`, `^T`) as transpose instead of `^\top`. Affects 11 / 50 lectures; hardest in the LQ/DP-derivation lectures (`lqcontrol`, `lagrangian_lqdp`, `perm_income_cons`, `smoothing`, `markov_jump_lq`, `dyn_stack`, `lq_inventories`, `calvo_machine_learn`, `cross_product_trick`, `perm_income`, `mccall_q`).
- **[qe-writing-006]** — Title Case in H2/H3/H4 headings rather than sentence case. Affects 21 / 50 lectures.
- **[qe-math-A1]** — Bare `E`, `\mathbb E` (no braces), or `E_0`/`E_t` for expectation. Affects 17 / 50 lectures.
- **[qe-math-004]** / **[qe-writing-004]** — `\vec`, `\mathbf`, `\mathcal`, `\mathscr`, `\mathsf`, `\cal` for plain symbols. 15 / 50 lectures.
- **[qe-math-A3]** — `{\cal N}` / `\mathcal{N}` / `\operatorname{Beta}` for distributions. 9 / 50 lectures.
- **[qe-math-001]** — `\cr` instead of `\\` for row separators inside `aligned` blocks. 7 / 50 lectures.
- **[qe-math-003]** — Matrices use `pmatrix`, `array`, or `\left(\begin{matrix}\right)` instead of `bmatrix`. 5 / 50 lectures, very heavy in `lqcontrol` (17 array matrices) and `lq_inventories` (11 array matrices).
- **[qe-writing-A1]** — Smart quotes ’ “ ” in narrative. 20 / 50 lectures.
- **[qe-writing-001]** — Multi-sentence paragraphs. 43 / 50 lectures (low severity in most).

### Critical (build-risk)

- **[qe-math-A6]** — Broken `{eq}` reference: `{eq}`eq:Kalman102}` (missing closing backtick) in `cross_product_trick.md:133`. Also the label `(eq:Kalman102)` is attached to a bare `align*` block (line 121) rather than a numbered `$$ … $$` block, so the label cannot bind. **One Critical finding in the series.**

## Lectures ranked by priority (lowest score first)

| #  | Lecture | W | M | C | F | R | L | A | Overall | Priority |
|----|---------|---|---|---|---|---|---|---|---------|----------|
| 1  | [calvo_machine_learn](calvo_machine_learn.md) | 7 | 3 | 5 | 8 | 4 | 5 | N/A | 5.3 | HIGH |
| 2  | [smoothing](smoothing.md) | 8 | 3 | 8 | 6 | 4 | 4 | N/A | 5.5 | HIGH |
| 3  | [perm_income_cons](perm_income_cons.md) | 5 | 4 | 7 | 8 | 5 | 4 | N/A | 5.5 | HIGH |
| 4  | [lqcontrol](lqcontrol.md) | 5 | 3 | 7 | 5 | 7 | 4 | 8 | 5.6 | HIGH |
| 5  | [cross_product_trick](cross_product_trick.md) | 6 | 3 | N/A | N/A | N/A | 8 | N/A | 5.7 | HIGH |
| 6  | [calvo](calvo.md) | 8 | 8 | 5 | 5 | 4 | 5 | N/A | 5.8 | HIGH |
| 7  | [dyn_stack](dyn_stack.md) | 7 | 4 | 8 | 5 | 9 | 3 | N/A | 6.0 | HIGH |
| 8  | [lagrangian_lqdp](lagrangian_lqdp.md) | 6 | 3 | 6 | 9 | 8 | 4 | N/A | 6.0 | HIGH |
| 9  | [cons_news](cons_news.md) | 7 | 7 | 8 | 5 | 7 | 3 | N/A | 6.2 | HIGH |
| 10 | [markov_jump_lq](markov_jump_lq.md) | 7 | 3 | 8 | 4 | 9 | 7 | N/A | 6.3 | HIGH |
| 11 | [perm_income](perm_income.md) | 6 | 5 | 8 | 6 | 5 | 8 | N/A | 6.3 | MEDIUM |
| 12 | [chang_ramsey](chang_ramsey.md) | 8 | 7 | 5 | 5 | 5 | 9 | N/A | 6.5 | MEDIUM |
| 13 | [tax_smoothing_1](tax_smoothing_1.md) | 8 | 6 | 5 | 8 | 4 | 8 | N/A | 6.5 | HIGH |
| 14 | [smoothing_tax](smoothing_tax.md) | 8 | 7 | 8 | 4 | 3 | 8 | 8 | 6.6 | HIGH |
| 15 | [odu](odu.md) | 6 | 7 | 5 | 6 | 9 | 6 | 8 | 6.7 | MEDIUM |
| 16 | [discrete_dp](discrete_dp.md) | 9 | 8 | 5 | 7 | 9 | 3 | N/A | 6.8 | HIGH |
| 17 | [mccall_model](mccall_model.md) | 5 | 7 | 7 | 6 | 9 | 6 | 8 | 6.9 | MEDIUM |
| 18 | [chang_credible](chang_credible.md) | 8 | 7 | 5 | 9 | 5 | 8 | N/A | 7.0 | MEDIUM |
| 19 | [mccall_q](mccall_q.md) | 5 | 6 | 7 | 7 | 9 | 9 | N/A | 7.2 | LOW |
| 20 | [os_numerical](os_numerical.md) | 6 | 7 | 8 | 5 | N/A | 9 | 9 | 7.3 | LOW |
| 21 | [lq_inventories](lq_inventories.md) | 6 | 4 | 8 | 8 | 9 | 9 | 8 | 7.4 | HIGH |
| 22 | [opt_tax_recur](opt_tax_recur.md) | 8 | 6 | 8 | 5 | 9 | 9 | N/A | 7.5 | LOW |
| 23 | [tax_smoothing_2](tax_smoothing_2.md) | 8 | 6 | 8 | 5 | 9 | 9 | N/A | 7.5 | LOW |
| 24 | [ifp_egm_transient_shocks](ifp_egm_transient_shocks.md) | 7 | 8 | 4 | 7 | 9 | 9 | 9 | 7.6 | HIGH |
| 25 | [ifp_egm](ifp_egm.md) | 7 | 8 | 4 | 9 | 9 | 9 | N/A | 7.7 | HIGH |
| 26 | [calvo_abreu](calvo_abreu.md) | 8 | 8 | 8 | 9 | 4 | 9 | N/A | 7.7 | HIGH |
| 27 | [lqramsey](lqramsey.md) | 8 | 8 | 8 | 6 | 6 | 9 | 9 | 7.7 | LOW |
| 28 | [un_insure](un_insure.md) | 8 | 7 | 8 | 5 | 9 | 9 | N/A | 7.7 | LOW |
| 29 | [tax_smoothing_3](tax_smoothing_3.md) | 8 | 7 | 8 | 6 | 9 | 9 | N/A | 7.8 | LOW |
| 30 | [amss2](amss2.md) | 9 | 8 | 8 | 9 | 5 | 8 | N/A | 7.8 | LOW |
| 31 | [career](career.md) | 7 | 8 | 8 | 6 | 8 | 9 | 9 | 7.9 | LOW |
| 32 | [ifp_advanced](ifp_advanced.md) | 7 | 7 | 7 | 8 | 9 | 9 | 9 | 8.0 | LOW |
| 33 | [amss](amss.md) | 8 | 7 | 8 | 8 | 9 | 8 | 8 | 8.0 | LOW |
| 34 | [os_stochastic](os_stochastic.md) | 6 | 7 | 9 | 9 | 9 | 9 | 8 | 8.1 | LOW |
| 35 | [mccall_model_with_sep_markov](mccall_model_with_sep_markov.md) | 8 | 9 | 7 | 7 | N/A | 9 | 9 | 8.2 | LOW |
| 36 | [ifp_opi](ifp_opi.md) | 7 | 8 | 8 | 7 | 10 | 9 | 9 | 8.3 | LOW |
| 37 | [jv](jv.md) | 6 | 8 | 8 | 8 | 10 | 9 | 9 | 8.3 | LOW |
| 38 | [mccall_fitted_vfi](mccall_fitted_vfi.md) | 9 | 8 | 7 | 6 | 10 | 9 | 9 | 8.3 | LOW |
| 39 | [os_egm](os_egm.md) | 7 | 8 | 9 | 9 | 8 | 9 | N/A | 8.3 | LOW |
| 40 | [os_egm_jax](os_egm_jax.md) | 9 | 9 | 9 | 5 | N/A | 9 | 9 | 8.3 | LOW |
| 41 | [short_path](short_path.md) | 9 | 9 | 9 | 5 | N/A | 9 | 9 | 8.3 | LOW |
| 42 | [ifp_discrete](ifp_discrete.md) | 7 | 8 | 8 | 9 | 9 | 9 | 9 | 8.4 | LOW |
| 43 | [amss3](amss3.md) | 9 | 9 | 8 | 6 | 10 | 9 | N/A | 8.5 | LOW |
| 44 | [mccall_model_with_separation](mccall_model_with_separation.md) | 9 | 8 | 6 | 9 | 10 | 9 | 9 | 8.6 | NONE |
| 45 | [os_time_iter](os_time_iter.md) | 7 | 8 | 8 | 9 | 10 | 9 | 9 | 8.6 | NONE |
| 46 | [mccall_persist_trans](mccall_persist_trans.md) | 9 | 9 | 9 | 9 | 10 | 9 | 9 | 9.1 | NONE |
| 47 | [os](os.md) | 9 | 9 | 9 | 9 | 10 | 9 | 9 | 9.1 | NONE |
| 48 | [intro](intro.md) | 10 | N/A | N/A | N/A | N/A | N/A | N/A | 10.0 | NONE |
| 49 | [status](status.md) | 10 | N/A | 10 | N/A | N/A | N/A | N/A | 10.0 | NONE |
| 50 | [zreferences](zreferences.md) | 10 | N/A | N/A | N/A | 10 | N/A | N/A | 10.0 | NONE |

## Series-level recommendations

1. **Fix the one Critical build-risk first.** Repair `cross_product_trick.md:133` — change `{eq}`eq:Kalman102}` to `{eq}`eq:Kalman102`` and re-attach the equation label to a numbered `$$ … $$` block.

2. **Citation style (qe-ref-001).** Sweep the series for narrative-author parenthetical `{cite}` patterns and switch to `{cite:t}`. The Calvo / Chang / Ramsey / smoothing / tax-smoothing / AMSS lectures are the highest-yield targets. The mechanical rule is: any `<Author name> \{cite\}\`...\`` instance should become `\{cite:t\}\`...\`` and let bibtex render the name.

3. **Cross-series links (qe-link-002).** Replace all raw markdown URLs to `python.quantecon.org`, `python-intro.quantecon.org`, `python-advanced.quantecon.org`, `python-programming.quantecon.org` with `{doc}` intersphinx references. Heaviest lift in `discrete_dp`, `cons_news`, `smoothing`, `dyn_stack`, `calvo`, `odu`, `lagrangian_lqdp`.

4. **Embedded matplotlib titles (qe-fig-003).** Delete every `ax.set_title(...)`, `fig.suptitle(...)`, `plt.title(...)`. If a figure needs a caption, use the caption argument in the surrounding `{figure}` directive (MyST). Worst lectures: `markov_jump_lq`, `cons_news`, `dyn_stack`, `os_numerical`, `smoothing_tax`.

5. **Lowercase axis labels (qe-fig-006).** Convert `'Time'`, `'Periods'`, `'Initial Government Debt'`, `'Gross Interest Rate'`, etc. to lowercase. Highest-impact files: `tax_smoothing_2`, `lqcontrol`, `smoothing`, `tax_smoothing_3`, `lqramsey`, `smoothing_tax`.

6. **`pip install` placement (qe-code-003).** Move installs to the top of the lecture: `tax_smoothing_1:162`, `calvo_machine_learn:402-404`, `calvo_abreu:278`. Remove duplicate install on `calvo:82`. Remove `myst-nb` from `mccall_model_with_separation:40` (build-time dep).

7. **Benchmarking idioms (qe-code-004 / qe-code-005).** Replace 6× `time.time()` in each of `ifp_egm` / `ifp_egm_transient_shocks` with `quantecon.Timer`. Replace `%timeit` / `%%timeit` in `discrete_dp` and `lagrangian_lqdp` with `quantecon.timeit`.

8. **Binary-package install notes (qe-code-006).** Add an installation note for `chang_credible` (polytope), `chang_ramsey` (polytope, cvxopt), `odu` (interpolation), `calvo_machine_learn` (optax) explaining that they are not in Anaconda and may require special install steps.

9. **Math conventions (carry-forward).** The big v1 fixes — transpose to `^\top`, sentence-case H2/H3 headings, `\mathbb{E}` with braces, drop `\vec`/`\mathbf`/`\mathcal` decoration, replace `pmatrix`/`array` matrices with `bmatrix`, replace `{\cal N}` with `N`, replace `\cr` with `\\` — remain the most pervasive issues in the series and should be tackled together.

10. **Use the strong files as templates.** `mccall_persist_trans`, `os`, `os_time_iter`, `mccall_model_with_separation`, `amss3`, `mccall_fitted_vfi`, `os_egm`, `os_egm_jax`, `short_path`, and `ifp_discrete` are good models of the target style across all categories; refactor weaker lectures using them as references.
