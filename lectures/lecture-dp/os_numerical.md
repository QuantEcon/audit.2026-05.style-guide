# Style Audit — os_numerical

- **Series:** lecture-dp
- **File:** `lectures/os_numerical.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Systemic Title Case in H2/H3 headings. |
| Math         | 7/10  | Mostly clean. |
| Code         | 8/10  | Unicode Greek; no pip install needed; PEP8; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Three `ax.set_title(...)` calls — all Title Case. |
| References   | N/A   | No `{cite}` directives. |
| Links        | 9/10  | `{doc}` used 6×; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `solution-start` with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Systemic Title Case in H2/H3 headings. *Examples:* `## Reviewing the Model` (55), `## Value Function Iteration` (86), `### The Bellman Operator` (106), `### Fitted Value Function Iteration` (125), `### Implementation` (156), `### Policy Function` (411). *Count:* 6 headings.

### Medium severity
- **[qe-fig-003]** — Three `ax.set_title(...)` calls. *Lines:* 309 ('Value function iterations'), 365 ('Value function'), 384 ('Comparison between analytical and numerical value functions').

### Low severity
- **[qe-writing-001]** — A couple of multi-sentence paragraphs (e.g. 26-29, 31-32).

## Strengths
- Lecture title in correct Title Case.
- Equation labels and `{eq}` references used consistently.
- Definitions bolded correctly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- "IID" / Greek-letter conventions consistent.
- Unicode Greek in code.
- `{doc}` used for cross-series.
- Exercise uses `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Convert H2/H3 headings to sentence case.
2. Remove the 3 `ax.set_title(...)` calls.
