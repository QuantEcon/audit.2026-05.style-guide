# rs_inventory_q

- **Series:** lecture-python.myst
- **File:** `lectures/rs_inventory_q.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-006` ×3; `qe-writing-001` ×2; `qe-writing-004` ×1, +1 more. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×5; `qe-math-002` ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×7; `qe-fig-005` ×4; `qe-fig-008` ×9, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 318, 323, 360, 692, 699, 728, 738. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 312, 313, 358, 687, 688, 694, 695, 726, 736. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 4. *Lines:* 471, 472, 483, 505. *Example:* apostrophe transpose `a'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 66, 84, 418, 461, 479. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 59, 124, 368. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 308, 347, 685, 717. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 307, 345, 684, 714. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 557, 559. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 471. *Example:* mid-sentence 'Step'.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 557. *Example:* 2 spaces.


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (5 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
3. `qe-math-002` — Use \top for transpose notation (4 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (7 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
7. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
