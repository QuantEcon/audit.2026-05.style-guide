# Style Audit — lu_tricks

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lu_tricks.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 4.5/10 | `\begin{matrix}` used instead of `\begin{bmatrix}`. |
| Code         | 7/10  | Mixed unicode/spelled Greek (8 vs 3); no install cell (numpy only). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 1 `figsize=`; no `:name:` fields. |
| References   | 7/10  | 5 `{cite}` used; 4 narrative refs would benefit from `{cite:t}`. |
| Links        | 8/10  | 2 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 7/10  | 4 gated exercises but no associated solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — `\begin{matrix}` used for matrices instead of `\begin{bmatrix}` (carry-forward from v1 M4). *Example:* `lectures/lu_tricks.md:295`, `:305`, `:311`, `:392`, `:403`. *Count:* 10 occurrences.

### Medium severity
- **[qe-ref-001]** — Multiple narrative author refs ("Whittle (1963)", "Sargent (1979)", etc.) should use `{cite:t}`. *Count:* ~4 occurrences.

### Low severity
- **[qe-writing-006]** — Title "Classical Control with Linear Algebra" uses lowercase "with" — but sister lecture `classical_filtering.md` uses "With". Pick one convention.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- "IID" used correctly in narrative (qe-writing-A1) at L30.
- Subheadings sentence case (qe-writing-006).
- One-sentence paragraph rule respected (qe-writing-001).
- Exercises gated (qe-admon-001).
- `{doc}` used for cross-series references (qe-link-002).

## Recommended actions
1. Convert `\begin{matrix}` blocks to `\begin{bmatrix}` (qe-math-003).
2. Reconcile capitalisation of "With/with" in titles with `classical_filtering.md` (qe-writing-006).
3. Use `{cite:t}` for narrative refs (qe-ref-001).
4. Add associated solutions for exercises (qe-admon-005).
