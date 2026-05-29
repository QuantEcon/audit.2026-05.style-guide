# Style Audit — mccall_q

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_q.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=1, uni=5). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8.5/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 85, line 242, line 316. *Count:* 5.

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=5).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (7 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 7 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=5).
3. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (7 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` parameter missing from 7 `.plot()` calls.
