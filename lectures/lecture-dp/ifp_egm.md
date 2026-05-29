# Style Audit — ifp_egm

- **Series:** lecture-dp
- **File:** `lectures/ifp_egm.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in many H2/H3 headings. |
| Math         | 8/10  | `\mathbb{E}` correct; `\mathsf` for state space. |
| Code         | 4/10  | Six `time.time()` calls for benchmarking; no figsize; pip install at top. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 9/10  | No matplotlib titles, no Title-Case labels, no figsize. |
| References   | 9/10  | 6 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | `{doc}` used 6×; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises in body. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Six `time.time()` calls for benchmarking. *Lines:* 669, 671, 674, 677, 680, 683. Style guide requires `quantecon.Timer` context manager.

### Medium severity
- **[qe-writing-006]** — Title Case H2/H3 headings. *Examples:* `## The Household Problem` (73), `### Set-Up` (80), `### Value Function and Euler Equation` (165), `### Optimality Results` (207), `## NumPy Implementation` (325), `### Set Up` (340), `### Solver` (374), `## JAX Implementation` (488), `### Timing` (651), `### Dynamics` (704), `### A Sanity Check` (767). *Count:* 10+ headings.

### Low severity
- **[qe-writing-004]** — `\mathsf Z`, `\mathsf S` for sets (lines 120, 145, 167, 211, 222).
- **[qe-writing-001]** — A few multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- Definitions bolded.
- Equation labels and `{eq}` references used cleanly.
- `\mathbb{E}` and `\mathbb{E}_t` used consistently.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek (β, γ, σ) in code.
- `{doc}` used for cross-series.
- No matplotlib titles, no spine, no Title-Case axis labels, no figsize.

## Recommended actions
1. Replace `time.time()`-based benchmarking with `quantecon.Timer` context manager (6 occurrences).
2. Convert H2/H3 headings to sentence case.
3. Optionally drop `\mathsf` styling on state-space symbols.
