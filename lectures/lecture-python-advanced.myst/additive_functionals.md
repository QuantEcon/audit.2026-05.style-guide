# additive_functionals

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/additive_functionals.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | `qe-writing-008` ×21. |
| Math         | 4/10  | `qe-math-010` (proposed) ×16; `qe-math-011` (proposed) ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3.5/10 | `qe-fig-003` ×11; `qe-fig-005` ×10; `qe-fig-008` ×8, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 422, 622, 718, 1059, 1085, 1255, 1312, 1367, 1425. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 11. *Lines:* 431, 441, 451, 456, 526, 610, 686, 721, 724, 1258, …. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 10. *Lines:* 696, 874, 930, 964, 1054, 1074, 1220, 1308, 1352, 1414. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 1061, 1086, 1088, 1090, 1314, 1426, 1429, 1432. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 16. *Lines:* 999, 1005, 1008, 1013, 1030, 1099, 1295, 1297, 1328, 1339, …. *Example:* non-blackboard `\mathrm{Var}`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 21. *Lines:* 38, 44, 57, 66, 68, 89, 207, 225, 229, 863, …. *Example:* 2 spaces.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 227, 1279, 1285. *Example:* raw link to python.quantecon.org.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 3. *Lines:* 101, 103, 120. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 68, 82. *Example:* {cite} in author position: '{cite}`Hansen_2012_Eca` and'.

### Low severity
_None found._


## Strengths

- Writing, Code, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (16 occurrences).
2. `qe-fig-003` — No matplotlib embedded titles (11 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (10 occurrences).
4. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (3 occurrences).
5. `qe-link-002` — Use doc links for cross-series references (3 occurrences).
6. `qe-ref-001` — Use correct citation style (2 occurrences).
7. `qe-writing-008` — Remove excessive whitespace between words (21 occurrences).
