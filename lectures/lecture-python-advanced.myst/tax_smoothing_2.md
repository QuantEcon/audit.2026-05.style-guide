# tax_smoothing_2

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tax_smoothing_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×19. |
| Math         | 4/10  | `qe-math-002` ×57; `qe-math-011` (proposed) ×1. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×9; `qe-fig-006` ×9; `qe-fig-005` ×4, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 9. *Lines:* 476, 479, 523, 526, 821, 824, 827, 830, 841. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 477, 480, 524, 527, 822, 825, 828, 831, 842. *Example:* axis label `Time`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 475, 478, 522, 525, 820, 823, 826, 829, 840. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 57. *Lines:* 268, 274, 280, 287, 617, 625, 631, 637, 664, 671. *Example:* apostrophe transpose `x_t'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 29, 32, 41, 44, 66, 292, 321, 488, 490, 491, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 466, 514, 809. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 474, 521, 819. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 437, 494, 816, 836. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 142. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 32, 35, 41. *Example:* {cite} in narrative flow: 'by  {cite}`'.

### Low severity
_None found._


## Strengths

- Writing, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (57 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (9 occurrences).
3. `qe-fig-006` — Lowercase axis labels (9 occurrences).
4. `qe-ref-001` — Use correct citation style (3 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
7. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
