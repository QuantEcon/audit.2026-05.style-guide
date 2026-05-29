# Style Audit — ross_recovery

- **Series:** lecture-python.myst
- **File:** `lectures/ross_recovery.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 8/10 | Matrices use `pmatrix` rather than `bmatrix`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=8, uni=16). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-003]** — Matrices use `pmatrix` rather than `bmatrix`. *Example:* line 1179. *Count:* 2 lines.

### Low severity
- **[qe-math-011 (proposed)]** — Normal distribution as `\mathcal{N}` rather than `N`. *Example:* line 561.
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 485.
- **[qe-code-002]** — Mixed Greek conventions in code (word=8, uni=16).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 1368).

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-math-003`: Matrices use `pmatrix` rather than `bmatrix`.
2. Address `qe-math-011 (proposed)`: Normal distribution as `\mathcal{N}` rather than `N`.
3. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=8, uni=16).
5. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
