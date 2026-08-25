# qr_decomp

- **Series:** lecture-python.myst
- **File:** `lectures/qr_decomp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, links  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×3; `qe-writing-001` ×1; `qe-writing-008` ×22. |
| Math         | 3/10  | `qe-math-002` ×19; `qe-math-003` ×10; `qe-math-006` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 19. *Lines:* 42, 378, 382, 384, 386, 387, 415, 427, 436, 461. *Example:* `^T` transpose in `Q^T`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 10. *Lines:* 68, 114, 115, 116, 129, 130, 136, 147, 148. *Example:* array used as matrix.
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 1. *Lines:* 155. *Example:* bare \begin{align*} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 29, 165, 301. *Example:* H2 Title Case: 'Matrix Factorization' (Factorization).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 22. *Lines:* 31, 33, 42, 47, 49, 63, 73, 96, 108, 111, …. *Example:* 2 spaces.

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 379. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (19 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (10 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
4. `qe-math-006` — Use aligned environment correctly for PDF compatibility (1 occurrence).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (22 occurrences).
