# Style Audit — back_prop

- **Series:** lecture-python.myst
- **File:** `lectures/back_prop.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.5 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 10/10 | Unicode Greek used consistently. |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9/10 | Plotly figures used but no `{only} latex` directive present for PDF compatibility. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 72, line 153, line 211. *Count:* 5.
- **[qe-fig-010]** — Plotly figures used but no `{only} latex` directive present for PDF compatibility.

### Medium severity
_None found._

### Low severity
_None found._

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-fig-010`: Plotly figures used but no `{only} latex` directive present for PDF compatibility.
