# Style Audit — jv

- **Series:** lecture-dp
- **File:** `lectures/jv.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Multiple Title Case H3 headings. |
| Math         | 8/10  | Clean Bellman; `\text{Beta}` instead of `\mathrm{Beta}`; `\mathbb{P}` used. |
| Code         | 8/10  | Unicode Greek; no pip install (uses base packages only); figsize 3×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 8/10  | No embedded titles; mostly clean; figsize 3×. |
| References   | 10/10 | One `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | No raw cross-series URLs. |
| Admonitions  | 9/10  | Two `{exercise}`/`exercise-start` + `solution-start` with `:label:` and dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Title Case H3 headings. *Examples:* `### Model Features` (45), `### Parameterization` (106), `### Back-of-the-Envelope Calculations` (130), `## Solving for Policies` (359). *Count:* 4 headings.
- **[qe-math-A3]** — Distribution written as `\text{Beta}(2, 2)` (lines 118, 127); style guide prefers `\mathrm{Beta}`.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs (e.g. 134-140, 163-170).
- **[qe-fig-001]** — `figsize=` set 3 times.

## Strengths
- Lecture title in correct Title Case (via `{index}` directive).
- `\mathbb{E}` and `\mathbb{P}` used (lines 150-151).
- "IID" used correctly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align` issues.
- Equation labels with `{eq}` references used cleanly.
- Exercises use `{exercise}` and `exercise-start`/`exercise-end` plus `solution-start`/`solution-end` with `:class: dropdown`.

## Recommended actions
1. Convert H3s to sentence case: "Model features", "Back-of-the-envelope calculations", "Solving for policies".
2. Replace `\text{Beta}` with `\mathrm{Beta}`.
