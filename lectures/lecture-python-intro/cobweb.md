# Style Audit — cobweb

- **Series:** lecture-python-intro
- **File:** `lectures/cobweb.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title Case H1, sentence-case H2; one-sentence paragraphs throughout. |
| Math         | 9/10  | Clean equations; `{math}` directives with labels; no transpose. |
| Code         | 8/10  | Spelled-out Greek `α` shown only in matplotlib kwargs (acceptable); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 7/10  | `figsize=` on lines 443, 567; one `ax.set_title(r'$\\alpha={}$'.format(a))` inside solution block (exception applies); no figure `:name:`. |
| References   | 8/10  | `{cite}` used; no clear in-text mis-use ("Early papers ... include {cite}" is appropriately parenthetical). |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | Solutions use `:class: dropdown` + exercise labels (qe-admon-002, qe-admon-005 OK); gated form throughout. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W1** — A few brief two-sentence paragraphs (e.g. lines 47–48).
- **W2** — H1 has trailing whitespace in "## Overview " (line 19); minor.
- **[qe-fig-001]** — `figsize=` overrides on lines 443, 567. *Count:* 2 occurrences.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:` for cross-referencing.

## Strengths
- Section headings sentence case (qe-writing-006 compliant).
- `{math}` blocks with `:label:` (M14 compliant).
- Italic for emphasis (`*expectations*`, `*expected*`).
- Clean one-sentence paragraph style.
- All solutions gated, dropdown, and linked to exercises.

## Recommended actions
1. Trim trailing whitespace from H1/H2.
2. Remove `figsize=` overrides on lines 443, 567.
