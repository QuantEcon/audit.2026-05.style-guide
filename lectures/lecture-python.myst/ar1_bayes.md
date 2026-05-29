# ar1_bayes

- **Series:** lecture-python.myst
- **File:** `lectures/ar1_bayes.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9.5/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 181 `PyMC Implementation`, line 295 `Numpyro Implementation`. *Count:* 2.
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 21.

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 72.
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
3. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
4. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
