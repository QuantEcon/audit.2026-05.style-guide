# perm_income

- **Series:** lecture-python.myst
- **File:** `lectures/perm_income.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×15; `qe-writing-001` ×4; `qe-writing-008` ×29. |
| Math         | 4.5/10 | `qe-math-002` ×8; `qe-math-010` (proposed) ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×3; `qe-fig-003` ×1; `qe-fig-006` ×1, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 497, 498, 499, 835, 836. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 8. *Lines:* 158, 394, 406, 417, 624, 670. *Example:* apostrophe transpose `A'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 664, 897. *Example:* non-blackboard `\mathrm{Var}`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 15. *Lines:* 56, 107, 186, 217, 274, 331, 421, 526, 531, 636, …. *Example:* H2 Title Case: 'The Savings Problem' (Savings, Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 29. *Lines:* 45, 69, 76, 91, 173, 196, 223, 269, 271, 383, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 495, 512, 827. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 834. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 474, 511, 804. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 859, 899. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 173, 222, 998, 1006. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 502. *Example:* axis label `Time`.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (15 occurrences).
2. `qe-math-002` — Use \top for transpose notation (8 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (3 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-ref-001` — Use correct citation style (3 occurrences).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (3 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (29 occurrences).
