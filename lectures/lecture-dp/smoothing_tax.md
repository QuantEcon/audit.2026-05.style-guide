# smoothing_tax

- **Series:** lecture-dp
- **File:** `lectures/smoothing_tax.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-008` ×60; `qe-writing-004` ×1; `qe-writing-001` ×1. |
| Math         | 8.5/10 | `qe-math-002` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×7; `qe-fig-006` ×9; `qe-fig-005` ×2, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 250, 257, 284, 292, 585, 593, 604. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 255, 263, 289, 298, 590, 600, 607, 608, 613. *Example:* axis label `Periods`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 20. *Lines:* 251, 252, 253, 258, 259, 260, 285, 286, 287, 293, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 364. *Example:* `^T` transpose in `R^T`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 60. *Lines:* 26, 40, 42, 44, 46, 49, 68, 72, 75, 76, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 248, 282. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 239, 281. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 80. *Example:* raw link to python-intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 847. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 80. *Example:* mid-sentence 'Savings'.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (7 occurrences).
2. `qe-fig-006` — Lowercase axis labels (9 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
4. `qe-math-002` — Use \top for transpose notation (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (60 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
7. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
