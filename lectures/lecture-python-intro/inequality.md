# Style Audit — inequality

- **Series:** lecture-python-intro
- **File:** `lectures/inequality.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 mostly sentence case; one H3 Title Case violation. |
| Math         | 8/10  | Clean equations; no transpose; sums used. |
| Code         | 8/10  | `!pip install wbgapi plotly` at top with `hide-output` (qe-code-003 OK); standard Anaconda imports otherwise. |
| JAX          | out of scope | — |
| Figures      | 7/10  | Plotly figure has `{only} latex` directive (qe-fig-010 OK); 1 `ax.set_title(title)` outside exercise (line 503); axis labels "Gini coefficient" (lines 561, 596, 637, 596) — Title-Case-style (Gini is a proper noun but elsewhere should be lowercase). |
| References   | 8/10  | 1 `{cite}` (parenthetical). |
| Links        | 9/10  | `{doc}` link present (1 occurrence). |
| Admonitions  | 9/10  | `{prf:definition}` × 4 (qe-admon-004 OK); solutions gated, dropdown, linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W3** — "### Gini Coefficient and GDP per capita (over time)" (line 714) uses Title Case where sentence case expected. *Count:* 1 H3.
- **[qe-fig-003]** — `ax.set_title(title)` on line 503 outside exercise context. *Count:* 1 occurrence.

### Low severity
- **W1** — Some short two-sentence paragraphs.
- **W7** — Proper nouns "Roman Republic", "Augustus" — acceptable.
- **[qe-fig-006]** — Axis labels "Gini coefficient (income)" etc. start with capitalised "Gini" (proper-noun-like — acceptable, but borderline).
- **[qe-fig-005]** — No matplotlib figures use `{figure}` directive with `:name:` (plotly figure has `(fig:plotly-gini-gdppc-years)=` label which serves the purpose).

## Strengths
- Section headings comply with W3 (proper nouns Lorenz/Gini retained).
- `prf:definition`, `prf:example` used (qe-admon-004 OK).
- Bold/italic used appropriately.
- Clean one-sentence paragraph style.
- Plotly figure correctly wrapped with `{only} latex` directive (qe-fig-010 OK).
- `!pip install wbgapi plotly` at top with `hide-output` (qe-code-003 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Change "Gini Coefficient and GDP per capita" → "Gini coefficient and GDP per capita".
2. Move `set_title(title)` (line 503) to figure metadata.
