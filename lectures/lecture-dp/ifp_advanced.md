# ifp_advanced

- **Series:** lecture-dp
- **File:** `lectures/ifp_advanced.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×9; `qe-writing-001` ×2; `qe-writing-008` ×1. |
| Math         | 3/10  | `qe-math-010` (proposed) ×6; `qe-math-002` ×6; `qe-math-004` ×3, +1 more. |
| Code         | 7.5/10 | `qe-code-002` ×2; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×3; `qe-fig-003` ×1; `qe-fig-001` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 179, 182, 213, 234, 235, 294. *Example:* apostrophe transpose `u'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 6. *Lines:* 85, 141, 150, 152, 157. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 73, 77, 193, 198, 226, 251, 265, 668, 675. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 413, 414. *Example:* spelled-out `mu`.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 31. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 652, 752, 829. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 654. *Example:* .set(xlabel='log assets', ylabel='density', title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 638, 719, 796. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 203, 220, 232. *Example:* \mathbf.
- **[qe-math-007]** — Use automatic equation numbering, not manual tags. *Count:* 1. *Lines:* 158. *Example:* \label{ — use $$ … $$ (label) numbering.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 50, 168, 224. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 781, 784. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 513. *Example:* 2 spaces.


## Strengths

- Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (9 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (6 occurrences).
3. `qe-math-002` — Use \top for transpose notation (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-math-004` — Do not use bold face for matrices or vectors (3 occurrences).
6. `qe-ref-001` — Use correct citation style (3 occurrences).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
