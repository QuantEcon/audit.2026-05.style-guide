# Style Audit — money_inflation_nonlinear

- **Series:** lecture-python-intro
- **File:** `lectures/money_inflation_nonlinear.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | Most H2 section headings use Title Case (W3 violation). |
| Math         | 6/10  | No transpose; equations clean; minor stylistic issues only. |
| Code         | 8/10  | Unicode Greek (`α`, `π`) used throughout (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 7/10  | `figsize=` on line 348 only; no `ax.set_title` violations outside exercises; no figures use `{figure}` directive. |
| References   | 8/10  | 2 `{cite}` usages; parenthetical, no clear in-text mis-use. |
| Links        | 9/10  | `{doc}` cross-references used (11 occurrences). |
| Admonitions  | 9/10  | `{prf:example}` used (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
- **W3** — Section headings systematically use Title Case where sentence case is required. *Examples:* "## The Model" (48), "## Limiting Values of Inflation Rate" (78), "## Steady State Laffer curve" (162), "## Initial Price Levels" (206), "## Computing an Equilibrium Sequence" (278), "## Slippery Side of Laffer Curve Dynamics" (339). *Count:* 6+ headings.

### Medium severity
- **W1** — Multi-sentence paragraphs in Overview (lines 33–40, 42–46).

### Low severity
- **W7** — Inconsistent quoting style with double single-quotes (e.g. ''method 2'' line 27) instead of double quotes.
- **[qe-fig-001]** — `figsize=` on line 348. *Count:* 1 occurrence.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- H1 title is correct Title Case.
- Equation labelling and `{eq}` references are clean.
- Math notation consistent.
- Unicode Greek in code (qe-code-002 OK).
- `{doc}` cross-references used (qe-link-002 OK).
- `{prf:example}` directive (qe-admon-004 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert all section headings from Title Case to sentence case per qe-writing-006.
2. Split multi-sentence paragraphs.
3. Normalize quote style.
4. Remove `figsize=` on line 348.
