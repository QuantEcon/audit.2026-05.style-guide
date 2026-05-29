# lucas_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lucas_model.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Clean one-sentence paragraphs throughout; title in Title Case. |
| Math         | 8/10  | `\mathbb{E}` used; one `*` in a plot label is harmless. |
| Code         | 8/10  | Unicode Greek used (8 occurrences); no install cell (numpy/scipy only). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `figsize=`; 1 `{figure}` static image; no `:name:` fields. |
| References   | 8/10  | 1 `{cite}` used; never `{cite:t}`. |
| Links        | 6/10  | One raw `python.quantecon.org/markov_asset.html` URL (L36). |
| Admonitions  | 8/10  | 1 exercise and 1 solution with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — One raw `python.quantecon.org/markov_asset.html` URL. *Example:* `lectures/lucas_model.md:36`. *Count:* 1 occurrence.

### Low severity
- **[qe-math-012 (proposed)]** — `'$p*(y)$'` (L500) in a matplotlib label uses `*` next to `p` in a math context. *Count:* 1 occurrence.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-002]** — 1 static `{figure}` (`solution_mass_ex2.png`).

## Strengths
- `\mathbb{E}` and `\mathbb{E}_t` used for expectation throughout (qe-math-010, proposed), e.g. L106, L260.
- Sequences in curly brackets `\{y_t\}_{t=0}^{\infty}` (qe-math-005).
- "IID" used in text correctly (qe-writing-009, proposed) at L86, L385.
- Italic for emphasis (qe-writing-005), e.g. L58 *Pure exchange*, L122 *ex-dividend*.
- Equation labels via `:label:` and `{eq}` references (qe-math-007).
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- Exercise gated; solution has `:class: dropdown` (qe-admon-001, qe-admon-002).
- Unicode Greek used in code (qe-code-002).

## Recommended actions
1. Use `p^*` (or `p^{*}`) consistently rather than the literal `*` in plot label (qe-math-012, proposed).
2. Convert raw `python.quantecon.org` URL to `{doc}\`intermediate:markov_asset\`` (qe-link-002).
3. Add `:name: fig-...` fields (qe-fig-005).
