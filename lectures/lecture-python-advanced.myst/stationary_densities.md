# stationary_densities

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/stationary_densities.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; clean one-sentence paragraphs. |
| Math         | 8/10  | `\mathbf 1` for indicator; otherwise compliant. |
| Code         | 7/10  | Mixed spelled/unicode Greek (7 vs 10); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 1 `ax.set_title`; 4 `figsize=`; 1 `{figure}` static image; no `:name:` fields. |
| References   | 8/10  | 5 `{cite}` used; never `{cite:t}`. |
| Links        | 4/10  | 6 raw `python.quantecon.org/finite_markov.html` URLs (qe-link-002). |
| Admonitions  | 8/10  | 3 gated exercises and 3 solutions with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — 6 raw `python.quantecon.org/finite_markov.html` and `python-programming.quantecon.org/python_oop.html` URLs. *Example:* `lectures/stationary_densities.md:281`, `:290`, `:331`, `:445`, `:514`. *Count:* 6 occurrences.

### Medium severity
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.

### Low severity
- **[qe-math-008]** — `\mathbf 1` used for indicator. *Example:* `lectures/stationary_densities.md:551`. *Count:* 2 occurrences.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- Distribution names use plain letters: `\sim N(0,1)`, `\sim LN(0,1)` (qe-math-011, proposed) at L813, L941.
- One-sentence paragraph rule rigorously respected (qe-writing-001).
- Exercises gated; solutions use `:class: dropdown` (qe-admon-001, qe-admon-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `\mathbf 1` with `\mathbb{1}` (qe-math-008).
2. Convert raw cross-series URLs to `{doc}\`intermediate:finite_markov\``, `{doc}\`programming:python_oop\`` (qe-link-002).
3. Remove `ax.set_title` (qe-fig-003).
4. Add `:name: fig-...` fields (qe-fig-005).
