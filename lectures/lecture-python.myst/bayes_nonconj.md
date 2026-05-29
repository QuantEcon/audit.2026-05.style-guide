# Style Audit — bayes_nonconj

- **Series:** lecture-python.myst
- **File:** `lectures/bayes_nonconj.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.5 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One section heading uses Title Case. |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9.5/10 | `lw=2` parameter missing from 3 `.plot()` calls. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=7, uni=3).

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 944 `Markov chain Monte Carlo`.
- **[qe-fig-008]** — `lw=2` parameter missing from 3 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- Figures use descriptive `name:` fields for cross-referencing.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=7, uni=3).
2. Address `qe-writing-006`: One section heading uses Title Case.
3. Address `qe-fig-008`: `lw=2` parameter missing from 3 `.plot()` calls.
