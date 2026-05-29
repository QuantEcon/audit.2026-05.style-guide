# Style Audit — finite_markov

- **Series:** lecture-python.myst
- **File:** `lectures/finite_markov.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 9/10 | Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=6, uni=6). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 2 place(s). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 223, line 295, line 319. *Count:* 11 headings affected.

### Medium severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Examples:* line 854. *Count:* 3 occurrences.
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 309.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=6, uni=6).
- **[qe-fig-001]** — `figsize=` set in 2 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
3. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=6, uni=6).
5. Address `qe-fig-001`: `figsize=` set in 2 place(s).
