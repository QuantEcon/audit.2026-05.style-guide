# cagan_adaptive

- **Series:** lecture-python-intro
- **File:** `lectures/cagan_adaptive.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title and section headings comply; some multi-sentence paragraphs. |
| Math         | 8/10  | bmatrix used; `aligned` inside `$$`; labels and refs clean. |
| Code         | 8/10  | Unicode Greek (`π`, `μ`, `λ`, `α`) used throughout (qe-code-002 OK); no `quantecon` import so no pip-install needed. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 345, 482, 563, 705; one `ax.set_title` outside exercise context (line 359); no figure `:name:` fields. |
| References   | 7/10  | `{cite}` used; "proposed by {cite}\`Friedman1956\`" (line 82) should be `{cite:t}`. |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | Solutions use `:class: dropdown` and reference exercise labels (qe-admon-002, qe-admon-005 OK); gated `solution-start`/`solution-end` for executable code (qe-admon-001 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Several multi-sentence paragraphs (e.g. lines 23–25, 25, 130–131).
- **[qe-fig-001]** — Repeated `figsize=` overrides on lines 345, 482, 563, 705. *Count:* 4 occurrences.
- **[qe-ref-001]** — In-text citation should use `{cite:t}`. *Example:* `lectures/cagan_adaptive.md:82` ("proposed by {cite}\`Friedman1956\` and {cite}\`Cagan\`"). *Count:* 1 sentence with 2 citations.

### Low severity
- **W7** — Repeated double-quoting style with single quotes (e.g. ''method 2''); check consistency.
- **[qe-fig-003]** — `ax[i].set_title(subplot_title[i])` on line 359 outside any exercise/solution context. *Count:* 1 occurrence.
- **[qe-fig-005]** — No figures have a `:name:` field for cross-referencing.

## Strengths
- Section headings comply with W3 (sentence case).
- Equation labels and `{eq}` references throughout.
- Matrices use bmatrix (M4 OK).
- `aligned` inside `$$` (M12 OK).
- Unicode Greek used in code (qe-code-002 OK).
- All 4 solutions use `:class: dropdown` and link to their exercise labels (qe-admon-002, qe-admon-005 OK).

## Recommended actions
1. Convert "proposed by {cite}\`Friedman1956\`" → `{cite:t}` form on line 82.
2. Remove `figsize=` overrides; rely on `_config.yml` defaults.
3. Move title from `ax[i].set_title` (line 359) to the `mystnb` figure metadata or a `{figure}` directive.
4. Break up the multi-sentence paragraphs in the Overview.
