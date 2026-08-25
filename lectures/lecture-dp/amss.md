# amss

- **Series:** lecture-dp
- **File:** `lectures/amss.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×2; `qe-writing-008` ×67. |
| Math         | 7/10  | `qe-math-003` ×2; `qe-math-010` (proposed) ×1. |
| Code         | 9.5/10 | `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×3; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 451. *Example:* bare expectation `E_{t} \left[`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 67. *Lines:* 27, 31, 33, 146, 149, 170, 181, 198, 293, 297, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 879, 1012. *Example:* %%time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 900, 1036, 1079. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 909, 1040, 1084. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 889, 1022, 1071. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 907, 1039, 1083. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 802, 815. *Example:* pmatrix environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 513, 1092. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
2. `qe-math-003` — Use square brackets for matrix notation (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
5. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (67 occurrences).
7. `qe-fig-008` — Use lw=2 for line charts (3 occurrences).
