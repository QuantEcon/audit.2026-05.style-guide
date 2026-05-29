# schelling

- **Series:** lecture-python-intro
- **File:** `lectures/schelling.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; "### Set-Up" is Title Case where sentence case expected. |
| Math         | N/A   | no math content beyond simple coordinate references |
| Code         | 8/10  | Standard Anaconda imports only. |
| JAX          | out of scope | — |
| Figures      | 6/10  | 1 `ax.set_title(f'Cycle {cycle_num-1}')` on line 250 outside exercise context; 1 `ax.set_title` inside solution block (OK). |
| References   | 8/10  | 1 `{cite}` (parenthetical, OK). |
| Links        | 6/10  | Cross-series direct URL on line 154 (`python-programming.quantecon.org/python_oop.html`). |
| Admonitions  | 9/10  | `{prf:example}` used (qe-admon-004 OK); 1 solution gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W3** — "### Set-Up" (line 79) uses Title Case; should be "### Set-up" or "### Setup".
- **[qe-fig-003]** — `ax.set_title(f'Cycle {cycle_num-1}')` on line 250 outside exercise context. *Count:* 1 occurrence.
- **[qe-link-002]** — Cross-series link uses direct URL. *Example:* `lectures/schelling.md:154` (`[objects](https://python-programming.quantecon.org/python_oop.html)`). Should be `{doc}\`programming:python_oop\``.

### Low severity
- **W1** — Several two-sentence paragraphs (e.g. lines 33–35, 47–48).
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- H1 Title Case OK; most H2/H3 sentence case.
- Clear prose, one-sentence paragraph style mostly maintained.
- Bold for definitions ("**unit square**").
- `{prf:example}` directive (qe-admon-004 OK).
- Solution gated, dropdown, linked.

## Recommended actions
1. Change "Set-Up" → "Set-up" per W3.
2. Move `set_title` on line 250 to mystnb/figure metadata.
3. Replace direct URL on line 154 with `{doc}\`programming:python_oop\``.
4. Split a few multi-sentence paragraphs.
