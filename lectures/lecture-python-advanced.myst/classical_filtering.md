# classical_filtering

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/classical_filtering.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×2; `qe-writing-008` ×40; `qe-writing-004` ×1. |
| Math         | 3.5/10 | `qe-math-002` ×22; `qe-math-003` ×5. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 22. *Lines:* 77, 113, 119, 129, 408, 409, 429, 430, 470, 982, …. *Example:* \prime transpose.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 5. *Lines:* 371, 444, 461, 484, 491. *Example:* matrix environment.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 345, 602, 724, 1007. *Example:* {cite} in narrative flow: 'see {cite}`'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 40. *Lines:* 27, 39, 59, 81, 87, 93, 106, 107, 122, 132, …. *Example:* 2 spaces.

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 52, 938. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 973. *Example:* mid-sentence 'Prediction'.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (22 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (5 occurrences).
3. `qe-ref-001` — Use correct citation style (5 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (40 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
