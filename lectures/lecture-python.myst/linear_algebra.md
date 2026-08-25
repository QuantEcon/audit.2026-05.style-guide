# linear_algebra

- **Series:** lecture-python.myst
- **File:** `lectures/linear_algebra.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×18; `qe-writing-001` ×4; `qe-writing-004` ×1, +1 more. |
| Math         | 5/10  | `qe-math-002` ×114. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-007` ×8; `qe-fig-005` ×5; `qe-fig-001` ×5, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 6.5/10 | `qe-link-002` ×6; `qe-link-001` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 104, 174, 298, 695, 951. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 103, 170, 294, 682, 941. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 8. *Lines:* 107, 109, 177, 179, 700, 702, 954, 956. *Example:* spine removal.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 6. *Lines:* 68, 206, 610, 616, 634, 1379. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 114. *Lines:* 231, 239, 476, 478, 847, 913, 1131, 1132, 1154, 1155, …. *Example:* apostrophe transpose `x'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 18. *Lines:* 124, 220, 391, 426, 486, 637, 656, 755, 778, 814, …. *Example:* H3 Title Case: 'Vector Operations' (Operations).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 5. *Lines:* 88, 352, 1006, 1146, 1217. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 716, 725. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 1146, 1217, 1378, 1381. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 1166. *Example:* mid-sentence 'Theory'.

### Low severity
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 847. *Example:* full URL to own series (python.quantecon.org).


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (114 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (18 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (6 occurrences).
4. `qe-fig-007` — Keep figure box and spines (8 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
7. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
