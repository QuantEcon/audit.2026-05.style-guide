# numpy

- **Series:** lecture-python-programming
- **File:** `lectures/numpy.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×12; `qe-writing-001` ×3; `qe-writing-008` ×4. |
| Math         | 8.5/10 | `qe-math-010` (proposed) ×1. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×2; `qe-fig-008` ×13; `qe-fig-001` ×4. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 519, 522, 525, 528, 532, 535, 538, 541, 545, 548, …. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 1190. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 69, 122, 161, 222, 314, 383, 432, 836, 891, 923, …. *Example:* H2 Title Case: 'NumPy Arrays' (Arrays).

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1442. *Example:* install cell at line 1442 of 1539 (not near the top).
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 570, 635, 705, 778. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1111, 1397. *Example:* {figure} without :name:.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 27, 468, 1436. *Example:* 5 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 27, 83, 103, 826. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (12 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (13 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (4 occurrences).
