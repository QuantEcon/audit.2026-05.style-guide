# Style Audit — information_market_equilibrium

- **Series:** lecture-python.myst
- **File:** `lectures/information_market_equilibrium.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 9.5/10 | Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 9 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 751. *Count:* 2
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=30, uni=2).
- **[qe-fig-001]** — `figsize=` set in 9 places — usually unnecessary (defaults from `_config.yml`).
- **[qe-fig-003]** — `ax.set_title()` used 3 times outside exercise blocks. *Examples:* line 1297, line 1411, line 1510.

### Low severity
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 601.

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
2. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=30, uni=2).
3. Address `qe-fig-001`: `figsize=` set in 9 places — usually unnecessary (defaults from `_config.yml`).
4. Address `qe-fig-003`: `ax.set_title()` used 3 times outside exercise blocks.
5. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
