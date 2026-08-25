# likelihood_ratio_process_2

- **Series:** lecture-python.myst
- **File:** `lectures/likelihood_ratio_process_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×6; `qe-writing-009` (proposed) ×4; `qe-writing-008` ×80. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-005` ×13; `qe-fig-003` ×4; `qe-fig-006` ×4, +2 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 14. *Lines:* 638, 730, 761, 1153, 1510, 1514, 1549, 1553, 1615, 1629, …. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 13. *Lines:* 637, 708, 760, 1199, 1213, 1279, 1284, 1614, 1628, 1639, …. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 37, 412, 838. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 421, 667, 669, 671, 838, 1664. *Example:* 2 sentences in one paragraph.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 80. *Lines:* 54, 246, 402, 408, 410, 412, 418, 421, 422, 429, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 64, 145. *Example:* spelled-out `gamma`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 651, 739, 746, 788. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 650, 659, 719, 786. *Example:* axis label `Likelihood ratio $l_t$`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 647, 657. *Example:* plot() without lw=.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 4. *Lines:* 186, 202, 207, 262. *Example:* i.i.d..

### Low severity
_None found._


## Strengths

- Math, Links, Admonitions score 9 or above — no material violations measured in those categories.
- No `qe-math-006` violations — Use aligned environment correctly for PDF compatibility.
- No `qe-admon-003` violations — Use tick count management for nested directives.
- No `qe-math-007` violations — Use automatic equation numbering, not manual tags.
- No `qe-admon-004` violations — Use prf prefix for proof directives.

## Recommended actions

1. `qe-fig-005` — Descriptive figure names for cross-referencing (13 occurrences).
2. `qe-writing-001` — Use one sentence per paragraph (6 occurrences).
3. `qe-ref-001` — Use correct citation style (5 occurrences).
4. `qe-fig-003` — No matplotlib embedded titles (4 occurrences).
5. `qe-writing-009` (proposed) — Write "IID" — not "i.i.d." or "iid" (4 occurrences).
6. `qe-fig-006` — Lowercase axis labels (4 occurrences).
7. `qe-code-002` — Use Unicode symbols for Greek letters in code (4 occurrences).
