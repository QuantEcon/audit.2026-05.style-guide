# Style Audit — mccall_model

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 9/10 | Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=6, uni=18). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8.5/10 | `ax.set_title()` used 2 times outside exercise blocks. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 78, line 117, line 133. *Count:* 12 headings affected.

### Medium severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Examples:* line 226. *Count:* 3 occurrences.
- **[qe-fig-003]** — `ax.set_title()` used 2 times outside exercise blocks. *Examples:* line 602, line 868.
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 382.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=6, uni=18).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (6 plot calls, 0 named).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
3. Address `qe-fig-003`: `ax.set_title()` used 2 times outside exercise blocks.
4. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
5. Address `qe-code-002`: Mixed Greek conventions in code (word=6, uni=18).
