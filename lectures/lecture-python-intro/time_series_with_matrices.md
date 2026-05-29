# Style Audit — time_series_with_matrices

- **Series:** lecture-python-intro
- **File:** `lectures/time_series_with_matrices.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 5.9 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | H1 Title Case OK; H2 sentence case mostly; minor multi-sentence paragraphs. |
| Math         | 4/10  | Heavy use of `\begin{array}` for matrices (M4); `^T` for transpose (M2); `\mathcal N` for normal distribution (M9). |
| Code         | 9/10  | Unicode Greek (`α`, `β`, `σ`, `y`) used throughout (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 7/10  | `figsize=` on line 54 only; no `ax.set_title`/spines violations; no `{figure}` directives. |
| References   | 8/10  | 1 `{cite}` usage (parenthetical, OK). |
| Links        | 4/10  | 3 direct URLs to `python.quantecon.org` on lines 371, 526, 541 — should be `{doc}` links. |
| Admonitions  | N/A   | no exercises / solutions |

## Issues

### Critical
_None found._

### High severity
- **M4** — Uses `\begin{array}` instead of `\begin{bmatrix}` for matrix display throughout. *Examples:* lines 93–115, 284, 613–625. *Count:* 6+ matrix blocks.
- **M2** — Uses `^T` for transpose (line 394: `\tilde A (\sigma_u^2 I_{T \times T} ) \tilde A^T`).
- **[qe-link-002]** — 3 cross-series direct URLs that should be `{doc}` links. *Examples:* `lectures/time_series_with_matrices.md:371` (`[Multivariate Normal Distribution](https://python.quantecon.org/multivariate_normal.html)`), 526, 541. *Count:* 3 occurrences.

### Medium severity
- **M9** — Distribution name uses `\mathcal{N}` (line 382: `y \sim {\mathcal N}(\mu_y, \Sigma_y)`); should be plain `N`.

### Low severity
- **W1** — Some short two-sentence paragraphs (e.g. lines 33–36).
- **[qe-fig-001]** — `figsize=` on line 54. *Count:* 1 occurrence.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- H1 Title Case OK.
- Equation labels with `{math}` `:label:`.
- IID written correctly (line 275 via ref).
- Italic for emphasis (*initial conditions*, *terminal conditions*).
- Unicode Greek in code throughout.

## Recommended actions
1. Convert all `\begin{array}` matrix blocks to `\begin{bmatrix}` per M4.
2. Replace `^T` with `^\top` per M2.
3. Replace `{\mathcal N}` with `N` per M9.
4. Replace cross-series direct URLs (lines 371, 526, 541) with `{doc}\`intermediate:multivariate_normal\`` etc.
5. Remove `figsize=` on line 54.
