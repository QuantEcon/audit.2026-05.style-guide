# ross_recovery

- **Series:** lecture-python.myst
- **File:** `lectures/ross_recovery.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-004` ×9; `qe-writing-001` ×1. |
| Math         | 4/10  | `qe-math-010` (proposed) ×3; `qe-math-002` ×2; `qe-math-011` (proposed) ×1, +1 more. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×4; `qe-fig-004` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 795, 817, 849, 970, 1364. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 246, 454. *Example:* apostrophe transpose `U'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 485, 490. *Example:* bare expectation `E[`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 9. *Lines:* 69, 339, 495, 515, 656, 890, 928, 1056, 1106. *Example:* mid-sentence 'Theorem'.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 916, 917. *Example:* spelled-out `rho`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 801, 807, 869, 875. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 782, 813, 845, 1339. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 1179. *Example:* pmatrix environment.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 561. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1198. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 945. *Example:* caption of 9 words.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 10 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
2. `qe-math-002` — Use \top for transpose notation (2 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (9 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
7. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
