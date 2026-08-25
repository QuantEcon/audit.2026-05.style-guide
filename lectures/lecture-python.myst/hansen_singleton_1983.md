# hansen_singleton_1983

- **Series:** lecture-python.myst
- **File:** `lectures/hansen_singleton_1983.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-004` ×1; `qe-writing-008` ×22. |
| Math         | 3/10  | `qe-math-010` (proposed) ×33; `qe-math-004` ×143. |
| Code         | 8.5/10 | `qe-code-002` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 143. *Lines:* 139, 141, 146, 149, 156, 278, 283, 286, 299, 307, …. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 33. *Lines:* 215, 234, 237, 248, 250, 255, 268, 276, 283, 314, …. *Example:* bare expectation `E_{t-1}[`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 22. *Lines:* 43, 45, 49, 53, 55, 61, 63, 65, 1573, 1798, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 471, 1317. *Example:* spelled-out `mu`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 33. *Example:* mid-sentence 'Critique'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 1751. *Example:* figsize=.


## Strengths

- Figures, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 31 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (33 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (143 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (3 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (22 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
