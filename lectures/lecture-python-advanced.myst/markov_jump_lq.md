# Style Audit — markov_jump_lq

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/markov_jump_lq.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 5.7 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | Title in Title Case; sentence-case headings; some bolded labels. |
| Math         | 3.5/10 | Primes used systematically as transpose; bare `E`; "iid" usage. |
| Code         | 6/10  | Spelled Greek mixed with unicode (12 vs 6); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 4/10  | 6 `ax.set_title` calls (systemic); no `figsize=`; no `:name:` fields. |
| References   | 7/10  | 4 `{cite}` used; never `{cite:t}`. |
| Links        | 8/10  | 3 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Prime `'` used as transpose throughout. *Example:* `lectures/markov_jump_lq.md:81`, `:94`, `:108`, `:114`, `:115`, `:122`, `:128`. *Count:* ~25 occurrences.
- **[qe-fig-003]** — `ax.set_title` used in 6 cells — systemic. *Count:* 6 occurrences.

### Medium severity
- **[qe-math-010 (proposed)]** — Bare `E` for expectation. *Example:* `lectures/markov_jump_lq.md:94`. *Count:* 1 occurrence.
- **[qe-math-011 (proposed)]** — `\mathcal N` for Normal distribution. *Count:* 1 occurrence.
- **[qe-writing-009 (proposed)]** — "iid" used in narrative. *Count:* 1 occurrence.

### Low severity
- **[qe-writing-005]** — Heavy decorative bolding (e.g. `**linear quadratic dynamic programming problem**`).
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `'` with `^\top` for transpose throughout (qe-math-002).
2. Remove `ax.set_title` calls (qe-fig-003).
3. Replace bare `E` with `\mathbb{E}` (qe-math-010, proposed).
4. Replace `\mathcal N` with `N` (qe-math-011, proposed).
5. Replace "iid" with "IID" (qe-writing-009, proposed).
6. Add `:name: fig-...` fields (qe-fig-005).
