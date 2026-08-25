# markov_asset

- **Series:** lecture-python.myst
- **File:** `lectures/markov_asset.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×18; `qe-writing-008` ×32; `qe-writing-001` ×1. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×19; `qe-math-002` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×1; `qe-fig-008` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 313, 403, 617, 863, 1027, 1113. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 377. *Example:* apostrophe transpose `)'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 19. *Lines:* 110, 115, 117, 133, 155, 163, 170, 188, 292, 346, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 18. *Lines:* 94, 119, 148, 177, 193, 206, 237, 270, 333, 433, …. *Example:* H3 Title Case: 'Risk-Neutral Pricing' (Pricing).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 32. *Lines:* 56, 136, 140, 166, 168, 171, 202, 204, 341, 385, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 629. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 1029, 1030, 1117. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 175, 472. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 126, 127. *Example:* {cite} in author position: '{cite}`HarrisonKreps1979` and'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1079. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (18 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (19 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
5. `qe-ref-001` — Use correct citation style (2 occurrences).
6. `qe-math-002` — Use \top for transpose notation (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (32 occurrences).
