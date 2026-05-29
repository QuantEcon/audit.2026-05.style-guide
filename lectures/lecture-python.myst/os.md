# Style Audit — os

- **Series:** lecture-python.myst
- **File:** `lectures/os.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.5 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=1, uni=1). |
| JAX          | out of scope | not a JAX lecture |
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
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 159 `The Bellman equation`, line 317 `The Euler equation`. *Count:* 2.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=1).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.

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
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=1).
3. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
4. Address `qe-fig-008`: `lw=2` parameter missing from 4 `.plot()` calls.
