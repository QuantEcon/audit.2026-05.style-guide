# Style Audit — likelihood_ratio_process_2

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_ratio_process_2.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 10/10 | No math issues. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 6/10 | `figsize=` set in 14 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 6 times outside exercise blocks. *Examples:* line 649, line 786, line 1169.

### Medium severity
- **[qe-writing-A1]** — Uses "i.i.d." or "iid" in text rather than "IID". *Examples:* lines 184, 200. *Count:* 4 occurrences.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=18, uni=12).
- **[qe-fig-001]** — `figsize=` set in 14 places — usually unnecessary (defaults from `_config.yml`).
- **[qe-fig-006]** — Axis labels capitalised in 4 places. *Examples:* line 648, line 657, line 717.

### Low severity
- **[qe-writing-006]** — One section heading uses Title Case. *Example:* line 169 `Blume and Easley's setting`.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (11 plot calls, 0 named).

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 6 times outside exercise blocks.
2. Address `qe-writing-A1`: Uses "i.i.d." or "iid" in text rather than "IID".
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=18, uni=12).
4. Address `qe-fig-001`: `figsize=` set in 14 places — usually unnecessary (defaults from `_config.yml`).
5. Address `qe-fig-006`: Axis labels capitalised in 4 places.
