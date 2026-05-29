# Style Audit — odu

- **Series:** lecture-python.myst
- **File:** `lectures/odu.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 9.5/10 | Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=9, uni=12). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 7 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 8.5/10 | 4 full URLs to python.quantecon.org (same series) — use markdown `[](label)` form. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 70, line 82, line 116. *Count:* 8.

### Medium severity
- **[qe-link-001]** — 4 full URLs to python.quantecon.org (same series) — use markdown `[](label)` form. *Examples:* line 38, line 41, line 861.

### Low severity
- **[qe-math-008]** — Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`. *Example:* line 113.
- **[qe-code-002]** — Mixed Greek conventions in code (word=9, uni=12).
- **[qe-fig-001]** — `figsize=` set in 7 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 850).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (4 plot calls, 0 named).
- **[qe-fig-006]** — One capitalised axis label (line 849).
- **[qe-fig-008]** — `lw=2` parameter missing from 4 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-link-001`: 4 full URLs to python.quantecon.org (same series) — use markdown `[](label)` form.
3. Address `qe-math-008`: Ones vector typeset with `\mathbf{1}` rather than `\mathbb{1}`.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=9, uni=12).
5. Address `qe-fig-001`: `figsize=` set in 7 places — usually unnecessary.
