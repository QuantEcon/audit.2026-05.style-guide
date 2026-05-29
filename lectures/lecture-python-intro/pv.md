# pv

- **Series:** lecture-python-intro
- **File:** `lectures/pv.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title Case H1, sentence-case H2; one-sentence paragraphs throughout. |
| Math         | 9/10  | bmatrix; sequences with `\{...\}`; labels via `(label)`. |
| Code         | 8/10  | Unicode Greek (`δ`) used in code (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 7/10  | No `figsize=` violations; 2 `ax.set_title(...)` inside solution blocks (OK by exception); no `{figure}` directives. |
| References   | N/A   | no `{cite}` citations |
| Links        | 9/10  | `{doc}` cross-references used (5 occurrences). |
| Admonitions  | 9/10  | 7 solutions all gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK); 11 exercise/solution pairs total. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W1** — A few short two-sentence paragraphs (e.g. lines 28–31).
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Sequences use `\{p_t\}_{t=0}^T` (M6 compliant).
- bmatrix throughout.
- Equation labels and `{eq}` / `[](label)` cross-references used.
- Bold for definitions like "**present value model**", "**difference equation**".
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.
- Strong exercise/solution structure (7 paired).

## Recommended actions
1. None critical.
