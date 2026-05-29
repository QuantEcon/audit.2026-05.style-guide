# imp_sample

- **Series:** lecture-python.myst
- **File:** `lectures/imp_sample.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 7.5/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 8.
- **[qe-fig-003]** — `ax.set_title()` used 4 times outside exercise blocks. *Examples:* line 94, line 106, line 174.

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 49.
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 9 `.plot()` calls.

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
2. Address `qe-fig-003`: `ax.set_title()` used 4 times outside exercise blocks.
3. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
4. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
