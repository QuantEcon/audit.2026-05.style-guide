# polars

- **Series:** lecture-python-programming
- **File:** `lectures/polars.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-004` ×2; `qe-writing-001` ×4. |
| Math         | N/A   | no mathematical content. |
| Code         | 9/10  | `qe-code-004` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×4; `qe-fig-003` ×1; `qe-fig-001` ×2, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 10. *Lines:* 430, 436, 439, 445, 482, 486, 493, 501, 508, 517. *Example:* time.perf_counter(.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 706, 785. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 593. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 322, 584, 701, 784. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 87, 317, 532, 662. *Example:* 3 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 76, 87. *Example:* mid-sentence 'Series'.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 591. *Example:* plot() without lw=.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
5. `qe-code-004` — Use quantecon Timer context manager (10 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (2 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (1 occurrence).
