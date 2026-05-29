# Style Audit — opt_transport

- **Series:** lecture-python.myst
- **File:** `lectures/opt_transport.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 5/10 | Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). |
| Code         | 9.5/10 | Greek letters spelled out in code; consider unicode forms. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). *Examples:* line 206, line 213. *Count:* 10 occurrences across 10 lines.
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 60, line 131, line 137. *Count:* 9.

### Medium severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Examples:* line 154. *Count:* 16 occurrences.

### Low severity
- **[qe-math-002]** — Single transpose using prime or `^T` rather than `\top`. *Example:* line 200.
- **[qe-code-002]** — Greek letters spelled out in code; consider unicode forms. *Count:* 3.
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-math-004`: Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors).
2. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
3. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
4. Address `qe-math-002`: Single transpose using prime or `^T` rather than `\top`.
5. Address `qe-code-002`: Greek letters spelled out in code; consider unicode forms.
