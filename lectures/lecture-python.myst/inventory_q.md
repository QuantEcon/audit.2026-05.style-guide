# Style Audit — inventory_q

- **Series:** lecture-python.myst
- **File:** `lectures/inventory_q.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.3 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=3, uni=10). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 2 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 76 `The Model`, line 154 `Solving via Value Function Iteration`. *Count:* 4.

### Low severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Example:* line 231.
- **[qe-code-002]** — Mixed Greek conventions in code (word=3, uni=10).
- **[qe-fig-001]** — `figsize=` set in 2 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=3, uni=10).
4. Address `qe-fig-001`: `figsize=` set in 2 place(s).
