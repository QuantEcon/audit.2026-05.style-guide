# lqcontrol

- **Series:** lecture-dp
- **File:** `lectures/lqcontrol.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×13; `qe-writing-001` ×1; `qe-writing-008` ×12. |
| Math         | 3/10  | `qe-math-002` ×85; `qe-math-010` (proposed) ×15; `qe-math-003` ×17. |
| Code         | 7.5/10 | `qe-code-002` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-005` ×10; `qe-fig-006` ×4; `qe-fig-008` ×18, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 6. *Lines:* 672, 740, 1318, 1436, 1458, 1586. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 683, 751, 1331, 1480, 1595. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 5. *Lines:* 1051, 1121, 1197, 1201, 1205. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 10. *Lines:* 649, 735, 1051, 1121, 1197, 1201, 1205, 1287, 1403, 1555. *Example:* {figure} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 18. *Lines:* 691, 693, 695, 697, 698, 759, 761, 763, 765, 766, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 85. *Lines:* 100, 253, 271, 293, 316, 324, 373, 385, 397, 406, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 17. *Lines:* 170, 176, 182, 188, 195, 213, 221, 229, 237, 623, …. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 100, 314, 386, 398, 421, 432, 445, 469, 598, 807, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 13. *Lines:* 84, 298, 305, 577, 781, 785, 800, 842, 910, 920, …. *Example:* H3 Title Case: 'The Law of Motion' (Law, Motion).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 262, 285, 345, 358, 366, 541, 562, 713, 860, 1055, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 702, 770, 1348, 1497. *Example:* axis label `Time`.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 54. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 262. *Example:* 3 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 262. *Example:* {cite} in narrative flow: 'See {cite}`'.


## Strengths

- References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (85 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (13 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (15 occurrences).
4. `qe-math-003` — Use square brackets for matrix notation (17 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (10 occurrences).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (6 occurrences).
7. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
