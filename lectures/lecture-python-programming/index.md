# Summary

Style audit of the **lecture-python-programming** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-21
- **Corpus snapshot:** `ceec881028`
- **Lectures audited:** 27
- **Average overall score:** 8.1 / 10
- **Average per-category scores:** writing 4.1, math 9.0, code 8.5, figures 7.3, links 9.8, admon 9.9  *(references not in scope for this series)*
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
- **Judgment-review coverage:** **26 of 27 reviewed** — scores for the unreviewed 1 reflect the 41 measured rules only, so they are not directly comparable with the reviewed ones.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
The highest-scoring series overall (8.6) and the corpus's model for code and mathematics:
Math scores 9.1, and `qe-code-002` — spelled-out Greek letters, which reaches 106 lectures
corpus-wide — appears in **1 of 27** here, four occurrences in total.

It also carries the weakest single category anywhere in the corpus: **Writing, at 5.7**.
That is almost entirely one rule. `qe-writing-006` (Title Case in H2+ headings) appears in
**23 of 27 lectures**, 178 headings in total — 85 % of the series. And it accounts for the
whole HIGH list: **all 5 HIGH lectures are floored by Writing**, none by anything else.

One scripted sweep over heading capitalisation would clear every HIGH lecture in this
series. No other series has that property.
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 19    | 70.4% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 5     | 18.5% |
| NONE     | 3     | 11.1% |
<!-- /qe:series-priority -->

## Top systemic issues across the series

Ranked by how many of the series' lectures each rule reaches.

