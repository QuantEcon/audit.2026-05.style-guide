# pandas

- **Series:** lecture-python-programming
- **File:** `lectures/pandas.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×8; `qe-writing-004` ×2; `qe-writing-008` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×8; `qe-fig-002` ×3; `qe-fig-001` ×2, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 46, 473, 489, 583, 624, 686, 726, 753. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 182, 210, 295, 348, 428, 496, 515, 594. *Example:* H3 Title Case: 'Select Data by Position' (Data, Position).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 727, 798. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 46, 686, 753. *Example:* static image .png.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 86, 387. *Example:* mid-sentence 'Series'.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 802. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 75. *Example:* 2 spaces.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (8 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
4. `qe-fig-002` — Prefer code-generated figures (3 occurrences).
5. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
