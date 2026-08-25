# lqcontrol

- **Series:** lecture-python.myst
- **File:** `lectures/lqcontrol.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-001` ×1; `qe-writing-008` ×12. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×15. |
| Code         | 7.5/10 | `qe-code-002` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×9; `qe-fig-006` ×3; `qe-fig-008` ×13, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 5. *Lines:* 679, 1286, 1405, 1427, 1556. *Example:* spelled-out `beta`.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 5. *Lines:* 1018, 1088, 1164, 1168, 1172. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 9. *Lines:* 634, 1018, 1088, 1164, 1168, 1172, 1255, 1372, 1525. *Example:* {figure} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 698, 700, 702, 704, 705, 1307, 1309, 1311, 1312, 1457, …. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 101, 301, 373, 387, 410, 421, 434, 458, 587, 786, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 247, 272, 332, 345, 353, 530, 551, 724, 839, 1022, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 690, 1299, 1449, 1565. *Example:* figsize=.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 3. *Lines:* 709, 1316, 1466. *Example:* axis label `Time`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 247. *Example:* 3 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 247. *Example:* {cite} in narrative flow: 'See {cite}`'.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (15 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (9 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (5 occurrences).
4. `qe-fig-006` — Lowercase axis labels (3 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (12 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (13 occurrences).
