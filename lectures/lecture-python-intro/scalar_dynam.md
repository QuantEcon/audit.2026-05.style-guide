# Style Audit — scalar_dynam

- **Series:** lecture-python-intro
- **File:** `lectures/scalar_dynam.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 sentence case; one-sentence paragraphs throughout. |
| Math         | 9/10  | Sequences `\{x_t\}` (M6 OK); `{math}` with labels; clean. |
| Code         | 8/10  | Standard Anaconda imports; spelled-out `alpha=` matplotlib kwarg only. |
| JAX          | out of scope | — |
| Figures      | 7/10  | No `figsize=`/`ax.set_title` violations; 3 spines manipulations (`set_position('zero')` + `set_color('none')`) on lines 341–344. |
| References   | N/A   | no `{cite}` citations |
| Links        | 9/10  | `{doc}` cross-references used (2 occurrences). |
| Admonitions  | 9/10  | 1 solution gated, dropdown, exercise-linked; `{prf:example}` used. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-007]** — Spines manipulated via `set_color('none')` + `set_position('zero')` (lines 341–344). *Count:* 3 occurrences within one figure helper.

### Low severity
- **W7** — Backtick double quotes `` ``parameters'' `` on line 161 (TeX-style quotes inside double backticks); should be `"parameters"`.
- **W1** — Some two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Sequences use `\{x_t\}` curly brackets (M6 OK).
- Equation labels via `{math}` `:label:` (M14 OK).
- Bold for definitions (**composition**, **dynamic system**, **trajectory**, **state space**, **state variable**).
- Clean sentence-case section headings.
- `{doc}` cross-references used (qe-link-002 OK).
- `{prf:example}` directive (qe-admon-004 OK).
- Solution gated, dropdown, linked.

## Recommended actions
1. Replace ``\`\`parameters''`` with `"parameters"`.
2. Drop spine `set_color('none')` / `set_position('zero')` calls per qe-fig-007.
