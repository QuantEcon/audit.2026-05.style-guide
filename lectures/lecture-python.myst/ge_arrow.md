# Style Audit — ge_arrow

- **Series:** lecture-python.myst
- **File:** `lectures/ge_arrow.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 7.5/10 | Transpose denoted `'` (prime) or `^T` instead of `\top`. |
| Code         | 10/10 | Unicode Greek used consistently. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 148, line 242, line 287. *Count:* 15 headings affected.

### Medium severity
- **[qe-math-002]** — Transpose denoted `'` (prime) or `^T` instead of `\top`. *Examples:* line 742 (`^T`). *Count:* 3 occurrences.

### Low severity
- **[qe-math-A1]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 298.
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Code uses Unicode Greek letters throughout.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-math-002`: Transpose denoted `'` (prime) or `^T` instead of `\top`.
3. Address `qe-math-A1`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
4. Address `qe-fig-001`: `figsize=` set in 1 place(s).
