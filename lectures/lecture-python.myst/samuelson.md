# samuelson

- **Series:** lecture-python.myst
- **File:** `lectures/samuelson.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=7, uni=66). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 6 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 8/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 847 `Digression: Using Sympy to find roots`, line 1134 `Illustration of Samuelson class`. *Count:* 3.
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 41.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=7, uni=66).
- **[qe-fig-001]** — `figsize=` set in 6 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
- **[qe-fig-007]** — Spine hidden once (line 436).
- **[qe-fig-008]** — `lw=2` parameter missing from 8 `.plot()` calls.
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 387.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=7, uni=66).
4. Address `qe-fig-001`: `figsize=` set in 6 places — usually unnecessary.
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
