# lp_intro

- **Series:** lecture-python-intro
- **File:** `lectures/lp_intro.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×3; `qe-writing-001` ×4; `qe-writing-008` ×36. |
| Math         | 6.5/10 | `qe-math-002` ×9. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 9. *Lines:* 287, 305, 380, 562, 564, 598, 637. *Example:* apostrophe transpose `c'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 36. *Lines:* 27, 31, 70, 80, 160, 166, 168, 170, 172, 176, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 118, 119, 132. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 193, 200, 208, 419. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 240, 405, 513. *Example:* mid-sentence 'Example'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 109. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (9 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (3 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (36 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
