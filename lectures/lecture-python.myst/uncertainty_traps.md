# uncertainty_traps

- **Series:** lecture-python.myst
- **File:** `lectures/uncertainty_traps.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×2; `qe-writing-001` ×4; `qe-writing-008` ×5. |
| Math         | 6/10  | `qe-math-010` (proposed) ×2; `qe-math-004` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×6; `qe-fig-002` ×3; `qe-fig-001` ×3, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 147, 302, 321, 408, 471, 482. *Example:* {figure} without :name:.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 169, 195. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 58, 102. *Example:* H2 Title Case: 'The Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 35, 37, 39, 151, 338. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 412, 472, 483. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 147, 302, 321. *Example:* static image .png.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 336, 340, 343. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 336, 358, 404, 426. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 413. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 60. *Example:* {cite} in narrative flow: 'in {cite}`'.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-math-004` — Do not use bold face for matrices or vectors (3 occurrences).
6. `qe-ref-001` — Use correct citation style (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (5 occurrences).
