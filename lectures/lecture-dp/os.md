# Style Audit — os

- **Series:** lecture-dp
- **File:** `lectures/os.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 9/10  | Clean Bellman equations; labels and references consistent. |
| Code         | 9/10  | Unicode Greek; no pip install needed; PEP8; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles, no spine issues, no figsize, no Title-Case labels. |
| References   | 10/10 | Single `{cite}` parenthetical. |
| Links        | 9/10  | `{doc}` used 5×; no raw cross-series URLs. |
| Admonitions  | 9/10  | Two `{exercise}` + `solution-start` blocks with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-writing-001]** — A small number of multi-sentence paragraphs (e.g. 22-23, 130-136).
- **[qe-writing-005]** — "**dynamic programming**" not used as a definition consistently; minor.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Equation labels (`crra_utility`, `cake_objective`, `bellman-cep`) used cleanly with `{eq}` references.
- Definitions bolded correctly (**feasible**, **state variable**, **control variable**, **parameters**, **consumption smoothing**).
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` violations.
- "IID" / `\mathbb{E}` consistent where used.
- Unicode Greek (β, γ) in code.
- `{doc}` used for cross-series.
- Exercises use `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Optional minor: split a few multi-sentence paragraphs.
