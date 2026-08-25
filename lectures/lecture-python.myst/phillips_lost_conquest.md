# phillips_lost_conquest

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_lost_conquest.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-006` ×2; `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-004` ×5; `qe-fig-003` ×2; `qe-fig-006` ×1, +3 more. |
| References   | 7.5/10 | `qe-ref-001` ×7. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 182, 284, 317, 390, 465. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 5. *Lines:* 175, 277, 305, 372. *Example:* caption of 9 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 183, 188, 286, 319, 320. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 7. *Lines:* 54, 57, 87, 206, 420. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 301, 334. *Example:* H2 Title Case: 'Why the Fed was slow: a counterfactual' (Fed).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 186, 192. *Example:* .set_title.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 417. *Example:* mid-sentence 'Critique'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 451. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 392. *Example:* axis label `Taylor-rule aggressiveness $\phi_\pi$`.


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-ref-001` — Use correct citation style (7 occurrences).
3. `qe-fig-004` — Caption formatting conventions (5 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
6. `qe-fig-006` — Lowercase axis labels (1 occurrence).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
