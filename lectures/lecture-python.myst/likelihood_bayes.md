# Style Audit — likelihood_bayes

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_bayes.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9/10 | Transpose denoted `'` (prime) or `^T` instead of `\top`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=3, uni=3). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 71, line 196, line 610. *Count:* 6.

### Medium severity
- **[qe-math-002]** — Transpose denoted `'` (prime) or `^T` instead of `\top`. *Examples:* line 807 (`^T`). *Count:* 2 occurrences.
- **[qe-writing-A1]** — Uses "i.i.d." or "iid" in text rather than "IID". *Examples:* lines 198, 442. *Count:* 5 occurrences.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=3, uni=3).
- **[qe-fig-001]** — `figsize=` set in 1 place(s).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (5 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 5 `.plot()` calls.

## Strengths
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-math-002`: Transpose denoted `'` (prime) or `^T` instead of `\top`.
3. Address `qe-writing-A1`: Uses "i.i.d." or "iid" in text rather than "IID".
4. Address `qe-code-002`: Mixed Greek conventions in code (word=3, uni=3).
5. Address `qe-fig-001`: `figsize=` set in 1 place(s).
