# tax_smoothing_3

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_3.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×19. |
| Math         | 9/10  | `qe-math-011` (proposed) ×1. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×4; `qe-fig-006` ×4; `qe-fig-005` ×2, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 29, 32, 33, 35, 39, 41, 44, 100, 101, 103, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 242, 304. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 273, 314. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 275, 278, 316, 319. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 262, 290. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 276, 279, 317, 320. *Example:* axis label `Time`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 274, 277, 315, 318. *Example:* plot() without lw=.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 97. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 32, 35. *Example:* {cite} in author position: '{cite}`barro1999determinants` and'.

### Low severity
_None found._


## Strengths

- Writing, Math, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
2. `qe-ref-001` — Use correct citation style (3 occurrences).
3. `qe-fig-006` — Lowercase axis labels (4 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
6. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (19 occurrences).
