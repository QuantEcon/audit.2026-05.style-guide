# Style Audit — wald_friedman

- **Series:** lecture-python.myst
- **File:** `lectures/wald_friedman.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One section heading uses Title Case. |
| Math         | 9.5/10 | Normal distribution as `\mathcal{N}` rather than `N`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 7/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=17, uni=16).
- **[qe-fig-003]** — `ax.set_title()` used 2 times outside exercise blocks. *Examples:* line 655, line 889.

### Low severity
- **[qe-math-011 (proposed)]** — Normal distribution as `\mathcal{N}` rather than `N`. *Example:* line 1206.
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 81 `Source of the Problem`.
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
- **[qe-fig-006]** — One capitalised axis label (line 780).
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 348.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=17, uni=16).
2. Address `qe-fig-003`: `ax.set_title()` used 2 times outside exercise blocks.
3. Address `qe-math-011 (proposed)`: Normal distribution as `\mathcal{N}` rather than `N`.
4. Address `qe-writing-006`: One section heading uses Title Case.
5. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
