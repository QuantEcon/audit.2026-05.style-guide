# misspecified_recovery

- **Series:** lecture-python.myst
- **File:** `lectures/misspecified_recovery.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×4; `qe-writing-004` ×3. |
| Math         | 3/10  | `qe-math-010` (proposed) ×16; `qe-math-004` ×49; `qe-math-003` ×2, +1 more. |
| Code         | 7.5/10 | `qe-code-002` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-004` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 9. *Lines:* 124, 132, 147, 151, 1511, 1513, 1516, 1517, 1981. *Example:* spelled-out `eta`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 1333. *Example:* apostrophe transpose `)'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 49. *Lines:* 156, 157, 159, 170, 171, 175, 189, 196, 211, 213, …. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 16. *Lines:* 730, 741, 773, 779, 858, 877, 880, 1792, 1793, 1809, …. *Example:* bare expectation `E\left[`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 253, 414, 1268, 1633. *Example:* H3 Title Case: 'Degenerate Martingale Component' (Martingale, Component).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 1225, 1745, 1976. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1235, 1248. *Example:* .set_title.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 2188, 2194. *Example:* pmatrix environment.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 47, 493, 1136. *Example:* mid-sentence 'Theory'.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 1201. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1668. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 6 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (16 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (49 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (4 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (9 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (3 occurrences).
6. `qe-math-003` — Use square brackets for matrix notation (2 occurrences).
7. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
