# merging_of_opinions

- **Series:** lecture-python.myst
- **File:** `lectures/merging_of_opinions.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×2; `qe-writing-006` ×1; `qe-writing-004` ×1, +1 more. |
| Math         | 8/10  | `qe-math-011` (proposed) ×4. |
| Code         | 8.5/10 | `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×4; `qe-fig-001` ×8. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 578, 675, 742, 828, 985, 1012, 1041, 1239. *Example:* figsize=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 353. *Example:* H2 Title Case: 'The Beta–Bernoulli model' (Beta).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 60, 568. *Example:* spelled-out `beta`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 588, 599, 607, 624. *Example:* .set_title.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 4. *Lines:* 884, 947. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 290, 312. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 314. *Example:* mid-sentence 'Step'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 229, 1277. *Example:* 2 spaces.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 1307. *Example:* `` {cite} `` in author position: '`` {cite}`DiaconisFreedman1986` `` study'.


## Strengths

- References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
2. `qe-math-011` (proposed) — Distribution names in plain letters, not \mathcal / \mathbb (4 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
4. `qe-code-002` — Use Unicode symbols for Greek letters in code (2 occurrences).
5. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
7. `qe-ref-001` — Use correct citation style (1 occurrence).
