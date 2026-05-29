# commod_price

- **Series:** lecture-python-intro
- **File:** `lectures/commod_price.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case, H2/H3 sentence case, one-sentence paragraphs throughout. |
| Math         | 8/10  | Uses `\mathbb{E}` and `\mathbb R_+` correctly; minor formatting issue with `\mathbb{E}_t \, p_{t+1}`. |
| Code         | 9/10  | `!pip install yfinance` at top with `hide-output` (qe-code-003 OK); standard imports otherwise; `alpha=` only as matplotlib kwarg. |
| JAX          | out of scope | — |
| Figures      | 9/10  | No `ax.set_title`/`figsize` overrides; clean matplotlib usage; no figures use `{figure}` directive (just `plt.show()`). |
| References   | 8/10  | All 6 `{cite}` usages appear to be end-of-sentence parenthetical-style — no clear in-text misuse. |
| Links        | N/A   | no cross-series links |
| Admonitions  | N/A   | no exercises / solutions |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **W7** — "no-arbitrage" appears in quotes inline (line 169) — minor stylistic; "ansatz" parenthetical at line 222 fine.
- **[qe-fig-005]** — No figures have a `:name:` for cross-referencing.

## Strengths
- Clean one-sentence paragraphs throughout.
- Correct use of `\mathbb{E}`, `\mathbb R_+`.
- Sequence `\{ Z_t \}_{t \geq 1}` is correct M6 form.
- "IID" written correctly in text (line 136).
- All section headings comply with W3.
- `!pip install yfinance` placed at top with `:tags: [hide-output]` (qe-code-003 OK).
- No matplotlib title / figsize / spines violations.

## Recommended actions
1. None critical; consider tightening some math operator spacing.
