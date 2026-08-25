# geom_series

- **Series:** lecture-python-intro
- **File:** `lectures/geom_series.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×3; `qe-writing-001` ×2; `qe-writing-008` ×1. |
| Math         | 8.5/10 | `qe-math-002` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-006` ×9; `qe-fig-005` ×4; `qe-fig-004` ×4, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 51, 790, 932, 994, 1113. *Example:* style override.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 709, 736, 758, 807, 1055, 1056, 1126, 1190, 1191. *Example:* axis label `Present Value, $p_0$`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 733, 734, 766, 887, 915, 940, 943, 997, 1052, 1115, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 616. *Example:* `^T` transpose in `G^{T}`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 118, 268, 438. *Example:* H2 Title Case: 'Example: The Money Multiplier in Fractional Reserve Banking' (Money, Multiplier, Fractional, Reserve).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 948. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 681, 720, 782, 900. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 983, 1041, 1103, 1160. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 110, 459. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 88. *Example:* 2 spaces.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
2. `qe-fig-006` — Lowercase axis labels (9 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
5. `qe-fig-004` — Caption formatting conventions (4 occurrences).
6. `qe-math-002` — Use \top for transpose notation (1 occurrence).
7. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
