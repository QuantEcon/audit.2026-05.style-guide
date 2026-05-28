# Style Audit — lecture-python-programming

- **Audit date:** 2026-05-27
- **Lectures audited:** 26
- **Average overall score:** 7.2 / 10
- **Average writing score:** 7.2 / 10
- **Average math score:** 7.3 / 10 (over 9 files containing math)

## Priority distribution

| Priority | Count | %    |
|----------|-------|------|
| HIGH     | 0     | 0%   |
| MEDIUM   | 15    | 57.7%|
| LOW      | 10    | 38.5%|
| NONE     | 1     | 3.8% |

## Top systemic issues across the series

1. **W3** — Section/subsection headings use Title Case instead of sentence case. Appears in **24 / 26** lectures and is the dominant style violation across the series. Multiple files exhibit 10–18 instances each.
2. **W1** — Occasional multi-sentence paragraphs in installation/expository prose. Affects roughly **8 / 26** lectures at the low-severity level.
3. **M7** — Inconsistent probability/expectation notation: `\mathbb E` written without braces, and one bare `E(X)` in display math. Affects **5 / 26** math-bearing lectures (numba, scipy, numpy, sympy, writing_good_code).

Additional minor systemic items:
- **M3 / M5** — One lecture (`python_oop.md`) uses `\mathbf{1}` for the indicator function instead of `\mathbb{1}`.
- **M11** — One lecture (`python_by_example.md`) uses `*` for multiplication inside `$...$`.

## Lectures ranked by priority (lowest score first)

| # | Lecture | Writing | Math | Overall | Priority |
|---|---------|---------|------|---------|----------|
| 1 | debugging | 6.5 | N/A | 6.5 | MEDIUM |
| 2 | functions | 6.5 | N/A | 6.5 | MEDIUM |
| 3 | getting_started | 6.5 | N/A | 6.5 | MEDIUM |
| 4 | names | 6.5 | N/A | 6.5 | MEDIUM |
| 5 | python_by_example | 6.5 | 7 | 6.5 | MEDIUM |
| 6 | python_essentials | 6.5 | N/A | 6.5 | MEDIUM |
| 7 | python_oop | 7 | 6 | 6.5 | MEDIUM |
| 8 | sympy | 7 | 6 | 6.5 | MEDIUM |
| 9 | jax_intro | 7 | N/A | 7.0 | MEDIUM |
| 10 | matplotlib | 7 | N/A | 7.0 | MEDIUM |
| 11 | numpy | 6.5 | 7.5 | 7.0 | MEDIUM |
| 12 | oop_intro | 7 | N/A | 7.0 | MEDIUM |
| 13 | pandas | 7 | N/A | 7.0 | MEDIUM |
| 14 | scipy | 6.5 | 7.5 | 7.0 | MEDIUM |
| 15 | writing_good_code | 7 | 7.5 | 7.0 | MEDIUM |
| 16 | troubleshooting | 7.5 | N/A | 7.5 | LOW |
| 17 | about_py | 7.5 | N/A | 7.5 | LOW |
| 18 | need_for_speed | 7.5 | N/A | 7.5 | LOW |
| 19 | numba | 7 | 8 | 7.5 | LOW |
| 20 | numpy_vs_numba_vs_jax | 7 | 8 | 7.5 | LOW |
| 21 | pandas_panel | 7.5 | N/A | 7.5 | LOW |
| 22 | autodiff | 8 | 8 | 8.0 | LOW |
| 23 | python_advanced_features | 8 | N/A | 8.0 | LOW |
| 24 | workspace | 8 | N/A | 8.0 | LOW |
| 25 | status | 8.5 | N/A | 8.5 | LOW |
| 26 | intro | 9 | N/A | 9.0 | NONE |

## Series-level recommendations

1. **Series-wide heading sweep.** The single highest-impact action is a global pass converting all H2/H3/H4 section headings from Title Case to sentence case (W3). This alone would lift most of the MEDIUM-priority lectures to LOW or NONE.
2. **Normalize `\mathbb{P}`, `\mathbb{E}`, `\mathbb{V}` with braces.** Several math-bearing lectures use bare `\mathbb E` or `\mathbb P`; standardize to `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}` for consistency.
3. **Fix isolated math violations.** `python_oop.md` should switch `\mathbf{1}` → `\mathbb{1}` (and remove the bold), and add an explanation per the style guide; `python_by_example.md` should replace `\pi * r^2` with juxtaposition or `\cdot`; `sympy.md` should change `E(X)` → `\mathbb{E}[X]` in the Poisson expectation example.
4. **Lecture titles are already correct.** The W2 rule (Title Case lecture title) is universally followed — no action needed there.
5. **Math-rule strengths to preserve.** Across all lectures the series correctly uses `\{...\}` for sequences, `\top` is not needed (no transposes), and no `align` inside `$$`, no `\tag`, and no bold vectors apart from the single `\mathbf{1}` case. These conventions are already in good shape.
