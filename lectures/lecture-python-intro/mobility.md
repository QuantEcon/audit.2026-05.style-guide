# mobility

- **Series:** lecture-python-intro
- **File:** `lectures/mobility.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-004` ×2; `qe-writing-006` ×1. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×4. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-004` ×1, +1 more. |
| References   | 7/10  | `qe-ref-001` ×19. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 92, 899, 904, 905. *Example:* missing braces: `\mathbb P`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 19. *Lines:* 248, 286, 298, 360, 504, 590, 597, 771, 804, 984, …. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 246. *Example:* H3 Title Case: 'The Shorrocks index' (Shorrocks).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 669. *Example:* .set_title.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 597. *Example:* mid-sentence 'Income'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 666. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 658. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1013. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-ref-001` — Use correct citation style (19 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-fig-005` — Descriptive figure names for cross-referencing (1 occurrence).
7. `qe-fig-004` — Caption formatting conventions (1 occurrence).
