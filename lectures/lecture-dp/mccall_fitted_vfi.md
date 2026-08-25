# mccall_fitted_vfi

- **Series:** lecture-dp
- **File:** `lectures/mccall_fitted_vfi.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-001` ×1. |
| Math         | 8/10  | `qe-math-004` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×6; `qe-fig-003` ×4; `qe-fig-001` ×5, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 408, 451, 563, 772, 861. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 210, 407, 448, 557, 812, 852. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 571, 581, 597, 782. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 223, 224, 823. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 2. *Lines:* 187, 188. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 842. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 203. *Example:* {cite} in narrative flow: '   {cite}`'.


## Strengths

- Writing, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (5 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
