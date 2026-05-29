# Style Audit — solow

- **Series:** lecture-python-intro
- **File:** `lectures/solow.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2 sentence case; no Overview section heading though. |
| Math         | 7/10  | Uses `(k_t)_{t \geq 0}` parenthesis sequence notation (M6 violation); `(A_t)_{t \geq 1}` likewise. |
| Code         | 8/10  | Unicode Greek (`α`, `δ`, `s`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 237, 338, 488, 607; no `ax.set_title`/spines violations. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | 2 solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **M6** — Sequence notation uses parentheses instead of curly braces. *Examples:* `(k_t)_{t \geq 0}` (line 108), `(A_t)_{t \geq 1}` (line 556). *Count:* 2 occurrences.
- **[qe-fig-001]** — `figsize=` overrides on lines 237, 338, 488, 607. *Count:* 4 occurrences.

### Low severity
- **W7** — `label=r'$c*(s)$'` (line 502) uses `*` in math context — should be `\cdot` or `^*`.
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Equation labels via `{math}` `:label:` (M14 OK).
- Bold for definitions (**homogeneous of degree one**, **Cobb-Douglas**, **CES**, **steady state**).
- Italic for emphasis used appropriately.
- Unicode Greek in code.
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Replace `(k_t)_{t \geq 0}` with `\{ k_t \}_{t \geq 0}` (M6).
2. Use `\cdot` or `^*` in matplotlib labels.
3. Remove `figsize=` overrides.
