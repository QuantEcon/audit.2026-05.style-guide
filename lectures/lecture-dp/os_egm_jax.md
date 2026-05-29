# Style Audit — os_egm_jax

- **Series:** lecture-dp
- **File:** `lectures/os_egm_jax.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Short clean H2 headings; sentence-case where present. |
| Math         | 9/10  | Minimal math; nothing violated. |
| Code         | 9/10  | Unicode Greek; no pip install needed (JAX assumed installed); uses `qe.Timer`. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 5/10  | One `ax.set_title('Optimal policies: CRRA utility approaching log case')`; one Title-Case `set_xlabel('State x')` + `set_ylabel('Consumption σ(x)')`. |
| References   | N/A   | No `{cite}` directives. |
| Links        | 9/10  | `{doc}` used 3×; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `solution-start` with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-003]** — `ax.set_title('Optimal policies: CRRA utility approaching log case')` (line 391).
- **[qe-fig-006]** — Title-Case axis labels `set_xlabel('State x')` and `set_ylabel('Consumption σ(x)')` (lines 388, 389).

### Low severity
_None found._

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- All H2 headings sentence case ("Overview", "Implementation", "Exercises").
- Mostly code-focused — minimal math, but what is there is clean.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align` issues.
- Unicode Greek in code; uses `qe.Timer()` (line 240).
- Exercise uses `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Remove the `ax.set_title(...)` call.
2. Lowercase the two axis labels (`'state x'`, `'consumption σ(x)'`).
