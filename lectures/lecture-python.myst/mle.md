# mle

- **Series:** lecture-python.myst
- **File:** `lectures/mle.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-004` ×2; `qe-writing-001` ×1. |
| Math         | 3/10  | `qe-math-002` ×19; `qe-math-004` ×106. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-006` ×4; `qe-fig-001` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 130, 180, 232, 301, 418, 628, 827. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 127, 175, 217, 415, 624, 800. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 19. *Lines:* 207, 465, 871, 900, 901, 918, 919, 926, 927, 929, …. *Example:* apostrophe transpose `i'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 106. *Lines:* 195, 202, 207, 212, 215, 257, 264, 267, 276, 278, …. *Example:* \mathbf.

### Medium severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 184, 185, 829, 830. *Example:* axis label `Number of billionaires in 2008`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 136, 239, 635. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 740. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 844. *Example:* mid-sentence 'Likelihood'.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (19 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (106 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
5. `qe-fig-006` — Lowercase axis labels (4 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (7 occurrences).
