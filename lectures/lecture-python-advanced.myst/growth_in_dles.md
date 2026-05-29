# Style Audit — growth_in_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/growth_in_dles.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; one-sentence paragraphs. |
| Math         | 4/10  | Systemic `\begin{array}` blocks instead of `\begin{bmatrix}`. |
| Code         | 7/10  | Spelled Greek only (3); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | No `ax.set_title`; no `figsize=`; no `:name:` fields. |
| References   | 7/10  | 2 `{cite}` used; "Hansen & Sargent (2013) {cite}", "Hall (1978)", "Jones-Manuelli (1990)" narrative refs should use `{cite:t}`. |
| Links        | 8/10  | 1 `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — `\left[ \begin{array}{...} ... \end{array} \right]` used throughout for matrices instead of `\begin{bmatrix}` (carry-forward from v1 M4). *Example:* `lectures/growth_in_dles.md:172`, `:231`, `:241`, `:246`, `:255`. *Count:* 8 occurrences.

### Medium severity
- **[qe-ref-001]** — Narrative author refs ("Hansen & Sargent (2013)", "Hall (1978)", "Jones-Manuelli (1990)") should use `{cite:t}` (carry-forward from v1 implication). *Count:* 3 occurrences.

### Low severity
- **[qe-writing-005]** — Bold labels for `**Preferences**`, `**Technology**`, `**Information**` sections (not strictly definitions).
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- `\mathbb{E}` used for expectation (qe-math-A1).
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- One-sentence paragraph rule respected (qe-writing-001).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert `\begin{array}` blocks to `\begin{bmatrix}` (qe-math-003).
2. Use `{cite:t}` for narrative author refs (qe-ref-001).
3. Reduce decorative bolding (qe-writing-005).
