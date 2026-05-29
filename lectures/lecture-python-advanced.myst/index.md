# Summary

- **Audit date:** 2026-05-28
- **Lectures audited:** 62
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope per series instructions)*
- **Average overall score:** 7.0 / 10
- **Average per-category scores:** writing 8.2, math 5.6, code 7.0, figures 6.5, references 7.9, links 7.5, admonitions 7.8  *(N/A categories excluded from each average)*

## Priority distribution

| Priority | Count | % |
|----------|-------|----|
| HIGH     | 6     | 10% |
| MEDIUM   | 27    | 44% |
| LOW      | 25    | 40% |
| NONE     | 4     | 6% |

## Top systemic issues across the series

1. **[qe-fig-005]** — Figures lack descriptive `:name: fig-...` fields for `{numref}` cross-referencing — appears in 45 / 62 lectures.
2. **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, `gamma`, ...) in code parameters instead of unicode (`α`, `β`, `γ`) — appears in 35 / 62 lectures.
3. **[qe-math-010 (proposed)]** — Bare `E_t` / `E_0` / `E[...]` for expectation instead of `\mathbb{E}` — appears in 26 / 62 lectures.
4. **[qe-writing-005]** — Decorative bolding for non-definition keywords (should use italics) — appears in 25 / 62 lectures.
5. **[qe-fig-001]** — `figsize=` set without justification — appears in 24 / 62 lectures.
6. **[qe-math-011 (proposed)]** — `\mathcal{N}` / `\cal N` / `\mathcal N` used as the Normal distribution instead of plain `N` — appears in 18 / 62 lectures.
7. **[qe-fig-003]** — `ax.set_title()` embedding titles in matplotlib — appears in 18 / 62 lectures.
8. **[qe-link-002]** — Raw `python.quantecon.org` / `python-intro.quantecon.org` / `python-programming.quantecon.org` URLs instead of `{doc}` with intersphinx prefix — appears in 17 / 62 lectures.
9. **[qe-math-002]** — Prime `'`, `^\prime`, or `^T` used as transpose instead of `^\top` — appears in 16 / 62 lectures.
10. **[qe-math-003]** — `\begin{array}`, `\begin{matrix}`, or `\begin{pmatrix}` used instead of `\begin{bmatrix}` — appears in 15 / 62 lectures.
11. **[qe-ref-001]** — Narrative "Author (Year) {cite}" patterns that should use `{cite:t}` — appears in 12 / 62 lectures.
12. **[qe-fig-002]** — Static `{figure}` PNG references that could be code-generated — appears in 10 / 62 lectures.
13. **[qe-writing-001]** — Multi-sentence paragraphs that should be split — appears in 15 / 62 lectures.

## Lectures ranked by priority (lowest score first)

