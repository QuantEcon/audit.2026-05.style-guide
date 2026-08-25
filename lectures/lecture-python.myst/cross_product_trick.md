# cross_product_trick

- **Series:** lecture-python.myst
- **File:** `lectures/cross_product_trick.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, links  *(JAX out of scope)*
- **Overall score:** 6.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×2; `qe-writing-008` ×24; `qe-writing-009` (proposed) ×1. |
| Math         | 3/10  | `qe-math-002` ×52; `qe-math-006` ×5; `qe-math-013` (proposed) ×1. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 52. *Lines:* 48, 63, 68, 84, 85, 86, 119, 120, 127, 128, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 5. *Lines:* 82, 104, 118, 126, 140. *Example:* bare \begin{align*} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 33, 92. *Example:* H2 Title Case: 'Undiscounted Dynamic Programming Problem' (Dynamic, Programming, Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 24. *Lines:* 20, 22, 27, 28, 41, 65, 75, 80, 94, 95, …. *Example:* 2 spaces.

### Medium severity
_None found._

### Low severity
- **[qe-math-013 (proposed)]** — Reference equations via {eq}`label`. *Count:* 1. *Lines:* 133. *Example:* malformed {eq} reference `{eq}`eq:Kalman102}`.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 110. *Example:* i.i.d..


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (52 occurrences).
2. `qe-math-006` — Use aligned environment correctly for PDF compatibility (5 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (24 occurrences).
5. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (1 occurrence).
6. `qe-math-013` (proposed) — Reference equations via {eq}`label` (1 occurrence).
