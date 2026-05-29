# amss2

- **Series:** lecture-dp
- **File:** `lectures/amss2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H2/H3 sentence case throughout. |
| Math         | 8/10  | Mostly clean; `aligned` blocks well used. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 2×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No embedded titles; lowercase labels; figsize 2×. |
| References   | 5/10  | Five narrative-author `{cite}` patterns (e.g. "Lucas-Stokey {cite}…", "AMSS {cite}…"). |
| Links        | 8/10  | `{doc}` used 8×; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-ref-001]** — Five narrative-author `{cite}` patterns ("Lucas-Stokey {cite}`LucasStokey1983`" 5×, "AMSS {cite}`aiyagari2002optimal`"). Should be `{cite:t}`.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs (lines 34-41, 57-79).
- **[qe-writing-009 (proposed)]** — Smart quotes ’ used occasionally.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Definitions bolded ("**measurability constraints**", "**weak**").
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- `aligned` used inside `$$`.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series.
- No matplotlib titles, no spine, no Title-Case axis labels.

## Recommended actions
1. Switch the 5 narrative `Author {cite}…` references to `{cite:t}` form.
2. Optional minor: tighten a few multi-sentence paragraphs.
3. Optional: normalise smart-quotes.
