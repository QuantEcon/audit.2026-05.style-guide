# Style Audit — util_rand_resp

- **Series:** lecture-python.myst
- **File:** `lectures/util_rand_resp.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 7/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 37, line 58, line 62. *Count:* 17 headings affected.
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks. *Examples:* line 300, line 334, line 420.

### Medium severity
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 18.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (21 plot calls, 0 named).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks.
3. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
4. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (21 plot calls, 0 named).
