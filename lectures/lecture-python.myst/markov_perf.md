# Style Audit — markov_perf

- **Series:** lecture-python.myst
- **File:** `lectures/markov_perf.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 6/10 | Transpose denoted `'` (prime) and/or `^T` instead of `\top`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Transpose denoted `'` (prime) and/or `^T` instead of `\top`. *Examples:* line 265 `$\Pi_{it} := R_i + F_{-it}' S_i F_{-it}$...`. *Count:* 19 occurrences.
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 91, line 177, line 188. *Count:* 8.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=18, uni=4).
- **[qe-fig-003]** — `ax.set_title()` used 2 times outside exercise blocks. *Examples:* line 494, line 850.

### Low severity
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Axis labels lowercase.

## Recommended actions
1. Address `qe-math-002`: Transpose denoted `'` (prime) and/or `^T` instead of `\top`.
2. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=18, uni=4).
4. Address `qe-fig-003`: `ax.set_title()` used 2 times outside exercise blocks.
5. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
