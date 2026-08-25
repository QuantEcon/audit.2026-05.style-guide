# lu_tricks

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lu_tricks.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-004` ×6; `qe-writing-001` ×4; `qe-writing-008` ×10. |
| Math         | 7/10  | `qe-math-003` ×10. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 10. *Lines:* 295, 305, 311, 392, 403, 412, 423, 457, 462, 467. *Example:* matrix environment.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 6. *Lines:* 25, 34. *Example:* mid-sentence 'Dynamic'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 10. *Lines:* 34, 41, 94, 220, 333, 385, 432, 439, 1065. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 942. *Example:* .set(title=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 25, 1028, 1045, 1065. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 937. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 920. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (10 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (6 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (10 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
