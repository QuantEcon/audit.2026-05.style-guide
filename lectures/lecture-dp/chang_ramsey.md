# chang_ramsey

- **Series:** lecture-dp
- **File:** `lectures/chang_ramsey.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×2; `qe-writing-001` ×2; `qe-writing-008` ×26. |
| Math         | 7.5/10 | `qe-math-002` ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×2; `qe-fig-008` ×5, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 941, 1054, 1071, 1101, 1124. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 1057, 1079, 1104, 1105, 1131. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 759. *Example:* apostrophe transpose `Z'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 26. *Lines:* 36, 44, 46, 109, 125, 137, 214, 232, 249, 270, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 1072, 1106, 1125. *Example:* .suptitle.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1053, 1100. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 44, 581. *Example:* {cite} in narrative flow: '  {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 831, 851. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 852, 887. *Example:* mid-sentence 'Step'.

### Low severity
_None found._


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
5. `qe-ref-001` — Use correct citation style (2 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (26 occurrences).
