# long_run_risk_operator

- **Series:** lecture-python.myst
- **File:** `lectures/long_run_risk_operator.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-001` ×6; `qe-writing-004` ×4; `qe-writing-006` ×1, +1 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×2; `qe-fig-008` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 2146, 2150, 2154, 2155, 2161, 2162, 2163. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 391, 955, 1011, 1066. *Example:* non-blackboard `\Pr`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 747, 900, 2764, 2992, 3215, 3278. *Example:* 2 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1726. *Example:* H3 Title Case: 'A Breeden SDF' (Breeden).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 14. *Lines:* 34, 44, 52, 121, 143, 179, 213, 248, 962, 1002, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 1405, 2610. *Example:* caption of 9 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 2948, 3025. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 699, 966, 2557, 2672. *Example:* mid-sentence 'Assumption'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 2144. *Example:* figsize=.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 17 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (6 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
5. `qe-fig-004` — Caption formatting conventions (2 occurrences).
6. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (14 occurrences).
