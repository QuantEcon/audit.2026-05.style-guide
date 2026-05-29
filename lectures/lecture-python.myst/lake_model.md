# Style Audit — lake_model

- **Series:** lecture-python.myst
- **File:** `lectures/lake_model.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=5, uni=8). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9/10 | `figsize=` set in 8 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=5, uni=8).
- **[qe-fig-001]** — `figsize=` set in 8 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 369).

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-code-002`: Mixed Greek conventions in code (word=5, uni=8).
2. Address `qe-fig-001`: `figsize=` set in 8 places — usually unnecessary.
3. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 369).
