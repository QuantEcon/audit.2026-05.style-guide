# mccall_model

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×12; `qe-writing-001` ×1; `qe-writing-008` ×6. |
| Math         | 3/10  | `qe-math-002` ×12; `qe-math-010` (proposed) ×1; `qe-math-001` ×1, +1 more. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×8; `qe-fig-003` ×2; `qe-fig-008` ×2. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 373, 427, 495, 581, 858, 931, 1049, 1089. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 12. *Lines:* 170, 228, 293, 644, 647, 648, 654, 655, 661, 662, …. *Example:* apostrophe transpose `w'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 104. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 78, 117, 133, 200, 257, 287, 317, 485, 612, 741, …. *Example:* H2 Title Case: 'The McCall Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 52, 111, 174, 202, 351. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 602, 868. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 375, 1178. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 382. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 1. *Lines:* 425. *Example:* unicode `β` inside a math environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 33. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 226. *Example:* ones vector `\mathbf{1}` used 1x with no 'vector of ones' explanation in the prose.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (12 occurrences).
2. `qe-math-002` — Use \top for transpose notation (12 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (8 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (2 occurrences).
5. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-math-001` — Prefer UTF-8 unicode for simple parameter mentions, be consistent (1 occurrence).
