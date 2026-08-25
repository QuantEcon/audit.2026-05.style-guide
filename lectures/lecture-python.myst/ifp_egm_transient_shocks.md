# ifp_egm_transient_shocks

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_egm_transient_shocks.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×8; `qe-writing-008` ×2. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 9/10  | `qe-code-004` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×7; `qe-fig-003` ×3; `qe-fig-008` ×10, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 6. *Lines:* 590, 592, 595, 598, 601, 604. *Example:* time.time(.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 365, 616, 631, 795, 933, 982, 1048. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 368, 369, 618, 619, 656, 658, 937, 944, 994, 1068. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 115, 116, 122. *Example:* apostrophe transpose `u'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 59, 174, 189, 377, 384, 814, 821, 894. *Example:* H2 Title Case: 'The Household Problem' (Household, Problem).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 805, 940, 947. *Example:* .set(xlabel='assets', title=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 686, 1017. *Example:* {cite} in narrative flow: 'see {cite}`'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 570, 706. *Example:* 2 spaces.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 934. *Example:* figsize=.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (8 occurrences).
2. `qe-math-002` — Use \top for transpose notation (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (7 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
5. `qe-ref-001` — Use correct citation style (2 occurrences).
6. `qe-fig-008` — Use lw=2 for line charts (10 occurrences).
7. `qe-code-004` — Use quantecon Timer context manager (6 occurrences).
