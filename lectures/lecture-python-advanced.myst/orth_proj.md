# orth_proj

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/orth_proj.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×2; `qe-writing-001` ×3; `qe-writing-008` ×16. |
| Math         | 3/10  | `qe-math-002` ×52; `qe-math-003` ×6. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-002` ×6. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 6. *Lines:* 73, 79, 85, 154, 195, 249. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 73, 79, 85, 154, 195, 249. *Example:* {figure} without :name:.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 52. *Lines:* 351, 356, 364, 366, 375, 383, 385, 402, 417, 420, …. *Example:* apostrophe transpose `X'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 535, 545, 560, 569, 777, 791. *Example:* array used as matrix.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 16. *Lines:* 71, 77, 111, 130, 186, 311, 333, 348, 394, 437, …. *Example:* 2 spaces.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 53, 665. *Example:* raw link to python-intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 348, 740, 883. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 55, 104. *Example:* mid-sentence 'Theory'.

### Low severity
_None found._


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (52 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (6 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
6. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (16 occurrences).
