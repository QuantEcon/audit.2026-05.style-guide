# Style Audit — multivariate_normal

- **Series:** lecture-python.myst
- **File:** `lectures/multivariate_normal.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 5.5/10 | Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=19, uni=26). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9.5/10 | `figsize=` set in 2 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). *Examples:* line 606, line 650. *Count:* 11 occurrences across 9 lines.
- **[qe-math-A1]** — Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`. *Examples:* lines 2266, 2269. *Count:* 20 chunks.

### Medium severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Examples:* line 650. *Count:* 6 occurrences.
- **[qe-writing-A1]** — Uses "i.i.d." or "iid" in text rather than "IID". *Examples:* lines 602, 1830. *Count:* 3 occurrences.

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 1389 `Constructing a Wold representation`.
- **[qe-code-002]** — Mixed Greek conventions in code (word=19, uni=26).
- **[qe-fig-001]** — `figsize=` set in 2 place(s).
- **[qe-fig-008]** — `lw=2` missing on most `.plot()` calls (1/15).

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-math-004`: Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors).
2. Address `qe-math-A1`: Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`.
3. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
4. Address `qe-writing-A1`: Uses "i.i.d." or "iid" in text rather than "IID".
5. Address `qe-writing-006`: One section heading uses Title Case.
