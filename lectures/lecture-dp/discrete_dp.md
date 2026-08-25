# discrete_dp

- **Series:** lecture-dp
- **File:** `lectures/discrete_dp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-001` ×1; `qe-writing-008` ×4. |
| Math         | 4/10  | `qe-math-002` ×6; `qe-math-010` (proposed) ×1; `qe-math-004` ×1, +1 more. |
| Code         | 8/10  | `qe-code-002` ×2; `qe-code-005` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×6; `qe-fig-003` ×1; `qe-fig-002` ×2, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 7/10  | `qe-link-002` ×10. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 552, 566, 750, 862, 882, 916. *Example:* {figure} without :name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 10. *Lines:* 75, 76, 90, 193, 209, 543, 616, 624, 715, 911. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 6. *Lines:* 247, 264, 273, 305, 319, 419. *Example:* apostrophe transpose `s'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 1. *Lines:* 202. *Example:* missing braces: `\mathbb E`.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 933, 934. *Example:* spelled-out `beta`.
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 3. *Lines:* 844, 845, 846. *Example:* %timeit.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 751, 865, 885, 925. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 552, 566. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 904. *Example:* .set_title.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 1. *Lines:* 1001. *Example:* \mathbf.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 727. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 183, 285, 543, 951. *Example:* 2 spaces.

### Low severity
- **[qe-math-008]** — Explain special notation (vectors/matrices). *Count:* 1. *Lines:* 1001. *Example:* ones vector `\mathbf{1}` used 1x with no 'vector of ones' explanation in the prose.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 152. *Example:* {cite} in narrative flow: 'of {cite}`'.


## Strengths

- References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (6 occurrences).
2. `qe-link-002` — Use doc links for cross-series references (10 occurrences).
3. `qe-fig-005` — Descriptive figure names for cross-referencing (6 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
5. `qe-math-010` (proposed) — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces (1 occurrence).
6. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
7. `qe-math-004` — Do not use bold face for matrices or vectors (1 occurrence).
