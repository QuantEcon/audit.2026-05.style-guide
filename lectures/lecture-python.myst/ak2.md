# Style Audit — ak2

- **Series:** lecture-python.myst
- **File:** `lectures/ak2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=2, uni=11). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 6 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | N/A | No external links. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 176 `Activities in Factor Markets`, line 690 `Experiment 1: Tax cut`. *Count:* 3.

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=2, uni=11).
- **[qe-fig-001]** — `figsize=` set in 6 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 819).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (25 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 25 `.plot()` calls.

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
2. Address `qe-code-002`: Mixed Greek conventions in code (word=2, uni=11).
3. Address `qe-fig-001`: `figsize=` set in 6 places — usually unnecessary.
4. Address `qe-fig-003`: `ax.set_title()` used once outside exercise blocks (line 819).
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (25 plot calls, 0 named).
