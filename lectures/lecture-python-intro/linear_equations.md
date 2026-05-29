# linear_equations

- **Series:** lecture-python-intro
- **File:** `lectures/linear_equations.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 sentence case; some short paragraphs. |
| Math         | 7/10  | bmatrix used; `^T` for transpose on line 1274 (M2 violation); equations clean otherwise. |
| Code         | 8/10  | Standard Anaconda imports only; spelled-out `alpha=` only as matplotlib kwarg (acceptable). |
| JAX          | out of scope | — |
| Figures      | 7/10  | No `figsize=` overrides, no `ax.set_title` violations; 6 spines manipulations (set_color/set_position pattern around figure code). |
| References   | N/A   | no `{cite}` citations |
| Links        | 4/10  | 5 direct URLs to `python-programming.quantecon.org/numpy.html` and `python.quantecon.org/linear_algebra.html` (lines 352, 660, 666, 955, 1388) — should be `{doc}` links. |
| Admonitions  | 9/10  | `{prf:example}` × 7 used (qe-admon-004 OK); 2 solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Multiple cross-series links use direct URLs instead of `{doc}` references. *Examples:* `lectures/linear_equations.md:352` (`[NumPy arrays](https://python-programming.quantecon.org/numpy.html#numpy-arrays)`), 660, 666, 955, 1388. *Count:* 5 occurrences. **Systemic.**

### Medium severity
- **M2** — Uses `^T` for transpose on line 1274 (`\hat{x} = (A^T A)^{-1} A^T b`) — should be `^\top`. *Count:* 1 equation (2 instances within).
- **[qe-fig-007]** — Spines manipulated via `set_color('none')` + `set_position('zero')` to hide the box. *Count:* 6 occurrences across vector/coord figures.

### Low severity
- **W1** — Some short two-sentence paragraphs.
- **W3** — "## {index}`Vectors <single: Vectors>`" mixes index directive with heading (line 130).
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- bmatrix used throughout for matrices (M4 OK).
- Equation labels via `{math}` `:label:` (M14 OK).
- Bold for definitions (**vector**, **least squares solution**, etc.).
- Section headings mostly sentence case.
- `{prf:example}` used 7 times (qe-admon-004 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Replace direct cross-series URLs (lines 352, 660, 666, 955, 1388) with `{doc}\`programming:numpy\`` / `{doc}\`intermediate:linear_algebra\`` form.
2. Replace `^T` with `^\top` on line 1274.
3. Drop the spine `set_color('none')` calls per qe-fig-007 (keep default box).
