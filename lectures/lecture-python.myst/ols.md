# Style Audit — ols

- **Series:** lecture-python.myst
- **File:** `lectures/ols.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 9/10 | Single transpose using prime or `^T` rather than `\top`. |
| Code         | 9.5/10 | Greek letters spelled out in code; consider unicode forms. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `ax.set_title()` used 3 times outside exercise blocks. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 78 `Simple Linear Regression`, line 304 `Extending the Linear Regression Model`. *Count:* 2.
- **[qe-fig-003]** — `ax.set_title()` used 3 times outside exercise blocks. *Examples:* line 163, line 298, line 435.
- **[qe-fig-006]** — Axis labels capitalised in 4 places. *Examples:* line 161, line 162, line 433.
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 638.

### Low severity
- **[qe-math-002]** — Single transpose using prime or `^T` rather than `\top`. *Example:* line 664.
- **[qe-code-002]** — Greek letters spelled out in code; consider unicode forms. *Count:* 2.

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-fig-003`: `ax.set_title()` used 3 times outside exercise blocks.
3. Address `qe-fig-006`: Axis labels capitalised in 4 places.
4. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
5. Address `qe-math-002`: Single transpose using prime or `^T` rather than `\top`.
