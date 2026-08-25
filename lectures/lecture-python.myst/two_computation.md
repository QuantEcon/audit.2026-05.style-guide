# two_computation

- **Series:** lecture-python.myst
- **File:** `lectures/two_computation.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×7. |
| Math         | 3/10  | `qe-math-002` ×15; `qe-math-010` (proposed) ×6; `qe-math-004` ×2, +1 more. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-003` ×28; `qe-fig-006` ×46; `qe-fig-005` ×5, +3 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 10. *Lines:* 294, 599, 1578, 1885, 2037, 2096, 2152, 2509, 2727, 2923. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 28. *Lines:* 602, 606, 711, 1895, 1907, 2046, 2064, 2104, 2114, 2123, …. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 2024, 2080, 2151, 2488, 2710. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 46. *Lines:* 301, 302, 603, 607, 709, 710, 1167, 1586, 1587, 1893, …. *Example:* axis label `Date born`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 15. *Lines:* 153, 162, 173, 367, 368, 369, 377, 479, 488. *Example:* apostrophe transpose `)'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 6. *Lines:* 149, 153, 227, 358. *Example:* bare expectation `E_t[`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 51, 91, 133, 229, 341, 380. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 1143, 1571. *Example:* caption of 10 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 601, 605, 708, 1160. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 2. *Lines:* 459, 472. *Example:* \mathbf.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 459. *Example:* ones vector `\mathbf{1}` used 2x with no 'vector of ones' explanation in the prose.


## Strengths

- Writing, Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 10 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (15 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (6 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (28 occurrences).
4. `qe-fig-006` — Lowercase axis labels (46 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
6. `qe-math-004` — Do not use bold face for matrices or vectors (2 occurrences).
7. `qe-fig-004` — Caption formatting conventions (2 occurrences).
