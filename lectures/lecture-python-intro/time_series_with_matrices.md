# time_series_with_matrices

- **Series:** lecture-python-intro
- **File:** `lectures/time_series_with_matrices.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-004` ×7; `qe-writing-001` ×2; `qe-writing-008` ×27. |
| Math         | 7.5/10 | `qe-math-003` ×7. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×9; `qe-fig-008` ×9; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 9. *Lines:* 222, 254, 315, 328, 346, 466, 486, 655, 670. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 223, 255, 316, 474, 488, 656, 657, 673, 674. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 7. *Lines:* 93, 100, 107, 284, 607, 613, 619. *Example:* array used as matrix.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 371, 518, 533. *Example:* mid-sentence 'Distribution'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 27. *Lines:* 40, 373, 391, 460, 462, 464, 496, 512, 516, 520, …. *Example:* 2 spaces.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 371, 518, 533. *Example:* raw link to python.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 78, 213. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 54. *Example:* style override.


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (7 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (7 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (9 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-link-002` — Use doc links for cross-series references (3 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (27 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (9 occurrences).
