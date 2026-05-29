# Style Audit — muth_kalman

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/muth_kalman.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.8 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; one-sentence paragraph norm followed in most places. |
| Math         | 6/10  | `\mathcal N` for normal distribution; bare `E[...]` for expectation. |
| Code         | 7/10  | No spelled Greek (zero); 2 quantecon imports; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 5/10  | 3 `ax.set_title` calls; no `figsize=`; no `:name:` fields. |
| References   | 7/10  | 4 `{cite}` used; "Muth (1960)" narrative ref should use `{cite:t}`. |
| Links        | 8/10  | 4 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title` used in 3 cells.

### Medium severity
- **[qe-math-A3]** — `\mathcal N` used as the Normal distribution (carry-forward from v1 M9). *Example:* `lectures/muth_kalman.md:116`. *Count:* 1 occurrence.
- **[qe-math-A1]** — Bare `E[...]` for expectation (carry-forward from v1 M7). *Example:* `lectures/muth_kalman.md:144`-`145`. *Count:* 2 occurrences.
- **[qe-ref-001]** — "Muth (1960) {cite}" narrative pattern should use `{cite:t}`. *Count:* ~3 occurrences.

### Low severity
- **[qe-writing-001]** — Occasional two-sentence paragraphs, e.g. L83-85.
- **[qe-writing-005]** — `**question**`/`**answer**` (L84-85) and `**moving average**` (L358) are emphasis, not definitions — should be italic.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Correct use of `\begin{bmatrix}` everywhere (qe-math-003).
- Sequences in curly brackets `\{y_t\}` (qe-math-005) — see L77, L315.
- "IID" used correctly (qe-writing-A1) on L104, L119.
- Title in Title Case; section headings in sentence case (qe-writing-006).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Remove `ax.set_title` calls (qe-fig-003).
2. Replace `\mathcal N` with `N` for the Normal distribution (qe-math-A3).
3. Replace bare `E[\cdot]` with `\mathbb{E}[\cdot]` (qe-math-A1).
4. Use italic, not bold, for non-definition emphasis (qe-writing-005).
5. Use `{cite:t}` for narrative refs (qe-ref-001).
