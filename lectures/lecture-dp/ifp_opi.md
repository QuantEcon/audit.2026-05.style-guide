# Style Audit — ifp_opi

- **Series:** lecture-dp
- **File:** `lectures/ifp_opi.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in most H2 headings. |
| Math         | 8/10  | Clean Bellman/policy operator; otherwise compliant. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 1×. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 7/10  | One `ax.set_title('OPI execution time vs step size m')`; figsize 1×. |
| References   | 10/10 | No `{cite}` directives (no citations). |
| Links        | 9/10  | `{doc}` used 4×; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `solution-start`/`solution-end` with `:label:` and dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Title Case in H2 headings. *Examples:* `## Model and Primitives` (56), `## Operators and Policies` (107), `## Value Function Iteration` (219), `## Optimistic Policy Iteration` (245), `## Timing Comparison` (293). *Count:* 5 headings.
- **[qe-fig-003]** — `ax.set_title('OPI execution time vs step size m')` (line 408).

### Low severity
- **[qe-writing-001]** — Minor: a couple of multi-sentence paragraphs (e.g. 24-26).
- **[qe-fig-001]** — `figsize=` set 1 time.

## Strengths
- Lecture title in correct Title Case.
- Definitions bolded ("**optimistic policy iteration**" — line 24).
- `\mathbb{E}` used (line 65).
- Equation labels and `{eq}` references used cleanly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series.
- Exercise uses `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Convert H2 headings to sentence case.
2. Remove the `ax.set_title(...)` call.
