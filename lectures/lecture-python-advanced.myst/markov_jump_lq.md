# markov_jump_lq

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/markov_jump_lq.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-009` (proposed) ×1; `qe-writing-008` ×5. |
| Math         | 3/10  | `qe-math-002` ×45; `qe-math-010` (proposed) ×1; `qe-math-011` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-002` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×6; `qe-fig-005` ×2; `qe-fig-008` ×12. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 8. *Lines:* 409, 509, 519, 536, 578, 602, 647, 703. *Example:* spelled-out `beta`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 488, 550, 619, 660, 682, 716. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 443, 444, 448, 451, 485, 545, 546, 655, 656, 672, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 45. *Lines:* 81, 94, 108, 114, 115, 122, 128, 169, 191, 197, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 288. *Example:* non-blackboard `\Pr`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 57, 59, 64, 99, 294. *Example:* 3 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 434, 478. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 37. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 180. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 39, 41, 43. *Example:* {cite} in narrative flow: 'in {cite}`'.

### Low severity
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 179. *Example:* i.i.d..


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (45 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (8 occurrences).
4. `qe-ref-001` — Use correct citation style (3 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
6. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
7. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