<!-- qe:series-systemic -->
1. **`qe-writing-006`** — Capitalize lecture titles properly — **23 / 27** lectures, 178 occurrences.
2. **`qe-fig-005`** — Descriptive figure names for cross-referencing — **21 / 27** lectures, 128 occurrences.
3. **`qe-writing-008`** — Remove excessive whitespace between words — **16 / 27** lectures, 43 occurrences.
4. **`qe-fig-008`** — Use lw=2 for line charts — **15 / 27** lectures, 66 occurrences.
5. **`qe-writing-001`** — Use one sentence per paragraph — **15 / 27** lectures, 29 occurrences.
6. **`qe-fig-001`** — Do not set figure size unless necessary — **9 / 27** lectures, 22 occurrences.
7. **`qe-writing-004`** — Avoid unnecessary capitalization in narrative text — **6 / 27** lectures, 14 occurrences.
8. **`qe-fig-002`** — Prefer code-generated figures — **5 / 27** lectures, 15 occurrences.
9. **`qe-fig-003`** — No matplotlib embedded titles — **5 / 27** lectures, 11 occurrences.
10. **`qe-code-003`** — Package installation at lecture top — **3 / 27** lectures, 3 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-002`** — Use dropdown class for solutions
- **`qe-code-005`** — Use quantecon timeit for benchmarking
- **`qe-fig-004`** — Caption formatting conventions
- **`qe-fig-010`** — Plotly figures require latex directive
- **`qe-link-001`** — Use markdown style links for lectures in same lecture series
- **`qe-math-003`** — Use square brackets for matrix notation
- **`qe-math-004`** — Do not use bold face for matrices or vectors
- **`qe-math-005`** — Use curly brackets for sequences
- **`qe-math-006`** — Use aligned environment correctly for PDF compatibility
- **`qe-math-007`** — Use automatic equation numbering, not manual tags
- **`qe-math-008`** — Explain special notation (vectors/matrices)
- **`qe-math-011`** *(proposed)* — Distribution names in plain letters, not \mathcal / \mathbb
- **`qe-math-013`** *(proposed)* — Reference equations via {eq}`label`
- **`qe-ref-001`** — Use correct citation style
- **`qe-writing-009`** *(proposed)* — Write "IID" — not "i.i.d." or "iid"
<!-- /qe:series-clean -->

## Series-level recommendations

<!-- qe:series-recommendations -->
1. **`qe-writing-006` — sentence-case the H2+ headings** (23 / 27, 178 headings). This is
   the series. It is a sweep, but it needs the proper-noun allowlist in
   `tools/qestyle_rules.py` to avoid lowercasing `Python`, `Jupyter` or `Anaconda` — the
   list is already curated from this corpus.
2. **`qe-fig-005` — name the figures** (21 / 27, 128 figures). Second-largest reach, same
   mechanical fix as elsewhere.
3. **`qe-writing-008` — collapse repeated spaces** (16 / 27, 43 occurrences). Small here;
   fold it into the same commit as item 1.
4. **`qe-fig-008` — `lw=2` on line plots** (15 / 27, 66 calls).
5. **`python_by_example.md` — two unclosed `{exercise-start}` fences** (lines 499 and 549,
   `qe-admon-003`). Structural rather than stylistic: each swallows the rest of its
   exercise, including a nested `{hint}` at the same tick count. These are the only two
   malformed gated directives in roughly 690 across the whole corpus — fix them regardless
   of the rest.
6. **Leave the code alone.** This series is where the other four should be looking for
   Greek-letter and timing conventions, not the reverse.
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [about_py](about_py.md) | 3 | — | 10 | 7.5 | — | 8 | — | **7.1** | HIGH |
| 2 | [python_by_example](python_by_example.md) | 3 | 9 | 7.5 | 6.5 | — | 10 | 7.5 | **7.2** | HIGH |
| 3 | [pandas](pandas.md) | 3 | — | 7 | 6.5 | — | 10 | 10 | **7.3** | HIGH |
| 4 | [pandas_panel](pandas_panel.md) | 3.5 | — | 8.5 | 4.5 | — | 10 | 10 | **7.3** | HIGH |
| 5 | [jax_intro](jax_intro.md) | 3 | — | 7.5 | 7 | — | 10 | 10 | **7.5** | HIGH |
| 6 | [numpy](numpy.md) | 3 | 8 | 7 | 7 | — | 10 | 10 | **7.5** | HIGH |
| 7 | [matplotlib](matplotlib.md) | 4 | 10 | 7 | 4.5 | — | 10 | 10 | **7.6** | HIGH |
| 8 | [numba](numba.md) | 3 | 7.5 | 8.5 | 7.5 | — | 9 | 10 | **7.6** | HIGH |
| 9 | [scipy](scipy.md) | 3 | 7.5 | 7 | 8 | — | 10 | 10 | **7.6** | HIGH |
| 10 | [names](names.md) | 3 | — | 8.5 | 7 | — | 10 | 10 | **7.7** | HIGH |
| 11 | [workspace](workspace.md) | 4.5 | — | 8.5 | 5.5 | — | 10 | 10 | **7.7** | LOW |
| 12 | [getting_started](getting_started.md) | 3 | — | 10 | 7 | — | 10 | 10 | **8.0** | HIGH |
| 13 | [python_oop](python_oop.md) | 3 | 10 | 7.5 | 7.5 | — | 10 | 10 | **8.0** | HIGH |
| 14 | [autodiff](autodiff.md) | 7 | 7.5 | 7.5 | 6.5 | — | 10 | 10 | **8.1** | LOW |
| 15 | [polars](polars.md) | 4.5 | — | 9 | 7 | — | 10 | 10 | **8.1** | LOW |
| 16 | [sympy](sympy.md) | 4 | 8 | 8.5 | 10 | — | 8 | 10 | **8.1** | HIGH |
| 17 | [functions](functions.md) | 3 | 10 | 8.5 | 7.5 | — | 10 | 10 | **8.2** | HIGH |
| 18 | [oop_intro](oop_intro.md) | 4 | — | 9 | — | — | 10 | 10 | **8.2** | HIGH |
| 19 | [troubleshooting](troubleshooting.md) | 5.5 | — | — | 9 | — | 10 | — | **8.2** | LOW |
| 20 | [need_for_speed](need_for_speed.md) | 3 | — | 10 | 8.5 | — | 10 | 10 | **8.3** | HIGH |
| 21 | [numpy_vs_numba_vs_jax](numpy_vs_numba_vs_jax.md) | 3 | 10 | 8.5 | 8.5 | — | 10 | 10 | **8.3** | HIGH |
| 22 | [python_advanced_features](python_advanced_features.md) | 4.5 | — | 8.5 | 8.5 | — | 10 | 10 | **8.3** | LOW |
| 23 | [python_essentials](python_essentials.md) | 3 | 10 | 8.5 | — | — | 10 | 10 | **8.3** | HIGH |
| 24 | [writing_good_code](writing_good_code.md) | 4.5 | 10 | 10 | 7.5 | — | 10 | 10 | **8.7** | NONE |
| 25 | [debugging](debugging.md) | 3.5 | 10 | 10 | 9 | — | 10 | 10 | **8.8** | HIGH |
| 26 | [status](status.md) | 10 | — | 9 | — | — | 10 | — | **9.7** | NONE |
| 27 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
