# Style Audit — lecture-python-programming

- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Lectures audited:** 26
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope for this series)*
- **Average overall score:** 8.0 / 10
- **Average per-category scores:** writing 7.2, math 7.3, code 8.5, figures 6.5, references — (none in scope), links 9.1, admonitions 8.7

## Priority distribution

| Priority | Count | %     |
|----------|-------|-------|
| HIGH     | 3     | 11.5% |
| MEDIUM   | 0     | 0%    |
| LOW      | 19    | 73.1% |
| NONE     | 4     | 15.4% |

The three HIGH-priority lectures all triggered the rule "any in-scope category ≤ 4" via the Figures category. Their *overall* scores are 7.0–7.5 (within the LOW band on its own), but a single-category floor of 4 (`matplotlib`, `pandas_panel`, `workspace`) raises priority.

## Top systemic issues across the series

1. **[qe-writing-006]** *(carry-forward W3 — Title Case in section headings)* — appears in **24 / 26** lectures and remains the dominant style violation across the series. Multiple files exhibit 10–18 instances each. Unchanged from v1.

2. **[qe-fig-005]** *(missing `name:` field on figure directives)* — appears in **~20 / 26** lectures. Every `{figure}` / `{image}` directive observed lacks a `name:` field, preventing `{numref}` cross-referencing. This is the single largest gap in the Figures category.

3. **[qe-fig-003]** *(embedded matplotlib titles via `ax.set_title` / `plt.title` / `plt.suptitle`)* — appears in **5 lectures** outside the exercise/solution exception: `pandas_panel.md` (×4), `workspace.md` (×2), `matplotlib.md` (×2 — but pedagogically motivated), `jax_intro.md` (×1). `matplotlib.md` and `workspace.md` use it in demo code; `pandas_panel.md` uses it in non-exercise body code (clear violation).

4. **[qe-fig-001]** *(unnecessary `figsize=` overrides)* — appears in **9 / 26** lectures: `matplotlib.md` (×4 — pedagogical), `numpy_vs_numba_vs_jax.md` (×1 — 3D plot), `jax_intro.md` (×1), `pandas.md` (×2 in solutions), `pandas_panel.md` (none — pandas_panel uses default size), `python_oop.md` (×1), `writing_good_code.md` (×2), `numpy.md` (×4 historical leftovers — actually re-checked, mostly in matplotlib code samples). Total occurrences ~15.

5. **[qe-link-002]** *(direct URLs to sibling lecture series instead of `{doc}` cross-references)* — appears in **3 lectures**: `about_py.md` (×1, jax), `numba.md` (×1, intro), `sympy.md` (×3, intro + intermediate).

## Top strengths

- **[qe-code-002]** *(Unicode Greek in code)* — universally adopted in math-heavy lectures (α, β, γ, δ, ϵ, μ, ν, ρ, σ, λ, θ, ξ, η, Δ all appear). Programming-series exemplar.
- **[qe-code-003]** *(non-Anaconda installs at top with `hide-output`)* — 100 % compliant across 10 lectures with `!pip install` cells (autodiff, jax_intro, numba, need_for_speed, numpy, oop_intro, pandas, pandas_panel, numpy_vs_numba_vs_jax, scipy).
- **[qe-code-004]** *(`qe.Timer` for benchmarking)* — used exemplarily across 6 lectures (numba 8+ blocks, numpy_vs_numba_vs_jax 17+ blocks, need_for_speed, jax_intro, scipy, numpy). No `time.time()` patterns and no `tic`/`toc` legacy code anywhere.
- **[qe-code-005]** *(no `%timeit` / `%%timeit`)* — 100 % compliant. Series consistently uses `qe.Timer` instead.
- **[qe-code-006]** *(binary-package warnings)* — N/A. No graphviz / similar binary packages used in this series.
- **[qe-admon-002]** *(`:class: dropdown` for solutions)* — 100 % compliant across all 17 lectures with solutions. Every `solution-start` directive observed in the audit corpus carries `:class: dropdown`.
- **[qe-admon-005]** *(solutions cross-reference exercises via `:label:`)* — 100 % compliant. Every `solution-start <label>` matches a corresponding `exercise-start :label: <label>`.
- **[qe-link-002]** *(intra-series `{doc}` cross-references)* — used cleanly in ~13 lectures (autodiff, functions, jax_intro, numba, oop_intro, pandas_panel, python_advanced_features, python_by_example, python_oop, numpy, numpy_vs_numba_vs_jax, troubleshooting, writing_good_code).
- **References category** — no `{cite}` used anywhere in the series, so qe-ref-001 is N/A across all 26 lectures. The series does not draw on bibliographic citations.

