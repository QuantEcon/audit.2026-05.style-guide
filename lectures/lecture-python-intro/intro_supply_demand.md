# Style Audit — intro_supply_demand

- **Series:** lecture-python-intro
- **File:** `lectures/intro_supply_demand.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; clean one-sentence paragraphs. |
| Math         | 8/10  | Equations clean; no transpose; uses `\$` for currency in prose. |
| Code         | 8/10  | Standard Anaconda imports only; `alpha=` is matplotlib kwarg (not user variable). |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `figsize=` overrides, no `ax.set_title` violations, axis labels OK; no figures use `{figure}` directive. |
| References   | N/A   | no `{cite}` citations |
| Links        | 5/10  | Multiple direct cross-series URLs to `python-programming.quantecon.org/scipy.html` (lines 853, 854, 898, 899) — should be `{doc}` links. |
| Admonitions  | 9/10  | `{prf:example}` × 2 (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Multiple cross-series links use direct URLs instead of `{doc}` references. *Examples:* `lectures/intro_supply_demand.md:853` (`[SciPy](https://python-programming.quantecon.org/scipy.html)`), 854, 898, 899. *Count:* 4 occurrences. **Systemic.**

### Medium severity
_None found._

### Low severity
- **W3** — "### A comment on quantity." (line 140) has a trailing period; minor.
- **W1** — Occasional two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Section headings sentence case (W3 OK).
- Bold for definitions (**consumer surplus**).
- `prf:example` directives used for structure (qe-admon-004 OK).
- Clear one-sentence paragraph style.
- No matplotlib title/figsize/spines violations.
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Replace direct `python-programming.quantecon.org` URLs (lines 853, 854, 898, 899) with `{doc}\`programming:scipy\`` links per qe-link-002.
2. Remove trailing period from H3 on line 140.
