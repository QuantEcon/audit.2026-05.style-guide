# Style Audit — chang_ramsey

- **Series:** lecture-dp
- **File:** `lectures/chang_ramsey.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.5 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | All H2/H3 sentence case. |
| Math         | 7/10  | `\vec` used heavily; otherwise clean. |
| Code         | 5/10  | Installs `polytope cvxopt` (binary, non-Anaconda) without notes; figsize 5×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Two `fig.suptitle(...)` calls; Title-Case axis labels; figsize 5×. |
| References   | 5/10  | Three narrative-author `{cite}` patterns. |
| Links        | 9/10  | `{doc}` used throughout; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-006]** — `!pip install polytope cvxopt` (line 29) — both binary scientific-Python packages, no installation notes.

### Medium severity
- **[qe-math-004]** — `\vec z`, `\vec h`, `\vec M`, `\vec q`, `\vec m`, `\vec x`, `\vec c`, `\vec y` used extensively. *Count:* 30+ occurrences.
- **[qe-ref-001]** — Three narrative-author `{cite}` patterns. Should be `{cite:t}`.
- **[qe-fig-003]** — Two `fig.suptitle(rf"$\beta = {model.β}$", ...)` calls. *Lines:* 1069, 1122.
- **[qe-fig-001]** — `figsize=` set 5 times.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs.
- **[qe-writing-009 (proposed)]** — Smart quotes ’ used occasionally.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case.
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent; Unicode Greek in code.
- No transpose, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; `{doc}` used for cross-series.

## Recommended actions
1. Add a note about `polytope`/`cvxopt` package binary install requirements.
2. Remove `\vec` arrows on sequence symbols.
3. Switch narrative `Author {cite}…` to `{cite:t}` form.
4. Remove the two `fig.suptitle(...)` calls.
5. Reduce unnecessary `figsize=` usage.
6. Tighten compound paragraphs.
