# calvo

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/calvo.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 8/10  | Few transpose primes; otherwise clean. |
| Code         | 7/10  | Mixed unicode/spelled Greek; 2 install cells with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `ax.set_title` calls; 5 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 16 `{cite}` used; never `{cite:t}`. |
| Links        | 6/10  | Several raw `python-intro.quantecon.org` URLs alongside heavy `{doc}` use. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — Multiple raw `python-intro.quantecon.org/lqcontrol.html` and `markov_perf.html` URLs. *Example:* `lectures/calvo.md:67`, `:193`, `:288`, `:765`. *Count:* 4 occurrences.
- **[qe-fig-003]** — `ax.set_title` used in 2 cells.

### Low severity
- **[qe-math-002]** — A handful of primes used as transpose. *Count:* ~7 occurrences (most primes here are next-period notation).
- **[qe-writing-005]** — `**time inconsistency**`, `**Ramsey plan**`, `**machine learning**` bold-as-keyword use is borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 5 `figsize=` settings.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code (15 spelled vs 11 unicode).

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case section headings (qe-writing-006) — e.g. "Model components", "Friedman's optimal rate of deflation".
- `\begin{bmatrix}` used; no `array` or `pmatrix` violations.
- Equation labels and `{eq}` references used consistently (qe-math-007).
- One-sentence paragraph rule respected (qe-writing-001).
- Heavy `{doc}` cross-series linking (9 occurrences).
- Install cells at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert raw `python-intro.quantecon.org` URLs to `{doc}\`intermediate:lqcontrol\`` etc. (qe-link-002).
2. Review remaining `'` occurrences and substitute `^\top` where the prime denotes transpose (qe-math-002).
3. Remove `ax.set_title` calls (qe-fig-003).
4. Add `:name: fig-...` fields to figures (qe-fig-005).
