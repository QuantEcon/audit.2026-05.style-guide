# Style Audit — heavy_tails

- **Series:** lecture-python-intro
- **File:** `lectures/heavy_tails.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3/H4 sentence case; one-sentence paragraphs throughout. |
| Math         | 9/10  | `\mathbb P`, `\mathbb E` used consistently; density `f` lowercase, CDF `F` uppercase (M10 OK); plain `N` for normal. |
| Code         | 8/10  | `!pip install yfinance` + `!pip install wbgapi` at top with `hide-output` (qe-code-003 OK); `alpha=` only as matplotlib kwarg. |
| JAX          | out of scope | — |
| Figures      | 5/10  | `figsize=` on 5 lines (354, 627, 671, 825, 853); 4 `ax.set_title(...)` outside exercise context (lines 365, 372, 676, etc.) with title-like content; "X value" axis label (line 553) uppercase. |
| References   | 7/10  | 16 `{cite}` usages; clean parenthetical-style throughout, no clear in-text mis-use. |
| Links        | 6/10  | Same-series direct URL `https://intro.quantecon.org/heavy_tails.html#...` on line 649; `{doc}` used elsewhere. |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK); `{prf:theorem}`, `{prf:example}` used. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — `figsize=` overrides on lines 354, 627, 671, 825, 853. *Count:* 5 occurrences.
- **[qe-fig-003]** — `ax.set_title(...)` outside exercise context. *Examples:* line 365 (`fr"draws from $N(0, \\sigma^2)$..."`), 372 (`f"draws from the Cauchy distribution"`), 676 (`label`). *Count:* 4 occurrences.

### Medium severity
- **[qe-link-001]** — Same-series link uses full URL instead of markdown link. *Example:* `lectures/heavy_tails.md:649` (`[below](https://intro.quantecon.org/heavy_tails.html#heavy-tails-in-economic-cross-sections)`). Should be `[below](#heavy-tails-in-economic-cross-sections)`.
- **[qe-fig-006]** — Axis label "X value" (line 553) starts uppercase; should be lowercase or use `$X$`.

### Low severity
- **W1** — A few short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- `\mathbb P`, `\mathbb E` consistently used (M7 OK).
- Density/CDF convention M10 compliant.
- Section headings sentence case.
- Bold and italic used appropriately.
- IID-related discussion uses correct casing.
- `!pip install yfinance` and `wbgapi` at top with `hide-output` (qe-code-003 OK).
- Solutions all gated, dropdown, linked.
- `{prf:theorem}`, `{prf:example}` directives (qe-admon-004 OK).

## Recommended actions
1. Remove the 5 `figsize=` overrides.
2. Move `ax.set_title` content into mystnb / `{figure}` metadata.
3. Replace direct same-series URL on line 649 with internal anchor link.
4. Lowercase "X value" → "x value" axis label.
