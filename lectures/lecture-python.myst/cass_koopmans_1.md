# Style Audit — cass_koopmans_1

- **Series:** lecture-python.myst
- **File:** `lectures/cass_koopmans_1.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=6, uni=10). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 82, line 102, line 154. *Count:* 11 headings affected.

### Medium severity
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 31.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=6, uni=10).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=6, uni=10).
4. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
5. Address `qe-fig-008`: `lw=2` parameter missing from 4 `.plot()` calls.
