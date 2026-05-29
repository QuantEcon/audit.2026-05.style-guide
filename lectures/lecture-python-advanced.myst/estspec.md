# Style Audit — estspec

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/estspec.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | One-sentence paragraphs throughout; sentence-case headings; title in Title Case. |
| Math         | 8/10  | Clean math; sequences in curly braces. |
| Code         | 6/10  | 7 spelled Greek; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 5/10  | 1 `ax.set_title`; 3 `figsize=`; 3 `{figure}` static images; no `:name:` fields. |
| References   | 8/10  | 1 `{cite}` used; never `{cite:t}`. |
| Links        | 9/10  | No cross-series URL links; self-contained. |
| Admonitions  | 8/10  | 2 gated exercises and 2 solutions with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-002]** — 3 `{figure}` directives reference static PNGs (`periodogram1.png`, `window_smoothing.png`, `ar_smoothed_periodogram.png`); could be code-generated.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.

### Low severity
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 3 `figsize=` settings.
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, etc.) in code parameters (7 occurrences).

## Strengths
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- Sequences in curly brackets `\{X_t\}`, `\{\epsilon_t\}` (qe-math-005).
- Equation labels with `{math}` `:label:` and `{eq}` references (qe-math-007).
- No bold for vectors/matrices; no `\tag`; no `align` inside `$$`.
- Exercises gated (qe-admon-001); solutions use `:class: dropdown` (qe-admon-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Code-generate the periodogram figures (qe-fig-002).
2. Remove `ax.set_title` call (qe-fig-003).
3. Add `:name: fig-...` fields (qe-fig-005).
4. Convert spelled Greek to unicode (qe-code-002).
