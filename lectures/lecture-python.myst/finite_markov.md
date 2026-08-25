# finite_markov

- **Series:** lecture-python.myst
- **File:** `lectures/finite_markov.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×11; `qe-writing-004` ×4; `qe-writing-001` ×2, +1 more. |
| Math         | 3.5/10 | `qe-math-010` (proposed) ×21; `qe-math-003` ×6. |
| Code         | 9.5/10 | `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×8; `qe-fig-002` ×6; `qe-fig-008` ×2, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 6. *Lines:* 200, 538, 572, 607, 635, 1115. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 200, 538, 572, 607, 635, 801, 1058, 1115. *Example:* {figure} without :name:.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 156, 179, 457, 548, 923, 1016. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 21. *Lines:* 99, 100, 110, 368, 369, 370, 437, 903, 911, 937, …. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 11. *Lines:* 223, 295, 319, 419, 440, 466, 742, 790, 893, 965, …. *Example:* H3 Title Case: 'Rolling Our Own' (Our, Own).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 35. *Lines:* 71, 174, 225, 227, 229, 340, 374, 376, 447, 472, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 312, 316. *Example:* %time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 809, 1067. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 1079, 1081. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 309. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 227, 1377. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 472, 494, 495. *Example:* mid-sentence 'Law'.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (11 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (21 occurrences).
3. `qe-math-003` — Use square brackets for matrix notation (6 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (35 occurrences).
