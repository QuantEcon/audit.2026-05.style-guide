# Style Audit — ifp_discrete

- **Series:** lecture-dp
- **File:** `lectures/ifp_discrete.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Several Title Case H2/H3 ("Set Up", "Asset Dynamics"). |
| Math         | 8/10  | One parenthesised sequence; `\mathsf` for state-space; otherwise clean. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; no figsize. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 9/10  | No matplotlib titles; lowercase labels; no figsize. |
| References   | 9/10  | 3 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | One `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `{solution-start}` with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Title Case in H2/H3 headings: `## Set Up` (87), `### Asset Dynamics` (353).
- **[qe-math-005]** — Sequence written with parentheses `(y_t)_{t \geq 0}` rather than curly brackets (line 106).

### Low severity
- **[qe-writing-004]** — `\mathsf Y` and `\mathsf S` used for state spaces (lines 106, 110); prefer plain letters.

## Strengths
- Lecture title in correct Title Case.
- Definitions bolded correctly ("**income fluctuation problem**", "**household problem**", "**value function**").
- `\mathbb{E}` used (line 92, 118).
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top.
- Exercise uses `{exercise}` + `{solution-start}` with `:class: dropdown` and labels.

## Recommended actions
1. Convert "Set Up" → "Set up", "Asset Dynamics" → "Asset dynamics".
2. Switch `(y_t)_{t \geq 0}` to `\{y_t\}_{t \geq 0}` (line 106).
3. Optionally drop `\mathsf` styling on state-space symbols.
