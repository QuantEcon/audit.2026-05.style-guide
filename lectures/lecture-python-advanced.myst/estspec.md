# estspec

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/estspec.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-001` ×2; `qe-writing-008` ×4. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×7; `qe-fig-006` ×2; `qe-fig-003` ×1, +3 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 223, 243, 299, 338, 458, 487, 535. *Example:* {figure} without :name:.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 306, 495, 540. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 243, 338, 458. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 308. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 309, 310. *Example:* axis label `Weights`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 323, 444. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 321, 323, 329, 404. *Example:* 2 spaces.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 307. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 51. *Example:* {cite} in narrative flow: 'see {cite}`'.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-fig-006` — Lowercase axis labels (2 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (4 occurrences).
7. `qe-fig-002` — Prefer code-generated figures (3 occurrences).
