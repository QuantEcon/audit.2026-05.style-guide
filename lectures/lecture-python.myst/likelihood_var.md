# Style Audit — likelihood_var

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_var.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One section heading uses Title Case. |
| Math         | 8.5/10 | Bold used for vectors/matrices. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 7/10 | `figsize=` set in 2 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 6 times outside exercise blocks. *Examples:* line 328, line 397, line 404.

### Medium severity
- **[qe-math-004]** — Bold used for vectors/matrices. *Example:* line 507. *Count:* 3.
- **[qe-math-011 (proposed)]** — Normal distribution as `\mathcal{N}` rather than `N`. *Examples:* lines 66, 72. *Count:* 2.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=13, uni=2).

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 477 `Application: Samuelson multiplier-accelerator`.
- **[qe-fig-001]** — `figsize=` set in 2 place(s).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (12 plot calls, 0 named).
- **[qe-fig-006]** — One capitalised axis label (line 426).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 6 times outside exercise blocks.
2. Address `qe-math-004`: Bold used for vectors/matrices.
3. Address `qe-math-011 (proposed)`: Normal distribution as `\mathcal{N}` rather than `N`.
4. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=13, uni=2).
5. Address `qe-writing-006`: One section heading uses Title Case.
