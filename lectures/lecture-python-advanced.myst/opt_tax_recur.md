# Style Audit — opt_tax_recur

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/opt_tax_recur.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; clean one-sentence paragraphs. |
| Math         | 7/10  | `{\cal S}` for state space; primes are next-period notation. |
| Code         | 7/10  | Mixed spelled/unicode Greek (4 spelled vs 0 unicode); 2 quantecon imports; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 1 `ax.set_title`; 5 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 5 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 5 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-009]** — `{\cal S}` (calligraphic S) used for the state space. *Example:* `lectures/opt_tax_recur.md:84`, `:820`, `:826`, `:837`, `:848`. *Count:* 5 occurrences.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.

### Low severity
- **[qe-math-010 (proposed)]** — One bare `E` occurrence per scan.
- Primes (`s'`, `x'(s')`) are next-period notation; no qe-math-002 violation.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 5 `figsize=` settings.
- **[qe-code-002]** — 4 spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003); audit any `\begin{pmatrix}` blocks.
- Sequences in curly brackets (qe-math-005).
- Equation labels and `{eq}` references (qe-math-007).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `{\cal S}` with plain `S` (qe-math-009).
2. Audit and convert any `\begin{pmatrix}` blocks to `\begin{bmatrix}` (qe-math-003).
3. Remove `ax.set_title` (qe-fig-003).
4. Convert spelled Greek to unicode (qe-code-002).
