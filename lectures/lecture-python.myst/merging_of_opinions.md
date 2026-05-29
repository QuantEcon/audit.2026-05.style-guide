# Style Audit — merging_of_opinions

- **Series:** lecture-python.myst
- **File:** `lectures/merging_of_opinions.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 9/10 | Normal distribution as `\mathcal{N}` rather than `N`. |
| Code         | 8.5/10 | Greek letters spelled out in code; spec prefers unicode (α, β). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8.5/10 | `figsize=` set in 8 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-011 (proposed)]** — Normal distribution as `\mathcal{N}` rather than `N`. *Examples:* lines 884, 947. *Count:* 2.
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 271 `The Blackwell–Dubins theorem`, line 353 `The Beta–Bernoulli model`. *Count:* 3.
- **[qe-code-002]** — Greek letters spelled out in code; spec prefers unicode (α, β). *Count:* 10.
- **[qe-fig-003]** — `ax.set_title()` used 4 times outside exercise blocks. *Examples:* line 588, line 599, line 607.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 8 places — usually unnecessary.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-math-011 (proposed)`: Normal distribution as `\mathcal{N}` rather than `N`.
2. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
3. Address `qe-code-002`: Greek letters spelled out in code; spec prefers unicode (α, β).
4. Address `qe-fig-003`: `ax.set_title()` used 4 times outside exercise blocks.
5. Address `qe-fig-001`: `figsize=` set in 8 places — usually unnecessary.
