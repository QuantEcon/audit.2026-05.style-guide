# matsuyama

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/matsuyama.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×2; `qe-writing-004` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×5; `qe-fig-003` ×1; `qe-fig-002` ×2, +2 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 656, 709, 721, 741, 801. *Example:* {figure} without :name:.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['ipywidgets'].
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 679, 755, 806. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 2. *Lines:* 709, 721. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 673. *Example:* .set(title=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 336. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 790, 797. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 27. *Example:* mid-sentence 'Innovation'.

### Low severity
- **[qe-fig-009]** — Figure sizing. *Count:* 1. *Lines:* 709. *Example:* :scale: 50 (outside 80–100%).
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 52. *Example:* {cite} in author position: '{cite}`Deneckere1992` and'.


## Strengths

- Math, Code, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (5 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
4. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
5. `qe-fig-003` — No matplotlib embedded titles (1 occurrence).
6. `qe-code-003` — Package installation at lecture top (1 occurrence).
7. `qe-ref-001` — Use correct citation style (1 occurrence).
