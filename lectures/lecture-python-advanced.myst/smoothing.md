# Style Audit — smoothing

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/smoothing.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 6/10  | Mixed `E_t` and `\mathbb E_t`; primes used as transpose. |
| Code         | 7/10  | Mixed unicode/spelled Greek (4 spelled vs 3 unicode); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 2 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 4 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 2 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-002]** — Prime `'` used as transpose in several formulas. *Example:* `lectures/smoothing.md:190`. *Count:* ~10 occurrences (mixed with derivative `u'`).
- **[qe-math-010 (proposed)]** — Bare `E_t` mixed with `\mathbb E_t`. *Example:* `lectures/smoothing.md:190`, `:196`, `:199`. *Count:* ~3 occurrences (vs ~12 correct).
- **[qe-math-011 (proposed)]** — `\mathcal N` for Normal distribution. *Count:* 1 occurrence.

### Low severity
- **[qe-writing-005]** — `**complete markets**`, `**incomplete markets**` borderline definitional bold.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- One-sentence paragraph rule respected (qe-writing-001).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Standardise on `\mathbb{E}_t` (qe-math-010, proposed).
2. Replace prime `'` with `^\top` for transpose where it denotes transpose (qe-math-002).
3. Replace `\mathcal N` with `N` (qe-math-011, proposed).
4. Add `:name: fig-...` fields (qe-fig-005).
