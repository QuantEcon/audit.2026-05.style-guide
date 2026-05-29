# Style Audit — mle

- **Series:** lecture-python-intro
- **File:** `lectures/mle.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title Case H1, sentence-case H2/H3; one-sentence paragraphs. |
| Math         | 9/10  | Lowercase `f` for density (M10); `IID` written correctly; clean equations. |
| Code         | 9/10  | Standard Anaconda imports only; unicode Greek (`μ`, `σ`) used (qe-code-002 OK). |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `figsize=` / `ax.set_title` violations; no `{figure}` directives. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | `{prf:example}` used (qe-admon-004 OK); 2 solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W1** — Occasional two-sentence paragraphs (e.g. lines 117–118, 153–154).
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:` for cross-referencing.

## Strengths
- Correct "IID" usage (line 195).
- Density `f`, distribution names plain.
- Equation labels and `{eq}` references.
- Bold/italic used appropriately.
- Clean sentence-case section headings.
- Unicode Greek in code.
- No matplotlib figure violations.
- `{prf:example}` directive (qe-admon-004 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. None critical.
