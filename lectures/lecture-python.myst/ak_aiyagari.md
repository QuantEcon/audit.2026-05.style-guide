# Style Audit — ak_aiyagari

- **Series:** lecture-python.myst
- **File:** `lectures/ak_aiyagari.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.5 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=1, uni=42). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8/10 | `figsize=` set in 6 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-003]** — `ax.set_title()` used 3 times outside exercise blocks. *Examples:* line 570, line 1153, line 1382.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=42).
- **[qe-fig-001]** — `figsize=` set in 6 places — usually unnecessary.
- **[qe-fig-008]** — `lw=2` parameter missing from 3 `.plot()` calls.

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` used 3 times outside exercise blocks.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=42).
3. Address `qe-fig-001`: `figsize=` set in 6 places — usually unnecessary.
4. Address `qe-fig-008`: `lw=2` parameter missing from 3 `.plot()` calls.
