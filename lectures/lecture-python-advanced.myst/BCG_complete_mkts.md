# BCG_complete_mkts

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/BCG_complete_mkts.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×7; `qe-writing-008` ×36. |
| Math         | 7.5/10 | `qe-math-002` ×2. |
| Code         | 9.5/10 | `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×2; `qe-fig-010` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 643, 809. *Example:* apostrophe transpose `u'`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 7. *Lines:* 324, 563, 613, 705, 851, 854, 1140. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 36. *Lines:* 39, 56, 67, 73, 78, 160, 217, 289, 298, 302, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 1168, 1173. *Example:* %%time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 955, 1092. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1099, 1109. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 873, 1086. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-010]** — Plotly figures require latex directive. *Count:* 1. *Lines:* 1. *Example:* plotly used with no {only} latex directive.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 56, 57. *Example:* raw link to python.quantecon.org.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 956. *Example:* plot() without lw=.


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (2 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (7 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (2 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (36 occurrences).
7. `qe-fig-010` — Plotly figures require latex directive (1 occurrence).