| # | Lecture | Writing | Math | Code | Fig | Ref | Link | Adm | Overall | Priority |
|---|---------|---------|------|------|-----|-----|------|-----|---------|----------|
| 1 | [hs_recursive_models](hs_recursive_models.md) | 6 | 2 | N/A | N/A | 7 | 4 | N/A | 4.7 | HIGH |
| 2 | [robustness](robustness.md) | 7 | 2 | 7 | 6 | 7 | 3 | N/A | 4.9 | HIGH |
| 3 | [black_litterman](black_litterman.md) | 7 | 2 | 5 | 4 | 8 | 6 | N/A | 5.0 | HIGH |
| 4 | [knowing_forecasts_of_others](knowing_forecasts_of_others.md) | 6 | 3 | 6 | 3 | 7 | 8 | N/A | 5.0 | HIGH |
| 5 | [classical_filtering](classical_filtering.md) | 7 | 2 | N/A | N/A | 7 | 8 | 7 | 5.6 | HIGH |
| 6 | [calvo_machine_learn](calvo_machine_learn.md) | 8 | 2 | 8 | 8 | 8 | 9 | N/A | 6.0 | HIGH |
| 7 | [markov_jump_lq](markov_jump_lq.md) | 7.5 | 3.5 | 6 | 4 | 7 | 8 | N/A | 5.7 | MEDIUM |
| 8 | [asset_pricing_lph](asset_pricing_lph.md) | 7 | 4 | 7 | N/A | 7 | 5 | 7 | 5.9 | MEDIUM |
| 9 | [entropy](entropy.md) | 7 | 4 | N/A | 7 | 8 | 6 | N/A | 5.9 | MEDIUM |
| 10 | [lucas_asset_pricing_dles](lucas_asset_pricing_dles.md) | 7 | 4 | 8 | 7 | 7 | 8 | N/A | 6.0 | MEDIUM |
| 11 | [additive_functionals](additive_functionals.md) | 8 | 4 | 6 | 6 | 7 | 6 | 7 | 6.4 | MEDIUM |
| 12 | [cattle_cycles](cattle_cycles.md) | 8 | 4 | 7 | 6 | 8 | 8 | N/A | 6.4 | MEDIUM |
| 13 | [cons_news](cons_news.md) | 7 | 4 | 7 | N/A | 8 | 7 | N/A | 6.4 | MEDIUM |
| 14 | [doubts_or_variability](doubts_or_variability.md) | 8 | 4 | 6 | 6 | 9 | 8 | 8 | 6.4 | MEDIUM |
| 15 | [dyn_stack](dyn_stack.md) | 8 | 5 | 6 | 5 | 7 | 6 | N/A | 6.4 | MEDIUM |
| 16 | [lu_tricks](lu_tricks.md) | 7.5 | 4.5 | 7 | 7 | 7 | 8 | 7 | 6.4 | MEDIUM |
| 17 | [orth_proj](orth_proj.md) | 8 | 3 | 8 | 6 | 9 | 9 | 9 | 6.4 | MEDIUM |
| 18 | [permanent_income_dles](permanent_income_dles.md) | 8 | 4 | 8 | 8 | 7 | 8 | N/A | 6.4 | MEDIUM |
| 19 | [risk_aversion_or_mistaken_beliefs](risk_aversion_or_mistaken_beliefs.md) | 8 | 4 | 6 | 4 | 9 | 8 | 8 | 6.4 | MEDIUM |
| 20 | [rob_markov_perf](rob_markov_perf.md) | 8 | 4 | 5 | 7 | 8 | 8 | N/A | 6.4 | MEDIUM |
| 21 | [smoothing_tax](smoothing_tax.md) | 8 | 5 | 7 | 6 | 7 | 8 | 7 | 6.4 | MEDIUM |
| 22 | [hs_invertibility_example](hs_invertibility_example.md) | 8 | 4 | 8 | 7 | 8 | 8 | N/A | 6.5 | MEDIUM |
| 23 | [BCG_incomplete_mkts](BCG_incomplete_mkts.md) | 7.5 | 6 | 7 | 7 | 8 | 8 | N/A | 6.6 | MEDIUM |
| 24 | [growth_in_dles](growth_in_dles.md) | 8 | 4 | 7 | 7 | 7 | 8 | N/A | 6.6 | MEDIUM |
| 25 | [lqramsey](lqramsey.md) | 8 | 5 | 7 | 7 | 8 | 8 | 7 | 6.6 | MEDIUM |
| 26 | [match_transport](match_transport.md) | 8 | 7 | 6 | 3 | 8 | 7 | N/A | 6.6 | MEDIUM |
| 27 | [smoothing](smoothing.md) | 8 | 6 | 7 | 7 | 8 | 8 | N/A | 6.6 | MEDIUM |
| 28 | [tax_smoothing_2](tax_smoothing_2.md) | 8 | 5 | 7 | 6 | 8 | 8 | N/A | 6.6 | MEDIUM |
| 29 | [tax_smoothing_3](tax_smoothing_3.md) | 8 | 5 | 8 | 7 | 8 | 8 | N/A | 6.6 | MEDIUM |
| 30 | [five_preferences](five_preferences.md) | 7.5 | 6.5 | 6 | 5 | 8 | 9 | N/A | 6.8 | MEDIUM |
| 31 | [muth_kalman](muth_kalman.md) | 8 | 6 | 7 | 5 | 7 | 8 | N/A | 6.8 | MEDIUM |
| 32 | [tax_smoothing_1](tax_smoothing_1.md) | 8 | 5 | 8 | 8 | 7 | 8 | N/A | 6.8 | MEDIUM |
| 33 | [discrete_dp](discrete_dp.md) | 8.5 | 7.5 | 5 | 6 | 8 | 4 | N/A | 7.0 | MEDIUM |
| 34 | [BCG_complete_mkts](BCG_complete_mkts.md) | 8 | 7 | 7 | 7 | 8 | 6 | N/A | 7.1 | LOW |
| 35 | [amss2](amss2.md) | 8.5 | 6.5 | 7 | 7 | 7 | 8 | N/A | 7.2 | LOW |
| 36 | [amss](amss.md) | 8.5 | 6.5 | 8 | 7 | 7 | 8 | 7 | 7.4 | LOW |
| 37 | [amss3](amss3.md) | 8.5 | 6.5 | 7 | 7 | 7 | 8 | N/A | 7.4 | LOW |
| 38 | [dovis_accounting_mf](dovis_accounting_mf.md) | 9 | 7 | 7 | 5 | 9 | 8 | 8 | 7.4 | LOW |
| 39 | [gorman_heterogeneous_households](gorman_heterogeneous_households.md) | 7 | 7 | 7 | 8 | 9 | 9 | N/A | 7.4 | LOW |
| 40 | [hansen_richard_1987](hansen_richard_1987.md) | 9 | 6 | 6 | 7 | 9 | 8 | 10 | 7.4 | LOW |
| 41 | [irfs_in_hall_model](irfs_in_hall_model.md) | 8 | 6 | 7 | 8 | 8 | 8 | N/A | 7.4 | LOW |
| 42 | [rosen_schooling_model](rosen_schooling_model.md) | 8.5 | 7.5 | 8 | 7 | 8 | 8 | N/A | 7.4 | LOW |
| 43 | [stationary_densities](stationary_densities.md) | 9 | 8 | 7 | 6 | 8 | 4 | 8 | 7.4 | LOW |
| 44 | [calvo](calvo.md) | 9 | 8 | 7 | 7 | 8 | 6 | N/A | 7.6 | LOW |
| 45 | [hansen_jagannathan_1991](hansen_jagannathan_1991.md) | 9 | 6 | 6 | 7 | 9 | 8 | 8 | 7.6 | LOW |
| 46 | [opt_tax_recur](opt_tax_recur.md) | 9 | 7 | 7 | 6 | 8 | 8 | N/A | 7.6 | LOW |
| 47 | [cagan_rational_expectations](cagan_rational_expectations.md) | 9 | 7 | 8 | 8 | 9 | 8 | 8 | 7.7 | LOW |
| 48 | [info_projection](info_projection.md) | 9 | 6 | 7 | 8 | 9 | 8 | 8 | 7.7 | LOW |
| 49 | [estspec](estspec.md) | 9 | 8 | 6 | 5 | 8 | 9 | 8 | 7.8 | LOW |
| 50 | [matsuyama](matsuyama.md) | 9 | 9 | 7 | 6 | 8 | 6 | 8 | 7.8 | LOW |
| 51 | [troubleshooting](troubleshooting.md) | 8.5 | N/A | N/A | 8 | N/A | 7 | N/A | 7.8 | LOW |
| 52 | [arma](arma.md) | 9 | 8 | 6 | 7 | 8 | 7 | N/A | 7.9 | LOW |
| 53 | [un_insure](un_insure.md) | 8.5 | 7.5 | 8 | 7 | 8 | 9 | N/A | 7.9 | LOW |
| 54 | [chang_ramsey](chang_ramsey.md) | 9 | 8 | 6 | 6 | 8 | 9 | N/A | 8.0 | LOW |
| 55 | [arellano](arellano.md) | 9 | 9 | 8 | 6 | 8 | 9 | 8 | 8.1 | LOW |
| 56 | [lucas_model](lucas_model.md) | 9 | 8 | 8 | 7 | 8 | 6 | 8 | 8.1 | LOW |
| 57 | [chang_credible](chang_credible.md) | 9 | 8 | 7 | 8 | 8 | 9 | N/A | 8.2 | LOW |
| 58 | [calvo_abreu](calvo_abreu.md) | 9 | 9 | 7 | 8 | 8 | 8 | N/A | 8.4 | LOW |
| 59 | [coase](coase.md) | 9.5 | 8.5 | 8 | 7 | 8 | 9 | 8 | 8.7 | NONE |
| 60 | [intro](intro.md) | 9.5 | N/A | N/A | N/A | N/A | N/A | N/A | 9.5 | NONE |
| 61 | [status](status.md) | 9.5 | N/A | 9 | N/A | N/A | N/A | N/A | 9.5 | NONE |
| 62 | [zreferences](zreferences.md) | 10 | N/A | N/A | N/A | 10 | N/A | N/A | 10.0 | NONE |

