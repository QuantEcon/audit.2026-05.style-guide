# Style Audit — cagan_ree

- **Series:** lecture-python-intro
- **File:** `lectures/cagan_ree.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | H1 Title Case OK; some H4 use Title Case; many multi-sentence paragraphs in Overview. |
| Math         | 7/10  | bmatrix used; equation labels; clean. |
| Code         | 8/10  | Unicode Greek (`π`, `μ`, `α`, `λ`) throughout (qe-code-002 OK); standard Anaconda imports only. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 341, 532, 590; 4 `ax.set_title` calls inside solution blocks (exception applies); no figure `:name:`. |
| References   | 8/10  | `{cite}` used; no clear in-text mis-use detected. |
| Links        | 9/10  | `{doc}` links used for cross-references (7 occurrences). |
| Admonitions  | 9/10  | Solutions use `:class: dropdown` + exercise labels (qe-admon-002, qe-admon-005 OK); gated form (qe-admon-001 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Several multi-sentence paragraphs throughout Overview (lines 19–26, 27–32, 39–46, 48–56).
- **W3** — "#### Experiment 1: Foreseen sudden stabilization" (line 301), "#### Experiment 2: an unforeseen sudden stabilization" (454), "#### Experiment 3" (619) — minor mixed casing across H4 headings.
- **W7** — Italic in mid-sentence: `_expenditures_`, `_tax collections_`, `_printing money_`, `_start_`, `_stop_` (lines 23–24, 44, 46) — should use `*emphasis*` consistently.
- **[qe-fig-001]** — Repeated `figsize=` overrides on lines 341, 532, 590. *Count:* 3 occurrences.

### Low severity
- **W7** — "Ends of Four Big Inflations" title-cased mid-sentence (line 50).
- **[qe-fig-005]** — No figures have a `:name:` field for cross-referencing.

## Strengths
- bmatrix used throughout (M4 OK).
- Equation labels and `{eq}` references used.
- Bold for definitions (**perfect foresight**).
- Unicode Greek in code (qe-code-002 OK).
- `{doc}` cross-series links used (qe-link-002 OK).
- All 4 solutions are gated, dropdown, and linked to their exercises.

## Recommended actions
1. Break Overview multi-sentence paragraphs.
2. Make H4 experiment headings sentence case consistently.
3. Switch `_underscored_` italics to `*asterisks*` for consistency.
4. Remove `figsize=` overrides on lines 341, 532, 590.
