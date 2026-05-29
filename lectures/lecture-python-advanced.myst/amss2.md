# amss2

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/amss2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 6.5/10 | Mixed `E_t` and `\mathbb E_t` (former rare). |
| Code         | 7/10  | Spelled Greek (`alpha`, `beta`); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `figsize=` settings; no `:name:` fields. |
| References   | 7/10  | 13 `{cite}`; several narrative author refs would benefit from `{cite:t}` (e.g. "Lucas-Stokey (1983)" sections). |
| Links        | 8/10  | Heavy `{doc}` use; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-010 (proposed)]** — A few bare `E_t` instead of `\mathbb{E}_t`. *Example:* `lectures/amss2.md:557`, `:609`, `:619`. *Count:* 3 occurrences.
- **[qe-ref-001]** — Narrative-style author references not using `{cite:t}` (e.g. "Lucas-Stokey (1983)" at L131). *Count:* ~4 occurrences with "in"/"of" preceding `{cite}`.

### Low severity
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`) in code parameters.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used consistently (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- One-sentence paragraph rule respected (qe-writing-001).
- Cross-series references via `{doc}` (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace remaining bare `E_t` with `\mathbb{E}_t` (qe-math-010, proposed).
2. Convert "Author (Year) {cite}`...`" patterns to `{cite:t}` (qe-ref-001).
3. Use unicode Greek in code (qe-code-002).
