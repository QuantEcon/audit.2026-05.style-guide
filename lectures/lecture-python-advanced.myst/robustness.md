# robustness

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/robustness.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×2; `qe-writing-006` ×1; `qe-writing-008` ×35. |
| Math         | 3/10  | `qe-math-002` ×117; `qe-math-004` ×13; `qe-math-010` (proposed) ×1. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-006` ×2; `qe-fig-005` ×4; `qe-fig-002` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×9. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 9. *Lines:* 162, 164, 260, 266, 319, 452, 617, 858, 1154. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 117. *Lines:* 171, 211, 221, 241, 242, 246, 248, 260, 274, 277, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 13. *Lines:* 388, 389, 397, 412, 417, 429, 441, 450, 510, 530, …. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 877. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 467. *Example:* H3 Title Case: "Using Agent 2's problem to construct bounds on value sets" (Agent).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 35. *Lines:* 41, 51, 63, 65, 90, 92, 138, 145, 191, 199, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 98, 122, 1120. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 98, 122, 948, 1120. *Example:* {figure} without :name:.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 1075, 1076. *Example:* axis label `Value`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 74, 289. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 1051. *Example:* spelled-out `beta`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1107. *Example:* plot() without lw=.


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (117 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (13 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (9 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-fig-006` — Lowercase axis labels (2 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
7. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
