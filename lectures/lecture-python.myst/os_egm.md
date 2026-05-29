# Style Audit — os_egm

- **Series:** lecture-python.myst
- **File:** `lectures/os_egm.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | Figures follow conventions. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 55 `Key Idea`, line 77 `Exogenous Grid`. *Count:* 4.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=3, uni=1).

### Low severity
_None found._

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=3, uni=1).
