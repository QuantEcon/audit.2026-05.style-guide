# networks

- **Series:** lecture-python-intro
- **File:** `lectures/networks.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×2; `qe-writing-004` ×1; `qe-writing-008` ×3. |
| Math         | 6.5/10 | `qe-math-004` ×3; `qe-math-003` ×3. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-004` ×3; `qe-fig-002` ×5, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 5. *Lines:* 171, 238, 248, 507, 714. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 312, 575, 631, 840, 1229. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 85, 160. *Example:* H3 Title Case: 'Example: Aircraft Exports' (Exports).

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 16. *Example:* non-Anaconda import with no install cell: ['quantecon_book_networks'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 118, 431. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 89, 401, 786. *Example:* Title Case caption (Aircraft, Network).
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 3. *Lines:* 549, 605, 618. *Example:* pmatrix environment.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 3. *Lines:* 1034, 1037, 1049. *Example:* \mathbf.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 695, 1146, 1151. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 87. *Example:* mid-sentence 'Data'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 262, 660, 931. *Example:* 2 spaces.

### Low severity
_None found._


## Strengths

- Code, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-006` — Capitalize lecture titles properly (2 occurrences).
2. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
3. `qe-math-004` — Do not use bold face for matrices or vectors (3 occurrences).
4. `qe-math-003` — Use square brackets for matrix notation (3 occurrences).
5. `qe-ref-001` — Use correct citation style (3 occurrences).
6. `qe-fig-004` — Caption formatting conventions (3 occurrences).
7. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
