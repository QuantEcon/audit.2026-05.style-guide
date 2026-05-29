# Style Audit — rs_inventory_q

- **Series:** lecture-python.myst
- **File:** `lectures/rs_inventory_q.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=6, uni=13). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9.5/10 | `figsize=` set in 4 places — usually unnecessary. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 59, line 124, line 163. *Count:* 7.

### Medium severity
_None found._

### Low severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Example:* line 379.
- **[qe-code-002]** — Mixed Greek conventions in code (word=6, uni=13).
- **[qe-fig-001]** — `figsize=` set in 4 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=6, uni=13).
4. Address `qe-fig-001`: `figsize=` set in 4 places — usually unnecessary.
