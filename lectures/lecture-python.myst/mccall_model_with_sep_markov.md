# Style Audit — mccall_model_with_sep_markov

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model_with_sep_markov.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=9, uni=10). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8.5/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | N/A | No citations. |
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
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 713.
- **[qe-code-002]** — Mixed Greek conventions in code (word=9, uni=10).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 880).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
2. Address `qe-code-002`: Mixed Greek conventions in code (word=9, uni=10).
3. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 880).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
