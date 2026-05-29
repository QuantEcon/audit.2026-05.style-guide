# Style Audit — permanent_income_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/permanent_income_dles.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 4/10  | `\begin{array}` used throughout for matrices; bare `E_0/E_t` for expectation. |
| Code         | 8/10  | Unicode Greek used (4 occurrences); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | 1 `figsize=`; no `:name:` fields. |
| References   | 7/10  | 3 `{cite}` used; "Hall (1978)" narrative ref should use `{cite:t}`. |
| Links        | 8/10  | 1 `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — `\begin{array}{c}...\end{array}` (with `\left[ \right]`) used everywhere instead of `\begin{bmatrix}` (carry-forward from v1 M4). *Example:* `lectures/permanent_income_dles.md:161`, `:163`, `:165`, `:166`, `:170`-`173`, `:256`-`260`. *Count:* ~10 occurrences.
- **[qe-math-A1]** — Bare `E_0` / `E_t` instead of `\mathbb{E}_0` (carry-forward from v1 M7). *Example:* `lectures/permanent_income_dles.md:70`, `:73`, `:129`. *Count:* ~4 occurrences.

### Medium severity
- **[qe-writing-005]** — `**Technology:**`, `**Information:**`, `**Preferences:**` use bold for labels rather than definitions.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs, e.g. L46-48, L268-271.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- Section heading in sentence case (qe-writing-006).
- `\begin{bmatrix}` is used in some places (L140, L266) — file knows the right convention.
- Equation references via `{eq}` (qe-math-007) and labelled `{math}` blocks.
- Unicode Greek in code (qe-code-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert every `\begin{array}` block to `\begin{bmatrix}` (qe-math-003).
2. Replace bare `E_t`/`E_0` with `\mathbb{E}_t`/`\mathbb{E}_0` (qe-math-A1).
3. Reduce decorative bolding (qe-writing-005).
4. Add `:name: fig-...` fields (qe-fig-005).
