# chang_credible

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/chang_credible.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-001` ×5; `qe-writing-004` ×2; `qe-writing-008` ×21. |
| Math         | 7.5/10 | `qe-math-002` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 568. *Example:* apostrophe transpose `Z'`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 5. *Lines:* 459, 612, 725, 792, 797. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 21. *Lines:* 38, 41, 43, 60, 69, 91, 93, 103, 134, 215, …. *Example:* 2 spaces.

### Medium severity
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 726, 765. *Example:* mid-sentence 'Step'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 833. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 828. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (5 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (21 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
