# perm_income_cons

- **Series:** lecture-python.myst
- **File:** `lectures/perm_income_cons.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×12; `qe-writing-008` ×19. |
| Math         | 4.5/10 | `qe-math-002` ×8; `qe-math-010` (proposed) ×2. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×3; `qe-fig-008` ×2, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 625, 635, 716, 759, 769, 788. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 8. *Lines:* 244, 247, 249, 298. *Example:* apostrophe transpose `x'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 227, 240. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 137, 165, 201, 221, 253, 328, 407, 472, 494, 508, …. *Example:* H3 Title Case: 'Digression on a Useful Isomorphism' (Useful, Isomorphism).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 53, 55, 89, 149, 156, 157, 174, 203, 219, 296, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 559, 601, 707. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 568, 609, 711. *Example:* .set(title=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 708, 709. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 163. *Example:* raw link to python-advanced.quantecon.org.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 396. *Example:* spelled-out `beta`.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (12 occurrences).
2. `qe-math-002` — Use \top for transpose notation (8 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
6. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (19 occurrences).
