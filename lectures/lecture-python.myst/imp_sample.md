# imp_sample

- **Series:** lecture-python.myst
- **File:** `lectures/imp_sample.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-008` ×27; `qe-writing-009` (proposed) ×1. |
| Math         | 5/10  | `qe-math-010` (proposed) ×7; `qe-math-001` ×3. |
| Code         | 7.5/10 | `qe-code-002` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-003` ×1; `qe-fig-004` ×1; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 9. *Lines:* 48, 101, 104, 221, 274, 275, 534, 536, 538. *Example:* spelled-out `beta`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 7. *Lines:* 74, 76, 155, 231, 300, 318, 494. *Example:* bare expectation `E \left[`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 27. *Lines:* 25, 31, 68, 76, 82, 157, 173, 183, 193, 201, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 432. *Example:* .set_title.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 3. *Lines:* 484. *Example:* unicode `μ` inside a math environment.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 424. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 460. *Example:* Title Case caption (Carlo).
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 66. *Example:* i.i.d..


## Strengths

- Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (7 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (9 occurrences).
3. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (3 occurrences).
4. `qe-writing-008` — Remove excessive whitespace between words (27 occurrences).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (1 occurrence).
7. `qe-fig-004` — Caption formatting conventions (1 occurrence).
