# ar1_bayes

- **Series:** lecture-python.myst
- **File:** `lectures/ar1_bayes.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 8. *Lines:* 244, 250, 327, 334, 337. *Example:* spelled-out `sigma`.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 220, 383, 557. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 39, 47. *Example:* raw link to intro.quantecon.org.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 441. *Example:* figsize=.


## Strengths

- Writing, Math, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (1 parenthetical, 1 in-text).

## Recommended actions

1. `qe-code-002` — Use Unicode symbols for Greek letters in code (8 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
4. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
