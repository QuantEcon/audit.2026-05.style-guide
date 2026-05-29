# Style Audit — endogenous_lake

- **Series:** lecture-python.myst
- **File:** `lectures/endogenous_lake.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One section heading uses Title Case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=5, uni=31). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8.5/10 | `figsize=` set in 2 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-003]** — `ax.set_title()` used 2 times outside exercise blocks. *Examples:* line 579, line 658.

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 71 `Set Up`.
- **[qe-code-002]** — Mixed Greek conventions in code (word=5, uni=31).
- **[qe-fig-001]** — `figsize=` set in 2 place(s).
- **[qe-fig-006]** — One capitalised axis label (line 657).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` used 2 times outside exercise blocks.
2. Address `qe-writing-006`: One section heading uses Title Case.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=5, uni=31).
4. Address `qe-fig-001`: `figsize=` set in 2 place(s).
5. Address `qe-fig-006`: One capitalised axis label (line 657).