## Series-level recommendations

### Writing & math issues
1. **Mass-replace bare expectation symbols.** Run a global pass converting bare `E_t`, `E_0`, `E[...]` to `\mathbb{E}_t`, `\mathbb{E}_0`, `\mathbb{E}[...]` (qe-math-010, proposed). This single fix would lift many MEDIUM lectures into LOW priority — 26 lectures affected.
2. **Eliminate transpose primes and `^T`.** Replace prime `'`, `^\prime`, and `^T` (when used as transpose) with `^\top` across the series (qe-math-002). Be careful to preserve derivative `u'`, `f'`, `v'` and next-period notation `x'`, `B'`, `\theta'` — 16 lectures affected.
3. **Switch distribution notation.** Replace `\mathcal{N}`, `\cal N`, `{\mathcal N}`, `{\cal N}` with plain `N` (qe-math-011, proposed) — 18 lectures affected.
4. **Convert all matrix environments.** Replace `\begin{array}`, `\begin{matrix}`, `\begin{pmatrix}` with `\begin{bmatrix}` (qe-math-003). The DLE-class lectures (`growth_in_dles`, `cattle_cycles`, `lucas_asset_pricing_dles`, `permanent_income_dles`, `hs_invertibility_example`) all share this issue — 15 lectures affected.
5. **Reduce decorative bolding.** Switch from `**term**` to italics (`*term*`) where intent is emphasis (qe-writing-005) — 25 lectures affected.
6. **Standardise "IID".** Replace "i.i.d." and "iid" with "IID" in narrative text (qe-writing-009, proposed) — 6 lectures affected.

