# Style Audit — rosen_schooling_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/rosen_schooling_model.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Clean sentence-case subheadings; mostly one-sentence paragraphs. |
| Math         | 7.5/10 | Mostly clean; "k+1 x 1" dimensions written in prose without math. |
| Code         | 8/10  | Unicode Greek used (6 occurrences, no spelled); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 4 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 1 `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-math-001]** — Plain-text "k+1 x 1 matrix" and "k_1 x k+1 matrix" (L110-111) mix narrative with bare LaTeX symbols (carry-forward from v1 W7); should be rendered inside `$...$`.
- **[qe-writing-006]** — Sub-subheadings such as "### Preferences", "### Technology", "### Information" — fine; no violation.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- `\begin{bmatrix}` used consistently (qe-math-003).
- `\mathbb{E}` used for expectation (qe-math-A1) at L75.
- Title in Title Case (qe-writing-006); sentence-case headings (qe-writing-006).
- One-sentence paragraph rule largely respected (qe-writing-001).
- Unicode Greek used in code (qe-code-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Wrap dimensional expressions like "k+1 x 1" in math mode: `$(k+1) \times 1$` (qe-math-001).
2. Add `:name: fig-...` fields (qe-fig-005).
