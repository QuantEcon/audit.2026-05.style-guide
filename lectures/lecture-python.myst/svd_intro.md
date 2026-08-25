# svd_intro

- **Series:** lecture-python.myst
- **File:** `lectures/svd_intro.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×8; `qe-writing-004` ×9; `qe-writing-001` ×7, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×6; `qe-fig-005` ×1; `qe-fig-001` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 963, 965, 968, 974, 976, 979. *Example:* .suptitle.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 7. *Lines:* 136, 138, 140, 474, 557, 595, 614. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 9. *Lines:* 29, 115, 353, 403, 479, 622, 1041. *Example:* mid-sentence 'Vector'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 31, 61, 127, 324, 359, 509, 537, 672. *Example:* H2 Title Case: 'The Setting' (Setting).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 94. *Lines:* 19, 27, 29, 31, 37, 44, 48, 53, 55, 57, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 962, 973. *Example:* figsize=.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 947. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (8 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (9 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (7 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (94 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
