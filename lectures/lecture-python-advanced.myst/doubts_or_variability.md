# doubts_or_variability

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/doubts_or_variability.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×4; `qe-writing-009` (proposed) ×3. |
| Math         | 3/10  | `qe-math-010` (proposed) ×128; `qe-math-011` (proposed) ×24; `qe-math-004` ×6, +1 more. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-004` ×1; `qe-fig-001` ×9; `qe-fig-008` ×2. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 363, 1182, 1276, 1346, 1453, 1785, 1899, 1951, 2107. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 2537. *Example:* apostrophe transpose `W'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 6. *Lines:* 265, 270, 2193, 2195, 2206. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 128. *Lines:* 173, 191, 219, 225, 227, 235, 242, 249, 257, 265, …. *Example:* bare expectation `E_t(`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 24. *Lines:* 441, 459, 918, 975, 977, 2282, 2590, 2606, 2633, 2647, …. *Example:* decorated distribution `\mathcal{N}`.

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 2113, 2126. *Example:* plot() without lw=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 52. *Example:* {cite} in author position: '{cite}`hansen1983stochastic` and'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 2352, 2582, 2778, 3115. *Example:* 2 sentences in one paragraph.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 3. *Lines:* 984, 2861, 3013. *Example:* iid.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 339. *Example:* Title Case caption (Hansen-Jagannathan).


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (128 occurrences).
2. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (24 occurrences).
3. `qe-math-004` — Do not use bold face for matrices or vectors (6 occurrences).
4. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
5. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (3 occurrences).
6. `qe-ref-001` — Use correct citation style (2 occurrences).
7. `qe-math-002` — Use \top for transpose notation (1 occurrence).
