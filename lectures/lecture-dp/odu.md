# odu

- **Series:** lecture-dp
- **File:** `lectures/odu.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-006` ×7; `qe-writing-004` ×1; `qe-writing-008` ×23. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×5; `qe-fig-003` ×3; `qe-fig-006` ×1, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 8/10  | `qe-link-002` ×4. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 233, 451, 466, 754, 846, 981, 1041. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 222, 448, 462, 750, 782. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 756, 847, 993, 1022, 1023, 1043, 1044, 1050, 1051. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 70, 82, 116, 242, 484, 499, 1064. *Example:* H3 Title Case: 'Model Features' (Features).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 23. *Lines:* 42, 102, 129, 131, 139, 149, 260, 863, 944, 945, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 850, 1047, 1054. *Example:* .set_title.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 38, 41, 861, 1071. *Example:* raw link to python.quantecon.org.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 705. *Example:* mid-sentence 'Distribution'.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 849. *Example:* axis label `Time`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 79. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.


## Strengths

- Math, Code, References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (7 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-link-002` — Use doc links for cross-series references (4 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (3 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
6. `qe-writing-008` — Remove excessive whitespace between words (23 occurrences).
7. `qe-ref-001` — Use correct citation style (1 occurrence).
