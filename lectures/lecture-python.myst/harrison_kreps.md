# Style Audit — harrison_kreps

- **Series:** lecture-python.myst
- **File:** `lectures/harrison_kreps.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=2, uni=3). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | N/A | No figures. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 76, line 153, line 170. *Count:* 11 headings affected.

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=2, uni=3).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=2, uni=3).
