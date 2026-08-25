# blackwell_kihlstrom

- **Series:** lecture-python.myst
- **File:** `lectures/blackwell_kihlstrom.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×6; `qe-writing-006` ×1; `qe-writing-008` ×6. |
| Math         | 3.5/10 | `qe-math-010` (proposed) ×13; `qe-math-004` ×2; `qe-math-008` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-004` ×2; `qe-fig-001` ×8. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 505, 566, 664, 840, 908, 994, 1074, 1130. *Example:* figsize=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 13. *Lines:* 100, 377, 389, 538, 586, 739, 861, 1335, 1341, 1359. *Example:* non-blackboard `\Pr`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 362, 366, 397, 404, 859, 877. *Example:* 3 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 1174. *Example:* H2 Title Case: 'The Data Processing Inequality and Coarse-Graining' (Data, Processing, Inequality, Coarse-Graining).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 35, 40, 44, 48. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 1048, 1103. *Example:* caption of 7 words.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 2. *Lines:* 818. *Example:* \mathbf.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 818. *Example:* ones vector `\mathbf{1}` used 2x with no 'vector of ones' explanation in the prose.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 703. *Example:* {cite} in narrative flow: '{cite}`'.


## Strengths

- Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (13 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (6 occurrences).
3. `qe-math-004` — Do not use bold face for matrices or vectors (2 occurrences).
4. `qe-fig-004` — Caption formatting conventions (2 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-ref-001` — Use correct citation style (1 occurrence).
7. `qe-math-008` — Explain special notation (vectors/matrices) (1 occurrence).
