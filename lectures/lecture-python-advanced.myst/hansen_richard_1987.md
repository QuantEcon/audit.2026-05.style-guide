# hansen_richard_1987

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hansen_richard_1987.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×2; `qe-writing-004` ×7; `qe-writing-001` ×8. |
| Math         | 5/10  | `qe-math-010` (proposed) ×75. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 75. *Lines:* 74, 87, 111, 150, 202, 260, 268, 292, 299, 323, …. *Example:* bare expectation `E(`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 8. *Lines:* 60, 319, 627, 631, 1055, 1062, 1067, 1072. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 7. *Lines:* 399, 584, 918, 938. *Example:* mid-sentence 'Law'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 311, 949. *Example:* H2 Title Case: 'The Riesz representation: the stochastic discount factor' (Riesz).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 658, 661. *Example:* spelled-out `Sigma`.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 725. *Example:* figsize=.


## Strengths

- Figures, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 8 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (75 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (7 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (8 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
6. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
