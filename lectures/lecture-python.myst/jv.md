# jv

- **Series:** lecture-python.myst
- **File:** `lectures/jv.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×3; `qe-writing-001` ×1; `qe-writing-008` ×3. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×3; `qe-fig-003` ×1; `qe-fig-008` ×4, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 59, 144, 380. *Example:* H3 Title Case: 'Model Features' (Features).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 402, 500, 569. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 406. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 398, 469, 561. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 405, 507, 508, 571. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 182. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 72, 83, 182. *Example:* 2 spaces.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 45. *Example:* {cite} in narrative flow: 'and {cite}`'.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
4. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (4 occurrences).
