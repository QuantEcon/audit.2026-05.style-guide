# permanent_income_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/permanent_income_dles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-004` ×7; `qe-writing-008` ×3. |
| Math         | 7.5/10 | `qe-math-003` ×9. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×1; `qe-fig-008` ×6; `qe-fig-001` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 281, 282, 283, 284, 289, 290. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 9. *Lines:* 161, 163, 165, 166, 170, 171, 172, 173, 256. *Example:* array used as matrix.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 40, 41, 48, 270. *Example:* mid-sentence 'Savings'.

### Medium severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 27, 157. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 29, 46, 274. *Example:* 2 spaces.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 277. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 276. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (7 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (9 occurrences).
3. `qe-ref-001` — Use correct citation style (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (6 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
