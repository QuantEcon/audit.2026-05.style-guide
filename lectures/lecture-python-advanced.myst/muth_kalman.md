# muth_kalman

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/muth_kalman.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-001` ×1; `qe-writing-008` ×3. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×2; `qe-math-011` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×3; `qe-fig-006` ×3; `qe-fig-005` ×4, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 280, 281, 301, 302, 319, 350, 352. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 144, 145. *Example:* bare expectation `E [`.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 284, 304, 321. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 278, 299, 317, 339. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 283, 305, 322. *Example:* axis label `Time`.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 97. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 116. *Example:* decorated distribution `{\mathcal N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 314. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 72, 155. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
3. `qe-fig-006` — Lowercase axis labels (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
7. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
