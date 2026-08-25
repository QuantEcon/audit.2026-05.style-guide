# numba

- **Series:** lecture-python-programming
- **File:** `lectures/numba.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×6; `qe-writing-001` ×2; `qe-writing-008` ×3. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×4; `qe-fig-008` ×2; `qe-fig-002` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 975, 1014. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 87, 100, 183, 217, 267, 300. *Example:* H3 Title Case: 'An Example' (Example).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 104, 340, 575, 885. *Example:* {image} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 349, 899. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 566. *Example:* raw link to intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 69, 211. *Example:* 3 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 70, 198, 219. *Example:* 2 spaces.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 575. *Example:* static image .png.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (6 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (2 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
5. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (3 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
