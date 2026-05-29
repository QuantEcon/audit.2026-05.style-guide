# monte_carlo

- **Series:** lecture-python-intro
- **File:** `lectures/monte_carlo.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3/H4 sentence case; one-sentence paragraphs. |
| Math         | 8/10  | `\mathbb E`, `\mathbb P` used (M7 OK); `LN` for lognormal (M9 OK); `\mathop{\mathrm{Var}}` instead of `\mathbb V`. |
| Code         | 9/10  | Unicode Greek (`μ`, `σ`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 7/10  | No `figsize=` violations; 1 `ax.set_title(title)` on line 549 outside exercise context; no `{figure}` directives. |
| References   | N/A   | no `{cite}` citations |
| Links        | 9/10  | `{doc}` link present (1 occurrence). |
| Admonitions  | 9/10  | 2 solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **M7** — Uses `\mathop{\mathrm{Var}} S` (line 101) instead of `\mathbb V[S]`. *Count:* 1 occurrence.
- **[qe-fig-003]** — `ax.set_title(title)` on line 549 outside exercise context. *Count:* 1 occurrence.

### Low severity
- **W3** — "#### A routine using loops in python" (line 156) — "python" should be "Python".
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- `\mathbb E`, `\mathbb P` consistently used (M7).
- Distribution `LN(\mu, \sigma)` plain (M9 OK).
- Equation labels and references.
- One-sentence paragraph style.
- Unicode Greek in code.
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Capitalize "Python" in the H4.
2. Replace `\mathop{\mathrm{Var}}` with `\mathbb V`.
3. Move `set_title(title)` on line 549 to figure metadata.
