# von_neumann_model

- **Series:** lecture-python.myst
- **File:** `lectures/von_neumann_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×7; `qe-writing-001` ×15; `qe-writing-004` ×4, +1 more. |
| Math         | 5.5/10 | `qe-math-004` ×26; `qe-math-001` ×1. |
| Code         | 7/10  | `qe-code-002` ×11. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-008` ×1, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 11. *Lines:* 152, 153, 170, 173, 185, 262, 291, 298. *Example:* spelled-out `alpha`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 26. *Lines:* 327, 331, 333, 336, 337, 340, 341, 380, 387, 701, …. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 15. *Lines:* 354, 574, 641, 646, 670, 696, 783, 789, 846, 905, …. *Example:* 2 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 362, 472, 509, 687, 739, 989, 1035. *Example:* H2 Title Case: 'Model Ingredients and Assumptions' (Ingredients, Assumptions).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 554, 610, 651, 982, 1066. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 949, 954. *Example:* .suptitle.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 1. *Lines:* 38. *Example:* unicode `β` inside a math environment.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 859. *Example:* {cite} in author position: '{cite}`hamburger1967computation` show'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 733, 985, 992, 1024. *Example:* mid-sentence 'Theorem'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 948. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 939. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 953. *Example:* plot() without lw=.


## Strengths

- Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (7 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (26 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (15 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (11 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
6. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
7. `qe-ref-001` — Use correct citation style (2 occurrences).
