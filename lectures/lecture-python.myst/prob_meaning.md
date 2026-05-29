# prob_meaning

- **Series:** lecture-python.myst
- **File:** `lectures/prob_meaning.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 9.5/10 | Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 6/10 | `figsize=` set in 8 places — usually unnecessary. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 7 times outside exercise blocks. *Examples:* line 243, line 276, line 308.

### Medium severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Examples:* lines 22, 325. *Count:* 3 occurrences.
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 72 `Frequentist Interpretation`, line 340 `Bayesian Interpretation`. *Count:* 3.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=15, uni=4).
- **[qe-fig-006]** — Axis labels capitalised in 4 places. *Examples:* line 559, line 616, line 622.

### Low severity
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 333.
- **[qe-fig-001]** — `figsize=` set in 8 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (10 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 10 `.plot()` calls.

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 7 times outside exercise blocks.
2. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
3. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
4. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=15, uni=4).
5. Address `qe-fig-006`: Axis labels capitalised in 4 places.
