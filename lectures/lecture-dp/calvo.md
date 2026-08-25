# calvo

- **Series:** lecture-dp
- **File:** `lectures/calvo.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×4; `qe-writing-001` ×2; `qe-writing-008` ×242. |
| Math         | 5.5/10 | `qe-math-002` ×10. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×2; `qe-fig-001` ×5; `qe-fig-008` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 8/10  | `qe-link-002` ×4. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 1051, 1352, 1390, 1414, 1447. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 10. *Lines:* 272, 485, 489, 501. *Example:* apostrophe transpose `}'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 242. *Lines:* 38, 41, 43, 45, 46, 51, 57, 59, 61, 63, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1263, 1463. *Example:* .set_title.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 67, 193, 288, 765. *Example:* raw link to python-intro.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 122, 153, 445. *Example:* {cite} in narrative flow: '.  {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 287, 416. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 67, 193, 765, 817. *Example:* mid-sentence 'Control'.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 931. *Example:* spelled-out `beta`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1454. *Example:* plot() without lw=.


## Strengths

- Code, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (10 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-link-002` — Use doc links for cross-series references (4 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
6. `qe-ref-001` — Use correct citation style (3 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (242 occurrences).
