# Summary

Style audit of the **lecture-python-programming** series.

<!-- qe:series-meta -->
- **Audit date:** 2026-08-21
- **Corpus snapshot:** `ceec881028`
- **Lectures audited:** 27
- **Average overall score:** 8.6 / 10
- **Average per-category scores:** writing 5.7, math 9.1, code 9.8, figures 7.2, links 9.8, admon 9.9  *(references not in scope for this series)*
- **JAX:** out of scope — the `qe-jax-*` rules target `lecture-jax`.
<!-- /qe:series-meta -->

<!-- qe:series-narrative -->
_The series-level reading of these numbers goes here._
<!-- /qe:series-narrative -->

## Priority distribution

<!-- qe:series-priority -->
| Priority | Count | % |
|----------|-------|---|
| HIGH     | 5     | 18.5% |
| MEDIUM   | 0     | 0.0% |
| LOW      | 11    | 40.7% |
| NONE     | 11    | 40.7% |
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
10. **`qe-fig-009`** — Figure sizing — **5 / 27** lectures, 7 occurrences.
<!-- /qe:series-systemic -->

## Clean across the series

Checked rules with no violation anywhere in the series — the conventions this series
already holds to.

<!-- qe:series-clean -->
- **`qe-admon-001`** — Use gated syntax for executable code in exercises
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
_generated_
<!-- /qe:series-recommendations -->

## Lectures ranked by priority (lowest score first)

Scores are 0–10 per category; **Overall** is the mean of the in-scope categories, and
**Priority** follows [spec §4](../spec.md). A dash means the category is not applicable to
that lecture. Click a lecture for its full report.

<!-- qe:series-ranked -->
| # | Lecture | Writing | Math | Code | Figures | References | Links | Admon | Overall | Priority |
|---|---------|---|---|---|---|---|---|---|---------|----------|
| 1 | [about_py](about_py.md) | 4.5 | — | 10 | 7 | — | 8 | — | **7.4** | LOW |
| 2 | [python_by_example](python_by_example.md) | 4 | 9 | 10 | 6 | — | 10 | 7.5 | **7.8** | HIGH |
| 3 | [numpy](numpy.md) | 3.5 | 8.5 | 9 | 7 | — | 10 | 10 | **8.0** | HIGH |
| 4 | [numba](numba.md) | 4.5 | 7.5 | 10 | 7.5 | — | 9 | 10 | **8.1** | LOW |
| 5 | [scipy](scipy.md) | 4.5 | 7.5 | 8.5 | 8 | — | 10 | 10 | **8.1** | LOW |
| 6 | [matplotlib](matplotlib.md) | 5.5 | 10 | 9 | 4.5 | — | 10 | 10 | **8.2** | LOW |
| 7 | [pandas](pandas.md) | 4.5 | — | 10 | 6.5 | — | 10 | 10 | **8.2** | LOW |
| 8 | [pandas_panel](pandas_panel.md) | 6.5 | — | 10 | 4.5 | — | 10 | 10 | **8.2** | LOW |
| 9 | [jax_intro](jax_intro.md) | 4.5 | — | 10 | 7 | — | 10 | 10 | **8.3** | LOW |
| 10 | [troubleshooting](troubleshooting.md) | 6 | — | — | 9 | — | 10 | — | **8.3** | LOW |
| 11 | [getting_started](getting_started.md) | 5 | — | 10 | 7 | — | 10 | 10 | **8.4** | LOW |
| 12 | [need_for_speed](need_for_speed.md) | 4 | — | 10 | 8 | — | 10 | 10 | **8.4** | HIGH |
| 13 | [polars](polars.md) | 6.5 | — | 9 | 7 | — | 10 | 10 | **8.5** | LOW |
| 14 | [workspace](workspace.md) | 7 | — | 10 | 5.5 | — | 10 | 10 | **8.5** | LOW |
| 15 | [names](names.md) | 6 | — | 10 | 7 | — | 10 | 10 | **8.6** | NONE |
| 16 | [python_oop](python_oop.md) | 4 | 10 | 10 | 7.5 | — | 10 | 10 | **8.6** | HIGH |
| 17 | [autodiff](autodiff.md) | 8 | 7.5 | 10 | 6.5 | — | 10 | 10 | **8.7** | NONE |
| 18 | [python_essentials](python_essentials.md) | 3.5 | 10 | 10 | — | — | 10 | 10 | **8.7** | HIGH |
| 19 | [writing_good_code](writing_good_code.md) | 4.5 | 10 | 10 | 7.5 | — | 10 | 10 | **8.7** | NONE |
| 20 | [functions](functions.md) | 5 | 10 | 10 | 7.5 | — | 10 | 10 | **8.8** | NONE |
| 21 | [sympy](sympy.md) | 7.5 | 8 | 10 | 10 | — | 8 | 10 | **8.9** | NONE |
| 22 | [debugging](debugging.md) | 5 | 10 | 10 | 9 | — | 10 | 10 | **9.0** | NONE |
| 23 | [numpy_vs_numba_vs_jax](numpy_vs_numba_vs_jax.md) | 5.5 | 10 | 10 | 8.5 | — | 10 | 10 | **9.0** | NONE |
| 24 | [oop_intro](oop_intro.md) | 7 | — | 10 | — | — | 10 | 10 | **9.2** | NONE |
| 25 | [python_advanced_features](python_advanced_features.md) | 7.5 | — | 10 | 8.5 | — | 10 | 10 | **9.2** | NONE |
| 26 | [status](status.md) | 10 | — | 9 | — | — | 10 | — | **9.7** | NONE |
| 27 | [intro](intro.md) | 10 | — | — | — | — | 10 | — | **10.0** | NONE |
<!-- /qe:series-ranked -->
