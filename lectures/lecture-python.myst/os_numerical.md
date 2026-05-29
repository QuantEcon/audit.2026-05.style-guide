# Style Audit — os_numerical

- **Series:** lecture-python.myst
- **File:** `lectures/os_numerical.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=7, uni=7). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `ax.set_title()` used 3 times outside exercise blocks. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 55, line 86, line 106. *Count:* 5.

### Medium severity
- **[qe-fig-003]** — `ax.set_title()` used 3 times outside exercise blocks. *Examples:* line 309, line 365, line 384.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=7, uni=7).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (11 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` missing on most `.plot()` calls (1/11).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-fig-003`: `ax.set_title()` used 3 times outside exercise blocks.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=7, uni=7).
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (11 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` missing on most `.plot()` calls (1/11).
