# information_market_equilibrium

- **Series:** lecture-python.myst
- **File:** `lectures/information_market_equilibrium.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-009` (proposed) ×2; `qe-writing-001` ×1; `qe-writing-008` ×3. |
| Math         | 3.5/10 | `qe-math-010` (proposed) ×7; `qe-math-002` ×6. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×3; `qe-fig-001` ×9. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 595, 707, 1020, 1080, 1173, 1287, 1396, 1502, 1523. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 59, 61, 234, 235, 239, 245. *Example:* apostrophe transpose `y'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 7. *Lines:* 286, 373, 425, 472, 475, 1567. *Example:* non-blackboard `\mathcal{P}`.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 548, 702. *Example:* spelled-out `rho`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 1274, 1382, 1459. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1367. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 1368, 1372, 1457. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 2. *Lines:* 751, 757. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 9 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (7 occurrences).
2. `qe-math-002` — Use \top for transpose notation (6 occurrences).
3. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (9 occurrences).
