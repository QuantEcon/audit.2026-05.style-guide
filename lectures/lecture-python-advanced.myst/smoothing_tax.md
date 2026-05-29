# Style Audit — smoothing_tax

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/smoothing_tax.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 5/10  | Primes used as transpose; bare `E_t`; `^T` for transpose. |
| Code         | 7/10  | Mixed unicode/spelled Greek (4 vs 8); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 1 `ax.set_title`; 2 `figsize=`; no `:name:` fields. |
| References   | 7/10  | 10 `{cite}` used; never `{cite:t}` despite some narrative refs. |
| Links        | 8/10  | 10 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 7/10  | 1 gated exercise but no associated solution. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-002]** — Prime `'` used as transpose. *Example:* `\sum_{j'=1}^N Q_{ij'} b(j')`; plus `^T` transpose at one location. *Count:* ~7 occurrences (mixed primes; some next-period).
- **[qe-math-010 (proposed)]** — Bare `E_t` for expectation. *Count:* 5 occurrences.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.

### Low severity
- **[qe-writing-005]** — `**complete markets**`, `**incomplete markets**` bold borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003).
- One-sentence paragraph rule respected (qe-writing-001).
- Heavy `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace bare `E_t` with `\mathbb{E}_t` (qe-math-010, proposed).
2. Replace primes / `^T` used as transpose with `^\top` (qe-math-002).
3. Remove `ax.set_title` (qe-fig-003).
4. Add `:name: fig-...` fields (qe-fig-005).
