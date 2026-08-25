# complex_and_trig

- **Series:** lecture-python-intro
- **File:** `lectures/complex_and_trig.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×6; `qe-writing-001` ×2; `qe-writing-008` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-007` ×3; `qe-fig-005` ×2; `qe-fig-003` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 138, 139, 140, 141, 337. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 44, 106, 161, 179, 358, 421. *Example:* H3 Title Case: 'Complex Numbers' (Numbers).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 100, 135, 335. *Example:* style override.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 145. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 122, 326. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 3. *Lines:* 341, 342, 343. *Example:* spine removal.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 406, 563. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 234, 256. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (6 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-fig-007` — Keep figure box and spines (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (5 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (2 occurrences).
