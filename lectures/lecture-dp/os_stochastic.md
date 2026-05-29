# Style Audit — os_stochastic

- **Series:** lecture-dp
- **File:** `lectures/os_stochastic.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Systemic Title Case in H2/H3 headings. |
| Math         | 7/10  | `\mathbb E` bare (no braces); otherwise clean. |
| Code         | 9/10  | Unicode Greek; no pip install needed; PEP8; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles, no figsize, no Title-Case labels. |
| References   | 9/10  | 4 `{cite}` parenthetical. |
| Links        | 9/10  | `{doc}` used 3×; no raw cross-series URLs. |
| Admonitions  | 8/10  | One `{exercise}` + `{prf:proof}` directive (qe-admon-004 compliant). |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Systemic Title Case in H2/H3 headings. *Examples:* `## The Model` (74), `### Optimal Policies` (155), `### The Bellman Equation` (249), `### Greedy Policies` (291), `### The Bellman Operator` (329, 551), `### Review of Theoretical Results` (372), `### Unbounded Utility` (404), `### Scalar Maximization` (443), `### An Example` (596), `### Iterating to Convergence` (718), `### The Policy Function` (778). *Count:* 11+ headings.

### Medium severity
- **[qe-math-A1]** — `\mathbb E` written without braces (lines 122, 203, 206, 227).

### Low severity
- **[qe-writing-001]** — A couple of multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case (via `{index}` directive).
- Equation labels (`texs0_og2`, `og_conse`, `fpb30`, `vfcsdp0`) and `{eq}` references used cleanly.
- Definitions bolded correctly.
- "IID" used correctly (line 110).
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- Unicode Greek in code.
- `{doc}` used for cross-series.
- Uses `{prf:proof}` directive correctly (qe-admon-004 compliant).
- Exercise uses `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Convert all H2/H3 headings to sentence case.
2. Add braces to `\mathbb{E}`.
