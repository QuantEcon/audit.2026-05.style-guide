# subjective_beliefs_business_cycles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/subjective_beliefs_business_cycles.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×8; `qe-writing-001` ×2; `qe-writing-006` ×1, +1 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×38; `qe-math-002` ×41. |
| Code         | 9/10  | `qe-code-002` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×1; `qe-fig-001` ×5, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 332, 1262, 1470, 1647, 2421. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 41. *Lines:* 1059, 1093, 1108, 1113, 1116, 1122, 1137, 1158, 1175, 1200, …. *Example:* apostrophe transpose `)'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 38. *Lines:* 80, 88, 104, 114, 161, 480, 518, 519, 547, 577, …. *Example:* bare expectation `E_t[`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 8. *Lines:* 642, 758, 764, 844, 959, 1194, 1215. *Example:* mid-sentence 'Step'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1304. *Example:* H2 Title Case: 'A reduced-form emulator of the New Keynesian model' (New).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 2293, 2411. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 917, 1890, 1892. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 1362, 2268. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 1836. *Example:* spelled-out `tau`.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 894. *Example:* caption of 8 words.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 1745. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 498. *Example:* i.i.d..


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (38 occurrences).
2. `qe-math-002` — Use \top for transpose notation (41 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (8 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
5. `qe-fig-005` — Descriptive figure names for cross-referencing (2 occurrences).
6. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
7. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (1 occurrence).
