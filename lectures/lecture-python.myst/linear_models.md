# linear_models

- **Series:** lecture-python.myst
- **File:** `lectures/linear_models.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 1 place(s). |
| References   | N/A | No citations. |
| Links        | 8/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 77, line 119, line 147. *Count:* 25 headings affected.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=14, uni=2).
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 1343.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 1 place(s).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 1046.

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
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=14, uni=2).
3. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
4. Address `qe-fig-001`: `figsize=` set in 1 place(s).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
