# lq_inventories

- **Series:** lecture-python.myst
- **File:** `lectures/lq_inventories.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 8/10 | Transpose denoted `'` (prime) or `^T` instead of `\top`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-002]** — Transpose denoted `'` (prime) or `^T` instead of `\top`. *Examples:* line 131. *Count:* 4 occurrences.
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 417 `Inventories Not Useful`, line 448 `Inventories Useful but are Hardwired to be Zero Al`. *Count:* 2.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=5, uni=3).

### Low severity
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-math-002`: Transpose denoted `'` (prime) or `^T` instead of `\top`.
2. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=5, uni=3).
4. Address `qe-fig-001`: `figsize=` set in 1 place(s).
