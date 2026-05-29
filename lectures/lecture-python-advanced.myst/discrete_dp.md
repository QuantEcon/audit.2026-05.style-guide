# discrete_dp

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/discrete_dp.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.0 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 7.5/10 | One `\mathbf{1}` for ones vector instead of `\mathbb{1}`. |
| Code         | 5/10  | 3 `%timeit`/`%%timeit` cells (qe-code-005); 14 spelled Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 4 `figsize=`; 2 `{figure}` static images; no `:name:` fields. |
| References   | 8/10  | 7 `{cite}` used; never `{cite:t}`. |
| Links        | 4/10  | 5 raw cross-series URLs (anaconda, python-programming, python.quantecon.org); no `{doc}`. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Raw cross-series URLs to `python.quantecon.org/finite_markov.html`, `python-programming.quantecon.org/getting_started.html`, etc. *Example:* `lectures/discrete_dp.md:90`, `:193`, `:209`, `:715`, `:911`. *Count:* 5 occurrences.
- **[qe-code-005]** — 3 `%timeit` magic invocations instead of `qe.timeit`. *Count:* 3 occurrences.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, etc.) heavily used in code (14 occurrences).

### Low severity
- **[qe-math-008]** — `\mathbf{1}` used for ones vector. *Example:* `lectures/discrete_dp.md:1001`. *Count:* 1 occurrence.
- **[qe-writing-001]** — A few longer compound paragraphs in algorithm descriptions.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 4 `figsize=` settings.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\mathbb{E}` used for expectation (qe-math-010, proposed).
- Equation labels and `{eq}` references (qe-math-007).
- Primes in `s'`, `Q_{\sigma}(s, s')` are next-period notation, not transpose.
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert raw cross-series URLs to `{doc}\`intermediate:finite_markov\``, `{doc}\`programming:getting_started\`` etc. (qe-link-002).
2. Replace `%timeit` magic with `qe.timeit(...)` (qe-code-005).
3. Replace `\mathbf{1}` with `\mathbb{1}` and explain (qe-math-008).
4. Convert spelled Greek to unicode in code (qe-code-002).
