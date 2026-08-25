# rosen_schooling_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/rosen_schooling_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-001` ×2; `qe-writing-008` ×3. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×4; `qe-fig-008` ×14, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 14. *Lines:* 294, 295, 299, 300, 312, 313, 314, 318, 319, 320, …. *Example:* plot() without lw=.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 293, 311, 425, 519. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 297, 302, 316, 322. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 292, 310, 390, 485. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 383, 447. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 29, 136, 332. *Example:* 2 spaces.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 27. *Example:* {cite} in narrative flow: '{cite}`'.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (14 occurrences).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (4 occurrences).