## Lectures ranked by priority (lowest score first)

| #  | Lecture | Writing | Math | Code | Fig | Ref | Link | Adm | Overall | Priority |
|----|---------|---------|------|------|-----|-----|------|-----|---------|----------|
| 1  | [matplotlib](matplotlib.md)               | 7    | N/A  | 7   | 4   | N/A | 9    | 8   | 7.0     | HIGH     |
| 2  | [workspace](workspace.md)                 | 8    | N/A  | 7   | 4   | N/A | 9    | 9   | 7.4     | HIGH     |
| 3  | [pandas_panel](pandas_panel.md)           | 7.5  | N/A  | 8   | 3   | N/A | 10   | 9   | 7.5     | HIGH     |
| 4  | [about_py](about_py.md)                   | 7.5  | N/A  | 8   | 6   | N/A | 7    | 9   | 7.5     | LOW      |
| 5  | [names](names.md)                         | 6.5  | N/A  | 9   | 6   | N/A | 9    | N/A | 7.6     | LOW      |
| 6  | [sympy](sympy.md)                         | 7    | 6    | 8   | N/A | N/A | 7    | 8   | 7.2     | LOW      |
| 7  | [getting_started](getting_started.md)     | 6.5  | N/A  | 8   | 7   | N/A | 9    | 8   | 7.7     | LOW      |
| 8  | [numpy](numpy.md)                         | 6.5  | 7.5  | 8   | 7   | N/A | 9    | 8   | 7.7     | LOW      |
| 9  | [numba](numba.md)                         | 7    | 8    | 9   | 8   | N/A | 7    | 8   | 7.8     | LOW      |
| 10 | [pandas](pandas.md)                       | 7    | N/A  | 8   | 7   | N/A | 8    | 9   | 7.8     | LOW      |
| 11 | [writing_good_code](writing_good_code.md) | 7    | 7.5  | 9   | 5   | N/A | 10   | 9   | 7.9     | LOW      |
| 12 | [python_oop](python_oop.md)               | 7    | 6    | 9   | 7   | N/A | 10   | 9   | 8.0     | LOW      |
| 13 | [scipy](scipy.md)                         | 6.5  | 7.5  | 9   | 8   | N/A | 9    | 8   | 8.0     | LOW      |
| 14 | [debugging](debugging.md)                 | 6.5  | N/A  | 8   | 9   | N/A | 9    | 8   | 8.1     | LOW      |
| 15 | [functions](functions.md)                 | 6.5  | N/A  | 8   | N/A | N/A | 9    | 9   | 8.1     | LOW      |
| 16 | [need_for_speed](need_for_speed.md)       | 7.5  | N/A  | 9   | 6   | N/A | 9    | 9   | 8.1     | LOW      |
| 17 | [python_by_example](python_by_example.md) | 6.5  | 7    | 9   | 7   | N/A | 10   | 9   | 8.1     | LOW      |
| 18 | [troubleshooting](troubleshooting.md)     | 7.5  | N/A  | N/A | 8   | N/A | 9    | N/A | 8.2     | LOW      |
| 19 | [numpy_vs_numba_vs_jax](numpy_vs_numba_vs_jax.md) | 7    | 8    | 9   | 7   | N/A | 10   | 9   | 8.3     | LOW      |
| 20 | [jax_intro](jax_intro.md)                 | 7    | N/A  | 9   | 7   | N/A | 10   | 9   | 8.4     | LOW      |
| 21 | [python_essentials](python_essentials.md) | 6.5  | N/A  | 9   | N/A | N/A | 9    | 9   | 8.4     | LOW      |
| 22 | [oop_intro](oop_intro.md)                 | 7    | N/A  | 8   | N/A | N/A | 10   | 9   | 8.5     | LOW      |
| 23 | [autodiff](autodiff.md)                   | 8    | 8    | 9   | 8   | N/A | 10   | 9   | 8.7     | NONE     |
| 24 | [status](status.md)                       | 8.5  | N/A  | 9   | N/A | N/A | N/A  | N/A | 8.8     | NONE     |
| 25 | [python_advanced_features](python_advanced_features.md) | 8    | N/A  | 9   | N/A | N/A | 10   | 9   | 9.0     | NONE     |
| 26 | [intro](intro.md)                         | 9    | N/A  | N/A | N/A | N/A | 10   | N/A | 9.5     | NONE     |

