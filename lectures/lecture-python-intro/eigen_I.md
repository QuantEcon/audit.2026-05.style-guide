# eigen_I

- **Series:** lecture-python-intro
- **File:** `lectures/eigen_I.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×5; `qe-writing-006` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-007` ×12; `qe-fig-005` ×10; `qe-fig-003` ×7, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 212, 238, 530, 741, 1032, 1181. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 226, 231, 266, 278, 543, 547, 551. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 10. *Lines:* 129, 194, 517, 602, 730, 996, 1041, 1114, 1179, 1248. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 12. *Lines:* 136, 138, 219, 221, 245, 247, 537, 539, 614, 616, …. *Example:* spine removal.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 5. *Lines:* 34, 918, 925, 939, 965. *Example:* mid-sentence 'Series'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 858. *Example:* H2 Title Case: 'The Neumann Series Lemma' (Series, Lemma).

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 627, 1036. *Example:* plot() without lw=.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 1299. *Example:* axis label `Im`.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-007` — Keep figure box and spines (12 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (10 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (5 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (7 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-fig-006` — Lowercase axis labels (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (6 occurrences).
