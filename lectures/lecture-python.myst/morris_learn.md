# Style Audit — morris_learn

- **Series:** lecture-python.myst
- **File:** `lectures/morris_learn.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.5 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=3, uni=11). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | Figures follow conventions. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-A1]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 82. *Count:* 2
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 330 `Two Traders`, line 546 `General N–trader extension`. *Count:* 2.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=3, uni=11).

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-A1`: Uses "i.i.d." or "iid" in text rather than "IID".
2. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=3, uni=11).
