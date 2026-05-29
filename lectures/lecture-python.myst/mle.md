# Style Audit — mle

- **Series:** lecture-python.myst
- **File:** `lectures/mle.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | No writing issues. |
| Math         | 6/10 | Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=11, uni=11). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 8.5/10 | `figsize=` set in 7 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). *Examples:* line 187, line 194. *Count:* 106 occurrences across 57 lines.

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=11, uni=11).
- **[qe-fig-001]** — `figsize=` set in 7 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 152.

## Strengths
- Headings use sentence case consistently.
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
2. Address `qe-code-002`: Mixed Greek conventions in code (word=11, uni=11).
3. Address `qe-fig-001`: `figsize=` set in 7 places — usually unnecessary.
4. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
5. Address `qe-fig-008`: `lw=2` parameter missing from 4 `.plot()` calls.
