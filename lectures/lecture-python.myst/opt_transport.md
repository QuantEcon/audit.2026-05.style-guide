# opt_transport

- **Series:** lecture-python.myst
- **File:** `lectures/opt_transport.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×9; `qe-writing-008` ×44; `qe-writing-001` ×1. |
| Math         | 3/10  | `qe-math-002` ×14; `qe-math-004` ×10. |
| Code         | 9/10  | `qe-code-004` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×2; `qe-fig-002` ×1; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 5. *Lines:* 411, 415, 532, 537, 760. *Example:* %time.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 14. *Lines:* 154, 159, 161, 175, 201, 214, 222, 225, 236, 247, …. *Example:* apostrophe transpose `C'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 10. *Lines:* 206, 213, 214, 217, 222, 228, 247, 248, 567, 571. *Example:* \mathbf.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 60, 131, 137, 258, 480, 546, 646, 658, 677. *Example:* H2 Title Case: 'The Optimal Transport Problem' (Optimal, Transport, Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 44. *Lines:* 29, 66, 68, 74, 76, 110, 114, 155, 166, 168, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 84, 771. *Example:* {figure} without :name:.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 28. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 799. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 84. *Example:* static image .png.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (14 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (9 occurrences).
3. `qe-math-004` — Do not use bold face for matrices or vectors (10 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (44 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-code-004` — Use quantecon Timer context manager (5 occurrences).
