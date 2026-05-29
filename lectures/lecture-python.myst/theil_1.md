# Style Audit — theil_1

- **Series:** lecture-python.myst
- **File:** `lectures/theil_1.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.3 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 2 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | N/A | No external links. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=3, uni=1).

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 103.
- **[qe-fig-001]** — `figsize=` set in 2 place(s).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 366).

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=3, uni=1).
2. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
3. Address `qe-fig-001`: `figsize=` set in 2 place(s).
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 366).
