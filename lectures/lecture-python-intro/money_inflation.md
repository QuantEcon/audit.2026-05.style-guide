# money_inflation

- **Series:** lecture-python-intro
- **File:** `lectures/money_inflation.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | H1 Title Case OK; H2/H3 sentence case; double-space in "Two  computation strategies". |
| Math         | 8/10  | Sequences `\{p_t\}_{t=0}^\infty` (M6 OK); equation labels; clean. |
| Code         | 8/10  | Unicode Greek used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 328, 525, 889; 3 `ax.set_title(...)` inside solution blocks (OK by exception). |
| References   | 7/10  | 1 `{cite}` usage (parenthetical, OK). |
| Links        | 9/10  | `{doc}` cross-references used (8 occurrences). |
| Admonitions  | 9/10  | `{prf:example}` × 3 used (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Several multi-sentence paragraphs in Overview (lines 21–29, 31–43).
- **[qe-fig-001]** — `figsize=` overrides on lines 328, 525, 889. *Count:* 3 occurrences.

### Low severity
- **W7** — Word emphasis via inline italics with asterisks: `demand*s*`, `suppl*ies*` (line 73) — creative emphasis.
- **W7** — Typo "simulataneously" (line 129).
- **W2** — Extra spaces in H2 "## Two  computation strategies" (line 354).
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Sequences use `\{p_t\}_{t=0}^\infty` (M6 OK).
- Equation labels and `{eq}` references throughout.
- Bold for definitions (**inflation tax**, **Laffer curve**, **real balances**, **equilibrium**).
- `{doc}` cross-references used (qe-link-002 OK).
- `{prf:example}` directives (qe-admon-004 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Split multi-sentence Overview paragraphs.
2. Fix typo "simulataneously" → "simultaneously".
3. Trim double-spaces in H2.
4. Remove `figsize=` overrides.
