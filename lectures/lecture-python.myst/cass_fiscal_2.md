# Style Audit — cass_fiscal_2

- **Series:** lecture-python.myst
- **File:** `lectures/cass_fiscal_2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
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
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 44 `A Two-Country Cass-Koopmans Model`, line 79 `Capital Mobility and Taxation`. *Count:* 2.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-fig-001`: `figsize=` set in 1 place(s).
