# equalizing_difference

- **Series:** lecture-python-intro
- **File:** `lectures/equalizing_difference.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-008` ×42. |
| Math         | 8/10  | `qe-math-001` ×2. |
| Code         | 7.5/10 | `qe-code-002` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-006` ×5; `qe-fig-005` ×7; `qe-fig-008` ×8. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 9. *Lines:* 54, 384, 391, 398, 424, 439, 456, 471, 486. *Example:* spelled-out `Lambda`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 233, 249, 268, 345, 512, 562, 648. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 5. *Lines:* 522, 572, 573, 656, 657. *Example:* axis label `College wage premium $\phi$`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 238, 254, 273, 350, 519, 569, 570, 654. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 42. *Lines:* 22, 25, 27, 30, 32, 34, 38, 42, 69, 75, …. *Example:* 3 spaces.

### Medium severity
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 447, 462. *Example:* unicode `γ` inside a math environment.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 25. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-006` — Lowercase axis labels (5 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (9 occurrences).
4. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (2 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (42 occurrences).
6. `qe-ref-001` — Use correct citation style (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (8 occurrences).
