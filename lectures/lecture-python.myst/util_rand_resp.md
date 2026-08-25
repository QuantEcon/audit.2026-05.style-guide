# util_rand_resp

- **Series:** lecture-python.myst
- **File:** `lectures/util_rand_resp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×5; `qe-writing-008` ×13. |
| Math         | 5/10  | `qe-math-010` (proposed) ×113. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-008` ×3. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 113. *Lines:* 41, 42, 50, 64, 66, 73, 82, 84, 89, 108, …. *Example:* non-blackboard `\text{Pr}`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 58, 501, 557, 574, 652. *Example:* H3 Title Case: 'Leysieffer and Warner (1976)' (Warner).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 13. *Lines:* 376, 390, 465, 467, 469, 479, 666. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 423, 544, 638. *Example:* plot() without lw=.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 723. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- Code, Figures, References, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (113 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
3. `qe-writing-008` — Remove excessive whitespace between words (13 occurrences).
4. `qe-ref-001` — Use correct citation style (1 occurrence).
5. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
