# Style Audit — organization_capital

- **Series:** lecture-python.myst
- **File:** `lectures/organization_capital.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.4 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | Uses "i.i.d." or "iid" in text rather than "IID". |
| Math         | 9.5/10 | Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=11, uni=19). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 10 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | N/A | No external links. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — `figsize=` set in 10 places — usually unnecessary (defaults from `_config.yml`).

### Low severity
- **[qe-writing-009 (proposed)]** — Uses "i.i.d." or "iid" in text rather than "IID". *Example:* line 647.
- **[qe-math-010 (proposed)]** — Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`. *Example:* line 258.
- **[qe-code-002]** — Mixed Greek conventions in code (word=11, uni=19).

## Strengths
- Headings use sentence case consistently.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.
- Figures use descriptive `name:` fields for cross-referencing.

## Recommended actions
1. Address `qe-fig-001`: `figsize=` set in 10 places — usually unnecessary (defaults from `_config.yml`).
2. Address `qe-writing-009 (proposed)`: Uses "i.i.d." or "iid" in text rather than "IID".
3. Address `qe-math-010 (proposed)`: Bare `E[...]` or `\Pr(...)` used in place of `\mathbb{E}`/`\mathbb{P}`.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=11, uni=19).
