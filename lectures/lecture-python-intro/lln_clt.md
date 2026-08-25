# lln_clt

- **Series:** lecture-python-intro
- **File:** `lectures/lln_clt.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | 4/10  | `qe-math-010` (proposed) ×21; `qe-math-004` ×1; `qe-math-008` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×5; `qe-fig-001` ×3; `qe-fig-008` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 9/10  | `qe-admon-001` ×1. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 260, 302, 475, 526, 679. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 21. *Lines:* 59, 71, 72, 113, 127, 154, 165, 178, 183, 190, …. *Example:* missing braces: `\mathbb E`.

### Medium severity
- **[qe-admon-001]** — Use gated syntax for executable code in exercises. *Count:* 1. *Lines:* 567. *Example:* code cell inside non-gated {exercise}.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 490, 541, 685. *Example:* figsize=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 31. *Example:* raw link to python.quantecon.org.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 580. *Example:* \mathbf.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 495. *Example:* plot() without lw=.
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 580. *Example:* ones vector `\mathbf 1` used 1x with no 'vector of ones' explanation in the prose.


## Strengths

- Writing, Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (21 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-math-004` — Do not use bold face for matrices or vectors (1 occurrence).
4. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
5. `qe-admon-001` — Use gated syntax for executable code in exercises (1 occurrence).
6. `qe-math-008` — Explain special notation (vectors/matrices) (1 occurrence).
7. `qe-fig-001` — Do not set figure size unless necessary (3 occurrences).
