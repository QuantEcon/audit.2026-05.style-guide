# Style Audit — var_dmd

- **Series:** lecture-python.myst
- **File:** `lectures/var_dmd.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 10/10 | Clean code conventions. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | N/A | No figures. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 23, line 261, line 720. *Count:* 5.

### Medium severity
_None found._

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 32.

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
