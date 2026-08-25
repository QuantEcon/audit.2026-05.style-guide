# dyn_stack

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/dyn_stack.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×30; `qe-writing-004` ×1. |
| Math         | 5/10  | `qe-math-002` ×26. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×6; `qe-fig-005` ×6; `qe-fig-008` ×13, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×5. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 1031, 1101, 1106, 1110, 1364, 1429. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 1021, 1094, 1151, 1264, 1355, 1417. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 1097, 1099, 1104, 1105, 1108, 1109, 1155, 1156, 1276, 1277, …. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 5. *Lines:* 42, 324, 519, 814, 1411. *Example:* raw link to python.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 26. *Lines:* 355, 513, 516, 523, 529, 658, 669, 714, 887, 1073. *Example:* apostrophe transpose `y'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 30. *Lines:* 311, 314, 315, 339, 438, 441, 445, 557, 570, 583, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 987, 1144, 1340, 1398. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 1027, 1095, 1361. *Example:* figsize=.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 323. *Example:* mid-sentence 'Programming'.

### Low severity
_None found._


## Strengths

- References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (26 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (5 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (30 occurrences).
7. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
