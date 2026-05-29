# Style Audit — re_with_feedback

- **Series:** lecture-python.myst
- **File:** `lectures/re_with_feedback.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=1, uni=24). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `ax.set_title()` used 3 times outside exercise blocks. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 79, line 95, line 182. *Count:* 13 headings affected.

### Medium severity
- **[qe-fig-003]** — `ax.set_title()` used 3 times outside exercise blocks. *Examples:* line 452, line 496, line 955.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=1, uni=24).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 6 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-fig-003`: `ax.set_title()` used 3 times outside exercise blocks.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=1, uni=24).
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` parameter missing from 6 `.plot()` calls.
