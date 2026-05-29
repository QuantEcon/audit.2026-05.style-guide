# Style Audit — cass_koopmans_2

- **Series:** lecture-python.myst
- **File:** `lectures/cass_koopmans_2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=2, uni=13). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9.5/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 8/10 | 2 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 75, line 127, line 134. *Count:* 14 headings affected.

### Medium severity
- **[qe-link-002]** — 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. *Examples:* line 53, line 427.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=2, uni=13).
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.
- **[qe-link-001]** — 2 full URL(s) to same series. *Examples:* line 52, line 426.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-link-002`: 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=2, uni=13).
4. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
5. Address `qe-link-001`: 2 full URL(s) to same series.
