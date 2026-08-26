# rational_expectations

- **Series:** lecture-python.myst
- **File:** `lectures/rational_expectations.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-006` ×1; `qe-writing-008` ×30; `qe-writing-001` ×1. |
| Math         | 5.5/10 | `qe-math-002` ×14. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 10/10 | no mechanical violations detected. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 14. *Lines:* 502, 503, 511, 517, 645, 860. *Example:* apostrophe transpose `Y'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 202. *Example:* H3 Title Case: 'Further Reading' (Reading).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 30. *Lines:* 44, 49, 53, 86, 103, 104, 108, 112, 180, 215, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 690, 787, 884, 944. *Example:* spelled-out `beta`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 973. *Example:* 3 sentences in one paragraph.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 978. *Example:* `` {cite} `` in narrative flow: 'and `` {cite} ``'.


## Strengths

- Figures, References, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (14 occurrences).
2. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
3. `qe-writing-006` — Capitalize lecture titles properly (1 occurrence).
4. `qe-writing-008` — Remove excessive whitespace between words (30 occurrences).
5. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
6. `qe-ref-001` — Use correct citation style (1 occurrence).
