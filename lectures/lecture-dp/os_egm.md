# os_egm

- **Series:** lecture-dp
- **File:** `lectures/os_egm.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-006` ×4; `qe-writing-008` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×2; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-005` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 55, 77, 98, 214. *Example:* H2 Title Case: 'Key Idea' (Idea).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 241, 243. *Example:* spelled-out `mu`.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['quantecon'].
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 68, 116. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 318. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Math, Figures, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (4 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
3. `qe-code-003` — Package installation at lecture top (1 occurrence).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (2 occurrences).
