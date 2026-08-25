# solow

- **Series:** lecture-python-intro
- **File:** `lectures/solow.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-004` ×1; `qe-writing-001` ×1; `qe-writing-008` ×6. |
| Math         | 8.5/10 | `qe-math-005` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-008` ×10; `qe-fig-001` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 136, 233, 333, 484, 605. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 156, 248, 250, 339, 340, 345, 493, 502, 503, 615. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 70, 94, 103, 275, 296, 316. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 237, 338, 488, 607. *Example:* figsize=.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 2. *Lines:* 108, 556. *Example:* parenthesised sequence.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 316. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 536. *Example:* mid-sentence 'Rule'.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
2. `qe-math-005` — Use curly brackets for sequences (2 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (6 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
