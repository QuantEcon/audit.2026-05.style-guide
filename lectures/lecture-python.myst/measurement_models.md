# Style Audit — measurement_models

- **Series:** lecture-python.myst
- **File:** `lectures/measurement_models.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 8.5/10 | Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 2 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. *Examples:* line 954. *Count:* 6.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=11, uni=7).

### Low severity
- **[qe-math-A3]** — Normal distribution as `\mathcal{N}` rather than `N`. *Example:* line 328.
- **[qe-fig-001]** — `figsize=` set in 2 place(s).

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-math-A1`: Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`.
2. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=11, uni=7).
3. Address `qe-math-A3`: Normal distribution as `\mathcal{N}` rather than `N`.
4. Address `qe-fig-001`: `figsize=` set in 2 place(s).
