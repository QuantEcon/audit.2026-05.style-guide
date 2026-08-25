# growth_in_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/growth_in_dles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×6; `qe-writing-001` ×4; `qe-writing-006` ×1, +1 more. |
| Math         | 7.5/10 | `qe-math-003` ×8. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×5; `qe-fig-008` ×10. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 351, 433, 514, 546, 573. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 353, 354, 438, 439, 518, 519, 554, 555, 581, 582. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 8. *Lines:* 172, 231, 241, 246, 255, 263, 293, 410. *Example:* array used as matrix.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 6. *Lines:* 284, 395, 455, 500, 524, 535. *Example:* mid-sentence 'Example'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 463. *Example:* H3 Title Case: 'Example 3: a Jones-Manuelli (1990) economy' (Jones-Manuelli).

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 196, 275, 348, 534. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 27. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 29. *Example:* 2 spaces.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (6 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (8 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
7. `qe-ref-001` — Use correct citation style (1 occurrence).
