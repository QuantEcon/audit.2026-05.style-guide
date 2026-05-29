# Style Audit — ifp_advanced

- **Series:** lecture-dp
- **File:** `lectures/ifp_advanced.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in many H2/H3 headings. |
| Math         | 7/10  | `\mathbb E` bare; `\mathscr C`/`\mathsf Z` for sets; `\label{a:y0}` leak. |
| Code         | 7/10  | Unicode Greek; pip install at top; PEP8; figsize 3×; one `qe.Timer` use. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 8/10  | No matplotlib titles; lowercase labels; figsize 3×. |
| References   | 9/10  | 6 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | `{doc}` used 6×; no raw cross-series URLs. |
| Admonitions  | 9/10  | Two `{exercise}` + `{solution-start}` with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Title Case H2/H3 headings. *Examples:* `## The Model` (73), `### Set Up` (77), `### Assumptions` (123), `### Optimality` (164), `## Solution Algorithm` (193), `### A Time Iteration Operator` (198), `### Convergence Properties` (226), `### Using an Endogenous Grid` (251), `#### Finding Optimal Consumption` (265), `#### Iterating` (300), `## Wealth Inequality` (668), `### Measuring Inequality` (675). *Count:* 12+ headings.
- **[qe-math-007]** — `\label{a:y0}` inside a `$$ … $$` block (line 158). Manual LaTeX label conflicting with MyST numbering.
- **[qe-math-A1]** — `\mathbb E` written without braces in several display equations (lines 85, 141, 150, 152, 157, 181, 212).

### Low severity
- **[qe-writing-004]** — `\mathscr C`, `\mathsf Z`, `\mathbf S` for sets (lines 117, 166, 170, 200, 203).
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 3 times.

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- "IID" used correctly.
- Equation labels and `{eq}` references used cleanly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek; uses `qe.Timer` (line 496) for benchmarking — qe-code-004 compliant.
- Exercises use `{exercise}` + labels + `solution-start`/`solution-end` with dropdown.
- `{doc}` used for cross-series; no raw URLs.

## Recommended actions
1. Convert all H2/H3 headings to sentence case.
2. Remove the `\label{a:y0}` on line 158 (use `$$ … $$ (label)` form if needed).
3. Add braces to `\mathbb{E}`.
4. Drop `\mathscr`/`\mathsf`/`\mathbf` styling on plain sets where unambiguous.
