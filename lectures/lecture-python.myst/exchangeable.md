# Style Audit — exchangeable

- **Series:** lecture-python.myst
- **File:** `lectures/exchangeable.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 81, line 110, line 156. *Count:* 8.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=9, uni=2).
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 551.

### Low severity
- **[qe-math-A1]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 697.
- **[qe-fig-001]** — `figsize=` set in 1 place(s).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 654).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=9, uni=2).
3. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
4. Address `qe-math-A1`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
5. Address `qe-fig-001`: `figsize=` set in 1 place(s).
