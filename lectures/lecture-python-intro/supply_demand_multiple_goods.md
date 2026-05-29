# Style Audit — supply_demand_multiple_goods

- **Series:** lecture-python-intro
- **File:** `lectures/supply_demand_multiple_goods.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; one-sentence paragraphs throughout. |
| Math         | 9/10  | `\top` for transpose consistently; equation labels; clean. |
| Code         | 7/10  | `beta = ...` spelled-out in variable assignments (lines 368, 371, 373) instead of unicode `β`; `numpy`, `scipy` standard imports otherwise. |
| JAX          | out of scope | — |
| Figures      | N/A   | no matplotlib usage |
| References   | N/A   | no `{cite}` citations |
| Links        | 9/10  | `{doc}` link present (1 occurrence). |
| Admonitions  | 9/10  | 1 solution gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-002]** — `beta = 0.95` and many uses of `beta` as a variable (lines 368, 371, 373, etc.) — should be unicode `β` per series convention. *Count:* 14 spelled-out occurrences.

### Low severity
- **W1** — Occasional two-sentence paragraphs.

## Strengths
- Transpose `^\top` consistently used (M2 OK).
- Equation labels via `(label)` form (M14 OK).
- Section headings sentence case (W3 OK).
- Bold for definitions (**first welfare theorem**, **second welfare theorem**, **Marshallian**).
- `{doc}` cross-reference used (qe-link-002 OK).
- Solution gated, dropdown, linked.

## Recommended actions
1. Replace spelled-out `beta` with unicode `β` in code per qe-code-002.
