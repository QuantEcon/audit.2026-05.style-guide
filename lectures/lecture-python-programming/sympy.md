# sympy

- **Series:** lecture-python-programming
- **File:** `lectures/sympy.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-006` ×3. |
| Math         | 8/10  | `qe-math-001` ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 10/10 | no mechanical violations detected. |
| References   | N/A   | no citations in this lecture. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 45, 371, 515. *Example:* H2 Title Case: 'Getting Started' (Started).

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 200, 313, 664. *Example:* raw link to python.quantecon.org.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 4. *Lines:* 671, 678. *Example:* unicode `θ` inside a math environment.

### Low severity
_None found._


## Strengths

- Code, Figures, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (3 occurrences).
2. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (4 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (3 occurrences).
