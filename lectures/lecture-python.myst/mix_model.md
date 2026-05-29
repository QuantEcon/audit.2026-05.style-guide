# Style Audit — mix_model

- **Series:** lecture-python.myst
- **File:** `lectures/mix_model.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=5, uni=6). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 7/10 | `figsize=` set in 5 places — usually unnecessary. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 209, line 295, line 398. *Count:* 6.

### Medium severity
- **[qe-fig-006]** — Axis labels capitalised in 4 places. *Examples:* line 564, line 595, line 842.

### Low severity
- **[qe-writing-A1]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 42.
- **[qe-code-002]** — Mixed Greek conventions in code (word=5, uni=6).
- **[qe-fig-001]** — `figsize=` set in 5 places — usually unnecessary.
- **[qe-fig-003]** — `ax.set_title()` used once outside exercise blocks (line 696).
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (7 plot calls, 0 named).
- **[qe-fig-008]** — `lw=2` parameter missing from 7 `.plot()` calls.

## Strengths
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-fig-006`: Axis labels capitalised in 4 places.
3. Address `qe-writing-A1`: Uses "i.i.d." or "iid" in text rather than "IID".
4. Address `qe-code-002`: Mixed Greek conventions in code (word=5, uni=6).
5. Address `qe-fig-001`: `figsize=` set in 5 places — usually unnecessary.
