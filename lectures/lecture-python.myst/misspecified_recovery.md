# Style Audit — misspecified_recovery

- **Series:** lecture-python.myst
- **File:** `lectures/misspecified_recovery.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 4/10 | Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9.5/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). *Examples:* line 156, line 157. *Count:* 45 occurrences across 41 lines.
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 253, line 414, line 815. *Count:* 5.
- **[qe-math-010 (proposed)]** — Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`. *Examples:* lines 739, 773. *Count:* 10 chunks.

### Medium severity
- **[qe-math-003]** — Matrices use `pmatrix` (parentheses) rather than `bmatrix` (square brackets). *Examples:* lines 2188, 2191. *Count:* 4 lines.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=19, uni=7).

### Low severity
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-math-004`: Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors).
2. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
3. Address `qe-math-010 (proposed)`: Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`.
4. Address `qe-math-003`: Matrices use `pmatrix` (parentheses) rather than `bmatrix` (square brackets).
5. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=19, uni=7).
