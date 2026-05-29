# rob_markov_perf

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/rob_markov_perf.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 4/10  | Primes used as transpose; one `pmatrix`. |
| Code         | 5/10  | Heavy spelled Greek (22 occurrences); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 3 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 2 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 3 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Prime `'` used systematically as transpose. *Example:* `\Gamma_{it} := W_i' - M_i' F_{-it}`, `B_i' P A`, `x_t' R x_t`. *Count:* ~27 occurrences.
- **[qe-code-002]** — Spelled-out Greek heavily used (22 occurrences).

### Medium severity
- **[qe-math-003]** — `\begin{pmatrix}` used instead of `\begin{bmatrix}`. *Example:* `lectures/rob_markov_perf.md:778`. *Count:* 1 occurrence.

### Low severity
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — 3 `figsize=` settings.

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- `\begin{bmatrix}` used elsewhere (qe-math-003).
- One-sentence paragraph rule respected (qe-writing-001).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace prime `'` with `^\top` for transpose throughout (qe-math-002).
2. Convert the `pmatrix` to `bmatrix` (qe-math-003).
3. Convert spelled Greek to unicode in code (qe-code-002).
4. Add `:name: fig-...` fields (qe-fig-005).
