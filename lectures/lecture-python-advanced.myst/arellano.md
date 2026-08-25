# arellano

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/arellano.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×7. |
| Math         | 3.5/10 | `qe-math-002` ×31; `qe-math-010` (proposed) ×1. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×8; `qe-fig-002` ×4; `qe-fig-001` ×4. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 631, 652, 661, 672, 711, 742, 757, 777. *Example:* {figure} without :name:.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 31. *Lines:* 126, 128, 129, 131, 132, 133, 134, 145, 224, 250, …. *Example:* apostrophe transpose `B'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 101. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 32, 128, 133, 184, 301, 636. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 416, 417. *Example:* spelled-out `delta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 721, 745, 766, 799. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 4. *Lines:* 631, 652, 661, 672. *Example:* static image .png.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 317. *Example:* {cite} in narrative flow: 'to {cite}`'.


## Strengths

- Writing, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (31 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
4. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (7 occurrences).
7. `qe-fig-002` — Prefer code-generated figures (4 occurrences).
