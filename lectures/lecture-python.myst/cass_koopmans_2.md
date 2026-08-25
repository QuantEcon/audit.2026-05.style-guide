# cass_koopmans_2

- **Series:** lecture-python.myst
- **File:** `lectures/cass_koopmans_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×13; `qe-writing-008` ×61. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×2; `qe-fig-008` ×4, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7/10  | `qe-link-002` ×2; `qe-link-001` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 13. *Lines:* 75, 127, 134, 180, 221, 241, 318, 404, 414, 502, …. *Example:* H2 Title Case: 'Review of Cass-Koopmans Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 61. *Lines:* 29, 30, 37, 39, 45, 56, 63, 136, 138, 163, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 856, 894, 976. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 872, 908, 984, 987. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 853, 890. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 871, 907, 983, 986. *Example:* plot() without lw=.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 2. *Lines:* 52, 426. *Example:* full URL to own series (python.quantecon.org).
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 53, 427. *Example:* raw link to python-advanced.quantecon.org.

### Low severity
_None found._


## Strengths

- Math, Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (13 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
4. `qe-link-001` — Use markdown style links for lectures in same lecture series (2 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (61 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (4 occurrences).
