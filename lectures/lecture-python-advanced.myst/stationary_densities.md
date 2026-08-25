# stationary_densities

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/stationary_densities.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×4; `qe-writing-008` ×12. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×5. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×6; `qe-fig-004` ×1; `qe-fig-002` ×2, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 7.5/10 | `qe-link-002` ×7. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 696, 794, 824, 890, 959, 1016. *Example:* {figure} without :name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 7. *Lines:* 281, 290, 331, 415, 445, 520, 610. *Example:* raw link to python.quantecon.org.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 110, 420, 571, 1054. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 67, 244, 354, 385, 395, 445, 639, 660, 677, 678, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 77, 476, 879, 915. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 908, 1026. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 696, 794. *Example:* static image .png.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 678. *Example:* {cite} in author position: '{cite}`LasotaMackey1994`  and'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 66, 244, 328, 353. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 464. *Example:* caption of 7 words.


## Strengths

- Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (5 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (7 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-ref-001` — Use correct citation style (2 occurrences).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (12 occurrences).
