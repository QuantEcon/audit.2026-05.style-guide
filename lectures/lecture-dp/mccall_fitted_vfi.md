# Style Audit — mccall_fitted_vfi

- **Series:** lecture-dp
- **File:** `lectures/mccall_fitted_vfi.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 8/10  | Two `\mathbf v` bold-vector usages; otherwise clean. |
| Code         | 7/10  | Unicode Greek; pip install at top; PEP8; figsize 5×. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 6/10  | Two `ax.set_title(...)` calls (one f-string); figsize 5×; lowercase labels. |
| References   | 10/10 | Single `{cite}` parenthetical. |
| Links        | 9/10  | `{doc}` used 6×; no raw cross-series URLs. |
| Admonitions  | 9/10  | Two `{exercise}` + `solution-start` with `:label:` and dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-004]** — `\mathbf v` used to denote a value-function array. *Lines:* 187, 188.
- **[qe-fig-003]** — Two embedded `ax.set_title(...)` (one f-string). *Lines:* 782, 867.
- **[qe-fig-001]** — `figsize=` set 5 times.

### Low severity
- **[qe-writing-001]** — A couple of multi-sentence paragraphs (e.g. 52-57, 64-67).

## Strengths
- Lecture title correctly Title Case.
- All H2/H3 sentence case.
- "IID" correctly capitalised.
- Equation labels and `{eq}` references used cleanly.
- No transpose violations; no `align` issues; no `\tag`.
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series; no raw URLs.
- Exercises use `{exercise}` + `solution-start`/`solution-end` with dropdown.

## Recommended actions
1. Drop the bold on `\mathbf v` (use plain `v`).
2. Remove the two `ax.set_title(...)` calls.
3. Reduce unnecessary `figsize=` usage.
4. Tighten the few multi-sentence paragraphs.
