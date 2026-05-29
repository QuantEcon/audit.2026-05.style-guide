# lln_clt

- **Series:** lecture-python-intro
- **File:** `lectures/lln_clt.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 acronyms OK; H2/H3 sentence case; clean one-sentence paragraphs. |
| Math         | 8/10  | `\mathbb P` / `\mathbb E`; `\mathbf 1` used for indicator (M5/M3 concern). |
| Code         | 8/10  | Unicode Greek (`μ`, `σ`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 490, 541, 685; no `ax.set_title` violations outside exercise; no figures use `{figure}` directive. |
| References   | N/A   | no `{cite}` citations |
| Links        | 6/10  | Same-series link uses full URL on line 298 (`intro.quantecon.org/prob_dist.html#violin-plots`); cross-series direct URL on line 31 (`python.quantecon.org/lln_clt.html#the-multivariate-case`). |
| Admonitions  | 9/10  | `{prf:theorem}` × 4 (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **M5/M3** — `\mathbf 1\{U < p\}` (lines 578, 588) — uses bold for indicator; should be `\mathbb{1}` per M3.
- **[qe-fig-001]** — `figsize=` overrides on lines 490, 541, 685. *Count:* 3 occurrences.
- **[qe-link-002]** — Cross-series link uses direct URL. *Example:* `lectures/lln_clt.md:31` (`[in a more advanced lecture](https://python.quantecon.org/lln_clt.html#the-multivariate-case)`). Should be `{doc}\`intermediate:lln_clt\``.
- **[qe-link-001]** — Same-series link uses full URL. *Example:* `lectures/lln_clt.md:298` (`[violin plot](https://intro.quantecon.org/prob_dist.html#violin-plots)`). Should be `[violin plot](prob_dist.html#violin-plots)` or `[](prob_dist)`.

### Low severity
- **W1** — A few short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- `\mathbb P`, `\mathbb E` consistently (M7 OK).
- `IID` correctly written (line 176, 187).
- Density `f` lowercase (M10 OK).
- Equation labels with `{math}` `:label:`.
- `{prf:theorem}` used (qe-admon-004 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Replace `\mathbf 1` with `\mathbb{1}` per M3.
2. Replace direct cross-series URL on line 31 with `{doc}\`intermediate:lln_clt\``.
3. Replace same-series full URL on line 298 with relative link.
4. Remove `figsize=` overrides.
