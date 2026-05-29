# cattle_cycles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cattle_cycles.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 4/10  | Systemic `\begin{array}` for matrices. |
| Code         | 7/10  | Mixed unicode/spelled Greek (8 spelled vs 4 unicode); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 1 `ax.set_title`; 2 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 6 `{cite}` used; never `{cite:t}` despite narrative author references. |
| Links        | 8/10  | 1 `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — All matrices use `\left[ \begin{array}{...} ... \end{array} \right]` rather than `\begin{bmatrix}`. *Example:* `lectures/cattle_cycles.md:126`-`136`, `:143`-`163`, `:169`-`190`. *Count:* ~12 occurrences.

### Medium severity
- **[qe-fig-003]** — `ax.set_title` used in 1 cell.

### Low severity
- **[qe-writing-005]** — `**Remark**` (L100) used as a label rather than definition; `**Preferences**`/`**Technology**`/`**Information**` (L112, L121, L165) are labels.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, etc.) in code parameters (8 occurrences).

## Strengths
- `\mathbb{E}_0` used correctly for expectation (qe-math-010, proposed) at L93.
- Sequences in curly brackets `\{c_t, x_t\}`, `\{h_t, m_t\}` (qe-math-005) at L64-65, L90.
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert every `\begin{array}` to `\begin{bmatrix}` (qe-math-003).
2. Remove `ax.set_title` call (qe-fig-003).
3. Add `:name: fig-...` fields to figures (qe-fig-005).
4. Convert spelled Greek to unicode in code (qe-code-002).
