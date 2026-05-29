# ifp_egm

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_egm.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9/10 | Mixed Greek conventions in code (word=1, uni=6). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9/10 | Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 73, line 165, line 207. *Count:* 9.

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=6).
- **[qe-code-004]** — Manual `time.time()` timing pattern used (6 occurrences); prefer `qe.Timer()`.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 8 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=6).
3. Address `qe-code-004`: Manual `time.time()` timing pattern used (6 occurrences); prefer `qe.Timer()`.
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` parameter missing from 8 `.plot()` calls.
