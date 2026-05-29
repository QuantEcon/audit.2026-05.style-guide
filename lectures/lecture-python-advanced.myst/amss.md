# Style Audit — amss

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/amss.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 6.5/10 | `pmatrix` and `matrix` used for two equations; otherwise clean. |
| Code         | 8/10  | Mixed unicode/spelled Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | `figsize=` used 3 times; no `:name:` fields. |
| References   | 7/10  | `{cite}` used 6 times; one narrative reference ("Lucas and Stokey (1983)") would benefit from `{cite:t}`. |
| Links        | 8/10  | Heavy `{doc}` use (11 occurrences); no raw cross-series URLs. |
| Admonitions  | 7/10  | 1 exercise; no associated solution dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-003]** — `\begin{pmatrix}` and `\begin{matrix}` used for two matrices instead of `\begin{bmatrix}`. *Example:* `lectures/amss.md:802`, `:815`. *Count:* 2 occurrences.
- **[qe-ref-001]** — Narrative author references followed by `{cite}` (e.g. "Lucas and Stokey (1983) {cite}`LucasStokey1983`") should use `{cite:t}`. *Example:* `lectures/amss.md:191`, `:321`. *Count:* 2 occurrences.

### Low severity
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — `figsize=` set 3 times without justification.

## Strengths
- `\mathbb E_0`, `\mathbb E_t` used consistently (qe-math-010, proposed) at L302, L313, L335, L524, L534, L543, L551.
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- One-sentence paragraph rule respected (qe-writing-001).
- Sequences in curly brackets (qe-math-005).
- Heavy use of `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace the two `pmatrix`/`matrix` blocks with `bmatrix` (qe-math-003).
2. Convert "Author (Year) {cite}`...`" patterns to `{cite:t}` (qe-ref-001).
3. Add `:name: fig-...` fields to figures (qe-fig-005).
