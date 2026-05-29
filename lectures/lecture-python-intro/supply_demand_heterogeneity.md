# Style Audit — supply_demand_heterogeneity

- **Series:** lecture-python-intro
- **File:** `lectures/supply_demand_heterogeneity.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case, H2/H3 sentence case OK, mostly one-sentence paragraphs. |
| Math         | 8/10  | Consistent `\top` for transpose; bmatrix; clean. |
| Code         | 8/10  | Standard `numpy` / `scipy` imports; `beta = ...` used as variable (qe-code-002 minor — consider unicode `β`). |
| JAX          | out of scope | — |
| Figures      | N/A   | no matplotlib usage |
| References   | N/A   | no `{cite}` citations |
| Links        | 9/10  | `{doc}` link present (1 occurrence). |
| Admonitions  | N/A   | no exercises / solutions |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W3** — "### Risk economy with arrow securities" (line 343) — "arrow" should be "Arrow" (proper noun: Arrow securities); minor.
- **W1** — A few two-sentence paragraphs (e.g. lines 113–117).
- **[qe-code-002]** — `beta = 0.95` (line 327) and subsequent usages use spelled-out `beta` instead of unicode `β`. *Count:* 3 occurrences.

## Strengths
- Transpose consistently uses `\top` (M2 compliant).
- Sentence-case section headings.
- One-sentence paragraph style maintained.
- IID not relevant here.
- `{doc}` cross-reference used (qe-link-002 OK).

## Recommended actions
1. Capitalize "Arrow" in the H3.
2. Replace spelled-out `beta` with unicode `β` per qe-code-002.
3. Minor paragraph splits.
