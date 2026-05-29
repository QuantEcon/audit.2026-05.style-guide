# likelihood_ratio_process

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_ratio_process.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One section heading uses Title Case. |
| Math         | 8.5/10 | Bold used for vectors/matrices. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 6/10 | `figsize=` set in 12 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 8 times outside exercise blocks. *Examples:* line 196, line 558, line 601.

### Medium severity
- **[qe-math-004]** — Bold used for vectors/matrices. *Example:* line 1518. *Count:* 3.
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. *Examples:* line 399. *Count:* 6.
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 12.
- **[qe-fig-001]** — `figsize=` set in 12 places — usually unnecessary (defaults from `_config.yml`).

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 68 `Likelihood Ratio Process`.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (23 plot calls, 0 named).
- **[qe-fig-006]** — One capitalised axis label (line 1316).
- **[qe-fig-008]** — `lw=2` missing on most `.plot()` calls (6/23).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 8 times outside exercise blocks.
2. Address `qe-math-004`: Bold used for vectors/matrices.
3. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`.
4. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
5. Address `qe-fig-001`: `figsize=` set in 12 places — usually unnecessary (defaults from `_config.yml`).
