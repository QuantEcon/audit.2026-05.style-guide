# ifp_egm

- **Series:** lecture-dp
- **File:** `lectures/ifp_egm.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×9; `qe-writing-008` ×3. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 9/10  | `qe-code-004` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×1; `qe-fig-008` ×8. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 6. *Lines:* 669, 671, 674, 677, 680, 683. *Example:* time.time(.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 476, 695, 710, 789, 906. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 479, 480, 697, 698, 731, 733, 797, 798. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 260, 261, 267. *Example:* apostrophe transpose `u'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 73, 165, 207, 251, 325, 340, 488, 495, 767. *Example:* H2 Title Case: 'The Household Problem' (Household, Problem).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 916. *Example:* .set(xlabel='assets', title=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 49, 761. *Example:* {cite} in author position: '{cite}`Reiter2009`  and'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 49, 823. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (9 occurrences).
2. `qe-math-002` — Use \top for transpose notation (3 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
4. `qe-ref-001` — Use correct citation style (2 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (8 occurrences).
7. `qe-code-004` — Use quantecon Timer context manager (6 occurrences).
