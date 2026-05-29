# os_egm_jax

- **Series:** lecture-python.myst
- **File:** `lectures/os_egm_jax.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=8, uni=10). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8/10 | `ax.set_title()` used once outside exercise blocks (line 391). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-006]** — Axis labels capitalised in 2 places. *Examples:* line 388, line 389.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=8, uni=10).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 391).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-fig-006`: Axis labels capitalised in 2 places.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=8, uni=10).
3. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 391).
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
