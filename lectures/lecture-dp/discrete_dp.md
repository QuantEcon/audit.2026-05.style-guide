# discrete_dp

- **Series:** lecture-dp
- **File:** `lectures/discrete_dp.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | All H2/H3 sentence case. |
| Math         | 8/10  | One `\mathbf{1}` (ones vector); otherwise clean. |
| Code         | 5/10  | Three `%timeit` magics; pip install at top; Unicode Greek; figsize 4×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 7/10  | Two static PNG figures; no embedded titles; figsize 4×; no Title-Case labels. |
| References   | 9/10  | Citations parenthetical via `{cite}`; no narrative-author misuse. |
| Links        | 3/10  | Ten raw markdown links to `python.quantecon.org` / `python-intro.quantecon.org`. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Ten raw markdown links to `python.quantecon.org` / `python-intro.quantecon.org` (e.g. `short_path.html`, `mccall_model.html`, `finite_markov.html`, `optgrowth.html`). *Lines:* 75, 76, 193, 209, 543, 616, 624. Should be `{doc}` intersphinx references.

### Medium severity
- **[qe-math-008]** — Ones vector written as `\mathbf{1}` (line 1001). Should be `\mathbb{1}` and explained.
- **[qe-code-005]** — Three `%timeit` magics used for benchmarking. *Lines:* 844, 845, 846. Style guide prefers `quantecon.timeit`.
- **[qe-fig-002]** — Two static PNG figures (`finite_dp_simple_og.png`, `finite_dp_simple_og2.png`). *Lines:* 552, 566. Prefer code-generated figures where possible.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 4 times.

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- All H2/H3 headings sentence case ("Overview", "How to read this lecture", "Code", "References", "Discrete DPs", "Policies", "Formal definition", "Value and optimality", "Two operators", "The Bellman equation and the principle of optimality", "Solving discrete DPs", "Value function iteration", "Policy function iteration", "Modified policy function iteration", "Example: A growth model").
- `\mathbb{E}` used throughout.
- Equation labels and `{eq}` references used cleanly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top.

## Recommended actions
1. Convert 10 raw cross-series markdown URLs to `{doc}` intersphinx references.
2. Replace `\mathbf{1}` with `\mathbb{1}` (line 1001) and introduce the notation.
3. Replace `%timeit` magics with `quantecon.timeit` context.
4. Consider switching key definitions to `**bold**` (currently italicised).
