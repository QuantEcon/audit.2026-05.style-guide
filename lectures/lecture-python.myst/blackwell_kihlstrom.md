# Style Audit — blackwell_kihlstrom

- **Series:** lecture-python.myst
- **File:** `lectures/blackwell_kihlstrom.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 8/10 | Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=21, uni=37). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9.5/10 | `figsize=` set in 8 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`. *Examples:* lines 100, 378. *Count:* 13 chunks.

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 370 `Kihlstrom's Bayesian interpretation`, line 1173 `The Data Processing Inequality and Coarse-Graining`. *Count:* 3.

### Low severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Example:* line 817.
- **[qe-code-002]** — Mixed Greek conventions in code (word=21, uni=37).
- **[qe-fig-001]** — `figsize=` set in 8 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-math-010 (proposed)`: Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`.
2. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
3. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=21, uni=37).
5. Address `qe-fig-001`: `figsize=` set in 8 places — usually unnecessary.
