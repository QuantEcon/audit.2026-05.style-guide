# wald_friedman_2

- **Series:** lecture-python.myst
- **File:** `lectures/wald_friedman_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×6; `qe-writing-004` ×2; `qe-writing-001` ×2, +2 more. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×8. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×5; `qe-fig-005` ×5; `qe-fig-008` ×6, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 8.5/10 | `qe-link-001` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 188, 192, 534, 713, 719. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 176, 254, 528, 551, 637. *Example:* {figure} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 532, 533, 593, 594, 595, 596. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 8. *Lines:* 131, 142, 278, 315, 321, 327, 349, 457. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 100, 205, 225, 265, 540, 728. *Example:* H2 Title Case: 'A Dynamic Programming Approach' (Dynamic, Programming, Approach).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 43. *Lines:* 36, 38, 40, 46, 57, 66, 80, 83, 117, 120, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 97, 179. *Example:* spelled-out `gamma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 186, 531, 591, 710. *Example:* figsize=.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 2. *Lines:* 117, 763. *Example:* full URL to own series (python.quantecon.org).
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 36, 762. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 103. *Example:* mid-sentence 'Programming'.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 2. *Lines:* 46, 66. *Example:* i.i.d..

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 254. *Example:* static image .png.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 764. *Example:* {cite} in narrative flow: '{cite}`'.


## Strengths

- References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (6 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (8 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
7. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (2 occurrences).
