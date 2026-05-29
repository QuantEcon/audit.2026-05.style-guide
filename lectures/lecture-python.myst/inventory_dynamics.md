# Style Audit — inventory_dynamics

- **Series:** lecture-python.myst
- **File:** `lectures/inventory_dynamics.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 56 `Sample Paths`, line 169 `Marginal Distributions`. *Count:* 2.
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 10.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 1 place(s).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` missing on most `.plot()` calls (2/9).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
3. Address `qe-fig-001`: `figsize=` set in 1 place(s).
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` missing on most `.plot()` calls (2/9).
