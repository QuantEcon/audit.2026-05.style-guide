# olg

- **Series:** lecture-python-intro
- **File:** `lectures/olg.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; clean one-sentence paragraphs. |
| Math         | 9/10  | `\mathbb R_+`; equation labels via `{math}` with `:label:`; clean. |
| Code         | 8/10  | Unicode Greek (`α`, `β`, `R`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 448, 727; no `ax.set_title` violations outside exercise; no `{figure}` directives. |
| References   | 8/10  | 1 `{cite}` (parenthetical, OK). |
| Links        | 6/10  | Same-series direct URL `intro.quantecon.org/solow.html` on line 34; cross-series direct URL `python.quantecon.org/newton_method.html` on line 676. |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — `figsize=` overrides on lines 448, 727. *Count:* 2 occurrences.
- **[qe-link-001]** — Same-series link uses full URL. *Example:* `lectures/olg.md:34` (`[growth model](https://intro.quantecon.org/solow.html)`). Should be `[](solow)` or `[growth model](solow)`.
- **[qe-link-002]** — Cross-series link uses direct URL. *Example:* `lectures/olg.md:676` (`[Newton's method](https://python.quantecon.org/newton_method.html)`). Should be `{doc}\`intermediate:newton_method\``.

### Low severity
- **W1** — A few short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Equation labels via `{math}` `:label:` (M14 OK).
- Clean sentence-case section headings.
- Bold for definitions and italic for emphasis used appropriately.
- Sequences `\{...\}` notation correct.
- Unicode Greek in code.
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Replace same-series direct URL on line 34 with `[](solow)`.
2. Replace cross-series direct URL on line 676 with `{doc}\`intermediate:newton_method\``.
3. Remove `figsize=` overrides.
