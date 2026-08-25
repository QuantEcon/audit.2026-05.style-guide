# markov_perf

- **Series:** lecture-python.myst
- **File:** `lectures/markov_perf.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×8; `qe-writing-008` ×12. |
| Math         | 5/10  | `qe-math-002` ×35. |
| Code         | 7.5/10 | `qe-code-002` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×6; `qe-fig-003` ×1; `qe-fig-002` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 5. *Lines:* 453, 455, 562, 614. *Example:* spelled-out `beta`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 480, 509, 629, 730, 740, 839. *Example:* {figure} without :name:.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 35. *Lines:* 202, 203, 204, 205, 206, 248, 249, 250, 265, 266, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 91, 177, 188, 229, 326, 332, 351, 427. *Example:* H3 Title Case: 'Example: A Duopoly Model' (Duopoly, Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 80, 148, 149, 175, 220, 328, 330, 353, 392. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 492, 630, 848. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 509, 730, 740. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 495. *Example:* .set_title.

### Low severity
_None found._


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (35 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (8 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (5 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (12 occurrences).
7. `qe-fig-002` — Prefer code-generated figures (3 occurrences).
