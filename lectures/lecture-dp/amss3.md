# amss3

- **Series:** lecture-dp
- **File:** `lectures/amss3.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-008` ×69. |
| Math         | 9/10  | `qe-math-013` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×3; `qe-fig-008` ×3, +2 more. |
| References   | 7.5/10 | `qe-ref-001` ×6. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 177, 212, 226, 238, 259. *Example:* {figure} without :name:.
- **[qe-ref-001]** — Use correct citation style. *Count:* 6. *Lines:* 40, 60, 219, 231, 301, 398. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 69. *Lines:* 29, 34, 35, 37, 39, 42, 44, 46, 50, 52, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 200, 241. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 212, 226, 259. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 204, 249, 250. *Example:* .set(title=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 203, 244, 246. *Example:* plot() without lw=.

### Low severity
- **[qe-math-013 (proposed)]** — Reference equations via {eq}`label`. *Count:* 1. *Lines:* 422. *Example:* manual reference 'equation (42)'.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (6 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (69 occurrences).
5. `qe-math-013` (proposed) — Reference equations via {eq}`label` (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
7. `qe-fig-002` — Prefer code-generated figures (3 occurrences).
