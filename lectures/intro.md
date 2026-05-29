# QuantEcon Style Audit — Cross-Series Report (v2)

- **Audit date:** 2026-05-27 (v1) / 2026-05-28 (v2 extension)
- **Scope:** 5 lecture series, **299 lectures** audited against the [QuantEcon style guide](https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide/).
- **Scoring dimensions:** Writing, Math, Code, Figures, References, Links, Admonitions — 7 in-scope categories (49 rules + 7 proposed addendum rules). **JAX out of scope** for this audit run (rules only apply to JAX-specific lectures which are concentrated in `lecture-jax`, not in this corpus).
- **Spec / rubric:** [`_AUDIT_SPEC.md`](spec.md) — uses canonical `qe-*` rule IDs from [QuantEcon/action-style-guide](https://github.com/QuantEcon/action-style-guide).

## About this repository

This repo follows the QuantEcon **`audit.YYYY-MM.{topic}`** convention for time-bounded audits:

- The date prefix indicates when the audit was performed — useful for assessing staleness at a glance.
- The topic suffix (`style-guide` here) identifies what was audited.
- These repos are **disposable**: once an audit's findings have been actioned (or its data has been superseded by a fresher audit), the repo can be archived or deleted without affecting other QuantEcon infrastructure.

**What's committed here:**

- [`_AUDIT_SPEC.md`](spec.md) — the canonical scoring rubric and report template (v2, aligned with action-style-guide `qe-*` rule IDs)
- This top-level `README.md` — cross-series synthesis
- Five series-level `README.md` files — one per audited lecture series

**What's not committed:** the 299 per-lecture reports produced during the audit. The series-level synthesis is the durable artifact.

---

## Series scoreboard

Series ordered worst → best by overall average. Lower scores ⇒ higher priority. **Bold cells** are the weakest category for each series.

| # | Series | Lectures | Writing | Math | Code | Figures | References | Links | Admon | **Overall** | HIGH | MEDIUM | LOW | NONE |
|---|--------|----------|---------|------|------|---------|------------|-------|-------|-------------|------|--------|-----|------|
| 1 | [lecture-python-advanced.myst](lecture-python-advanced.myst/index.md) | 62 | 8.2 | **5.6** | 7.0 | 6.5 | 7.9 | 7.5 | 7.8 | **7.0** | 6 | 27 | 25 | 4 |
| 2 | [lecture-dp](lecture-dp/index.md) | 50 | 7.5 | 6.7 | 7.3 | **6.9** | 7.8 | 7.7 | 8.7 | **7.5** | 17 | 5 | 21 | 7 |
| 3 | [lecture-python-intro](lecture-python-intro/index.md) | 51 | 8.0 | 7.8 | 8.1 | **6.4** | 7.0 | 7.9 | 9.0 | **7.6** | 1 | 9 | 36 | 5 |
| 4 | [lecture-python-programming](lecture-python-programming/index.md) | 26 | 7.2 | 7.3 | 8.5 | **6.5** | N/A | 9.1 | 8.7 | **8.0** | 3 | 0 | 19 | 4 |
| 5 | [lecture-python.myst](lecture-python.myst/index.md) | 110 | **8.0** | 9.0 | 9.2 | 8.7 | 9.0 | 9.7 | 10.0 | **9.0** | 2 | 0 | 13 | 95 |
|   | **TOTAL / weighted avg** | **299** | **7.9** | **7.6** | **8.2** | **7.4** | **8.3** | **8.5** | **9.0** | **8.0** | **29** | **41** | **114** | **115** |

**Headline:** corpus averages **8.0/10** overall. The HIGH-priority count rose from 16 (v1) to **29** (v2) — the 5 extension categories surfaced 13 additional HIGH lectures, mostly in `lecture-dp` (10 new HIGH driven by References/Links/Figures floor) and `lecture-python-programming` (3 new HIGH driven by Figures).

### Priority distribution (visualised)

```
HIGH   ██████ 29        (9.7%)
MEDIUM █████████ 41       (13.7%)
LOW    ███████████████████████ 114    (38.1%)
NONE   ███████████████████████ 115    (38.5%)
```

`lecture-python.myst` is in excellent shape (86 % NONE/LOW). `lecture-dp` and `lecture-python-advanced.myst` are the highest-leverage targets for systemic remediation.

---

## Cross-series systemic patterns

Issues ranked by total lecture-count across all five series. **The v2 extension fundamentally changed the picture**: Figures and Code categories now contain three of the top five systemic issues across the corpus, on par with the long-standing W3 / Title Case heading problem.

### 1. **`qe-writing-006` — Title Case in section headings** (~170 / 299 lectures)
Still the single most prevalent violation. Carry-forward from v1.
- `lecture-python.myst`: 87 / 110 (79 %)
- `lecture-python-programming`: 24 / 26 (92 %)
- `lecture-dp`: 21 / 50
- `lecture-python-intro`: 19 / 51

### 2. **`qe-code-002` — Greek letters spelled out (`alpha`, `beta`) in code instead of unicode (`α`, `β`)** (~150 / 299 lectures)
Many lectures mix conventions within the same file.
- `lecture-python.myst`: 94 / 110 (mostly mixed within-lecture)
- `lecture-python-advanced.myst`: 35 / 62
- Smaller counts elsewhere; `lecture-python-programming` is the exemplar (100 % compliance on `qe-code-002` where applicable)

### 3. **`qe-fig-001` — Unnecessary `figsize=` overrides** (~125 / 299 lectures)
Defaults from `_config.yml` should apply unless there's a specific reason. Heavy offenders set `figsize=` 5–14 times in a single lecture.
- `lecture-python.myst`: 75 / 110
- `lecture-python-intro`: 26 / 51
- `lecture-dp`: 24 / 50
- `lecture-python-programming`: 9 / 26

### 4. **`qe-fig-005` — Figures lack descriptive `:name:` field for `numref` cross-referencing** (~120 / 299 lectures)
- `lecture-python-advanced.myst`: 45 / 62
- `lecture-python-intro`: 36 / 51
- `lecture-python-programming`: 20 / 26
- `lecture-python.myst` is the exemplar — 91 / 110 lectures use the convention correctly

### 5. **`qe-fig-003` — Embedded matplotlib titles (`ax.set_title`, `fig.suptitle`)** (~90 / 299 lectures)
Captions belong in MyST `{figure}` blocks, not embedded in the plot.
- `lecture-python.myst`: 44 / 110 (`navy_captain` ×13, `likelihood_ratio_process` ×8)
- `lecture-dp`: 17 / 50 (`markov_jump_lq` ×6, `cons_news` ×4)
- `lecture-python-intro`: 11 / 51
- `lecture-python-programming`: 5 / 26 (mostly pedagogical)

### 6. **`qe-link-002` — Raw markdown links to other QuantEcon series** (~60 / 299 lectures)
Should use `{doc}` with the intersphinx prefix.
- `lecture-python-advanced.myst`: 17 / 62
- `lecture-python.myst`: 17 / 110
- `lecture-dp`: 14 / 50 (`discrete_dp` ×10, `cons_news` ×7)
- `lecture-python-intro`: 9 / 51
- `lecture-python-programming`: 3 / 26

### 7. **`qe-math-A1` (proposed: `qe-math-010`) — `\mathbb{P/E/V}` with braces for probability, expectation, variance** (~60 / 299 lectures)
Carry-forward from v1.

### 8. **`qe-math-002` — `\top` for transpose** (~46 / 299 lectures)
Carry-forward from v1.

### 9. **`qe-ref-001` — Author-name narrative citations using `{cite}` instead of `{cite:t}`** (~37 / 299 lectures, **plus zero-usage in 2 entire series**)
- `lecture-dp` and `lecture-python-intro` have **zero `{cite:t}` usage** despite 22 and 15 lectures with citations that should use the in-text form
- `lecture-python-advanced.myst` is intermediate
- `lecture-python.myst` shows the correct pattern in newer lectures

### 10. **`qe-fig-006` — Title Case axis labels** (~50 / 299 lectures)
Should be lowercase. `two_computation` (`.myst`) has 46 instances; `tax_smoothing_2` (`dp`) has 9.

### 11. **`qe-math-A3` (proposed: `qe-math-011`) — `\mathcal{N}` for normal distribution** (~30 / 299 lectures)
Carry-forward from v1.

### 12. **`qe-writing-A1` (proposed: `qe-writing-009`) — `i.i.d.` / `iid` instead of `IID`** (~30 / 299 lectures)
Carry-forward from v1.

### 13. **`qe-fig-007` — Removed matplotlib spines** (~30 / 299 lectures)
Style guide says keep the default box. `french_rev` (`intro`) is an extreme outlier with 30 calls.

### 14. **`qe-code-003` — Pip install not at top of lecture / missing `hide-output` tag** (~15 / 299 lectures)
- `lecture-dp`: 5 lectures install packages mid-lecture
- Others scattered

### 15. **`qe-code-004` — `time.time()` benchmarking instead of `qe.Timer`** (~15 / 299 lectures)
- `lecture-dp`: heavy in `ifp_egm` and `ifp_egm_transient_shocks` (6 each)

---

## Build-risk findings (act immediately)

These can break PDF builds or produce broken references. **Two such findings in the corpus, both in `lecture-python.myst`:**

| Location | Issue | Rule | Risk |
|----------|-------|------|------|
| `lecture-python.myst/lectures/divergence_measures.md:134` | `\begin{align}` inside a `$$ … $$` block | `qe-math-006` | PDF build will fail. Replace with `\begin{aligned}`. |
| `lecture-python.myst/lectures/cross_product_trick.md:133` | Broken `{eq}` reference: `` {eq}`eq:Kalman102} `` (mismatched braces); label `(eq:Kalman102)` is attached to a bare `align*` block on line 121 rather than a numbered `$$ … $$` block | `qe-math-A6` / `qe-math-007` | Cross-reference cannot bind. |

---

## Consolidated HIGH-priority lectures (29 lectures, by lowest overall score)

29 lectures are HIGH priority because either their overall score ≤ 5.0 **or** a single category score ≤ 4. The full list:

### Overall ≤ 5.0 (deep multi-category issues)

| Series | Lecture | Writing | Math | Code | Fig | Ref | Link | Adm | Overall | Dominant issues |
|--------|---------|---------|------|------|-----|-----|------|-----|---------|-----------------|
| dp | lqcontrol | 5 | 3 | — | — | — | — | — | **4.0** | M2, M4 (17 array matrices), W3 |
| advanced | hs_recursive_models | 6 | 2 | — | — | — | — | — | **4.0** | M2, M5, M7, M9 |
| dp | lagrangian_lqdp | 6 | 3 | — | — | — | — | — | **4.5** | M2, M4 |
| dp | cross_product_trick | 6 | 3 | — | — | — | — | — | **4.5** | M2, M3, M4 + Critical `{eq}` ref |
| dp | perm_income_cons | 5 | 4 | — | — | — | — | — | **4.5** | W3, M2, M7 |
| advanced | black_litterman | 7 | 2 | — | — | — | — | — | **4.5** | M2 (heavy), M7, M9 |
| advanced | classical_filtering | 7 | 2 | — | — | — | — | — | **4.5** | M2, M7 |
| advanced | knowing_forecasts_of_others | 6 | 3 | — | — | — | — | — | **4.5** | M2, M7, M9 |
| advanced | robustness | 7 | 2 | — | — | — | — | — | **4.5** | M2 (heavy), M5, M9 |
| intro | supply_demand_foundations_v2 | 4 | 5 | — | — | — | — | — | **4.5** | W2 (no proper H1), W3, mixed `^T`/`^\top` |
| dp | lq_inventories | 6 | 4 | — | — | — | — | — | **5.0** | M2, M4 (11 array matrices) |
| dp | markov_jump_lq | 7 | 3 | — | — | — | — | — | **5.0** | M2, M9 + qe-fig-003 ×6 |
| dp | calvo_machine_learn | 7 | 3 | — | — | — | — | — | **5.0** | M2, M3, M5 + qe-ref-001 ×8 + binary pkg |
| advanced | calvo_machine_learn | 8 | 2 | — | — | — | — | — | **5.0** | M2, M3, M5 |

> Dashes = carry-forward from v1; new-category scores in the per-lecture reports.

### HIGH due to category floor ≤ 4 (single weak category drags into HIGH)

These lectures otherwise look fine but have a single in-scope category scoring ≤ 4:

- **`lecture-dp`** (10 new HIGH from extension):
  - `calvo` (Ref 4, Fig 5) — `{cite:t}` × 12, embedded titles, raw cross-series URLs
  - `calvo_abreu` (Ref 4) — `{cite}` × 7
  - `cons_news` (Link 3) — 7 raw cross-series markdown links + 4 `plt.title()`
  - `discrete_dp` (Link 3) — 10 raw cross-series links + `%timeit` magics
  - `dyn_stack` (Link 3, Math 4) — 5 raw cross-series links + apostrophe transpose
  - `ifp_egm` (Code 4) — 6× `time.time()` benchmarking
  - `ifp_egm_transient_shocks` (Code 4) — 6× `time.time()` benchmarking
  - `smoothing` (M2 / Math floor)
  - `smoothing_tax` (Ref 3, Fig 4) — 8 `{cite}` + Title Case axis labels + embedded titles
  - `tax_smoothing_1` (Ref 4) — `{cite}` misuse + mid-lecture pip install
- **`lecture-python.myst`** (no new HIGH from extension): both HIGH lectures are the v1 carry-forward (`cross_product_trick`, `misspecified_recovery`)
- **`lecture-python-programming`** (3 new HIGH from extension):
  - `matplotlib` (Fig 4) — pedagogical `figsize=` overrides + embedded titles
  - `pandas_panel` (Fig 4) — 4× embedded titles
  - `workspace` (Fig 4) — 2× embedded titles
- **`lecture-python-intro`** (no new HIGH from extension)
- **`lecture-python-advanced.myst`** (no new HIGH from extension): all 6 HIGH are v1 carry-forward

**Note:** `cross_product_trick` and `calvo_machine_learn` appear in both `lecture-dp` and (in different forms) in `lecture-python.myst` / `lecture-python-advanced.myst`. These are likely shared source files mirrored across series.

---

## Recommended remediation order

A high-leverage way to lift scores across the entire corpus, ordered by impact / effort:

### Pass 1 — Mechanical sweeps (cheap, very high impact)

1. **Section-heading case (`qe-writing-006`)** — script that lowercases all H2/H3/H4 first words except proper nouns/acronyms. Targets ~170 lectures.
2. **Greek letters in code (`qe-code-002`)** — script that replaces `alpha=`, `beta=`, `gamma=`, etc. with `α`, `β`, `γ` in code cells. ~150 lectures.
3. **Strip unnecessary `figsize=` (`qe-fig-001`)** — let `_config.yml` defaults apply. ~125 lectures.
4. **`IID` normalization (`qe-writing-A1` / `qe-writing-009`)** — global replace `i.i.d.` / `iid` → `IID`. ~30 lectures.
5. **Distribution naming (`qe-math-A3` / `qe-math-011`)** — `\mathcal{N}` → `N`. ~30 lectures.
6. **Missing `\mathbb{}` braces (`qe-math-A1` / `qe-math-010`)** — add braces wherever `\mathbb E` / `\mathbb P` appear without them.

### Pass 2 — Targeted file edits (moderate effort)

7. **Critical build-risk fixes** — `divergence_measures.md:134` (`align` → `aligned`) and `cross_product_trick.md:133` (broken `{eq}` ref). Do these immediately, separately from any larger remediation effort.
8. **Add `:name:` fields to figures (`qe-fig-005`)** — required for `{numref}` cross-references; ~120 lectures.
9. **Sweep raw cross-series URLs (`qe-link-002`)** — replace `python.quantecon.org/...` links with `{doc}\`programming:...\`` / `{doc}\`intermediate:...\`` etc. Use the intersphinx prefix table in `qe-link-002`. ~60 lectures.
10. **Transpose convention (`qe-math-002`)** — sweep prime / `^T` → `^\top` in the LQ-family cluster (`lqcontrol`, `lagrangian_lqdp`, `perm_income_cons`, `cross_product_trick`, `markov_perf`, `robustness`, `classical_filtering`, `black_litterman`, `smoothing`, `tax_smoothing_*`). Care to preserve derivative-prime (`u'`, `v'`) and next-period notation (`x'`).
11. **`{cite}` → `{cite:t}` for author-name citations (`qe-ref-001`)** — series-wide pass on `lecture-dp` and `lecture-python-intro` which have **zero** `{cite:t}` usage today. ~37 lectures total.

### Pass 3 — Bigger refactors (focus on HIGH-priority list)

12. **Strip embedded matplotlib titles (`qe-fig-003`)** — move captions to MyST `{figure}` blocks. ~90 lectures.
13. **Matrix environments (`qe-math-003`)** — convert `array`/`pmatrix`/`matrix` to `bmatrix` in `lqcontrol`, `lq_inventories`, `lagrangian_lqdp`, DLE-class lectures.
14. **Vector decoration (`qe-math-004`)** — strip `\mathbf` / `\boldsymbol` / `\vec` from vectors in `hs_recursive_models`, `robustness`, `calvo*` lectures, `dyn_stack`.
15. **Restructure `supply_demand_foundations_v2.md`** — give it a single Title Case H1 at the top, fix typos.

### Pass 4 — Editorial (high effort, smaller per-lecture impact)

16. **One-sentence paragraphs (`qe-writing-001`)** — manual editing pass on Overview sections of every lecture (script-assisted but human-driven).

---

## What changed in v2 vs v1

| Metric | v1 (writing + math) | v2 (7 categories) |
|--------|---------------------|-------------------|
| Lectures audited | 292 | 299 (lecture-python-advanced.myst added 7) |
| Rules in scope | 17 (W1–W8 + M1–M14, with 7 proposed addendum) | 49 + 7 proposed |
| Categories scored | 2 | 7 (JAX out of scope) |
| Overall corpus average | 7.8 | 8.0 |
| HIGH-priority lectures | 16 | 29 |
| Top systemic issue | W3 / heading case (170 lectures) | unchanged, plus parallel-tier issues from Code and Figures |

**The v2 extension didn't surface lectures that are *uniformly* broken** — most new HIGHs are otherwise-good lectures with one category scoring ≤ 4. This is informative: most quality issues are *category-specific*, not pervasive. A series-wide sweep targeting the top systemic issues from §Cross-series patterns would lift the bulk of the corpus into LOW/NONE.

---

## How to read the per-lecture reports

The per-lecture reports are not committed to this repo (see "About this repository"). They exist in the audit author's working tree and follow the [template in `_AUDIT_SPEC.md` §6](spec.md):

- 8-row score breakdown (Writing, Math, Code, JAX out of scope, Figures, References, Links, Admonitions)
- Issues bucketed by severity (Critical / High / Medium / Low) with `qe-*` Rule IDs
- Strengths
- Recommended actions

---

## Folder map

```
quantecon-style-audit/                 (this repo)
├── README.md                          ← you are here
├── _AUDIT_SPEC.md                     ← rubric + report template (v2)
├── lecture-python-intro/README.md     51 lectures
├── lecture-python-programming/README.md  26 lectures
├── lecture-python.myst/README.md     110 lectures
├── lecture-python-advanced.myst/README.md  62 lectures
└── lecture-dp/README.md               50 lectures
```

---

## Notes on calibration

- Scoring was deliberately strict: a 9–10 score required essentially no deviations.
- Categories not applicable to a given lecture are scored `N/A` and excluded from the overall (e.g. `lecture-python-programming` is N/A on References because no lecture in that series uses `{cite}`).
- JAX is **out of scope** for this audit run — not the same as N/A. JAX rules apply to JAX-specific lectures concentrated in `lecture-jax`, which was not audited here.
- v1 findings (writing + math) were preserved verbatim using v1 `W*/M*` rule IDs in carry-forward sections. Cross-series synthesis uses canonical `qe-*` IDs (with `qe-math-A*` / `qe-writing-A1` placeholders for the 7 proposed addendum rules); see [`_AUDIT_SPEC.md` §10](spec.md) for the v1↔v2 mapping.
- Inter-subagent calibration drift was observed during v1 (e.g. `lecture-python-programming` v1 scored zero HIGH despite systemic W3 issues — re-evaluated in v2). v2 series-level outputs are more consistent because each subagent worked from the v1 baseline.
