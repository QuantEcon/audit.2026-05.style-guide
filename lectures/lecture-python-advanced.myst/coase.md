# coase

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/coase.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-001` ×4; `qe-writing-008` ×7. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×5; `qe-fig-008` ×3; `qe-fig-002` ×2. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 9. *Lines:* 442, 445, 463, 471, 502, 503, 583, 585. *Example:* spelled-out `delta`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 145, 165, 529, 548, 627. *Example:* {figure} without :name:.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 68, 278, 301, 424, 570, 623. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 145, 165. *Example:* static image .png.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 537, 555, 638. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 306, 354, 381. *Example:* {cite} in narrative flow: 'In {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 89, 278, 570, 622. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (9 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
4. `qe-ref-001` — Use correct citation style (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (7 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
7. `qe-fig-002` — Prefer code-generated figures (2 occurrences).
