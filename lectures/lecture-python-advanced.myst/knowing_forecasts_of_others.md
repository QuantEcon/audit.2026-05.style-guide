# knowing_forecasts_of_others

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/knowing_forecasts_of_others.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-001` ×8; `qe-writing-009` (proposed) ×7; `qe-writing-004` ×4, +1 more. |
| Math         | 3/10  | `qe-math-003` ×26; `qe-math-010` (proposed) ×4; `qe-math-011` (proposed) ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-010` ×1. |
| References   | 7/10  | `qe-ref-001` ×11. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 26. *Lines:* 828, 830, 832, 834, 836, 848, 855, 862, 869, 876, …. *Example:* array used as matrix.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 477, 543, 563, 733. *Example:* bare expectation `E(`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 11. *Lines:* 36, 74, 1554, 1559, 1565, 1570, 1610, 1641, 1643, 1646. *Example:* {cite} in author position: '{cite}`townsend` showed'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 8. *Lines:* 83, 225, 229, 270, 290, 387, 774, 1643. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 144. *Lines:* 35, 36, 41, 44, 46, 60, 62, 66, 71, 74, …. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 7. *Lines:* 163, 176, 479, 536, 1416, 1494, 1528. *Example:* i.i.d..

### Medium severity
- **[qe-fig-010]** — Plotly figures require latex directive. *Count:* 1. *Lines:* 1. *Example:* plotly used with no {only} latex directive.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 2. *Lines:* 904, 1190. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 119, 186. *Example:* mid-sentence 'Expectations'.

### Low severity
_None found._


## Strengths

- Code, Figures, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-003` — Use square brackets for matrix notation (26 occurrences).
2. `qe-ref-001` — Use correct citation style (11 occurrences).
3. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (4 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (8 occurrences).
5. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (7 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (4 occurrences).
7. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (2 occurrences).
