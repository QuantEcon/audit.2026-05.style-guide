# smoothing

- **Series:** lecture-dp
- **File:** `lectures/smoothing.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×2; `qe-writing-008` ×52; `qe-writing-004` ×1. |
| Math         | 3/10  | `qe-math-010` (proposed) ×15; `qe-math-002` ×3; `qe-math-011` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×4; `qe-fig-006` ×4; `qe-fig-005` ×2, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×6. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 330, 331, 338, 339, 919, 920, 922, 927, 928, 930. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 6. *Lines:* 87, 121, 126, 263, 362, 793. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 151, 177, 190. *Example:* apostrophe transpose `C'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 177, 184, 204, 236, 378, 381, 398, 493, 799, 809, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 52. *Lines:* 26, 40, 42, 44, 54, 65, 68, 93, 99, 103, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 326, 916. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 329, 337, 918, 926. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 271, 907. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 333, 342, 924, 933. *Example:* axis label `Periods`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 140. *Example:* decorated distribution `{\cal N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 461, 519. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 87. *Example:* mid-sentence 'Savings'.

### Low severity
_None found._


## Strengths

- Code, References score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (15 occurrences).
2. `qe-math-002` — Use \top for transpose notation (3 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
6. `qe-fig-006` — Lowercase axis labels (4 occurrences).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
