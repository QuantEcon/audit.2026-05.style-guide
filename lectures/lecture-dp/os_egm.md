# Style Audit — os_egm

- **Series:** lecture-dp
- **File:** `lectures/os_egm.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in H2/H3 ("Key Idea", "Exogenous Grid"). |
| Math         | 8/10  | Clean Euler/EGM equations. |
| Code         | 9/10  | Unicode Greek; no pip install needed; PEP8; uses `qe.Timer`. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles, no figsize, no Title-Case labels. |
| References   | 8/10  | "Carroll {cite}…" narrative-author pattern (1×). |
| Links        | 9/10  | `{doc}` used 10×; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Title Case H2/H3 headings: `## Key Idea` (55), `### Exogenous Grid` (77), `### Endogenous Grid` (98), `### The Operator` (214), `### Testing` (259).
- **[qe-ref-001]** — Narrative-author citation (1 occurrence). Should be `{cite:t}`.

### Low severity
- **[qe-writing-001]** — A couple of compound paragraphs (e.g. 27-44).

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- Definitions bolded ("**endogenous grid method**", "**endogenously**").
- Equation labels with `{eq}` references used cleanly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- Unicode Greek in code; uses `qe.Timer()` (line 340).
- `{doc}` used for cross-series.

## Recommended actions
1. Convert H2/H3 headings to sentence case.
2. Switch narrative `Author {cite}…` to `{cite:t}` form.
