# back_prop

- **Series:** lecture-python.myst
- **File:** `lectures/back_prop.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×5; `qe-writing-008` ×42; `qe-writing-001` ×1. |
| Math         | 6/10  | `qe-math-003` ×6; `qe-math-002` ×1. |
| Code         | 8.5/10 | `qe-code-003` ×1; `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-010` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 246. *Example:* apostrophe transpose `h'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 258, 262, 266, 272, 277, 299. *Example:* array used as matrix.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 72, 153, 211, 312, 538. *Example:* H2 Title Case: 'A Deep (but not Wide) Artificial Neural Network' (Deep, Wide, Artificial, Neural).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 42. *Lines:* 59, 60, 69, 74, 78, 80, 84, 90, 121, 123, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 21. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-fig-010]** — Plotly figures require latex directive. *Count:* 1. *Lines:* 1. *Example:* plotly used with no {only} latex directive.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 33. *Example:* 3 sentences in one paragraph.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 519. *Example:* %%time.


## Strengths

- Figures, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (6 occurrences).
3. `qe-math-002` — Use \top for transpose notation (1 occurrence).
4. `qe-writing-008` — Remove excessive whitespace between words (42 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-fig-010` — Plotly figures require latex directive (1 occurrence).
7. `qe-code-003` — Package installation at lecture top (1 occurrence).
