# Style Audit — business_cycle

- **Series:** lecture-python-intro
- **File:** `lectures/business_cycle.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 sentence case (proper country names retained). |
| Math         | N/A   | no math content |
| Code         | 8/10  | `!pip install wbgapi` + `!pip install pandas-datareader` near top (lines 31–32) with `hide-output` tag; spelled-out `alpha=` only as matplotlib kwarg. |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `ax.set_title` violations; axis labels mostly lowercase (CPI/YoY are acronyms — OK); no figures with `:name:`. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no external cross-series links |
| Admonitions  | N/A   | no admonitions / exercises |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:` for cross-referencing (figures are pure `plt.show()` output).

## Strengths
- Section headings comply with qe-writing-006.
- Clean prose, one-sentence paragraphs.
- `!pip install wbgapi` and `!pip install pandas-datareader` placed at lecture top with `:tags: [hide-output]` (qe-code-003 OK).
- Axis labels lowercase except for legitimate acronyms (qe-fig-006 OK).
- No `ax.set_title` / `suptitle` calls (qe-fig-003 OK).

## Recommended actions
1. None critical.