### Code, figures, references, links & admonitions issues
7. **Add `:name: fig-...` fields to figures.** 45 / 62 lectures have figures without descriptive `:name:` fields, blocking `{numref}` cross-references (qe-fig-005). This is the single most pervasive deficit in the new categories. Modern lectures (`cagan_rational_expectations`, `doubts_or_variability`, `dovis_accounting_mf`, `risk_aversion_or_mistaken_beliefs`, `gorman_heterogeneous_households`, `hansen_richard_1987`, `hansen_jagannathan_1991`, `info_projection`) demonstrate the desired pattern (mystnb `caption:` + `name: fig-...`) — that pattern should be propagated.
8. **Unicode Greek in code.** Convert spelled-out Greek (`alpha`, `beta`, ...) to unicode (`α`, `β`, ...) in code cell parameters and function signatures (qe-code-002) — 35 lectures affected.
9. **Convert raw cross-series URLs to `{doc}`.** Replace `https://python.quantecon.org/...`, `python-intro.quantecon.org/...`, and `python-programming.quantecon.org/...` URLs with `{doc}\`intermediate:...\`` or `{doc}\`programming:...\`` intersphinx links (qe-link-002) — 17 lectures affected. Note: legacy `python-intro.quantecon.org` URLs are particularly stale and should map to `intermediate:` prefix.
10. **Remove `ax.set_title()` and lower axis labels.** Remove `ax.set_title()` calls and use mystnb `caption:` metadata instead (qe-fig-003) — 18 lectures affected. Lowercase axis labels in `set_xlabel`/`set_ylabel` (qe-fig-006) — 4 lectures affected.
11. **Drop unnecessary `figsize=`.** Trust the `_config.yml` defaults (qe-fig-001) — 24 lectures affected. The worst offender is `match_transport` (27 occurrences).
12. **Use `{cite:t}` for narrative refs.** Convert "Author (Year) {cite}`...`" patterns to `{cite:t}`...`` (qe-ref-001) — 12 lectures affected. Newer lectures (`cagan_rational_expectations`, `doubts_or_variability`, `dovis_accounting_mf`, `gorman_heterogeneous_households`, `hansen_richard_1987`, `hansen_jagannathan_1991`, `info_projection`, `risk_aversion_or_mistaken_beliefs`) already follow this pattern and can serve as templates.
13. **Treat the 6 HIGH-priority lectures first.** `hs_recursive_models`, `robustness`, `black_litterman`, `knowing_forecasts_of_others`, `classical_filtering`, `calvo_machine_learn` — all have math scores ≤ 3 and would benefit most from mechanical fixes. The worst figures/links sub-scores elsewhere are concentrated in `match_transport` figures (3) and `discrete_dp` / `robustness` / `stationary_densities` links (3–4).

### Notes on coverage

- 7 modern (post-2024) lectures are included: `cagan_rational_expectations`, `doubts_or_variability`, `dovis_accounting_mf`, `hansen_jagannathan_1991`, `hansen_richard_1987`, `info_projection`, `risk_aversion_or_mistaken_beliefs`. All score in the LOW-or-MEDIUM range.
- `hansen_richard_1987` is the strongest exemplar of `prf:`-prefixed proof directives in the series (26 `{prf:...}` directives) and should be referenced when remediating qe-admon-004 violations elsewhere.
- `orth_proj` (18 `{prf:...}`) is the other exemplar.
- JAX category is out-of-scope per series instructions; only `dovis_accounting_mf` and `calvo_machine_learn` import JAX in this series.
