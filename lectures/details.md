# Full findings & remediation plan

The complete cross-series breakdown behind the [front-page triage](intro.md). Start with the front page to decide *where* to focus; come here for the full numbers, the complete systemic-issue list, the full HIGH-priority lecture list, and the step-by-step remediation plan.

---

## Full scoreboard

Average score per category, per series (0–10). **Bold cells** mark each series' weakest category.

| # | Series | Lectures | Writing | Math | Code | Figures | References | Links | Admon | **Overall** | HIGH | MEDIUM | LOW | NONE |
|---|--------|----------|---------|------|------|---------|------------|-------|-------|-------------|------|--------|-----|------|
| 1 | [lecture-python-advanced.myst](lecture-python-advanced.myst/index.md) | 62 | 8.2 | **5.6** | 7.0 | 6.5 | 7.9 | 7.5 | 7.8 | **7.0** | 6 | 27 | 25 | 4 |
| 2 | [lecture-dp](lecture-dp/index.md) | 50 | 7.5 | 6.7 | 7.3 | **6.9** | 7.8 | 7.7 | 8.7 | **7.5** | 17 | 5 | 21 | 7 |
| 3 | [lecture-python-intro](lecture-python-intro/index.md) | 51 | 8.0 | 7.8 | 8.1 | **6.4** | 7.0 | 7.9 | 9.0 | **7.6** | 1 | 9 | 36 | 5 |
| 4 | [lecture-python-programming](lecture-python-programming/index.md) | 26 | 7.2 | 7.3 | 8.5 | **6.5** | N/A | 9.1 | 8.7 | **8.0** | 3 | 0 | 19 | 4 |
| 5 | [lecture-python.myst](lecture-python.myst/index.md) | 110 | **8.0** | 9.0 | 9.2 | 8.7 | 9.0 | 9.7 | 10.0 | **9.0** | 2 | 0 | 13 | 95 |
|   | **TOTAL / weighted avg** | **299** | **7.9** | **7.6** | **8.2** | **7.4** | **8.3** | **8.5** | **9.0** | **8.0** | **29** | **41** | **114** | **115** |

See the [charts](charts.md) for a visual version (heatmap, priority distribution, category averages).

---

## All systemic patterns

Every recurring issue, ranked by total lecture-count across the corpus. The front page covers the top six; this is the complete list. Rules tagged **(proposed)** are documented in the style guide but not yet in the `action-style-guide` registry.

### 1. `qe-writing-006` — Title Case in section headings (~170 / 299)
- `lecture-python.myst`: 87 / 110 (79 %) · `lecture-python-programming`: 24 / 26 (92 %) · `lecture-dp`: 21 / 50 · `lecture-python-intro`: 19 / 51

### 2. `qe-code-002` — Greek letters spelled out (`alpha`, `beta`) instead of unicode (~150 / 299)
- `lecture-python.myst`: 94 / 110 (mostly mixed within-lecture) · `lecture-python-advanced.myst`: 35 / 62 · `lecture-python-programming` is the exemplar (100 % compliant)

### 3. `qe-fig-001` — Unnecessary `figsize=` overrides (~125 / 299)
- `lecture-python.myst`: 75 / 110 · `lecture-python-intro`: 26 / 51 · `lecture-dp`: 24 / 50 · `lecture-python-programming`: 9 / 26

### 4. `qe-fig-005` — Figures lack a descriptive `:name:` for `numref` cross-referencing (~120 / 299)
- `lecture-python-advanced.myst`: 45 / 62 · `lecture-python-intro`: 36 / 51 · `lecture-python-programming`: 20 / 26 · `lecture-python.myst` exemplar (91 / 110 correct)

### 5. `qe-fig-003` — Embedded matplotlib titles (`ax.set_title`, `fig.suptitle`) (~90 / 299)
- `lecture-python.myst`: 44 / 110 (`navy_captain` ×13, `likelihood_ratio_process` ×8) · `lecture-dp`: 17 / 50 (`markov_jump_lq` ×6) · `lecture-python-intro`: 11 / 51 · `lecture-python-programming`: 5 / 26

### 6. `qe-link-002` — Raw markdown links to other QuantEcon series (~60 / 299)
- `lecture-python-advanced.myst`: 17 / 62 · `lecture-python.myst`: 17 / 110 · `lecture-dp`: 14 / 50 (`discrete_dp` ×10) · `lecture-python-intro`: 9 / 51 · `lecture-python-programming`: 3 / 26

### 7. `qe-math-010` (proposed) — `\mathbb{P/E/V}` with braces for probability, expectation, variance (~60 / 299)

### 8. `qe-math-002` — `\top` for transpose (~46 / 299)

