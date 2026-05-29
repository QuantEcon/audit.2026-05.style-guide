# wald_friedman_2

- **Series:** lecture-python.myst
- **File:** `lectures/wald_friedman_2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=1, uni=5). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8.5/10 | `figsize=` set in 4 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 2 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 100, line 205, line 225. *Count:* 6.

### Medium severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 46. *Count:* 2

### Low severity
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 457.
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=5).
- **[qe-fig-001]** — `figsize=` set in 4 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 6 `.plot()` calls.
- **[qe-link-001]** — 2 full URL(s) to same series. *Examples:* line 117, line 763.

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
3. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=5).
5. Address `qe-fig-001`: `figsize=` set in 4 places — usually unnecessary.
