# cons_news

- **Series:** lecture-dp
- **File:** `lectures/cons_news.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-004` ×8; `qe-writing-009` (proposed) ×4; `qe-writing-008` ×52. |
| Math         | 4.5/10 | `qe-math-003` ×17; `qe-math-010` (proposed) ×4. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×4; `qe-fig-008` ×11. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 748, 749, 768, 769, 770, 798, 799, 800, 807, 808, …. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 17. *Lines:* 549, 553, 557, 561, 565, 566, 576, 580, 584, 588, …. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 234, 380, 383, 405. *Example:* bare expectation `E [`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 8. *Lines:* 485, 486, 680, 711. *Example:* mid-sentence 'Difference'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 52. *Lines:* 40, 45, 49, 58, 62, 65, 66, 67, 82, 87, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 631, 660. *Example:* spelled-out `beta`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 747, 767, 801, 810. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 746, 766, 796, 805. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 4. *Lines:* 127, 146, 149, 481. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (17 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (8 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
5. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (4 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
7. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
