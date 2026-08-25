# rob_markov_perf

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/rob_markov_perf.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×55; `qe-writing-004` ×1. |
| Math         | 4/10  | `qe-math-002` ×44; `qe-math-003` ×1. |
| Code         | 7.5/10 | `qe-code-002` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-001` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 6. *Lines:* 470, 495, 536, 736, 741, 797. *Example:* spelled-out `beta`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 44. *Lines:* 122, 123, 124, 125, 126, 127, 157, 184, 185, 186, …. *Example:* apostrophe transpose `x_t'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 55. *Lines:* 37, 39, 47, 61, 62, 65, 66, 69, 71, 77, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 858, 884, 949. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 857, 883, 947. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 779. *Example:* pmatrix environment.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 47. *Example:* {cite} in author position: '{cite}`HansenSargent2008` and'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 458. *Example:* mid-sentence 'Equilibrium'.

### Low severity
_None found._


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (44 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (6 occurrences).
3. `qe-ref-001` — Use correct citation style (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (55 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
7. `qe-math-003` — Use square brackets for matrix notation (1 occurrence).
