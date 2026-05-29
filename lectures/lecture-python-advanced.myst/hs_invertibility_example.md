# hs_invertibility_example

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hs_invertibility_example.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.5 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 4/10  | All matrices use `\begin{array}` instead of `\begin{bmatrix}`. |
| Code         | 8/10  | Unicode Greek used; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 3 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 5 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 2 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — Systemic use of `\left[ \begin{array}{...} ... \end{array} \right]` instead of `\begin{bmatrix}`. *Example:* `lectures/hs_invertibility_example.md:109`-`120`, `:123`-`128`, `:131`-`136`, `:202`-`209`, `:224`-`231`. *Count:* ~7 occurrences.

### Medium severity
- **[qe-writing-005]** — `**news and noise**`, `**shock-invertibility**`, `**fiscal foresight**` (L51-65) used as semi-definitions; `**Preferences**`/`**Technology**`/`**Information**` (L74, L88, L106) are labels, not definitions.

### Low severity
- **[qe-writing-006]** — Title "Shock Non Invertibility" — should arguably be "Shock Non-Invertibility" with hyphen.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 3 `figsize=` settings.

## Strengths
- `\mathbb{E}` used for expectation (qe-math-010, proposed), e.g. L77, L195.
- Title in Title Case (qe-writing-006); section headings in sentence case (qe-writing-006).
- No `\tag`; equations use no manual labels.
- Unicode Greek used in code (qe-code-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert every `\begin{array}` to `\begin{bmatrix}` (qe-math-003).
2. Reduce decorative bolding for non-definitional labels (qe-writing-005).
3. Add `:name: fig-...` fields (qe-fig-005).