### 9. `qe-ref-001` — Author-name narrative citations using `{cite}` instead of `{cite:t}` (~37 / 299, plus zero usage in 2 entire series)
- `lecture-dp` and `lecture-python-intro` have **zero `{cite:t}` usage** despite 22 and 15 lectures with citations that should use the in-text form

### 10. `qe-fig-006` — Title Case axis labels (~50 / 299)
- Should be lowercase. `two_computation` (`.myst`) has 46 instances; `tax_smoothing_2` (`dp`) has 9.

### 11. `qe-math-011` (proposed) — `\mathcal{N}` for the normal distribution (~30 / 299)

### 12. `qe-writing-009` (proposed) — `i.i.d.` / `iid` instead of `IID` (~30 / 299)

### 13. `qe-fig-007` — Removed matplotlib spines (~30 / 299)
- `french_rev` (`intro`) is an extreme outlier with 30 calls.

### 14. `qe-code-003` — Pip install not at top of lecture / missing `hide-output` (~15 / 299)
- `lecture-dp` has 5 lectures that install packages mid-lecture.

### 15. `qe-code-004` — `time.time()` benchmarking instead of `qe.Timer` (~15 / 299)
- Heavy in `lecture-dp`'s `ifp_egm` and `ifp_egm_transient_shocks` (6 each).

---

## All HIGH-priority lectures (29)

HIGH = overall ≤ 5.0 **or** a single category ≤ 4.

### Overall ≤ 5.0 — deep math/writing issues

| Series | Lecture | Writing | Math | Overall | Dominant issues |
|--------|---------|---------|------|---------|-----------------|
| dp | lqcontrol | 5 | 3 | **4.0** | transpose (`qe-math-002`), 17 array matrices (`qe-math-003`), Title Case headings (`qe-writing-006`) |
| advanced | hs_recursive_models | 6 | 2 | **4.0** | transpose, bold vectors (`qe-math-004`), expectation (`qe-math-010`), distribution naming (`qe-math-011`) |
| dp | lagrangian_lqdp | 6 | 3 | **4.5** | transpose, array matrices |
| dp | cross_product_trick | 6 | 3 | **4.5** | transpose, array matrices, + Critical `{eq}` ref |
| dp | perm_income_cons | 5 | 4 | **4.5** | Title Case headings, transpose, expectation |
| advanced | black_litterman | 7 | 2 | **4.5** | transpose (heavy), expectation, distribution naming |
| advanced | classical_filtering | 7 | 2 | **4.5** | transpose, expectation |
| advanced | knowing_forecasts_of_others | 6 | 3 | **4.5** | transpose, expectation, distribution naming |
| advanced | robustness | 7 | 2 | **4.5** | transpose (heavy), bold vectors, distribution naming |
| intro | supply_demand_foundations_v2 | 4 | 5 | **4.5** | no top-level H1, Title Case headings, mixed transpose |
| dp | lq_inventories | 6 | 4 | **5.0** | transpose, 11 array matrices |
| dp | markov_jump_lq | 7 | 3 | **5.0** | transpose, distribution naming, embedded titles (`qe-fig-003` ×6) |
| dp | calvo_machine_learn | 7 | 3 | **5.0** | transpose, array matrices, bold vectors, `{cite}` misuse ×8, binary pkg |
| advanced | calvo_machine_learn | 8 | 2 | **5.0** | transpose, array matrices, bold vectors |

Writing/Math shown; full per-category scores are in each lecture's report (sidebar).

### HIGH due to a single category floor ≤ 4

Otherwise-sound lectures dragged into HIGH by one weak category:

- **`lecture-dp`** (10): `calvo` (Ref 4, Fig 5 — `{cite:t}` ×12, embedded titles, raw URLs), `calvo_abreu` (Ref 4 — `{cite}` ×7), `cons_news` (Link 3 — 7 raw links + 4 `plt.title()`), `discrete_dp` (Link 3 — 10 raw links + `%timeit`), `dyn_stack` (Link 3, Math 4), `ifp_egm` (Code 4 — 6× `time.time()`), `ifp_egm_transient_shocks` (Code 4), `smoothing` (Math floor), `smoothing_tax` (Ref 3, Fig 4), `tax_smoothing_1` (Ref 4 — `{cite}` + mid-lecture pip install)
- **`lecture-python.myst`** (2): `cross_product_trick`, `misspecified_recovery`
- **`lecture-python-programming`** (3): `matplotlib`, `pandas_panel`, `workspace` — all Fig 4 (embedded titles / pedagogical `figsize=`)
- **`lecture-python-advanced.myst`** (6): the 6 in the table above
- **`lecture-python-intro`** (1): `supply_demand_foundations_v2` (in the table above)

