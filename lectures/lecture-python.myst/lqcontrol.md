# Style Audit — lqcontrol

- **Series:** lecture-python.myst
- **File:** `lectures/lqcontrol.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 5/10 | Transpose denoted `'` (prime) and/or `^T` instead of `\top`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 8.5/10 | 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Transpose denoted `'` (prime) and/or `^T` instead of `\top`. *Examples:* line 270 `$$ x_t' I x_t + u_t' I u_t = \| x_t \|^2 + \| u_t \|^2 $$...`. *Count:* 38 occurrences.
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 84, line 298, line 305. *Count:* 13 headings affected.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=23, uni=13).
- **[qe-fig-006]** — Axis labels capitalised in 4 places. *Examples:* line 702, line 770, line 1348.
- **[qe-link-002]** — 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. *Examples:* line 54.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.

## Recommended actions
1. Address `qe-math-002`: Transpose denoted `'` (prime) and/or `^T` instead of `\top`.
2. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=23, uni=13).
4. Address `qe-fig-006`: Axis labels capitalised in 4 places.
5. Address `qe-link-002`: 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links.
