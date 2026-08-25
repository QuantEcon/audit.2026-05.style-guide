# inventory_q

- **Series:** lecture-dp
- **File:** `lectures/inventory_q.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×2; `qe-writing-001` ×3; `qe-writing-008` ×1. |
| Math         | 4/10  | `qe-math-010` (proposed) ×3; `qe-math-002` ×3; `qe-math-005` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×2; `qe-fig-008` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 380, 685, 686, 692, 693, 730, 739. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 435, 457, 500. *Example:* apostrophe transpose `a'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 143, 416, 433. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 76, 154. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 683, 722. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 690, 697, 732, 741. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 682, 719. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 3. *Lines:* 92, 94, 96. *Example:* parenthesised sequence.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 489, 558, 562. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 490. *Example:* 2 spaces.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
3. `qe-math-002` — Use \top for transpose notation (3 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
6. `qe-math-005` — Use curly brackets for sequences (3 occurrences).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
