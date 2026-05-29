# Style Audit — perm_income_cons

- **Series:** lecture-python.myst
- **File:** `lectures/perm_income_cons.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 8/10 | Transpose denoted `'` (prime) and/or `^T` instead of `\top`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9.5/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Transpose denoted `'` (prime) and/or `^T` instead of `\top`. *Examples:* line 244 `$v(x) = - x'Px - d$...`. *Count:* 5 occurrences.
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 137, line 165, line 201. *Count:* 12 headings affected.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=12, uni=1).
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 163.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-math-002`: Transpose denoted `'` (prime) and/or `^T` instead of `\top`.
2. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=12, uni=1).
4. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
5. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
