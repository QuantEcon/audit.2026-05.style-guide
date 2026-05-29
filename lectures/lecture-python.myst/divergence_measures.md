# Style Audit — divergence_measures

- **Series:** lecture-python.myst
- **File:** `lectures/divergence_measures.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 8/10 | `\begin{align}` used inside `$$` math (breaks PDF builds; use `aligned`). |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 4 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
- **[qe-math-006]** — `\begin{align}` used inside `$$` math (breaks PDF builds; use `aligned`). *Example:* line 134. *Count:* 1 occurrences.

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 6.
- **[qe-fig-006]** — Axis labels capitalised in 4 places. *Examples:* line 441, line 442, line 446.

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 336.
- **[qe-fig-001]** — `figsize=` set in 4 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named).

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- No `ax.set_title()` in main figures.
- No embedded matplotlib titles in main figures.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-math-006`: `\begin{align}` used inside `$$` math (breaks PDF builds; use `aligned`).
2. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
3. Address `qe-fig-006`: Axis labels capitalised in 4 places.
4. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
5. Address `qe-fig-001`: `figsize=` set in 4 places — usually unnecessary.
