# tsyrennikov_2013

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/tsyrennikov_2013.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×4; `qe-writing-009` (proposed) ×2; `qe-writing-008` ×1. |
| Math         | 3/10  | `qe-math-002` ×54; `qe-math-010` (proposed) ×6. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×6; `qe-fig-005` ×2; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 1880, 1889, 1899, 1909, 1923, 1936. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 1783, 1786, 2049, 2056, 2065, 2073, 2263. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 54. *Lines:* 79, 324, 347, 423, 427, 438, 439, 448, 460, 476, …. *Example:* apostrophe transpose `n_2'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 6. *Lines:* 136, 144, 221, 222, 1004, 1955. *Example:* non-blackboard `\Pr`.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 743. *Example:* install cell at line 743 of 2335 (not near the top).
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 1781, 1854, 2045. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 2162, 2249. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 29, 2149, 2237, 2303. *Example:* 2 sentences in one paragraph.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 2. *Lines:* 48, 100. *Example:* i.i.d..

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 1847. *Example:* caption of 10 words.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 30. *Example:* 2 spaces.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 16 in-text).

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (54 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (6 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (2 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
7. `qe-code-003` — Package installation at lecture top (1 occurrence).
