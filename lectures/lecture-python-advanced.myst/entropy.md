# entropy

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/entropy.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, figures, references, links  *(JAX out of scope)*
- **Overall score:** 6.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×6; `qe-writing-008` ×47; `qe-writing-004` ×1. |
| Math         | 4/10  | `qe-math-002` ×15; `qe-math-011` (proposed) ×2. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-002` ×4. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 8.5/10 | `qe-link-001` ×2. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 15. *Lines:* 106, 269, 279, 288, 296, 304, 311, 330, 441, 456, …. *Example:* apostrophe transpose `w'`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 359, 385, 471, 481. *Example:* {cite} in author position: '{cite}`Backus_Chernov_Zin`  use'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 125, 315, 377, 523, 530, 539. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 47. *Lines:* 40, 48, 64, 77, 78, 110, 125, 128, 156, 180, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 4. *Lines:* 115, 519, 526, 535. *Example:* static image .png.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 2. *Lines:* 33, 34. *Example:* full URL to own series (python-advanced.quantecon.org).
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 2. *Lines:* 256. *Example:* decorated distribution `{\cal N}`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 33. *Example:* mid-sentence 'Model'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 115. *Example:* non-descriptive name `fig1`.


## Strengths

- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (15 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (6 occurrences).
3. `qe-ref-001` — Use correct citation style (5 occurrences).
4. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (2 occurrences).
5. `qe-link-001` — Use markdown style links for lectures in same lecture series (2 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (47 occurrences).
7. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
