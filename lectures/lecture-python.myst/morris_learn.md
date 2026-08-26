# morris_learn

- **Series:** lecture-python.myst
- **File:** `lectures/morris_learn.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-001` ×2; `qe-writing-009` (proposed) ×2; `qe-writing-006` ×1, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 10/10 | no mechanical violations detected. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 330. *Example:* H2 Title Case: 'Two Traders' (Traders).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 48. *Lines:* 40, 49, 54, 55, 56, 58, 104, 105, 128, 140, …. *Example:* 2 spaces.

### Medium severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 158, 620. *Example:* `` {cite} `` in author position: '`` {cite}`harsanyi1968games3` `` argued'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 151, 220. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 154. *Example:* mid-sentence 'Priors'.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 2. *Lines:* 82, 104. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- Math, Code, Figures, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-writing-001` — Use one sentence per paragraph (2 occurrences).
2. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (2 occurrences).
3. `qe-ref-001` — Use correct citation style (2 occurrences).
4. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
5. `qe-writing-008` — Remove excessive whitespace between words (48 occurrences).
6. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (1 occurrence).
