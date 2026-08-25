# gorman_heterogeneous_households

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/gorman_heterogeneous_households.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-001` ×6; `qe-writing-009` (proposed) ×5; `qe-writing-006` ×1, +1 more. |
| Math         | 8.5/10 | `qe-math-002` ×1. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×5; `qe-fig-003` ×2; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 1762, 1879, 1922, 2052, 2209. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 1759, 1847, 1905, 2038, 2166. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 1048. *Example:* `^T` transpose in `R^T`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 250, 1297, 1462, 1474, 1522, 1990. *Example:* 2 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 308. *Example:* H2 Title Case: 'Dynamic, Stochastic Economy' (Stochastic, Economy).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 42. *Lines:* 32, 35, 39, 53, 58, 61, 67, 72, 76, 80, …. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 5. *Lines:* 326, 1327, 1508, 1523, 1553. *Example:* i.i.d..

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 1270, 1374. *Example:* spelled-out `beta`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1927, 1936. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 1764, 1768. *Example:* plot() without lw=.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 158. *Example:* caption of 7 words.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 15 in-text).

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (6 occurrences).
2. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (5 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
6. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
7. `qe-math-002` — Use \top for transpose notation (1 occurrence).
