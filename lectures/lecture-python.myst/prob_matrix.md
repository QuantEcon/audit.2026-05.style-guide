# Style Audit — prob_matrix

- **Series:** lecture-python.myst
- **File:** `lectures/prob_matrix.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 9/10 | Multiplication written with `*` rather than `\cdot` or juxtaposition. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8.5/10 | `figsize=` set in 2 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Examples:* lines 134, 137. *Count:* 4 occurrences.
- **[qe-math-012 (proposed)]** — Multiplication written with `*` rather than `\cdot` or juxtaposition. *Example:* line 1126. *Count:* 3.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=16, uni=12).
- **[qe-fig-006]** — Axis labels capitalised in 3 places. *Examples:* line 1721, line 1722, line 1837.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 2 place(s).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 1838).

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
2. Address `qe-math-012 (proposed)`: Multiplication written with `*` rather than `\cdot` or juxtaposition.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=16, uni=12).
4. Address `qe-fig-006`: Axis labels capitalised in 3 places.
5. Address `qe-fig-001`: `figsize=` set in 2 place(s).
