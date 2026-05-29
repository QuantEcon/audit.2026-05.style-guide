# Style Audit — geom_series

- **Series:** lecture-python-intro
- **File:** `lectures/geom_series.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | H1 OK; multiple H2 sections use Title Case (W3). |
| Math         | 7/10  | `aligned` and `split` used; equation labels; no transpose. |
| Code         | 7/10  | Standard Anaconda imports; `alpha=` matplotlib kwargs only (not user variables). |
| JAX          | out of scope | — |
| Figures      | 4/10  | `figsize=` on lines 51, 932, 994, 1113; 7 `ax.set_title` calls inside solution blocks (OK), 1 outside (line 948: "An Increase in {param} on Output" — Title Case in title); 5+ axis labels with uppercase first letter ("Present Value, $p_0$", "Cumulative deposits", "Percentage error (%)"). |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK); 1 `{prf:example}`. |

## Issues

### Critical
_None found._

### High severity
- **W3** — Multiple H2 sections in Title Case. *Examples:* "## Example: The Money Multiplier in Fractional Reserve Banking" (line 118), "## Example: The Keynesian Multiplier" (~280), "## Example: Interest Rates and Present Values" (~438). *Count:* 3+ section headings.
- **[qe-fig-001]** — `figsize=` overrides on lines 51, 932, 994, 1113. *Count:* 4 occurrences.
- **[qe-fig-006]** — Axis labels with uppercase first letter outside acronyms. *Examples:* "Present Value, $p_0$" (lines 709, 736, 758), "Number of banks $N$", "Marginal propensity to consume $b$", "Cumulative deposits", "Percentage error (%)". *Count:* 5+ occurrences.

### Medium severity
- **W1** — Several multi-sentence paragraphs throughout.
- **M12** — `\begin{aligned} \begin{split}...\end{split}\end{aligned}` (line 616) — using `split` inside `aligned` is unusual; should be just `aligned`.
- **[qe-fig-003]** — `ax.set_title(f'An Increase in {param} on Output')` (line 948) — Title Case title outside exercise context.

### Low severity
- **W7** — Mid-sentence capitalization inconsistencies.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- H1 Title Case OK.
- `{math}` labels and `{eq}` refs used.
- Bold for definitions (**multiplier**, **money multiplier**, etc.).
- Solutions gated, dropdown, linked.

## Recommended actions
1. Convert "## Example: The Money Multiplier..." headings to sentence case.
2. Simplify the nested `aligned`/`split` math environment.
3. Remove `figsize=` overrides.
4. Lowercase axis labels.
5. Move the `set_title` on line 948 into mystnb metadata.
6. Split multi-sentence paragraphs.
