# Style Audit — amss3

- **Series:** lecture-dp
- **File:** `lectures/amss3.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | All H2/H3 headings sentence case. |
| Math         | 9/10  | Clean math; `aligned` properly used inside `$$`. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 2×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | Three static PNG figures (`amss3_g1.png`, `amss3_g2.png`, `amss3_g3.png`); figsize 2×. |
| References   | 10/10 | 21 `{cite}` references, all parenthetical; no narrative-author misuse. |
| Links        | 9/10  | 12 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-002]** — Three static PNG figures used (`amss3_g1.png`, `amss3_g2.png`, `amss3_g3.png`). *Lines:* 212, 226, 259. Prefer code-generated figures where possible.

### Low severity
- **[qe-math-001]** — `\cr` line separator used inside `aligned` block (lines 105-109); MyST convention is `\\`.
- **[qe-writing-001]** — A couple of multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Definitions bolded.
- Equation labels and `{eq}` references used cleanly.
- "IID" used correctly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top.
- `{doc}` used for cross-series; no raw URLs.
- Excellent citation discipline.
- No matplotlib titles, no spine, no Title-Case axis labels.

## Recommended actions
1. Regenerate the 3 static PNG figures from code where possible.
2. Replace `\cr` with `\\` inside the `aligned` block.
