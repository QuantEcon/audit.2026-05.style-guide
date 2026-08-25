# match_transport

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/match_transport.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-001` ×4; `qe-writing-008` ×133. |
| Math         | 7.5/10 | `qe-math-002` ×2. |
| Code         | 7.5/10 | `qe-code-002` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3/10  | `qe-fig-007` ×11; `qe-fig-003` ×9; `qe-fig-006` ×9, +4 more. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 8/10  | `qe-link-002` ×4. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 5. *Lines:* 2041, 2042, 2044, 2081, 2089. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 37. *Lines:* 241, 243, 578, 583, 704, 708, 772, 774, 964, 1277, …. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 9. *Lines:* 262, 610, 733, 797, 989, 1323, 1927, 2408, 2515. *Example:* plt.title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 9. *Lines:* 2273, 2274, 2311, 2312, 2407, 2486, 2487, 2513, 2514. *Example:* axis label `Occupations`.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 11. *Lines:* 799, 800, 992, 993, 994, 1327, 1328, 1329, 1931, 1932, …. *Example:* spine removal.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 594, 598, 2270, 2308, 2485. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 464. *Example:* apostrophe transpose `x'`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 133. *Lines:* 18, 20, 23, 26, 28, 30, 32, 34, 36, 38, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 2242, 2284. *Example:* caption of 9 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 2242, 2284. *Example:* mystnb figure without name:.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 40, 44. *Example:* raw link to python.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 34, 1015, 1630, 1732. *Example:* {cite} in author position: '{cite}`boerma2023composite` show'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 42, 355, 2282, 2420. *Example:* 2 sentences in one paragraph.

### Low severity
_None found._


## Strengths

- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-007` — Keep figure box and spines (11 occurrences).
2. `qe-math-002` — Use \top for transpose notation (2 occurrences).
3. `qe-fig-003` — No matplotlib embedded titles (9 occurrences).
4. `qe-fig-006` — Lowercase axis labels (9 occurrences).
5. `qe-code-002` — Use Unicode symbols for Greek letters in code (5 occurrences).
6. `qe-writing-001` — Use one sentence per paragraph (4 occurrences).
7. `qe-link-002` — Use doc links for cross-series references (4 occurrences).
