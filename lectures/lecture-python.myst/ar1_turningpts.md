# Style Audit — ar1_turningpts

- **Series:** lecture-python.myst
- **File:** `lectures/ar1_turningpts.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 8/10 | Transpose denoted `'` (prime) or `^T` instead of `\top`. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8.5/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | N/A | No external links. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 60, line 188, line 283. *Count:* 7.

### Medium severity
- **[qe-math-002]** — Transpose denoted `'` (prime) or `^T` instead of `\top`. *Examples:* line 297 (`^T`). *Count:* 3 occurrences.
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 29.

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 69.
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 153).
- **[qe-fig-008]** — `lw=2` parameter missing from 3 `.plot()` calls.

## Strengths
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-math-002`: Transpose denoted `'` (prime) or `^T` instead of `\top`.
3. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
4. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
5. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
