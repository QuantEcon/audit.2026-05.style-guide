# risk_aversion_or_mistaken_beliefs

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/risk_aversion_or_mistaken_beliefs.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×2; `qe-writing-009` (proposed) ×1; `qe-writing-008` ×5. |
| Math         | 3/10  | `qe-math-010` (proposed) ×34; `qe-math-011` (proposed) ×18. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3.5/10 | `qe-fig-006` ×19; `qe-fig-005` ×12; `qe-fig-004` ×2, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 10. *Lines:* 196, 549, 603, 657, 758, 1112, 1527, 1572, 1618, 1704. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 12. *Lines:* 188, 278, 539, 594, 646, 756, 885, 1096, 1193, 1503, …. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 19. *Lines:* 212, 213, 214, 554, 555, 612, 662, 663, 776, 1116, …. *Example:* axis label `Density`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 34. *Lines:* 150, 152, 290, 832, 856, 870, 876, 909, 912, 917, …. *Example:* bare expectation `E_t(`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 18. *Lines:* 104, 125, 137, 152, 164, 219, 223, 251, 329, 361, …. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 32, 52, 68, 704. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 278, 885, 1193. *Example:* static image .png.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 1605. *Example:* caption of 7 words.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 703, 1194. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 246. *Example:* i.i.d..


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 14 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (34 occurrences).
2. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (18 occurrences).
3. `qe-fig-006` — Lowercase axis labels (19 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (12 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
6. `qe-fig-004` — Caption formatting conventions (2 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (10 occurrences).
