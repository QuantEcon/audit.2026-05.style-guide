# navy_captain

- **Series:** lecture-python.myst
- **File:** `lectures/navy_captain.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×7; `qe-writing-008` ×32; `qe-writing-001` ×1. |
| Math         | 4.5/10 | `qe-math-002` ×6; `qe-math-010` (proposed) ×4. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-003` ×20; `qe-fig-005` ×19; `qe-fig-006` ×4, +2 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 446, 573, 723, 762, 816, 940. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 20. *Lines:* 193, 326, 400, 437, 450, 456, 692, 738, 740, 766, …. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 19. *Lines:* 186, 284, 309, 394, 434, 445, 539, 681, 720, 750, …. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 18. *Lines:* 316, 319, 398, 435, 575, 576, 577, 578, 685, 686, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 616, 626, 633. *Example:* \prime transpose.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 250, 251, 340, 698. *Example:* non-blackboard `\Pr`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 208, 461, 779, 835, 860, 995, 1054. *Example:* H2 Title Case: 'Frequentist Decision Rule' (Decision, Rule).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 32. *Lines:* 46, 51, 64, 70, 80, 86, 91, 94, 95, 102, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 33, 115. *Example:* spelled-out `gamma`.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 323, 324, 1028, 1048. *Example:* axis label `Probability of false alarm`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 73. *Example:* 3 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (7 occurrences).
2. `qe-math-002` — Use \top for transpose notation (6 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (20 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (19 occurrences).
5. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
6. `qe-fig-006` — Lowercase axis labels (4 occurrences).
7. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
