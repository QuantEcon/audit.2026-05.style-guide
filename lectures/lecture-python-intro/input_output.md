# Style Audit — input_output

- **Series:** lecture-python-intro
- **File:** `lectures/input_output.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; clean one-sentence paragraphs. |
| Math         | 9/10  | `\top` for transpose consistently; bmatrix-style display; equation labels. |
| Code         | 8/10  | 3 `!pip install` commands at top (lines 23–25) under `:tags: [hide-output]` (line 21) — installing `quantecon_book_networks`, etc. |
| JAX          | out of scope | — |
| Figures      | 7/10  | One `figsize=` on line 89; one axis label "Output multipliers" (line 597) starts uppercase; no `set_title` violations. |
| References   | 8/10  | 2 `{cite}` usages, parenthetical, no in-text mis-use. |
| Links        | 9/10  | `{doc}` links used (3 occurrences). |
| Admonitions  | 9/10  | `{prf:theorem}` × 2 (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W1** — A few short two-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` on line 89. *Count:* 1 occurrence.
- **[qe-fig-006]** — Axis label "Output multipliers" (line 597) starts uppercase; should be lowercase.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Transpose `^\top` used consistently throughout (M2 OK).
- Equation labels and `{eq}` references used.
- Bold for definitions (**Leontief**, **conjugate pair**, **primal**, **dual**).
- `!pip install` block at top with `hide-output` (qe-code-003 OK).
- `{prf:theorem}` directives used (qe-admon-004 OK).
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions gated, dropdown, linked.

## Recommended actions
1. Lowercase axis label "Output multipliers" → "output multipliers".
2. Remove `figsize=` on line 89.
