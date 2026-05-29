# Style Audit — wealth_dynamics

- **Series:** lecture-python.myst
- **File:** `lectures/wealth_dynamics.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=1, uni=1). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | Figures lack descriptive `name:` fields for cross-referencing (14 plot calls, 0 named). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 62, line 85, line 90. *Count:* 7.

### Medium severity
- **[qe-fig-006]** — Axis labels capitalised in 2 places. *Examples:* line 186, line 187.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=1).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (14 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 14 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- No embedded matplotlib titles in main figures.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-fig-006`: Axis labels capitalised in 2 places.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=1).
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (14 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` parameter missing from 14 `.plot()` calls.
