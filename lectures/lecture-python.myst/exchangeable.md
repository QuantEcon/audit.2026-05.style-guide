# exchangeable

- **Series:** lecture-python.myst
- **File:** `lectures/exchangeable.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×2; `qe-writing-006` ×1; `qe-writing-008` ×62. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 700. *Example:* bare expectation `E\left[`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 290. *Example:* H2 Title Case: "Bayes' Law" (Law).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 62. *Lines:* 31, 36, 43, 44, 48, 58, 60, 83, 94, 99, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 73, 412. *Example:* spelled-out `gamma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 446, 479, 534. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 685. *Example:* .set(xlabel='$t$', title=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 683, 684, 721. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 640, 659. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 681. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (62 occurrences).
6. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
