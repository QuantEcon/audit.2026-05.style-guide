# Style Audit — classical_filtering

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/classical_filtering.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 5.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title case for title; sentence-case headings; some long paragraphs. |
| Math         | 2/10  | Systemic `^\prime` for transpose; `\begin{matrix}` blocks; `^T` used for transpose too. |
| Code         | N/A   | no executable code cells |
| JAX          | N/A   | not a JAX lecture |
| Figures      | N/A   | no figures |
| References   | 7/10  | 9 `{cite}`; three narrative refs would benefit from `{cite:t}` (e.g. "Anderson and Moore (1979)"). |
| Links        | 8/10  | 4 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 7/10  | 2 gated exercises but no solutions (lecture says "this lecture has no solutions"). |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — `^\prime` used as transpose throughout (carry-forward from v1 M2). *Example:* `lectures/classical_filtering.md:77`, `:113`, `:119`, `:129`, `:408`, `:429`, `:430`, `:990`; also `L^T` at L476. *Count:* ~15 occurrences.
- **[qe-math-003]** — `\begin{matrix}` used instead of `\begin{bmatrix}` (carry-forward from v1 M4). *Example:* `lectures/classical_filtering.md:371`, `:444`, `:461`, `:484`, `:491`. *Count:* 5 occurrences.

### Medium severity
- **[qe-writing-006]** — Title "Classical Prediction and Filtering With Linear Algebra" uses capitalised "With" — inconsistent with sister lecture `lu_tricks` "Classical Control with Linear Algebra".
- **[qe-ref-001]** — Three narrative author references could use `{cite:t}`.

### Low severity
- **[qe-writing-001]** — Some longer paragraphs.

## Strengths
- `\mathbb{E}` used for expectation (qe-math-A1).
- Equation labels and `{eq}` references (qe-math-007).
- Subheadings in sentence case (qe-writing-006).
- Exercises gated (qe-admon-001).
- `{doc}` used for cross-series references (qe-link-002).

## Recommended actions
1. Replace `^\prime` and `^T` with `^\top` throughout (qe-math-002).
2. Convert `\begin{matrix}` blocks to `\begin{bmatrix}` (qe-math-003).
3. Reconcile capitalisation of "with" in title (qe-writing-006).
4. Convert "Author (Year)" narrative references to `{cite:t}` (qe-ref-001).
