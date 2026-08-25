# mccall_q

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_q.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-008` ×79; `qe-writing-004` ×1; `qe-writing-001` ×1. |
| Math         | 7.5/10 | `qe-math-002` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×4; `qe-fig-008` ×7; `qe-fig-001` ×5. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 136, 225, 627, 648, 669. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 137, 212, 628, 629, 649, 670, 681. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 301, 304. *Example:* \prime transpose.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 79. *Lines:* 33, 36, 38, 44, 51, 56, 58, 64, 66, 89, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 128, 221, 625, 639. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 483. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 344. *Example:* mid-sentence 'Law'.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 20. *Example:* {cite} in narrative flow: '{cite}`'.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
3. `qe-writing-008` — Remove excessive whitespace between words (79 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-ref-001` — Use correct citation style (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (7 occurrences).
