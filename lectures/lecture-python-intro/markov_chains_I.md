# markov_chains_I

- **Series:** lecture-python-intro
- **File:** `lectures/markov_chains_I.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-001` ×1; `qe-writing-008` ×15. |
| Math         | 3/10  | `qe-math-010` (proposed) ×15; `qe-math-004` ×7; `qe-math-003` ×1. |
| Code         | 9.5/10 | `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×4; `qe-fig-002` ×2; `qe-fig-008` ×1. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 9/10  | `qe-admon-001` ×1. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 7. *Lines:* 1258, 1259, 1261. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 145, 165, 332, 333, 343, 546, 547, 548, 620, 1008, …. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 15. *Lines:* 30, 38, 47, 70, 80, 97, 103, 336, 555, 1003, …. *Example:* 2 spaces.

### Medium severity
- **[qe-admon-001]** — Use gated syntax for executable code in exercises. *Count:* 1. *Lines:* 1165. *Example:* code cell inside non-gated {exercise}.
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 490, 494. *Example:* %time.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 105, 1122. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 261, 844, 934, 1206. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 487. *Example:* raw link to python-programming.quantecon.org.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 1. *Lines:* 237. *Example:* array used as matrix.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 711. *Example:* {cite} in author position: '{cite}`sargent2023economic` and'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 231. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 1223. *Example:* plot() without lw=.


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (15 occurrences).
2. `qe-math-004` — Do not use bold face for matrices or vectors (7 occurrences).
3. `qe-ref-001` — Use correct citation style (2 occurrences).
4. `qe-fig-005` — Descriptive figure names for cross-referencing (4 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-math-003` — Use square brackets for matrix notation (1 occurrence).
7. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
