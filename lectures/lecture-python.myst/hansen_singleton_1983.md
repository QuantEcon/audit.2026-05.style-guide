# hansen_singleton_1983

- **Series:** lecture-python.myst
- **File:** `lectures/hansen_singleton_1983.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One section heading uses Title Case. |
| Math         | 5.5/10 | Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=6, uni=8). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). *Examples:* line 153, line 155. *Count:* 141 occurrences across 35 lines.

### Medium severity
_None found._

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 1208 `Predictability and the R-squared restriction`.
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 1641.
- **[qe-code-002]** — Mixed Greek conventions in code (word=6, uni=8).
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-math-004`: Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors).
2. Address `qe-writing-006`: One section heading uses Title Case.
3. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=6, uni=8).
5. Address `qe-fig-001`: `figsize=` set in 1 place(s).
