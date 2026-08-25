# sargent_surico

- **Series:** lecture-python.myst
- **File:** `lectures/sargent_surico.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-006` ×1; `qe-writing-008` ×2. |
| Math         | 5.5/10 | `qe-math-002` ×13. |
| Code         | 6/10  | `qe-code-002` ×89; `qe-code-004` ×8; `qe-code-005` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×16; `qe-fig-005` ×6; `qe-fig-001` ×12, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 89. *Lines:* 112, 118, 323, 324, 330, 331, 368, 374, 375, 383, …. *Example:* spelled-out `beta`.
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 8. *Lines:* 1086, 1088, 1548, 1552, 1554, 1557, 1627, 1630. *Example:* time.time(.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 12. *Lines:* 88, 89, 90, 258, 290, 418, 1096, 1135, 1178, 1731, …. *Example:* style override.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 16. *Lines:* 265, 267, 300, 303, 426, 428, 1102, 1103, 1140, 1143, …. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 254, 404, 1095, 1132, 1787, 1860. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 13. *Lines:* 181, 182, 183, 184, 190, 202, 204, 782, 929. *Example:* apostrophe transpose `A'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1269. *Example:* H2 Title Case: 'Estimating with Hamiltonian Monte Carlo' (Monte, Carlo).

### Medium severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 585. *Example:* 2 spaces.

### Low severity
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 1. *Lines:* 1548. *Example:* hand-rolled benchmark loop — use qe.timeit.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 1724. *Example:* caption of 10 words.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (3 parenthetical, 22 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (13 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (16 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (89 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (12 occurrences).
7. `qe-fig-004` — Caption formatting conventions (1 occurrence).
