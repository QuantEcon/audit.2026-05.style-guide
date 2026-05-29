# Style Audit — knowing_forecasts_of_others

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/knowing_forecasts_of_others.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 5.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Title in Title Case; sentence-case headings; multi-sentence paragraphs; "i.i.d." in narrative. |
| Math         | 3/10  | Systemic `\begin{array}` for matrices; `\mathcal{N}` for Normal; bare `E_t`. |
| Code         | 6/10  | Spelled-Greek mixed with unicode; plotly import (binary package); install cells with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 3/10  | Plotly figures used (L919) without `{only} latex` directive (qe-fig-010, High). |
| References   | 7/10  | 30 `{cite}` used; many narrative author refs would benefit from `{cite:t}`. |
| Links        | 8/10  | No raw cross-series URLs; self-contained. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — `\begin{array}{...}` used systematically for matrices instead of `\begin{bmatrix}` (carry-forward from v1 M4). *Example:* `lectures/knowing_forecasts_of_others.md:828`, `:830`, `:832`, `:834`, `:836`. *Count:* 26 occurrences.
- **[qe-fig-010]** — Plotly figures used without `{only} latex` directive for PDF compatibility. *Example:* `lectures/knowing_forecasts_of_others.md:919`. *Count:* 2 plotly imports.
- **[qe-code-006]** — Plotly-orca is a binary package (`!conda install -y -c plotly plotly plotly-orca`); a binary-install warning admonition would be helpful.

### Medium severity
- **[qe-writing-A1]** — "i.i.d." used in text instead of "IID" (carry-forward from v1 W6). *Example:* `lectures/knowing_forecasts_of_others.md:163`, `:176`, `:479`, `:536`, `:1416`. *Count:* 7 occurrences.
- **[qe-math-A3]** — `\mathcal{N}` used as Normal distribution (carry-forward from v1 M9). *Count:* 3 occurrences.
- **[qe-math-A1]** — Bare `E_t` for expectation (carry-forward from v1 M7). *Count:* 3 occurrences.
- **[qe-ref-001]** — 7 narrative-style "in {cite}" patterns; some should be `{cite:t}`.

### Low severity
- **[qe-writing-005]** — Bold for keyword definitions used throughout.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- Sequences in curly brackets (qe-math-005).
- Heavy use of `{cite}` for references.
- Install cells at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert `\begin{array}` blocks to `\begin{bmatrix}` (qe-math-003).
2. Add `{only} latex` directive after each plotly figure (qe-fig-010).
3. Add binary-install warning admonition for `plotly-orca` (qe-code-006).
4. Replace "i.i.d." / "iid" with "IID" (qe-writing-A1).
5. Replace `\mathcal{N}` with `N` (qe-math-A3).
6. Replace bare `E_t` with `\mathbb{E}_t` (qe-math-A1).