**Note:** `cross_product_trick` and `calvo_machine_learn` appear in both `lecture-dp` and (in different forms) `lecture-python.myst` / `lecture-python-advanced.myst` — likely shared source files mirrored across series, so a single fix may resolve multiple entries.

---

## Step-by-step remediation plan

Ordered by impact / effort. The front-page "biggest wins" are Pass 1 + the top of Pass 2.

### Pass 1 — Mechanical sweeps (cheap, very high impact)

1. **Section-heading case (`qe-writing-006`)** — lowercase H2/H3/H4 first words except proper nouns / acronyms. ~170 lectures.
2. **Greek letters in code (`qe-code-002`)** — replace `alpha=`, `beta=`, etc. with `α`, `β` in code cells. ~150 lectures.
3. **Strip unnecessary `figsize=` (`qe-fig-001`)** — let `_config.yml` defaults apply. ~125 lectures.
4. **`IID` normalization (`qe-writing-009`, proposed)** — global replace `i.i.d.` / `iid` → `IID`. ~30 lectures.
5. **Distribution naming (`qe-math-011`, proposed)** — `\mathcal{N}` → `N`. ~30 lectures.
6. **Missing `\mathbb{}` braces (`qe-math-010`, proposed)** — add braces wherever `\mathbb E` / `\mathbb P` appear without them.

### Pass 2 — Targeted file edits (moderate effort)

7. **Critical build-risk fixes** — `divergence_measures.md:134` (`align` → `aligned`) and `cross_product_trick.md:133` (broken `{eq}` ref). Do these immediately.
8. **Add `:name:` fields to figures (`qe-fig-005`)** — required for `{numref}` cross-references. ~120 lectures.
9. **Sweep raw cross-series URLs (`qe-link-002`)** — replace `python.quantecon.org/...` links with `{doc}\`programming:...\`` / `{doc}\`intermediate:...\``. ~60 lectures.
10. **Transpose convention (`qe-math-002`)** — sweep prime / `^T` → `^\top` in the LQ-family cluster (`lqcontrol`, `lagrangian_lqdp`, `perm_income_cons`, `cross_product_trick`, `markov_perf`, `robustness`, `classical_filtering`, `black_litterman`, `smoothing`, `tax_smoothing_*`). Preserve derivative-prime (`u'`, `v'`) and next-period notation (`x'`).
11. **`{cite}` → `{cite:t}` for author-name citations (`qe-ref-001`)** — series-wide pass on `lecture-dp` and `lecture-python-intro`, which have **zero** `{cite:t}` usage today. ~37 lectures.

### Pass 3 — Bigger refactors (focus on the HIGH-priority list)

12. **Strip embedded matplotlib titles (`qe-fig-003`)** — move captions to MyST `{figure}` blocks. ~90 lectures.
13. **Matrix environments (`qe-math-003`)** — convert `array`/`pmatrix`/`matrix` to `bmatrix` in `lqcontrol`, `lq_inventories`, `lagrangian_lqdp`, DLE-class lectures.
14. **Vector decoration (`qe-math-004`)** — strip `\mathbf` / `\boldsymbol` / `\vec` from vectors in `hs_recursive_models`, `robustness`, `calvo*` lectures, `dyn_stack`.
15. **Restructure `supply_demand_foundations_v2.md`** — give it a single Title Case H1 at the top, fix typos.

### Pass 4 — Editorial (high effort, smaller per-lecture impact)

16. **One-sentence paragraphs (`qe-writing-001`)** — manual editing pass on Overview sections (script-assisted but human-driven).

---

## How to read the per-lecture reports

Every lecture has its own report (sidebar, grouped by series), following the [template in the spec](spec.md):

- 8-row score breakdown (Writing, Math, Code, JAX out of scope, Figures, References, Links, Admonitions)
- Issues bucketed by severity (Critical / High / Medium / Low) with `qe-*` rule IDs
- Strengths
- Recommended actions

---

## Notes on calibration

- Scoring was deliberately strict: a 9–10 score required essentially no deviations.
- Categories not applicable to a given lecture are scored `N/A` and excluded from the overall (e.g. `lecture-python-programming` is N/A on References because no lecture in that series uses `{cite}`).
- **JAX is out of scope** — not the same as N/A. JAX rules apply to JAX-specific lectures concentrated in `lecture-jax`, which was not audited here.
- 7 of the rules cited are **(proposed)** — documented in the QuantEcon style guide but not yet in the `action-style-guide` rule registry. They are tracked in [issue #18](https://github.com/QuantEcon/action-style-guide/issues/18).
