# Style Audit — markov_chains_II

- **Series:** lecture-python-intro
- **File:** `lectures/markov_chains_II.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; one-sentence paragraphs throughout. |
| Math         | 9/10  | `\mathbb{1}` used as indicator (M3-style usage); bmatrix; sequences `\{X_t\}`. |
| Code         | 9/10  | `!pip install quantecon` at top with `hide-output` (qe-code-003 OK); unicode Greek used. |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `figsize=` / `ax.set_title` violations; no `{figure}` directives. |
| References   | 7/10  | 4 `{cite}` usages; 2 are in-text ("see Chapter 4 of {cite}", "Theorem 5.2 of {cite}") — should be `{cite:t}`. |
| Links        | 9/10  | `{doc}` cross-references used (3 occurrences). |
| Admonitions  | 9/10  | `{prf:theorem}` × 5 used (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-ref-001]** — In-text citations should use `{cite:t}`. *Examples:* `lectures/markov_chains_II.md:158` ("see Chapter 4 of {cite}\`sargent2023economic\`"), 159 ("Theorem 5.2 of {cite}\`haggstrom2002finite\`"). *Count:* 2 occurrences.

### Low severity
- **W1** — A few two-sentence paragraphs (e.g. lines 39–44).

## Strengths
- `\mathbb{1}` used for indicator and explained (M3 OK).
- Bold for definitions (**accessible**, **reachable**, **communicate**, **irreducible**, **ergodicity**).
- Section headings sentence case (W3 OK).
- IID written correctly (line 202).
- `prf:theorem`, `prf:example` directives used for structure (qe-admon-004 OK).
- `quantecon` install at top with `hide-output` (qe-code-003 OK).
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert in-text `{cite}` on lines 158, 159 to `{cite:t}` form.