## Series-level recommendations

1. **Heading sweep remains the highest-leverage action.** Carried over from v1: a global pass converting all H2/H3/H4 section headings from Title Case to sentence case (qe-writing-006). This alone would lift most of the LOW-priority lectures into NONE.

2. **Figure metadata pass.** Add `name:` fields (e.g., `fig-jp-demo`, `fig-htop-parallel-npmat`, `fig-pandas-vs-rest`) to the ~50+ `{figure}` and `{image}` directives across the series so they become `{numref}`-able (qe-fig-005). This is mechanical and high-impact.

3. **Remove non-pedagogical `plt.title` / `ax.set_title`.** In `pandas_panel.md` four such calls appear in main-body code cells and should be replaced with figure-directive captions (qe-fig-003). Workspace.md needs its `sine_wave.py` demo cleaned up similarly. `matplotlib.md` and `jax_intro.md` are borderline (one is a Matplotlib tutorial, the other diagrams a PRNG tree) and may warrant an explicit "this is a demonstration, don't do this in production" callout.

4. **Cross-series link conversion.** Replace the ~5 bare quantecon.org URLs in `about_py.md`, `numba.md`, and `sympy.md` with `{doc}` cross-references using the appropriate intersphinx prefix (`jax:`, `intro:`, `intermediate:`) per qe-link-002.

5. **Normalize blackboard probability notation.** Carried over: `\mathbb E` → `\mathbb{E}`, `\mathbb P` → `\mathbb{P}` in `numba.md`, `numpy.md`, `scipy.md`, `writing_good_code.md` (qe-math-A1). Also: `python_oop.md` should switch `\mathbf{1}` → `\mathbb{1}`; `python_by_example.md` should replace `\pi * r^2` with `\pi r^2` (qe-math-A5); `sympy.md` narrative should switch `E(X)` to `\mathbb{E}[X]` (the SymPy code `E(X)` may remain since it is a SymPy function name).

6. **Gated-exercise consistency.** Several lectures mix bare `{exercise}` with `{exercise-start}` / `{exercise-end}`. Where the body contains only prose/math, bare `{exercise}` is technically allowed by qe-admon-001, but uniform gated syntax improves authoring consistency. Affected: `numba.md`, `numpy.md`, `python_essentials.md`, `scipy.md`, `sympy.md`.

7. **Preserve the strong Code-category baseline.** The series already does extremely well on `qe-code-002` (Greek unicode), `qe-code-003` (top-of-lecture installs with `hide-output`), `qe-code-004` (`qe.Timer`), and `qe-code-005` (no `%timeit`). Future contributions should keep this discipline.
