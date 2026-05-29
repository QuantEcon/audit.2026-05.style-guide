# Style Audit — matsuyama

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/matsuyama.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; clean one-sentence paragraphs. |
| Math         | 9/10  | Clean — no transpose, no `array`, no `\mathcal N`. |
| Code         | 7/10  | Unicode Greek heavily used (17 occurrences); no install cell (uses numba — in Anaconda). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 1 `ax.set_title`; 3 `figsize=`; 2 `{figure}` static images; no `:name:` fields. |
| References   | 8/10  | 1 `{cite}` used; never `{cite:t}`. |
| Links        | 6/10  | One raw `python-programming.quantecon.org/numba.html` URL (L336). |
| Admonitions  | 8/10  | 1 gated exercise and 1 solution with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — Raw `python-programming.quantecon.org/numba.html` URL. *Example:* `lectures/matsuyama.md:336`. *Count:* 1 occurrence.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.
- **[qe-fig-002]** — 2 `{figure}` directives reference static PNGs.

### Low severity
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- All subheadings sentence case (qe-writing-006).
- One-sentence paragraph rule rigorously respected (qe-writing-001).
- No qe-math-* violations detected.
- Exercise gated; solution has `:class: dropdown` (qe-admon-001, qe-admon-002).
- Heavy unicode Greek in code (qe-code-002).

## Recommended actions
1. Convert raw URL to `{doc}\`programming:numba\`` (qe-link-002).
2. Remove `ax.set_title` (qe-fig-003).
3. Code-generate the schematic figures (qe-fig-002).
4. Add `:name: fig-...` fields (qe-fig-005).
