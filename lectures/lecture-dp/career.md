# career

- **Series:** lecture-dp
- **File:** `lectures/career.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | "Model Features" H3 Title Case. |
| Math         | 8/10  | `\nonumber` inside aligned; otherwise clean. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 5×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | One static PNG figure; figsize 5×; no embedded titles. |
| References   | 8/10  | "Derek Neal {cite}…" — narrative-author misuse; otherwise clean. |
| Links        | 9/10  | No raw cross-series URLs. |
| Admonitions  | 9/10  | Excellent use of `exercise-start`/`exercise-end`/`solution-start` with labels and dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — H3 heading `### Model Features` (60) in Title Case.
- **[qe-fig-002]** — Static PNG figure `career_solutions_ex1_py.png` used as expected output of an exercise (line 372). Prefer code-generated figures.
- **[qe-fig-001]** — `figsize=` set 5 times.
- **[qe-ref-001]** — Narrative-author citation "Derek Neal {cite}`Neal1999`" (line 43). Should be `{cite:t}`.

### Low severity
- **[qe-math-001]** — `\nonumber` used inside `aligned` (lines 123-124); it has no effect outside numbered `align*` and clutters source.
- **[qe-writing-001]** — A couple of multi-sentence paragraphs.

## Strengths
- Lecture title correctly Title Case.
- `\mathbb{E}` used (line 101).
- Most H2/H3 headings sentence case ("Overview", "Model", "Implementation", "Exercises").
- Equation labels with `{eq}` references used cleanly.
- No transpose violations, no bold vectors, no align-inside-`$$` issues, no `i.i.d.`.
- pip install at top; Unicode Greek in code (`θ`, `ϵ`, `β`).
- Exercises use `exercise-start`/`exercise-end` with `:label:` and `{image}` directive properly nested.
- Solutions use `:class: dropdown`.

## Recommended actions
1. Rename `### Model Features` → `### Model features`.
2. Remove `\nonumber` tokens from the `aligned` block (lines 123-124).
3. Switch "Derek Neal {cite}`Neal1999`" to `{cite:t}` form.
4. Regenerate the static PNG figure from code.
