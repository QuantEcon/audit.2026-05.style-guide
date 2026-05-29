# dyn_stack

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/dyn_stack.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 5/10  | Primes used systematically as transpose. |
| Code         | 6/10  | 5 spelled Greek; 2 `quantecon` imports; install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 5/10  | 3 `ax.set_title` calls; 3 `figsize=`; no `:name:` fields. |
| References   | 7/10  | 2 `{cite}` used; narrative refs would benefit from `{cite:t}` or `{doc}`. |
| Links        | 6/10  | Two raw `python.quantecon.org` URLs (L42, L1411). |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Prime `'` used as transpose throughout. *Example:* `\check y_t' = ...`, `v(y_t) = - y_t' P y_t`. *Count:* ~19 occurrences.
- **[qe-fig-003]** — `ax.set_title` used in 3 cells.

### Medium severity
- **[qe-link-002]** — Raw cross-series URLs (`python.quantecon.org/lagrangian_lqdp.html`, `markov_perf.html`). *Example:* `lectures/dyn_stack.md:42`, `:1411`. *Count:* 2 occurrences.

### Low severity
- **[qe-writing-005]** — `**Stackelberg leader**`, `**Stackelberg follower**` borderline definitional bold.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 3 `figsize=` settings.
- **[qe-code-002]** — Spelled-out Greek in code parameters.

## Strengths
- `\begin{bmatrix}` used (qe-math-003).
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- Sequences in curly brackets (qe-math-005).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace prime `'` with `^\top` for transpose throughout (qe-math-002).
2. Remove `ax.set_title` calls (qe-fig-003).
3. Convert raw cross-series URLs to `{doc}\`intermediate:lagrangian_lqdp\`` (qe-link-002).
4. Add `:name: fig-...` fields (qe-fig-005).
