# Style Audit — short_path

- **Series:** lecture-dp
- **File:** `lectures/short_path.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Clean structure, sentence-case H2s, mostly one-sentence paragraphs. |
| Math         | 9/10  | Math is minimal but compliant. |
| Code         | 9/10  | No pip install needed; PEP8; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Four static PNG figures (`graph.png`, `graph2.png`, `graph3.png`, `graph4.png`). |
| References   | N/A   | No `{cite}` directives. |
| Links        | 9/10  | No raw cross-series URLs; uses Wikipedia external links. |
| Admonitions  | 9/10  | One `{exercise-start}` + `{solution-start}` with `:label:` and dropdown; one `{note}`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-002]** — Four static PNG figures (`graph.png`, `graph2.png`, `graph3.png`, `graph4.png`). *Lines:* 57, 78, 84, 96. These are graph visualizations that could in principle be code-generated (e.g. with `networkx` or graphviz) but here they are intentionally hand-drawn illustrations. Accept as low-priority.

### Low severity
- **[qe-writing-001]** — A few paragraphs run two sentences (e.g. 122-123, 145-148).
- **[qe-writing-005]** — "**dynamic programming**" (line 41) bolded as if defined, but used here as emphasis.

## Strengths
- Title in correct Title Case.
- All H2/H3 headings sentence case.
- Equation labels use `{math} :label:` form correctly with `{eq}` references.
- Simple notation ($J$, $Q$, $F_v$) consistent with qe-writing-004.
- No transpose, no bold vectors, no `\tag`, no `align` issues.
- Exercise uses `exercise-start`/`exercise-end` + `solution-start`/`solution-end` with `:class: dropdown`.

## Recommended actions
1. Consider tightening a couple of two-sentence paragraphs to single sentences.
2. Switch the bolded "dynamic programming" to italics when used as emphasis rather than definition.
