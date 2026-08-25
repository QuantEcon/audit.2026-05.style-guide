# arma

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/arma.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-001` ×1; `qe-writing-008` ×19. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×5; `qe-fig-003` ×1; `qe-fig-008` ×6, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 236, 474, 523, 563, 757. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 234, 468, 515, 555, 714. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 243, 528, 535, 568, 575, 746. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 118, 119, 133. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 105, 159, 291, 292, 313, 369, 380, 389, 402, 415, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 747. *Example:* .set(title=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 874. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 415. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 789. *Example:* {cite} in author position: '{cite}`Ljungqvist2012` use'.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
4. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (19 occurrences).
7. `qe-ref-001` — Use correct citation style (1 occurrence).
