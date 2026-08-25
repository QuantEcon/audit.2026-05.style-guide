# cagan_rational_expectations

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cagan_rational_expectations.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9.5/10 | `qe-writing-008` ×1. |
| Math         | 3/10  | `qe-math-002` ×5; `qe-math-010` (proposed) ×4; `qe-math-003` ×2. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-006` ×2; `qe-fig-004` ×2; `qe-fig-003` ×1, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 5. *Lines:* 761, 770, 944, 997. *Example:* apostrophe transpose `a_t'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 205, 209, 225, 270. *Example:* bare expectation `E_t(`.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 455, 1432, 1461. *Example:* spelled-out `alpha`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 1440, 1476. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 1482. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 451, 1178. *Example:* caption of 7 words.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 473, 1683. *Example:* axis label `True $\alpha$`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 632, 1037. *Example:* pmatrix environment.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 739, 1030. *Example:* {cite} in author position: '{cite}`sims1972money` proved'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1669. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 82. *Example:* 2 spaces.


## Strengths

- Writing, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (5 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
3. `qe-math-003` — Use square brackets for matrix notation (2 occurrences).
4. `qe-ref-001` — Use correct citation style (2 occurrences).
5. `qe-fig-006` — Lowercase axis labels (2 occurrences).
6. `qe-fig-004` — Caption formatting conventions (2 occurrences).
7. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
