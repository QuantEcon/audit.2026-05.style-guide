# olg

- **Series:** lecture-python-intro
- **File:** `lectures/olg.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×3. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×7; `qe-fig-008` ×11; `qe-fig-001` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×1; `qe-link-001` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 383, 441, 500, 523, 610, 718, 829. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 390, 392, 398, 508, 509, 527, 528, 616, 618, 841, …. *Example:* plot() without lw=.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 448, 727. *Example:* figsize=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 676. *Example:* raw link to python.quantecon.org.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 244, 629, 750. *Example:* 2 spaces.

### Low severity
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 34. *Example:* full URL to own series (intro.quantecon.org).


## Strengths

- Writing, Math, Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
3. `qe-fig-008` — Use lw=2 for line charts (11 occurrences).
4. `qe-link-001` — Use markdown style links for lectures in same lecture series (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
