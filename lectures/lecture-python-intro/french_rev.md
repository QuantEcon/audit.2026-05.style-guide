# french_rev

- **Series:** lecture-python-intro
- **File:** `lectures/french_rev.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×5; `qe-writing-001` ×2; `qe-writing-008` ×89, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-007` ×30; `qe-fig-004` ×19; `qe-fig-006` ×6, +3 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 19. *Lines:* 95, 144, 221, 273, 425, 461, 507, 570, 639, 733, …. *Example:* Title Case caption (Spending).
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 6. *Lines:* 124, 1049, 1050, 1134, 1214, 1215. *Example:* axis label `Millions of livres`.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 30. *Lines:* 119, 120, 164, 165, 249, 250, 295, 296, 440, 441, …. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 28. *Lines:* 244, 585, 586, 745, 749, 752, 800, 803, 806, 831, …. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 39, 313, 340, 405, 981. *Example:* {cite} in narrative flow: '     {cite}`'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 57, 80, 342, 979, 990. *Example:* H2 Title Case: 'Data Sources' (Sources).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 89. *Lines:* 19, 22, 24, 30, 32, 34, 36, 43, 45, 47, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 70, 1039, 1194. *Example:* style override.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 1033, 1125, 1193. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 142, 615. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 366. *Example:* mid-sentence 'Wealth'.

### Low severity
_None found._


## Strengths

- Math, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
2. `qe-fig-007` — Keep figure box and spines (30 occurrences).
3. `qe-fig-004` — Caption formatting conventions (19 occurrences).
4. `qe-ref-001` — Use correct citation style (5 occurrences).
5. `qe-fig-006` — Lowercase axis labels (6 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
