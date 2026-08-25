# two_auctions

- **Series:** lecture-python.myst
- **File:** `lectures/two_auctions.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×4; `qe-writing-009` (proposed) ×2; `qe-writing-008` ×64. |
| Math         | 5.5/10 | `qe-math-004` ×22; `qe-math-012` (proposed) ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-006` ×16; `qe-fig-007` ×7; `qe-fig-005` ×7, +3 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-001` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 200, 262, 316, 437, 492, 526, 614, 646. *Example:* style override.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 255, 315, 429, 455, 488, 525, 549. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 16. *Lines:* 270, 271, 327, 328, 443, 444, 460, 499, 500, 538, …. *Example:* axis label `Valuation, $v_i$`.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 7. *Lines:* 272, 329, 446, 501, 540, 623, 660. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 264, 265, 266, 439, 440, 494, 495, 616, 617. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 22. *Lines:* 101, 165, 166, 177, 292, 303, 304, 305, 306, 356, …. *Example:* \mathbf.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 64. *Lines:* 23, 47, 51, 58, 61, 68, 80, 86, 88, 90, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 445. *Example:* .set_title.
- **[qe-math-012 (proposed)]** — Multiplication via \cdot or juxtaposition, never *. *Count:* 3. *Lines:* 285, 356. *Example:* * as multiplication.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 96, 143, 347, 368. *Example:* mid-sentence 'Equilibrium'.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 2. *Lines:* 137, 161. *Example:* i.i.d..

### Low severity
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 16. *Example:* full URL to own series (python.quantecon.org).


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-004` — Do not use bold face for matrices or vectors (22 occurrences).
2. `qe-fig-006` — Lowercase axis labels (16 occurrences).
3. `qe-fig-007` — Keep figure box and spines (7 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
6. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (2 occurrences).
7. `qe-math-012` (proposed) — Multiplication via \cdot or juxtaposition, never * (3 occurrences).
