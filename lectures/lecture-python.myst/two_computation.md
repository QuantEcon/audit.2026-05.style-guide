# Style Audit — two_computation

- **Series:** lecture-python.myst
- **File:** `lectures/two_computation.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 7.5/10 | Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 5.5/10 | `figsize=` set in 10 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks. *Examples:* line 711, line 2173, line 2746.
- **[qe-fig-006]** — Axis labels capitalised in 46 places (should be lowercase). *Examples:* line 301, line 302, line 603.

### Medium severity
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. *Examples:* line 153. *Count:* 3.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=26, uni=12).
- **[qe-fig-001]** — `figsize=` set in 10 places — usually unnecessary (defaults from `_config.yml`).

### Low severity
- **[qe-math-002]** — Single transpose using prime or `^T` rather than `\top`. *Example:* line 478.
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Example:* line 459.

## Strengths
- Headings use sentence case consistently.
- Uses "IID" or no IID terminology.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks.
2. Address `qe-fig-006`: Axis labels capitalised in 46 places (should be lowercase).
3. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`.
4. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=26, uni=12).
5. Address `qe-fig-001`: `figsize=` set in 10 places — usually unnecessary (defaults from `_config.yml`).
