# dovis_accounting_mf

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/dovis_accounting_mf.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×3; `qe-writing-006` ×1; `qe-writing-009` (proposed) ×1, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×17; `qe-math-002` ×11; `qe-math-011` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×9; `qe-fig-007` ×2; `qe-fig-005` ×2, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 504, 604, 1226, 1618, 1976, 2132, 2166. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 9. *Lines:* 1619, 1624, 1628, 1641, 1646, 1650, 1654, 1658, 1663. *Example:* .suptitle.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 1623, 1627, 1631, 1632, 1645, 1649, 1653, 1657, 1662. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 11. *Lines:* 693, 694, 695, 740, 746, 752, 753. *Example:* apostrophe transpose `i_1'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 17. *Lines:* 132, 137, 193, 207, 314, 323, 331, 360, 363, 383, …. *Example:* non-blackboard `\Pr`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 680. *Example:* H2 Title Case: 'The full model with Gumbel shocks' (Gumbel).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 2116, 2165. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 2. *Lines:* 666, 667. *Example:* spine removal.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 1775. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 2054, 2062, 2074. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 272. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 688. *Example:* i.i.d..


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (2 parenthetical, 29 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (17 occurrences).
2. `qe-math-002` — Use \top for transpose notation (11 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (9 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
5. `qe-fig-007` — Keep figure box and spines (2 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
7. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
