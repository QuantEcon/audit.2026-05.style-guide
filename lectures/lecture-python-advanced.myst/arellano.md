# arellano

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/arellano.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Sentence-case headings; clean one-sentence paragraphs throughout. |
| Math         | 9/10  | Clean LaTeX; primes are next-period notation, not transpose. |
| Code         | 8/10  | Unicode Greek used in many places (`β`, `α`); `numba` `@jit`/`jitclass` used; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | `ax.set_title` used twice (L722, L746) — Title Case caption embedded; 4 `figsize=`; 4 `{figure}` static images. |
| References   | 8/10  | 4 `{cite}` used; no `{cite:t}` despite occasional narrative author references. |
| Links        | 9/10  | No cross-series links — self-contained. |
| Admonitions  | 8/10  | 1 exercise with gated start, 1 solution with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title("Bond price schedule ...")` and `ax.set_title("Value Functions")` embed titles in matplotlib. *Example:* `lectures/arellano.md:722`, `:746`. *Count:* 2 occurrences (one in Title Case).

### Medium severity
- **[qe-fig-002]** — 4 `{figure}` directives reference static PNGs which could be code-generated.

### Low severity
- **[qe-math-008]** — `\mathbb 1` (L274) used for the indicator function — convention is `\mathbb{1}`; should briefly explain the symbol per qe-math-008 guidance.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-006]** — Embedded `ax.set_title("Value Functions")` uses Title Case (also covered by qe-fig-003).

## Strengths
- `\mathbb E` used for expectation (qe-math-010, proposed) at L101.
- Primes `'` are used as next-period notation; convention explicitly stated at L148.
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- Equation labels and `{eq}` references (qe-math-007).
- One-sentence paragraph rule rigorously followed (qe-writing-001).
- Exercise gated (qe-admon-001); solution has `:class: dropdown` (qe-admon-002).
- Unicode Greek widely used in code (qe-code-002).

## Recommended actions
1. Remove `ax.set_title()` calls; move titles into `mystnb` figure metadata (qe-fig-003).
2. Replace static `{figure}` references with code-generated equivalents where feasible (qe-fig-002).
3. Add a brief gloss for `\mathbb 1` indicator (qe-math-008).
4. Add `:name: fig-...` fields to figures (qe-fig-005).
