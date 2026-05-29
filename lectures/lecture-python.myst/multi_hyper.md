# Style Audit — multi_hyper

- **Series:** lecture-python.myst
- **File:** `lectures/multi_hyper.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=3, uni=4). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 1 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 38, line 65, line 109. *Count:* 5.

### Medium severity
_None found._

### Low severity
- **[qe-math-A1]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 139.
- **[qe-code-002]** — Mixed Greek conventions in code (word=3, uni=4).
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-math-A1`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=3, uni=4).
4. Address `qe-fig-001`: `figsize=` set in 1 place(s).
