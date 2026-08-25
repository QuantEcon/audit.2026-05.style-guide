# olg_adaptive_money

- **Series:** lecture-python.myst
- **File:** `lectures/olg_adaptive_money.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-004` ×2; `qe-writing-006` ×1. |
| Math         | 6/10  | `qe-math-002` ×2; `qe-math-010` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×3; `qe-fig-003` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 410, 564, 702, 1018, 1072, 1285, 1348. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 186, 291. *Example:* apostrophe transpose `u'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 164. *Example:* non-blackboard `\operatorname{Prob}`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1104. *Example:* H3 Title Case: 'From escape dynamics to the *Conquest of American Inflation*' (Conquest, Inflation).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 419. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 695, 996, 1046. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1284, 1341. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 577, 1352. *Example:* plot() without lw=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 91, 874. *Example:* mid-sentence 'Inflation'.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 23 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-fig-004` — Caption formatting conventions (3 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
7. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
