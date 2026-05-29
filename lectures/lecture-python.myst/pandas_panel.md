# Style Audit — pandas_panel

- **Series:** lecture-python.myst
- **File:** `lectures/pandas_panel.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10 | Section headings use Title Case rather than sentence case. |
| Math         | N/A | no math content |
| Code         | 10/10 | Clean code conventions. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 8/10 | `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks. |
| References   | N/A | No citations. |
| Links        | 9/10 | 1 direct URL to another QuantEcon series — should use `{doc}` link. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks. *Examples:* line 393, line 410, line 421.

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 60 `Slicing and Reshaping Data`, line 175 `Merging Dataframes and Filling NaNs`. *Count:* 4.
- **[qe-link-002]** — 1 direct URL to another QuantEcon series — should use `{doc}` link. *Example:* line 34.

### Low severity
_None found._

## Strengths
- Uses "IID" or no IID terminology.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-fig-003`: `ax.set_title()` / `fig.suptitle()` used 5 times outside exercise blocks.
2. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
3. Address `qe-link-002`: 1 direct URL to another QuantEcon series — should use `{doc}` link.
