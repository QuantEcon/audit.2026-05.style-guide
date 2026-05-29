# un_insure

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/un_insure.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 7.5/10 | One bare `E` for expectation; otherwise clean. |
| Code         | 8/10  | Unicode Greek used (4 occurrences); no install cell (scipy/numpy only — OK). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 1 `figsize=`; no `:name:` fields. |
| References   | 8/10  | 9 `{cite}` used; never `{cite:t}`. |
| Links        | 9/10  | No cross-series URL links; self-contained. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-math-010 (proposed)]** — Bare `E` for expectation. *Example:* `lectures/un_insure.md:34`. *Count:* 1 occurrence.
- A stray `%\EQN hugo1` comment at L36 is harmless but should be removed.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- All primes are derivatives (`C'`, `p'`) — no qe-math-002 violation.
- Sequences in curly brackets (qe-math-005) at L30.
- One-sentence paragraph rule rigorously respected (qe-writing-001).
- Equation labels via `$$ ... $$ (label)` (qe-math-007).
- Unicode Greek used in code (qe-code-002).

## Recommended actions
1. Replace bare `E` with `\mathbb{E}` (qe-math-010, proposed).
2. Remove leftover TeX comment `%\EQN hugo1` (cosmetic).
3. Add `:name: fig-...` fields (qe-fig-005).
