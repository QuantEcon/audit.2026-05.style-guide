# odu

- **Series:** lecture-python.myst
- **File:** `lectures/odu.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-006` ×7; `qe-writing-004` ×1; `qe-writing-008` ×23. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×6; `qe-fig-003` ×3; `qe-fig-006` ×1, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 8.5/10 | `qe-link-001` ×4. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 8. *Lines:* 63, 67, 225, 884, 1022, 1023. *Example:* spelled-out `gamma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 233, 451, 466, 754, 846, 981, 1041. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 222, 448, 462, 750, 782, 950. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 70, 82, 116, 242, 484, 499, 1064. *Example:* H3 Title Case: 'Model Features' (Features).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 23. *Lines:* 42, 102, 129, 131, 139, 149, 260, 863, 944, 945, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 850, 1047, 1054. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 756, 847. *Example:* plot() without lw=.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 4. *Lines:* 38, 41, 861, 1071. *Example:* full URL to own series (python.quantecon.org).
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 79. *Example:* {cite} in author position: '{cite}`McCall1970` and'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 705. *Example:* mid-sentence 'Distribution'.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 849. *Example:* axis label `Time`.


## Strengths

- Math, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (7 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
3. `qe-code-002` — Use Unicode symbols for Greek letters in code (8 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
5. `qe-ref-001` — Use correct citation style (2 occurrences).
6. `qe-link-001` — Use markdown style links for lectures in same lecture series (4 occurrences).
7. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
