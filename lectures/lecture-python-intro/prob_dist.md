# Style Audit — prob_dist

- **Series:** lecture-python-intro
- **File:** `lectures/prob_dist.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3/H4 sentence case; clean one-sentence paragraphs. |
| Math         | 9/10  | `\mathbb P`, `\mathbb E`, `\mathbb V` (M7 OK); `\mathbb 1` for indicator (M3-compatible); density `p` lowercase (M10 OK). |
| Code         | 8/10  | `!pip install yfinance` at top with `hide-output` (qe-code-003 OK); unicode Greek (`μ`, `σ`) used in code (qe-code-002 OK). |
| JAX          | out of scope | — |
| Figures      | 5/10  | Axis label "S" capitalised on many plots (lines 128, 141, 244, 323, etc.) — `S` is a symbol so debatable; "PMF"/"CDF" uppercase OK as acronyms; no `ax.set_title`/`figsize=` violations. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | 1 solution gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **M3** — Uses `\mathbb 1` for indicator instead of `\mathbb{1}` (same symbol, slightly inconsistent style); generally OK.
- **[qe-fig-006]** — Axis label `'S'` appears many times (lines 128, 141, 244, 323, etc.); `S` is a math symbol that's OK if rendered, but as plain string it reads as title-case. Consider `r'$S$'`. *Count:* 10+ occurrences.

### Low severity
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- `\mathbb P`, `\mathbb E`, `\mathbb V` consistently used (M7 fully compliant).
- `\mathbb 1` indicator function explained (M3 compliant).
- Density `p` lowercase, CDF `F` uppercase (M10 OK).
- Section headings sentence case.
- Bold for definitions (**probability mass function**, **mean**, **variance**, **cumulative distribution function**, etc.).
- `yfinance` install at top with `hide-output` (qe-code-003 OK).
- Unicode Greek in code.

## Recommended actions
1. Render axis-label symbols as math: `set_xlabel(r'$S$')` instead of `'S'`.
