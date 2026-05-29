# Style Audit — amss3

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/amss3.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Sentence-case headings; one-sentence paragraphs. |
| Math         | 6.5/10 | A few bare `E_t` mixed with `\mathbb E_t`. |
| Code         | 7/10  | Spelled Greek (`alpha`, `beta`); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 3 `{figure}` directives reference static PNGs; 2 `figsize=`; no `:name:` fields. |
| References   | 7/10  | 21 `{cite}`; a couple of narrative refs would benefit from `{cite:t}`. |
| Links        | 8/10  | Heavy `{doc}` use (12 occurrences); no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — A handful of bare `E_t` / `E(` instead of `\mathbb{E}_t` (carry-forward from v1 M7). *Example:* `lectures/amss3.md:294`, `:349`, `:361`, `:516`. *Count:* 4 occurrences.

### Low severity
- **[qe-fig-002]** — 3 `{figure}` directives reference static PNGs which could be code-generated.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Spelled-out Greek in code parameters.

## Strengths
- Title in Title Case (qe-writing-006); sentence-case headings (qe-writing-006).
- `\begin{bmatrix}` used consistently (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- Heavy `{doc}` cross-series linking (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Standardise on `\mathbb{E}_t` throughout (qe-math-A1).
2. Add `:name: fig-...` fields to figures (qe-fig-005).
3. Use unicode Greek in code (qe-code-002).
