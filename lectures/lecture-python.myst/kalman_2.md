# Style Audit — kalman_2

- **Series:** lecture-python.myst
- **File:** `lectures/kalman_2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 8.5/10 | Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=3, uni=10). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 7/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`. *Examples:* lines 258, 260. *Count:* 13 chunks.
- **[qe-fig-006]** — Axis labels capitalised in 6 places (should be lowercase). *Examples:* line 259, line 267, line 406.

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 211 `An Innovations Representation`, line 276 `Some Computational Experiments`. *Count:* 3.
- **[qe-fig-003]** — `ax.set_title()` used 2 times outside exercise blocks. *Examples:* line 485, line 498.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=3, uni=10).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-math-010 (proposed)`: Bare `E[...]`, `\Pr(...)`, or `\Var(...)` used instead of `\mathbb{E}`, `\mathbb{P}`, `\mathbb{V}`.
2. Address `qe-fig-006`: Axis labels capitalised in 6 places (should be lowercase).
3. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
4. Address `qe-fig-003`: `ax.set_title()` used 2 times outside exercise blocks.
5. Address `qe-code-002`: Mixed Greek conventions in code (word=3, uni=10).
