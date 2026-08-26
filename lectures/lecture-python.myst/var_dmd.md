# var_dmd

- **Series:** lecture-python.myst
- **File:** `lectures/var_dmd.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×5; `qe-writing-004` ×16; `qe-writing-008` ×180, +1 more. |
| Math         | 5/10  | `qe-math-002` ×28. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 7.5/10 | `qe-ref-001` ×6. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 28. *Lines:* 72, 75, 79, 81, 97, 120, 160, 181, 196, 253, …. *Example:* apostrophe transpose `X'`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 6. *Lines:* 272, 443, 455, 518, 598, 726. *Example:* {cite} in narrative flow: 'and {cite}`'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 16. *Lines:* 106, 133, 265, 272, 275, 283, 285, 294, 369, 487, …. *Example:* mid-sentence 'Case'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 23, 261, 720, 821, 836. *Example:* H2 Title Case: 'First-Order Vector Autoregressions' (Vector, Autoregressions).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 180. *Lines:* 16, 32, 33, 40, 47, 53, 55, 63, 75, 77, …. *Example:* 2 spaces.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 692. *Example:* bare URL to python-advanced.quantecon.org.

### Low severity
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 32. *Example:* i.i.d..


## Strengths

- Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (28 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (5 occurrences).
3. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (16 occurrences).
4. `qe-ref-001` — Use correct citation style (6 occurrences).
5. `qe-writing-008` — Remove excessive whitespace between words (180 occurrences).
6. `qe-link-002` — Use doc links for cross-series references (1 occurrence).
7. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (1 occurrence).
