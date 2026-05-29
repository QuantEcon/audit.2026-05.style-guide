# Style Audit — hansen_singleton_1982

- **Series:** lecture-python.myst
- **File:** `lectures/hansen_singleton_1982.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 9/10 | Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 1 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`. *Examples:* line 260. *Count:* 4.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=5, uni=4).

### Low severity
- **[qe-writing-A1]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 756.
- **[qe-fig-001]** — `figsize=` set in 1 place(s).

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-math-A1`: Bare `E[...]` or `\Pr(...)` used instead of `\mathbb{E}`, `\mathbb{P}`.
2. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=5, uni=4).
3. Address `qe-writing-A1`: Uses "i.i.d." or "iid" in text rather than "IID".
4. Address `qe-fig-001`: `figsize=` set in 1 place(s).
