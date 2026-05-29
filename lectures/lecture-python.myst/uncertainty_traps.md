# Style Audit — uncertainty_traps

- **Series:** lecture-python.myst
- **File:** `lectures/uncertainty_traps.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=5, uni=9). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 58 `The Model`, line 102 `Information and Beliefs`. *Count:* 2.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=5, uni=9).
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 498).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` missing on most `.plot()` calls (1/5).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=5, uni=9).
3. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 498).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named).
