# os_time_iter

- **Series:** lecture-dp
- **File:** `lectures/os_time_iter.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-006` ×4. |
| Math         | 5/10  | `qe-math-002` ×8; `qe-math-001` ×2. |
| Code         | 9.5/10 | `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-008` ×3. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 8. *Lines:* 109, 144, 145, 153, 154, 190, 210, 354. *Example:* apostrophe transpose `u'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 68, 161, 215, 237. *Example:* H2 Title Case: 'The Euler Equation' (Equation).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 407, 488, 561. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 423, 427, 431. *Example:* plot() without lw=.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 380, 405. *Example:* unicode `σ` inside a math environment.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 562. *Example:* %%time.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 194. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (8 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (4 occurrences).
3. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-ref-001` — Use correct citation style (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
7. `qe-code-004` — Use quantecon Timer context manager (1 occurrence).
