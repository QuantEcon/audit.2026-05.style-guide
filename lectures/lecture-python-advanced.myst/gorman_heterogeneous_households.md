# Style Audit — gorman_heterogeneous_households

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/gorman_heterogeneous_households.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title in Title Case (trailing space); one H2 violates sentence case; "i.i.d." in narrative. |
| Math         | 7/10  | `\mathbb{E}` used; `\begin{bmatrix}` used; no transpose `^T` for matrices. |
| Code         | 7/10  | Mixed unicode/spelled Greek (9 spelled vs 13 unicode); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | Modern lecture with mystnb captions and `name:` fields; 5 `figsize=`. |
| References   | 9/10  | 14 `{cite}` and 14 `{cite:t}` used appropriately. |
| Links        | 9/10  | 1 `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — H2 "Dynamic, Stochastic Economy" (L308) uses Title Case for "Stochastic" — should be sentence case ("Dynamic, stochastic economy"). *Count:* 1 occurrence.
- **[qe-writing-A1]** — "i.i.d." used in text instead of "IID" (carry-forward from v1 W6). *Example:* `lectures/gorman_heterogeneous_households.md:326`, `:1329`, `:1510`, `:1525`, `:1555`. *Count:* 5 occurrences.

### Low severity
- **[qe-writing-006]** — Title "Gorman Aggregation " has a trailing space (L26).
- **[qe-writing-001]** — Several longer paragraphs in the dense expository sections (e.g. L72, L78-80).
- Three `^T` occurrences (L1050, L1056, L1059) are time horizons, not transpose — no qe-math-002 violation.
- **[qe-fig-001]** — 5 `figsize=` settings.

## Strengths
- `\mathbb{E}` used (qe-math-A1).
- `\begin{bmatrix}` used (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- Subheadings (other than the one flagged) in sentence case (qe-writing-006).
- Modern figure styling with mystnb captions, `name:` and `:label:` (qe-fig-005).
- Heavy correct `{cite:t}` use (qe-ref-001).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Rename "Dynamic, Stochastic Economy" to "Dynamic, stochastic economy" (qe-writing-006).
2. Replace "i.i.d." with "IID" in narrative (qe-writing-A1).
3. Trim trailing space in the title (qe-writing-006).
4. Convert spelled Greek to unicode in code (qe-code-002).
