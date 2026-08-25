# tax_smoothing_1

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_1.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-008` ×36. |
| Math         | 4.5/10 | `qe-math-002` ×11; `qe-math-011` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-002` ×2; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-006` ×6; `qe-fig-005` ×3; `qe-fig-008` ×3. |
| References   | 7/10  | `qe-ref-001` ×13. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 6. *Lines:* 377, 378, 390, 391, 504, 505. *Example:* axis label `Time`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 11. *Lines:* 262. *Example:* apostrophe transpose `x_t'`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 13. *Lines:* 41, 43, 61, 63, 82, 123, 132, 175. *Example:* {cite} in author position: '{cite}`barro1999determinants` and'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 36. *Lines:* 30, 41, 47, 52, 53, 60, 61, 82, 83, 123, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 327, 478. *Example:* spelled-out `beta`.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 158. *Example:* install cell at line 158 of 508 (not near the top).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 372, 385, 498. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 376, 389, 503. *Example:* plot() without lw=.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 220. *Example:* decorated distribution `{\cal N}`.

### Low severity
_None found._


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (11 occurrences).
2. `qe-ref-001` — Use correct citation style (13 occurrences).
3. `qe-fig-006` — Lowercase axis labels (6 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (36 occurrences).
7. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
