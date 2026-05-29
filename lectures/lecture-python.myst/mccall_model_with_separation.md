# mccall_model_with_separation

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model_with_separation.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=2, uni=2). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9.5/10 | Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 141 `The Bellman equations`, line 491 `Solving the Bellman equations`. *Count:* 2.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=2, uni=2).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=2, uni=2).
3. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named).
