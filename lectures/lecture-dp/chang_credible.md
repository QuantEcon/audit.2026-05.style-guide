# Style Audit — chang_credible

- **Series:** lecture-dp
- **File:** `lectures/chang_credible.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.0 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | All H2/H3 headings sentence case. |
| Math         | 7/10  | `\vec` used heavily; otherwise clean. |
| Code         | 5/10  | Installs `polytope` (binary, non-Anaconda) without notes; pip at top; Unicode Greek; figsize 1×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles; lowercase labels; 1 figsize. |
| References   | 5/10  | Three narrative-author `{cite}` patterns. |
| Links        | 8/10  | `{doc}` used; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-006]** — `!pip install polytope` (line 29) — `polytope` is a binary scientific-Python package, no installation notes provided.

### Medium severity
- **[qe-math-004]** — `\vec z`, `\vec h`, `\vec M`, `\vec q`, `\vec m`, `\vec x`, `\vec c`, `\vec y` used extensively (lines 108-131, 139-145, etc.). *Count:* 30+ occurrences.
- **[qe-ref-001]** — Three narrative-author `{cite}` patterns (e.g. "Chang {cite}`chang1998credible`"). Should be `{cite:t}`.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. 34-44, 53-58).
- **[qe-writing-009 (proposed)]** — Smart quotes ’ used occasionally.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Definitions/italics consistent (*sustainable plan*, *credible public policy*, *Ramsey planner*, *value of money*).
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series.
- No transpose, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- No matplotlib titles, no spine issues, no Title-Case axis labels.

## Recommended actions
1. Add a note about `polytope` package binary install (not in Anaconda).
2. Remove `\vec` arrows on sequence symbols.
3. Switch narrative `Author {cite}…` to `{cite:t}` form.
4. Tighten compound paragraphs.
5. Normalise smart-quotes.
