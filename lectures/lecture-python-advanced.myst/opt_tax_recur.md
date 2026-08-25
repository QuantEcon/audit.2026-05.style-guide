# opt_tax_recur

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/opt_tax_recur.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×3; `qe-writing-008` ×106. |
| Math         | 5/10  | `qe-math-002` ×3; `qe-math-003` ×2; `qe-math-010` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×5; `qe-fig-005` ×5; `qe-fig-006` ×1, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 1119, 1174, 1245, 1314, 1389. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 1127, 1175, 1250, 1316, 1395. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 1101, 1173, 1233, 1302, 1368. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 810, 820, 826. *Example:* apostrophe transpose `s'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 1157. *Example:* bare expectation `E_{t}[`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 106. *Lines:* 35, 38, 40, 46, 47, 48, 49, 51, 55, 65, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 1128, 1176, 1394. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 1061, 1072. *Example:* matrix environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 55, 286, 654. *Example:* 3 sentences in one paragraph.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 1254. *Example:* axis label `Initial Government Debt`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 55. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (3 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
5. `qe-math-003` — Use square brackets for matrix notation (2 occurrences).
6. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
7. `qe-writing-008` — Remove excessive whitespace between words (106 occurrences).
