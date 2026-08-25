# repeat_mh

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/repeat_mh.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-004` ×5; `qe-writing-001` ×4. |
| Math         | 3/10  | `qe-math-002` ×29; `qe-math-010` (proposed) ×5. |
| Code         | 9.5/10 | `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 29. *Lines:* 198, 205, 207, 215, 228, 229, 236, 239, 252, 671, …. *Example:* apostrophe transpose `W'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 5. *Lines:* 559, 597, 1266, 1315, 1821. *Example:* bare expectation `E(`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 5. *Lines:* 822, 824, 852, 993. *Example:* mid-sentence 'Step'.

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 1046, 1054. *Example:* bare time() reading.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 1770, 1832. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 128, 146, 247, 1803. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 8 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (29 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (5 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (5 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
6. `qe-code-004` — Use quantecon Timer context manager (2 occurrences).
