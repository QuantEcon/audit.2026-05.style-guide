# lq_inventories

- **Series:** lecture-python.myst
- **File:** `lectures/lq_inventories.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×2; `qe-writing-001` ×4; `qe-writing-008` ×4. |
| Math         | 3/10  | `qe-math-002` ×15; `qe-math-003` ×17. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×4; `qe-fig-008` ×10; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 306, 307, 308, 312, 326, 327, 328, 332, 333, 335. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 15. *Lines:* 131, 137, 148, 149, 151, 153, 661, 720. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 17. *Lines:* 114, 150, 151, 154, 157, 158, 161, 164, 165, 168, …. *Example:* array used as matrix.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 417, 448. *Example:* H2 Title Case: 'Inventories Not Useful' (Not, Useful).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 310, 316, 330, 338. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 489, 716, 722, 769. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 56, 62, 432, 507. *Example:* 2 spaces.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 278. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 304. *Example:* figsize=.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (15 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (17 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
7. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
