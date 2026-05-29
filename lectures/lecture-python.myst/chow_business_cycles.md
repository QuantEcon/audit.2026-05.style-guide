# Style Audit — chow_business_cycles

- **Series:** lecture-python.myst
- **File:** `lectures/chow_business_cycles.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 9/10 | Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8.5/10 | `figsize=` set in 11 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 845 `The Slutsky connection`, line 979 `Reconstructing $A$ and computing $F(\omega)$`. *Count:* 2.
- **[qe-math-A1]** — Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. *Examples:* line 914. *Count:* 3.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=13, uni=8).
- **[qe-fig-001]** — `figsize=` set in 11 places — usually unnecessary (defaults from `_config.yml`).

### Low severity
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (12 plot calls, 0 named).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-math-A1`: Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=13, uni=8).
4. Address `qe-fig-001`: `figsize=` set in 11 places — usually unnecessary (defaults from `_config.yml`).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (12 plot calls, 0 named).
