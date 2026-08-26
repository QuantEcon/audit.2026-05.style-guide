# os_stochastic

- **Series:** lecture-dp
- **File:** `lectures/os_stochastic.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×11; `qe-writing-004` ×1; `qe-writing-008` ×1. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×4. |
| Code         | 9.5/10 | `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×5. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 667, 688, 762, 788, 849. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 122, 203, 206, 227. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 11. *Lines:* 74, 155, 249, 291, 329, 372, 443, 551, 596, 718, …. *Example:* H2 Title Case: 'The Model' (Model).

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 167, 187, 273. *Example:* raw link to dp.quantecon.org.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 320. *Example:* mid-sentence 'Theorem'.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 843. *Example:* %%time.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 818. *Example:* 2 spaces.


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (11 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
4. `qe-link-002` — Use doc links for cross-series references (3 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
7. `qe-code-004` — Use quantecon Timer context manager (1 occurrence).
