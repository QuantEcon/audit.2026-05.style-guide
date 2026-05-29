# Style Audit — markov_asset

- **Series:** lecture-python.myst
- **File:** `lectures/markov_asset.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=11, uni=16). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `ax.set_title()` used once outside exercise blocks (line 629). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 8.5/10 | 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 94, line 119, line 148. *Count:* 18 headings affected.

### Medium severity
- **[qe-link-002]** — 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. *Examples:* line 175, line 472.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=11, uni=16).
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 629).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Figures use default sizing.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-link-002`: 2 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=11, uni=16).
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 629).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
