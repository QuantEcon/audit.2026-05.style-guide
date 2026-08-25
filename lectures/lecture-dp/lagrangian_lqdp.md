# lagrangian_lqdp

- **Series:** lecture-dp
- **File:** `lectures/lagrangian_lqdp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×7; `qe-writing-004` ×3; `qe-writing-008` ×72, +1 more. |
| Math         | 3/10  | `qe-math-002` ×73; `qe-math-003` ×6. |
| Code         | 8.5/10 | `qe-code-002` ×1; `qe-code-005` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×5. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 5. *Lines:* 61, 66, 676, 827. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 73. *Lines:* 87, 94, 102, 107, 113, 125, 128, 132, 161, 162, …. *Example:* apostrophe transpose `)'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 341, 356, 815, 817, 818, 820. *Example:* matrix environment.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 70, 236, 258, 672, 699, 705, 778. *Example:* H2 Title Case: 'Undiscounted LQ DP Problem' (Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 72. *Lines:* 38, 46, 52, 53, 73, 79, 87, 128, 177, 186, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 2. *Lines:* 662, 667. *Example:* %%timeit.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 446. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 676. *Example:* mid-sentence 'Linear'.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 476. *Example:* spelled-out `beta`.


## Strengths

- References, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-math-002` — Use \top for transpose notation (73 occurrences).
2. `qe-writing-006` — Capitalize lecture titles properly (7 occurrences).
3. `qe-math-003` — Use square brackets for matrix notation (6 occurrences).
4. `qe-link-002` — Use doc links for cross-series references (5 occurrences).
5. `qe-writing-004` — Avoid unnecessary capitalization in narrative text (3 occurrences).
6. `qe-writing-008` — Remove excessive whitespace between words (72 occurrences).
7. `qe-writing-001` — Use one sentence per paragraph (1 occurrence).
