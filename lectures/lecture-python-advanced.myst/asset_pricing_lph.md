# asset_pricing_lph

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/asset_pricing_lph.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-004` ×2; `qe-writing-001` ×2; `qe-writing-008` ×76, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×26; `qe-math-006` ×2; `qe-math-002` ×2. |
| Code         | 7/10  | `qe-code-002` ×13. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 7.5/10 | `qe-link-001` ×3; `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 13. *Lines:* 357, 358, 359, 360, 367, 373, 374. *Example:* spelled-out `alpha`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 508. *Example:* \prime transpose.
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 2. *Lines:* 684, 713. *Example:* bare \begin{align*} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 26. *Lines:* 118, 144, 266, 307, 394, 414, 470, 477, 633, 640, …. *Example:* bare expectation `E(`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 76. *Lines:* 22, 23, 25, 35, 39, 44, 51, 57, 63, 83, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 383. *Example:* plt.title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 380, 381, 387. *Example:* plot() without lw=.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 3. *Lines:* 57, 59, 93. *Example:* full URL to own series (python-advanced.quantecon.org).
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 96. *Example:* raw link to python.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 28, 83, 105. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 105, 457. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 725, 773. *Example:* mid-sentence 'Problem'.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 352. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 747. *Example:* i.i.d..


## Strengths

- Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (26 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (13 occurrences).
3. `qe-math-006` — Use aligned environment correctly for PDF compatibility (2 occurrences).
4. `qe-math-002` — Use \top for transpose notation (2 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (2 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
7. `qe-ref-001` — Use correct citation style (4 occurrences).
