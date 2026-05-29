# linear_algebra

- **Series:** lecture-python.myst
- **File:** `lectures/linear_algebra.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.8 / 10
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
| Links        | 7/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Transpose denoted `'` (prime) and/or `^T` instead of `\top`. *Examples:* line 847 `$\hat x = (A'A)^{-1}A'y$...`. *Count:* 108 occurrences.
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 124, line 220, line 391. *Count:* 19 headings affected.
- **[qe-link-002]** — 6 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. *Examples:* line 68, line 206, line 610.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=22, uni=1).

### Low severity
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 847.

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-math-002`: Transpose denoted `'` (prime) and/or `^T` instead of `\top`.
2. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
3. Address `qe-link-002`: 6 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links.
4. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=22, uni=1).
5. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
