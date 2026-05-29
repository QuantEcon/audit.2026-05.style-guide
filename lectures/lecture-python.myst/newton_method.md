# Style Audit — newton_method

- **Series:** lecture-python.myst
- **File:** `lectures/newton_method.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=8, uni=19). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8/10 | `figsize=` set in 4 places — usually unnecessary. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 100 `The Solow model`, line 471 `Multivariate Newton's method`. *Count:* 3.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=8, uni=19).
- **[qe-fig-001]** — `figsize=` set in 4 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 633).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` missing on most `.plot()` calls (1/6).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=8, uni=19).
3. Address `qe-fig-001`: `figsize=` set in 4 places — usually unnecessary.
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 633).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
