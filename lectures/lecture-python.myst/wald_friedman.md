# wald_friedman

- **Series:** lecture-python.myst
- **File:** `lectures/wald_friedman.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-004` ×4; `qe-writing-001` ×3; `qe-writing-006` ×1, +1 more. |
| Math         | 9/10  | `qe-math-011` (proposed) ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×5; `qe-fig-005` ×5; `qe-fig-006` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-001` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 606, 801, 844, 1177, 1352. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 621, 631, 655, 817, 889. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 326, 402, 738, 1162, 1336. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 81. *Example:* H2 Title Case: 'Source of the Problem' (Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 80. *Lines:* 36, 37, 40, 44, 45, 47, 49, 79, 89, 121, …. *Example:* 2 spaces.

### Medium severity
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 1206. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 36, 89, 129. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 992, 996, 998. *Example:* mid-sentence 'Type'.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 402. *Example:* static image .png.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 780. *Example:* axis label `Jensen–Shannon distance`.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 348. *Example:* full URL to own series (python.quantecon.org).


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-003` — No matplotlib embedded titles (5 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (3 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (80 occurrences).
7. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (1 occurrence).
