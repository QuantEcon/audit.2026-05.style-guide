# Style Audit — tax_smoothing_3

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_3.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Generally one-sentence paragraphs; title in Title Case; subheadings sentence case. |
| Math         | 5/10  | Bare `E_0`; `\cal N` for normal distribution. |
| Code         | 8/10  | Mostly unicode Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `figsize=`; no `ax.set_title`; no `:name:` fields. |
| References   | 8/10  | 4 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 4 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — Bare `E_0` for expectation (carry-forward from v1 M7). *Example:* `lectures/tax_smoothing_3.md:80`. *Count:* 1 occurrence.
- **[qe-math-A3]** — `\cal N` used as the Normal distribution (carry-forward from v1 M9). *Example:* `lectures/tax_smoothing_3.md:97`. *Count:* 1 occurrence.

### Low severity
- **[qe-writing-005]** — `**roll-over risk**` (L45) is a near-definition (OK); a few bolded labels (e.g. `**LQ**`) seem ornamental.
- **[qe-writing-001]** — A few multi-sentence paragraphs, e.g. L130-132.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Correct use of `\begin{bmatrix}` for the transition matrix Π (L181) (qe-math-003).
- Title "How to Pay for a War: Part 3" in Title Case (qe-writing-006).
- Sentence-case section headings (qe-writing-006).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `E_0` with `\mathbb{E}_0` (qe-math-A1).
2. Replace `{\cal N}` with `N` (qe-math-A3).
3. Add `:name: fig-...` fields (qe-fig-005).
