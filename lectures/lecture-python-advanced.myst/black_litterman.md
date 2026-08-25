# black_litterman

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/black_litterman.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-001` ×10; `qe-writing-004` ×3; `qe-writing-008` ×7. |
| Math         | 3/10  | `qe-math-002` ×36; `qe-math-010` (proposed) ×14; `qe-math-004` ×24, +1 more. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×5; `qe-fig-006` ×7; `qe-fig-005` ×4, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8.5/10 | `qe-link-001` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 203, 320, 413, 661, 715, 1261, 1397. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 204, 321, 427, 1268, 1401. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 7. *Lines:* 212, 326, 673, 674, 728, 729, 1403. *Example:* axis label `Assets`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 205, 206, 322, 323, 414, 416, 418, 428, 429, 430, …. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 36. *Lines:* 121, 130, 244, 252, 527, 555, 556, 583, 592, 748, …. *Example:* apostrophe transpose `w'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 24. *Lines:* 97, 104, 110, 121, 153, 261, 280, 292, 341, 357, …. *Example:* {\bf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 14. *Lines:* 759, 760, 762, 778, 821, 1025, 1035, 1111, 1117, 1124, …. *Example:* missing braces: `\mathbb E`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 6. *Lines:* 455, 463, 512, 518, 1161, 1215. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 10. *Lines:* 133, 569, 754, 847, 905, 954, 1127, 1275, 1333, 1414. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 38, 42, 66, 116, 837. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 172, 303, 1249, 1369. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 2. *Lines:* 30, 38. *Example:* full URL to own series (python-advanced.quantecon.org).
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 30. *Example:* mid-sentence 'Asset'.

### Low severity
_None found._


## Strengths

- Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (36 occurrences).
2. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (14 occurrences).
3. `qe-writing-001` — Use one sentence per paragraph (10 occurrences).
4. `qe-math-004` — Do not use bold face for matrices or vectors (24 occurrences).
5. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (6 occurrences).
6. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
7. `qe-fig-006` — Lowercase axis labels (7 occurrences).
