# business_cycle

- **Series:** lecture-python-intro
- **File:** `lectures/business_cycle.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, code, figures, links  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | `qe-writing-004` ×1; `qe-writing-001` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | 9/10  | `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-004` ×2; `qe-fig-006` ×1; `qe-fig-008` ×7, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 162, 375, 378, 381, 471, 648, 726. *Example:* plot() without lw=.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 28. *Example:* non-Anaconda import with no install cell: ['pandas_datareader'].
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 628, 756. *Example:* caption of 8 words.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 601. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 623. *Example:* mid-sentence 'Consumer'.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 53. *Example:* style override.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 736. *Example:* axis label `YoY real output change (%)`.


## Strengths

- Code, Links score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-004` — Caption formatting conventions (2 occurrences).
2. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
3. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
4. `qe-code-003` — Package installation at lecture top (1 occurrence).
5. `qe-fig-006` — Lowercase axis labels (1 occurrence).
6. `qe-fig-008` — Use lw=2 for line charts (7 occurrences).
7. `qe-fig-001` — Do not set figure size unless necessary (1 occurrence).
