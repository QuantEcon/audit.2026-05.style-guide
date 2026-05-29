# hoist_failure

- **Series:** lecture-python.myst
- **File:** `lectures/hoist_failure.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Multiplication with `*` rather than `\cdot` or juxtaposition. |
| Code         | 9.5/10 | `!pip install` cell missing `tags: [hide-output]` (line 53). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 8/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 132, line 209, line 319. *Count:* 6.

### Medium severity
- **[qe-link-002]** — 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. *Examples:* line 37.

### Low severity
- **[qe-math-012 (proposed)]** — Multiplication with `*` rather than `\cdot` or juxtaposition. *Example:* line 144.
- **[qe-code-003]** — `!pip install` cell missing `tags: [hide-output]` (line 53).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 6 `.plot()` calls.
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 36.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-link-002`: 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links.
3. Address `qe-math-012 (proposed)`: Multiplication with `*` rather than `\cdot` or juxtaposition.
4. Address `qe-code-003`: `!pip install` cell missing `tags: [hide-output]` (line 53).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
