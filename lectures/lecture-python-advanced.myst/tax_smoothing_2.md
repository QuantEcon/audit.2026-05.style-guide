# Style Audit — tax_smoothing_2

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_2.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; subheadings sentence case; mostly one-sentence paragraphs. |
| Math         | 5/10  | Bare `E_0`; `{\cal N}`; `\textrm{...}` mixed into a `\sim` definition. |
| Code         | 7/10  | Spelled Greek (3); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 1 `ax.set_title`; 3 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 6 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 4 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — Bare `E_0` for expectation (carry-forward from v1 M7). *Example:* `lectures/tax_smoothing_2.md:122`. *Count:* ~3 occurrences.
- **[qe-math-A3]** — `{\cal N}` used as Normal distribution (carry-forward from v1 M9). *Example:* `lectures/tax_smoothing_2.md:142`. *Count:* 1 occurrence.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.

### Low severity
- **[qe-writing-001]** — A few longer paragraphs and bulleted lists with embedded narrative.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Spelled Greek in code parameters.

## Strengths
- `\begin{bmatrix}` used throughout (qe-math-003).
- `aligned` (not `align`) inside `$$` (qe-math-006) — e.g. L128.
- Title in Title Case (qe-writing-006).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `E_0` with `\mathbb{E}_0` (qe-math-A1).
2. Replace `{\cal N}` with `N` (qe-math-A3).
3. Remove `ax.set_title` (qe-fig-003).
4. Add `:name: fig-...` fields (qe-fig-005).
