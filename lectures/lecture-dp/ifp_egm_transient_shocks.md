# Style Audit — ifp_egm_transient_shocks

- **Series:** lecture-dp
- **File:** `lectures/ifp_egm_transient_shocks.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in many H2/H3 headings. |
| Math         | 8/10  | `\mathbb{E}` correct; `\mathsf` for state space. |
| Code         | 4/10  | Six `time.time()` calls for benchmarking; pip install at top. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 7/10  | One Title-Case `'Gini coefficient'` ylabel; figsize 1×; no embedded titles. |
| References   | 9/10  | 2 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | `{doc}` used 5×; no raw cross-series URLs. |
| Admonitions  | 9/10  | Exercises use `{exercise}` + `solution-start` with `:label:` and dropdown. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Six `time.time()` calls for benchmarking. *Lines:* 590, 592, 595, 598, 601, 604. Style guide requires `quantecon.Timer` context manager.

### Medium severity
- **[qe-writing-006]** — Title Case H2/H3 headings. *Examples:* `## The Household Problem` (59), `### Set-Up` (69), `## NumPy Implementation` (174), `### Set Up` (189), `### Solver` (232), `## JAX Implementation` (377), `### Timing` (572), `### Dynamics` (625), `## Wealth Inequality` (814), `### Measuring Inequality` (821), `### Interest Rate and Inequality` (894). *Count:* 12+ headings.
- **[qe-fig-006]** — One Title-Case axis label `set_ylabel('Gini coefficient')` (line 939).

### Low severity
- **[qe-writing-004]** — `\mathsf Z` used for the Markov state space (line 99).
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 1 time.

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- `\mathbb{E}` used (line 74).
- "IID" used correctly (line 93).
- Equation labels and `{eq}` references used cleanly.
- Distribution name `N(0, 1)` written correctly (line 96).
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- Exercises use `{exercise}` + `solution-start`/`solution-end` with `:class: dropdown`.

## Recommended actions
1. Replace `time.time()` benchmarking with `quantecon.Timer` (6 occurrences).
2. Convert all H2/H3 headings to sentence case.
3. Lowercase the `'Gini coefficient'` ylabel.
4. Optionally drop `\mathsf` on `\mathsf Z`.
