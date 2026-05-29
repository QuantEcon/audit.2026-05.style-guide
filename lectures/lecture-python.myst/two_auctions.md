# Style Audit — two_auctions

- **Series:** lecture-python.myst
- **File:** `lectures/two_auctions.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 7.5/10 | Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). |
| Code         | 9.5/10 | Greek letters spelled out in code; consider unicode forms. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 6.5/10 | `figsize=` set in 7 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 9/10 | 1 full URL(s) to same series. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors). *Examples:* line 101, line 165. *Count:* 15 occurrences across 9 lines.
- **[qe-fig-006]** — Axis labels capitalised in 14 places (should be lowercase). *Examples:* line 270, line 271, line 327.

### Medium severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 137. *Count:* 2

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 449 `$\chi^2$ Distribution`.
- **[qe-math-012 (proposed)]** — Multiplication with `*` rather than `\cdot` or juxtaposition. *Example:* line 285.
- **[qe-code-002]** — Greek letters spelled out in code; consider unicode forms. *Count:* 5.
- **[qe-fig-001]** — `figsize=` set in 7 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 445).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (9 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 9 `.plot()` calls.
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 16.

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-math-004`: Vectors/matrices typeset with `\mathbf` or `\boldsymbol` (style guide says no bold for vectors).
2. Address `qe-fig-006`: Axis labels capitalised in 14 places (should be lowercase).
3. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
4. Address `qe-writing-006`: One section heading uses Title Case.
5. Address `qe-math-012 (proposed)`: Multiplication with `*` rather than `\cdot` or juxtaposition.
