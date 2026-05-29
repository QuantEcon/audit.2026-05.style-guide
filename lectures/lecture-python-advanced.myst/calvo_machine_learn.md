# Style Audit — calvo_machine_learn

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/calvo_machine_learn.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 2/10  | Systemic `^T` for transpose; bold `\mathbf{I}` for identity. |
| Code         | 8/10  | Strong unicode Greek use (46 occurrences); 3 install cells with `hide-output`. |
| JAX          | N/A   | Imports `jax` but is out-of-scope per instructions. |
| Figures      | 8/10  | No `figsize=`; no `ax.set_title`; many figures present. |
| References   | 8/10  | 8 `{cite}` used; never `{cite:t}`. |
| Links        | 9/10  | 15 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — `^T` used systematically as transpose. *Example:* `lectures/calvo_machine_learn.md:860`, `:862`, `:865`, `:867`, `:870`, `:879`-`881`. *Count:* ~23 occurrences.
- **[qe-math-004]** — Bold `\mathbf{I}` used for the identity matrix. *Example:* `lectures/calvo_machine_learn.md:865`, `:867`, `:870`, `:872`. *Count:* 4 occurrences.

### Medium severity
_None found._

### Low severity
- **[qe-writing-005]** — `**machine learning**`, `**Ramsey**` bold-as-keyword use is borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006); sentence-case headings (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003).
- Clean equation labels.
- Heavy unicode Greek usage in code (qe-code-002) — exemplary.
- Heavy `{doc}` use for cross-series references (qe-link-002).
- Install cells at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `^T` with `^\top` throughout (qe-math-002).
2. Replace `\mathbf{I}` with plain `I` (qe-math-004).
3. Add `:name: fig-...` fields to figures (qe-fig-005).
