# calvo_abreu

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/calvo_abreu.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×94; `qe-writing-001` ×1. |
| Math         | 9/10  | `qe-math-004` ×1. |
| Code         | 8/10  | `qe-code-003` ×1; `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-008` ×2; `qe-fig-001` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 94. *Lines:* 33, 35, 37, 39, 40, 45, 47, 49, 51, 53, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 275. *Example:* install cell at line 275 of 688 (not near the top).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 573, 579. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 196. *Example:* {\bf.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 39, 357. *Example:* {cite} in author position: '{cite}`Calvo1978` showed'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 203. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 422. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 571. *Example:* figsize=.


## Strengths

- Math, Figures, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (2 occurrences).
2. `qe-writing-008` — Remove excessive whitespace between words (94 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
4. `qe-math-004` — Do not use bold face for matrices or vectors (1 occurrence).
5. `qe-code-003` — Package installation at lecture top (1 occurrence).
6. `qe-code-002` — Use Unicode symbols for Greek letters in code (1 occurrence).
7. `qe-fig-008` — Use lw=2 for line charts (2 occurrences).
