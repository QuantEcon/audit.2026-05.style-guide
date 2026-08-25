# measurement_models

- **Series:** lecture-python.myst
- **File:** `lectures/measurement_models.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×12; `qe-writing-001` ×2; `qe-writing-008` ×20. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×9; `qe-math-011` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-002` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 8. *Lines:* 725, 728, 730, 733, 742, 1110, 1113, 1115. *Example:* spelled-out `psi`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 9. *Lines:* 628, 629, 630, 631, 640, 954, 1025, 1026, 1027. *Example:* bare expectation `E[`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 12. *Lines:* 1053, 1059, 1142, 1149, 1151, 1184, 1197, 1218, 1398, 1443, …. *Example:* mid-sentence 'Model'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 20. *Lines:* 63, 64, 69, 75, 134, 137, 159, 164, 277, 326, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 1286, 1419. *Example:* figsize=.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 328. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 45, 276. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Figures, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 13 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (9 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (12 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (8 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (20 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
