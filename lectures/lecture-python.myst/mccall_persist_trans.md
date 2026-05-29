# Style Audit — mccall_persist_trans

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_persist_trans.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 10/10 | No math issues. |
| Code         | 10/10 | Unicode Greek used consistently. |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9/10 | Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- Code uses Unicode Greek letters throughout.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
2. Address `qe-fig-008`: `lw=2` parameter missing from 4 `.plot()` calls.
