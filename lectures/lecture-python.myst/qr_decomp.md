# Style Audit — qr_decomp

- **Series:** lecture-python.myst
- **File:** `lectures/qr_decomp.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 9/10 | Single transpose using prime or `^T` rather than `\top`. |
| Code         | 10/10 | Clean code conventions. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | N/A | No figures. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 29 `Matrix Factorization`, line 165 `Some Code`. *Count:* 3.

### Low severity
- **[qe-math-002]** — Single transpose using prime or `^T` rather than `\top`. *Example:* line 385.

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-math-002`: Single transpose using prime or `^T` rather than `\top`.
