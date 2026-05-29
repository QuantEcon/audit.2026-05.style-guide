# Style Audit — ifp_opi

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_opi.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=4, uni=11). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9/10 | `figsize=` set in 1 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 56, line 107, line 219. *Count:* 5.

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=4, uni=11).
- **[qe-fig-001]** — `figsize=` set in 1 place(s).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 408).

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
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=4, uni=11).
3. Address `qe-fig-001`: `figsize=` set in 1 place(s).
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 408).
