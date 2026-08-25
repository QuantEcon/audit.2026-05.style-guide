# greek_square

- **Series:** lecture-python-intro
- **File:** `lectures/greek_square.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×2; `qe-writing-006` ×1; `qe-writing-008` ×45. |
| Math         | 8/10  | `qe-math-004` ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×2; `qe-fig-001` ×2. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 184. *Example:* H2 Title Case: 'Algorithm of the Ancient Greeks' (Ancient, Greeks).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 45. *Lines:* 30, 37, 43, 70, 86, 96, 106, 159, 186, 198, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 531, 690. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 699, 710. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 527, 686. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 4. *Lines:* 317, 321, 323, 329. *Example:* {\bf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 23, 86. *Example:* 7 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 19. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (4 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (45 occurrences).
7. `qe-ref-001` — Use correct citation style (1 occurrence).
