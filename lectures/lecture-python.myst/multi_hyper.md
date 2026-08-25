# multi_hyper

- **Series:** lecture-python.myst
- **File:** `lectures/multi_hyper.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-001` ×2; `qe-writing-004` ×1; `qe-writing-008` ×13. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 140, 147, 153, 157. *Example:* non-blackboard `\Pr`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 13. *Lines:* 29, 34, 57, 59, 61, 77, 104, 128, 276, 366, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 414, 427. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 254, 440. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 268. *Example:* mid-sentence 'Class'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 403. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 401. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
4. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (13 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
