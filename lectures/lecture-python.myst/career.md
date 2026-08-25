# career

- **Series:** lecture-python.myst
- **File:** `lectures/career.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-006` ×1; `qe-writing-008` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×6; `qe-fig-001` ×5; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 175, 320, 337, 424, 547. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 170, 313, 336, 373, 396, 542. *Example:* {image} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 64. *Example:* H3 Title Case: 'Model Features' (Features).

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 178, 429, 430. *Example:* plot() without lw=.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 373. *Example:* static image .png.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 74. *Example:* 2 spaces.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
3. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
4. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
6. `qe-fig-002` — Prefer code-generated figures (1 occurrence).
