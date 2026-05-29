# tax_smooth

- **Series:** lecture-python-intro
- **File:** `lectures/tax_smooth.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | H1 OK; most H2/H3 sentence case; "### Feasible Tax Variations" (line 482) Title Case. |
| Math         | 8/10  | bmatrix; sequences `\{G_t\}_{t=0}^S` (M6 OK); equation labels and refs. |
| Code         | 9/10  | Unicode Greek (`β`, `R`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 319, 373, 746; 3 `ax.set_title(...)` inside solution blocks (OK by exception); one axis label "Optimal flat tax $T_0$" (line 859) starts with uppercase. |
| References   | 7/10  | 2 `{cite}` usages; 1 is in-text ("called the ... in {cite}\`Barro1979\`") — should be `{cite:t}`. |
| Links        | 9/10  | `{doc}` cross-references used (5 occurrences). |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W3** — "### Feasible Tax Variations" (line 482) uses Title Case; should be sentence case.
- **[qe-fig-001]** — `figsize=` overrides on lines 319, 373, 746. *Count:* 3 occurrences.
- **[qe-ref-001]** — In-text citation should use `{cite:t}`. *Example:* `lectures/tax_smooth.md:123` ("called the 'present value of revenue-raising costs' in {cite}\`Barro1979\`"). *Count:* 1 occurrence.

### Low severity
- **W1** — Some short two-sentence paragraphs.
- **W7** — Mid-sentence Title Case in "Barro tax-smoothing model" — debatable proper-noun usage.
- **[qe-fig-006]** — Axis label "Optimal flat tax $T_0$" (line 859) starts with uppercase.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- bmatrix throughout (M4 OK).
- Sequences use `\{G_t\}_{t=0}^S` (M6 OK).
- Equation labels via `{math}` `:label:` form (M14 OK).
- Bold for definitions (**boundary conditions**, **terminal condition**, **smoother**).
- IID not relevant.
- Unicode Greek in code.
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert "### Feasible Tax Variations" → "### Feasible tax variations".
2. Convert in-text `{cite}` on line 123 to `{cite:t}`.
3. Remove `figsize=` overrides.
4. Lowercase axis label "Optimal flat tax".
