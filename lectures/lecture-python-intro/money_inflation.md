# money_inflation

- **Series:** lecture-python-intro
- **File:** `lectures/money_inflation.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-008` ×90; `qe-writing-004` ×1; `qe-writing-001` ×1. |
| Math         | 8/10  | `qe-math-001` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×3; `qe-fig-004` ×3; `qe-fig-008` ×10, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 329, 535, 538, 905, 908, 912, 1048, 1121, 1122, 1209. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 90. *Lines:* 35, 36, 43, 50, 54, 60, 78, 80, 81, 96, …. *Example:* 3 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 262, 328, 525, 889. *Example:* style override.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 313, 557, 930. *Example:* caption of 32 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 1038, 1108, 1203. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 446. *Example:* LaTeX `\gamma` outside math delimiters.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 410. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 1180. *Example:* mid-sentence 'Method'.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
3. `qe-fig-004` — Caption formatting conventions (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (90 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
