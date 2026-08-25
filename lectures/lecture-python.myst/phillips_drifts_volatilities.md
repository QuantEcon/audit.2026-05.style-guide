# phillips_drifts_volatilities

- **Series:** lecture-python.myst
- **File:** `lectures/phillips_drifts_volatilities.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×2; `qe-writing-004` ×4. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8/10  | `qe-code-002` ×4; `qe-code-004` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-004` ×11; `qe-fig-003` ×4; `qe-fig-001` ×13, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 13. *Lines:* 422, 1255, 1397, 1758, 1828, 2028, 2342, 2543, 2650, 2858, …. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 11. *Lines:* 410, 1384, 1821, 2134, 2335, 2503, 2536, 2643, 2760, 2851, …. *Example:* caption of 7 words.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 564, 2577. *Example:* H2 Title Case: 'A Metropolis-within-Gibbs sampler' (Metropolis-within-Gibbs).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 1754, 3017. *Example:* spelled-out `omega`.
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 3. *Lines:* 1008, 1081, 1115. *Example:* time.perf_counter(.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 1402, 1406, 2669, 2671. *Example:* .set_title.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 67, 107, 1781, 3323. *Example:* mid-sentence 'Inflation'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 3358. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Math, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (8 parenthetical, 20 in-text).

## Recommended actions

1. `qe-fig-004` — Caption formatting conventions (11 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (13 occurrences).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
