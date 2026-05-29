# Style Audit — supply_demand_foundations_v2

- **Series:** lecture-python-intro
- **File:** `lectures/supply_demand_foundations_v2.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 5.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | H1 "Multiple goods" sentence case for what should be lecture title; structure broken (lecture starts with H2); many Title Case H2 sections. |
| Math         | 5/10  | Mixed transpose: both `\top` and `^T` used (M2 inconsistent); equations generally clean otherwise. |
| Code         | N/A   | no executable `{code-cell}` blocks (only inline `python` fenced code as illustration) |
| JAX          | out of scope | — |
| Figures      | 7/10  | `figsize=` on lines 1129, 1344 (in inline code samples) — no actual matplotlib usage in code-cells; no `{figure}` directives. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | N/A   | no exercises / solutions |

## Issues

### Critical
_None found._

### High severity
- **W2** — H1 is `# Multiple goods` (line 145), buried 145 lines into the file, lowercase 'goods' (should be Title Case "Multiple Goods"); file actually begins with H2 `## Elements of Supply and Demand` (line 3), so no proper lecture title at top.
- **W3** — Many H2 sections use Title Case. *Examples:* "## Demand Curve Implied by Constrained Utility Maximization" (line 216), "## Endowment Economy, II" (317), "## Digression: Marshallian and Hicksian Demand Curves" (284), "## Dynamics and Risk as Special Cases of Pure Exchange Economy" (375), "## Supply Curve of a Competitive Firm" (511), "## Digression: A Supplier who is a monopolist" (602). *Count:* 6+ headings.

### Medium severity
- **M2** — Mixed transpose: `^\top` used in most places (line 160 onwards) but `\Pi^T \Pi` used in places (lines 188, 191). *Count:* 2-3 mixed instances.
- **W1** — Several multi-sentence paragraphs at top.
- **W7** — Typos: "compeitive" (line 33), "simulataneous" (line 137), "It we solve" (line 121), "we'll can" (line 114).

### Low severity
- **W7** — Mixed H4 capitalization: "#### Example: Two-person economy **without** production" (877), "#### A **dynamic economy**" (970).
- **[qe-fig-001]** — `figsize=` shown in inline code samples (lines 1129, 1344) — would carry over if these became `{code-cell}` blocks.

## Strengths
- `\top` used for transpose in most places (M2 mostly OK).
- Bold for definitions (**consumer surplus**, **producer surplus**, etc.).
- Equation labels and `{eq}` references.

## Recommended actions
1. Fix file structure: promote a proper Title Case H1 to the top of the file.
2. Convert all Title Case H2 headings to sentence case.
3. Normalize transpose notation to `\top` throughout.
4. Fix typos throughout.
5. Convert illustrative inline code blocks into executable `{code-cell}` blocks (and add exercises/solutions consistent with the series) to bring this lecture inline with the rest of the series.
