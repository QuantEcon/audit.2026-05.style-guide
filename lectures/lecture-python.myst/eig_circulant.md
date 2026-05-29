# eig_circulant

- **Series:** lecture-python.myst
- **File:** `lectures/eig_circulant.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9/10 | Transpose denoted `'` (prime) or `^T` instead of `\top`. |
| Code         | 10/10 | Clean code conventions. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 2 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 42, line 89, line 129. *Count:* 6.

### Medium severity
- **[qe-math-002]** — Transpose denoted `'` (prime) or `^T` instead of `\top`. *Examples:* line 121 (`^T`). *Count:* 2 occurrences.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 2 place(s).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 512).

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-math-002`: Transpose denoted `'` (prime) or `^T` instead of `\top`.
3. Address `qe-fig-001`: `figsize=` set in 2 place(s).
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 512).
