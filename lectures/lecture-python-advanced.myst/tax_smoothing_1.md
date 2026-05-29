# Style Audit — tax_smoothing_1

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_1.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.8 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; one-sentence paragraph rule mostly followed. |
| Math         | 5/10  | Bare `E_0`/`E_t`; `{\cal N}` for Normal distribution. |
| Code         | 8/10  | Mostly unicode Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | No `figsize=`; no `ax.set_title`; no `:name:` fields. |
| References   | 7/10  | 13 `{cite}` used; never `{cite:t}` despite some narrative refs. |
| Links        | 8/10  | 5 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-A1]** — Bare `E_0`/`E_t` instead of `\mathbb{E}_0` (carry-forward from v1 M7). *Example:* `lectures/tax_smoothing_1.md:70`, `:203`, `:354`, `:357`. *Count:* 4 occurrences.
- **[qe-math-A3]** — `{\cal N}` used as Normal distribution (carry-forward from v1 M9). *Example:* `lectures/tax_smoothing_1.md:220`. *Count:* 1 occurrence.

### Low severity
- **[qe-writing-001]** — Some two- to three-sentence paragraphs (e.g. L70).
- **[qe-writing-005]** — `**roll-over risk**` and other bolded labels are borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- `\begin{bmatrix}` used throughout (qe-math-003) at L234, L240, L279, L282, L444.
- Title "How to Pay for a War: Part 1" in Title Case (qe-writing-006).
- Section headings in sentence case (qe-writing-006).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `E_0`/`E_t` with `\mathbb{E}_0`/`\mathbb{E}_t` (qe-math-A1).
2. Replace `{\cal N}` with `N` (qe-math-A3).
3. Add `:name: fig-...` fields (qe-fig-005).
