# ifp_discrete

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_discrete.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-006` ×2. |
| Math         | 6/10  | `qe-math-001` ×2; `qe-math-002` ×1; `qe-math-005` ×1. |
| Code         | 7.5/10 | `qe-code-002` ×2; `qe-code-004` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 10. *Lines:* 312, 314, 322, 325, 332, 335, 499, 502, 509, 512. *Example:* bare time() reading.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 130. *Example:* apostrophe transpose `a'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 87, 353. *Example:* H2 Title Case: 'Set Up' (Up).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 182. *Example:* spelled-out `rho`.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 132, 145. *Example:* unicode `β` inside a math environment.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 359. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 366. *Example:* plot() without lw=.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 1. *Lines:* 106. *Example:* parenthesised sequence.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (2 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
4. `qe-math-002` — Use \top for transpose notation (1 occurrence).
5. `qe-code-004` — Use quantecon Timer context manager (10 occurrences).
6. `qe-math-005` — Use curly brackets for sequences (1 occurrence).
7. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
