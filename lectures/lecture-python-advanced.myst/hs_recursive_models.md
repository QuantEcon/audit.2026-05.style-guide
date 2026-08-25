# hs_recursive_models

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hs_recursive_models.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, references, links  *(JAX out of scope)*
- **Overall score:** 6.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-004` ×28; `qe-writing-001` ×15; `qe-writing-006` ×2, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×26; `qe-math-002` ×167. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 167. *Lines:* 220, 244, 271, 309, 310, 317, 318, 331, 332, 335, …. *Example:* \prime transpose.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 26. *Lines:* 217, 220, 259, 265, 271, 299, 309, 351, 873, 876, …. *Example:* bare expectation `E(`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 15. *Lines:* 324, 358, 365, 963, 1734, 1759, 1879, 1937, 1944, 1956, …. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 28. *Lines:* 91, 598, 710, 901, 959, 1187, 1419, 1436, 1465, 1474, …. *Example:* mid-sentence 'State'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 1695, 1892. *Example:* H2 Title Case: 'Gorman aggregation and Engel curves' (Engel).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 50. *Lines:* 40, 43, 57, 77, 82, 91, 96, 116, 118, 123, …. *Example:* 2 spaces.

### Medium severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 94, 158, 2452. *Example:* {cite} in narrative flow: '{cite}`'.

### Low severity
_None found._


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (26 occurrences).
2. `qe-math-002` — Use \top for transpose notation (167 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (28 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (15 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
6. `qe-ref-001` — Use correct citation style (4 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (50 occurrences).
