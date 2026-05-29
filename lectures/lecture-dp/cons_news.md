# cons_news

- **Series:** lecture-dp
- **File:** `lectures/cons_news.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Sentence-case headings; multiple `i.i.d.` uses. |
| Math         | 7/10  | `\mathbb E_t` may need braces; otherwise clean. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Four `plt.title(...)` calls — embedded matplotlib titles. |
| References   | 7/10  | "Eric Leeper, Todd Walker, and Susan Yang {cite}…" — should be `{cite:t}`; 2 occurrences. |
| Links        | 3/10  | Seven raw markdown links to `python-intro.quantecon.org`. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Seven raw markdown links to `python-intro.quantecon.org/perm_income_cons.html` and `python-intro.quantecon.org/kalman.html`. *Lines:* 36, 56, 86, 412, 486, 498, 501. Should be `{doc}` intersphinx references.

### Medium severity
- **[qe-writing-009 (proposed)]** — `i.i.d.` used in narrative. *Lines:* 127, 146, 149, 481. *Count:* 4.
- **[qe-fig-003]** — Four `plt.title(...)` calls embedding matplotlib titles. *Lines:* 747, 767, 801, 810.
- **[qe-ref-001]** — Two narrative-author `{cite}` patterns ("Eric Leeper, Todd Walker, and Susan Yang {cite}`Leeper_Walker_Yang`"). Should be `{cite:t}`.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. 42-45, 51-67).
- **[qe-writing-009 (proposed)]** — Right curly apostrophes ’ in narrative.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Matrices use `bmatrix` (9 matrix blocks).
- Definitions bolded ("**discount factor**", "**interest rate**", "**news**", "**information shocks**", "**Ricardian equivalence**", "**innovations representation**", "**covariance generating function**").
- Equation labels (`eqn_1`, `eqn_2`, `eqn_3`) and `{eq}` references used cleanly.
- No `\tag`, no `align`-inside-`$$`, no bold vectors, no `\mathcal N` for distribution.
- pip install at top; Unicode Greek in code; no figsize.

## Recommended actions
1. Convert 7 raw `python-intro.quantecon.org` markdown links to `{doc}` form.
2. Replace every `i.i.d.` with `IID`.
3. Remove the 4 `plt.title(...)` calls.
4. Switch narrative `Author {cite}…` to `{cite:t}` form.
5. Tighten multi-sentence paragraphs.
6. Normalise smart-quotes.
