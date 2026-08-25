# hansen_singleton_1982

- **Series:** lecture-python.myst
- **File:** `lectures/hansen_singleton_1982.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-009` (proposed) ×1; `qe-writing-008` ×1. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×11. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-004` ×1; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 11. *Lines:* 168, 188, 211, 239, 245, 376, 378, 568, 600, 1044, …. *Example:* bare expectation `E_t[`.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 781, 782. *Example:* spelled-out `xi`.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 957. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 932. *Example:* Title Case caption (Carlo).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 606. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 741. *Example:* iid.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.
- Citations distinguish `{cite}` from `{cite:t}` correctly (0 parenthetical, 33 in-text).

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (11 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
3. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (1 occurrence).
4. `qe-fig-004` — Caption formatting conventions (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (1 occurrence).
6. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
