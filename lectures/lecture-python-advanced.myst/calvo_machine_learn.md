# calvo_machine_learn

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/calvo_machine_learn.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×193; `qe-writing-001` ×1. |
| Math         | 3.5/10 | `qe-math-002` ×13; `qe-math-004` ×4; `qe-math-013` (proposed) ×1. |
| Code         | 7/10  | `qe-code-003` ×4; `qe-code-002` ×1; `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×4; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 13. *Lines:* 860, 862, 865, 867, 870, 879, 880, 881. *Example:* `^T` transpose in `\vec{\beta}^T`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 193. *Lines:* 18, 19, 21, 24, 27, 29, 31, 36, 39, 43, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 4. *Lines:* 399. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 656, 941. *Example:* %%time.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 1035, 1221, 1262, 1308. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 1223, 1264, 1313. *Example:* plot() without lw=.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 4. *Lines:* 865, 867, 870, 872. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1151. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 454. *Example:* spelled-out `beta`.
- **[qe-math-013 (proposed)]** — Reference equations via {eq}`label`. *Count:* 1. *Lines:* 383. *Example:* manual reference 'formula (1)'.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (13 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (4 occurrences).
3. `qe-code-003` — Package installation at lecture top (4 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (193 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-math-013` (proposed) — Reference equations via {eq}`label` (1 occurrence).
